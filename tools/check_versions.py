#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to check if BOM dependencies are up-to-date with their GitHub releases
and if the Unreleased section of CHANGELOG.md is empty.
"""

import re
import sys
import io
from typing import Dict, List, Tuple, Optional
import requests

class DependencyChecker:
    """Check BOM dependencies against GitHub releases."""

    def __init__(self, github_token: str):
        self.github_token = github_token
        self.headers = {
            "Authorization": f"token {github_token}",
            "Accept": "application/vnd.github.v3+json"
        }
        self.session = requests.Session()
        self.session.headers.update(self.headers)
        self.token_valid = None

    def verify_token(self) -> bool:
        """Verify if the GitHub token is valid."""
        print("  → Connecting to GitHub API...")
        try:
            response = self.session.get("https://api.github.com/user", timeout=10)
            self.token_valid = (response.status_code == 200)
            if self.token_valid:
                print("  ✓ Token is valid")
            else:
                print(f"  ✗ Invalid token (status: {response.status_code})")
            return self.token_valid
        except Exception as e:
            print(f"  ✗ Error while verifying token: {e}")
            self.token_valid = False
            return False

    def parse_properties_file(self, filepath: str) -> Dict[str, str]:
        """Parse a properties file and return a dictionary."""
        print(f"  → Reading file {filepath}...")
        properties = {}
        with open(filepath, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        properties[key.strip()] = value.strip()
        print(f"  ✓ {len(properties)} properties loaded")
        return properties

    def parse_build_gradle(self, filepath: str) -> List[Tuple[str, str, str]]:
        """
        Parse build.gradle.kts and extract dependencies.
        Returns list of tuples: (groupId, artifactId, version)
        """
        print(f"  → Analyzing file {filepath}...")
        dependencies = []
        api_pattern = re.compile(r'api\("([^:]+):([^:]+):([^"]+)"\)')

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        for match in api_pattern.finditer(content):
            group_id = match.group(1)
            artifact_id = match.group(2)
            version = match.group(3)
            dependencies.append((group_id, artifact_id, version))

        print(f"  ✓ {len(dependencies)} dependencies found")
        return dependencies

    def is_kmp_library(self, artifact_id: str) -> bool:
        """
        Check if the artifact is a KMP (Kotlin Multiplatform) library variant.
        These don't have individual GitHub releases.
        """
        return '-kmp-lib-' in artifact_id

    def map_to_github_repo(self, group_id: str, artifact_id: str) -> str:
        """
        Map Maven coordinates to GitHub repository.
        org.eclipse.keypop:keypop-reader-java-api -> eclipse-keypop/keypop-reader-java-api
        org.eclipse.keyple:keyple-service-java-lib -> eclipse-keyple/keyple-service-java-lib
        """
        if group_id == "org.eclipse.keypop":
            org = "eclipse-keypop"
        elif group_id == "org.eclipse.keyple":
            org = "eclipse-keyple"
        else:
            raise ValueError(f"Unknown group ID: {group_id}")

        return f"{org}/{artifact_id}"

    def get_latest_release(self, repo: str) -> Optional[str]:
        """Get the latest release version from GitHub."""
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        print(f"    → Retrieving latest release...")
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code == 200:
                data = response.json()
                tag_name = data.get('tag_name', '')
                # Remove 'v' prefix if present
                version = tag_name.lstrip('v')
                print(f"    ✓ Version found: {version}")
                return version
            elif response.status_code == 404:
                print(f"    ✗ No release found")
                return None
            else:
                print(f"    ⚠ API returned status {response.status_code}")
                return None
        except Exception as e:
            print(f"    ✗ Error: {e}")
            return None

    def check_unreleased_section(self, repo: str) -> Tuple[bool, str, Optional[str]]:
        """
        Check if the Unreleased section in CHANGELOG.md is empty.
        Returns (is_empty, message, full_content)
        """
        url = f"https://api.github.com/repos/{repo}/contents/CHANGELOG.md"
        print(f"    → Checking Unreleased section...")
        try:
            response = self.session.get(url, timeout=10)
            if response.status_code != 200:
                print(f"    ⚠ CHANGELOG.md not found")
                return (True, "CHANGELOG.md not found", None)

            # Get the download URL
            data = response.json()
            download_url = data.get('download_url')
            if not download_url:
                print(f"    ⚠ Could not access content")
                return (True, "Cannot access CHANGELOG.md content", None)

            # Download the actual file content
            changelog_response = self.session.get(download_url, timeout=10)
            if changelog_response.status_code != 200:
                print(f"    ⚠ Could not download CHANGELOG")
                return (True, "Cannot download CHANGELOG.md", None)

            content = changelog_response.text

            # Find the Unreleased section
            unreleased_pattern = re.compile(r'^##\s*\[Unreleased\]', re.MULTILINE)
            next_section_pattern = re.compile(r'^##\s+\[', re.MULTILINE)

            unreleased_match = unreleased_pattern.search(content)
            if not unreleased_match:
                print(f"    ⚠ Unreleased section not found")
                return (True, "No Unreleased section found", None)

            # Extract content after Unreleased header
            start_pos = unreleased_match.end()
            remaining_content = content[start_pos:]

            # Find the next section (next ## line)
            next_section_match = next_section_pattern.search(remaining_content)
            if next_section_match:
                section_content = remaining_content[:next_section_match.start()]
            else:
                section_content = remaining_content

            # Check if section is empty (only whitespace and separators)
            # Remove whitespace and common separators
            cleaned = section_content.strip()
            cleaned = re.sub(r'^[-=\s]+$', '', cleaned, flags=re.MULTILINE)
            cleaned = cleaned.strip()

            if cleaned:
                # Section has content
                print(f"    ⚠ Contains unreleased changes ({len(cleaned)} characters)")
                print(f"\n    CONTENT OF UNRELEASED SECTION:")
                print("    " + "-" * 76)
                # Display the full content with indentation
                for line in section_content.strip().split('\n'):
                    print(f"    {line}")
                print("    " + "-" * 76 + "\n")
                return (False, f"Has unreleased changes ({len(cleaned)} chars)", section_content.strip())
            else:
                print(f"    ✓ Section is empty")
                return (True, "Empty", None)

        except Exception as e:
            print(f"    ✗ Error: {e}")
            return (True, f"Error checking CHANGELOG: {e}", None)

    def check_dependency(self, group_id: str, artifact_id: str, current_version: str) -> Dict:
        """Check a single dependency."""
        result = {
            'group_id': group_id,
            'artifact_id': artifact_id,
            'current_version': current_version,
            'latest_version': None,
            'is_up_to_date': None,
            'unreleased_empty': None,
            'unreleased_message': None,
            'unreleased_content': None,
            'error': None,
            'skipped': False
        }

        try:
            # Check if this is a KMP library variant
            if self.is_kmp_library(artifact_id):
                print(f"    ⊘ KMP library skipped (no individual GitHub release)")
                result['skipped'] = True
                result['error'] = "KMP library variant (skipped)"
                return result

            repo = self.map_to_github_repo(group_id, artifact_id)

            # Check latest release
            latest_version = self.get_latest_release(repo)
            result['latest_version'] = latest_version

            if latest_version:
                result['is_up_to_date'] = (current_version == latest_version)
                if result['is_up_to_date']:
                    print(f"    ✓ Up to date")
                else:
                    print(f"    ⚠ Outdated: {current_version} → {latest_version}")
            else:
                result['error'] = "No release found on GitHub"

            # Check unreleased section
            is_empty, message, content = self.check_unreleased_section(repo)
            result['unreleased_empty'] = is_empty
            result['unreleased_message'] = message
            result['unreleased_content'] = content

        except Exception as e:
            print(f"    ✗ Error: {e}")
            result['error'] = str(e)

        return result

    def generate_report(self, results: List[Dict]) -> None:
        """Generate and print the verification report."""
        print("\n" + "="*80)
        print("BOM VERSION VERIFICATION REPORT")
        print("="*80 + "\n")

        outdated = []
        with_unreleased = []
        errors = []
        up_to_date = []
        skipped = []

        for result in results:
            dep_name = f"{result['group_id']}:{result['artifact_id']}"

            if result['skipped']:
                skipped.append(dep_name)
            elif result['error']:
                errors.append((dep_name, result['error']))
            else:
                if result['is_up_to_date']:
                    up_to_date.append(dep_name)
                else:
                    outdated.append((
                        dep_name,
                        result['current_version'],
                        result['latest_version']
                    ))

                if not result['unreleased_empty']:
                    with_unreleased.append((
                        dep_name,
                        result['unreleased_message'],
                        result['unreleased_content']
                    ))

        # Print outdated dependencies
        if outdated:
            print("[!] OUTDATED DEPENDENCIES:")
            print("-" * 80)
            for dep_name, current, latest in outdated:
                print(f"  {dep_name}")
                print(f"    Current: {current}")
                print(f"    Latest:  {latest}")
                print()
        else:
            print("[OK] All dependencies are up to date")
            print()

        # Print dependencies with unreleased changes
        if with_unreleased:
            print("[!] DEPENDENCIES WITH UNRELEASED CHANGES:")
            print("-" * 80)
            for dep_name, message, content in with_unreleased:
                print(f"  {dep_name}")
                print(f"    {message}")
                if content:
                    print(f"\n  CONTENT OF UNRELEASED SECTION:")
                    print("  " + "-" * 78)
                    for line in content.split('\n'):
                        print(f"  {line}")
                    print("  " + "-" * 78)
                print()
                print()
        else:
            print("[OK] All dependencies have empty Unreleased sections")
            print()

        # Print skipped dependencies
        if skipped:
            print("[INFO] SKIPPED DEPENDENCIES (KMP):")
            print("-" * 80)
            for dep_name in skipped:
                print(f"  {dep_name}")
            print()

        # Print errors
        if errors:
            print("[ERROR] ERRORS:")
            print("-" * 80)
            for dep_name, error in errors:
                print(f"  {dep_name}")
                print(f"    Error: {error}")
                print()

        # Print summary
        print("="*80)
        print("SUMMARY:")
        print("-" * 80)
        print(f"  Total dependencies:           {len(results)}")
        print(f"  Up to date:                   {len(up_to_date)}")
        print(f"  Outdated:                     {len(outdated)}")
        print(f"  With unreleased changes:      {len(with_unreleased)}")
        print(f"  Skipped (KMP):                {len(skipped)}")
        print(f"  Errors:                       {len(errors)}")
        print("="*80 + "\n")

        # Exit with error code if there are issues
        if outdated or with_unreleased or errors:
            sys.exit(1)
        else:
            sys.exit(0)


def main():
    """Main entry point."""
    print("="*80)
    print("BOM VERSION VERIFICATION")
    print("="*80 + "\n")

    # Parse user.properties to get GitHub token
    try:
        print("Phase 1: Configuration Loading")
        print("-" * 80)
        checker = DependencyChecker("")
        properties = checker.parse_properties_file("user.properties")
        github_token = properties.get('githubToken')

        if not github_token:
            print("  ✗ Error: githubToken not found in user.properties")
            sys.exit(1)

        print()
        print("Phase 2: GitHub Token Validation")
        print("-" * 80)
        checker = DependencyChecker(github_token)

        # Verify token
        if not checker.verify_token():
            print("\n  ✗ Error: Invalid GitHub Token")
            print("  The token must be a valid GitHub Personal Access Token.")
            sys.exit(1)

    except FileNotFoundError:
        print("  ✗ Error: user.properties file not found")
        sys.exit(1)
    except Exception as e:
        print(f"  ✗ Error while reading user.properties: {e}")
        sys.exit(1)

    # Parse build.gradle.kts
    try:
        print()
        print("Phase 3: Dependency Analysis")
        print("-" * 80)
        dependencies = checker.parse_build_gradle("build.gradle.kts")
    except FileNotFoundError:
        print("  ✗ Error: build.gradle.kts file not found")
        sys.exit(1)
    except Exception as e:
        print(f"  ✗ Error while analyzing build.gradle.kts: {e}")
        sys.exit(1)

    # Check each dependency
    print()
    print("Phase 4: Dependency Verification")
    print("-" * 80)
    results = []
    for i, (group_id, artifact_id, version) in enumerate(dependencies, 1):
        print(f"\n[{i}/{len(dependencies)}] {group_id}:{artifact_id}:{version}")
        result = checker.check_dependency(group_id, artifact_id, version)
        results.append(result)

    # Generate report
    checker.generate_report(results)


if __name__ == "__main__":
    main()