#!/usr/bin/env python3
"""
Script to automatically update CHANGELOG.md from build.gradle.kts changes.

Usage:
    python update_changelog.py [YYYY.MM.DD]

If no date is provided, uses today's date.
"""

import re
import sys
from datetime import date
from typing import Dict, List, Tuple, Optional
from dataclasses import dataclass


@dataclass
class Dependency:
    """Represents a dependency with its metadata."""
    artifact_id: str
    version: str
    category: str
    group_id: str


@dataclass
class ChangelogEntry:
    """Represents an entry in the changelog."""
    name: str
    version: str
    status: str
    prev_version: str
    category: str = ""


class BuildGradleParser:
    """Parser for build.gradle.kts file."""

    CATEGORY_MAPPING = {
        "Keypop": "**Keypop Dependencies**",
        "Keyple core": "**Keyple Core**",
        "Keyple distributed": "**Keyple Distributed**",
        "Keyple interop": "**Keyple Interop**",
        "Keyple card extensions": "**Keyple Card Extensions**",
        "Keyple reader plugins": "**Keyple Reader Plugins**",
    }

    # Patterns for KMP library variants to exclude from individual listing
    KMP_VARIANT_SUFFIXES = [
        "-jvm", "-android", "-iosarm64", "-iossimulatorarm64", "-iosx64"
    ]

    def __init__(self, filepath: str):
        self.filepath = filepath
        self.dependencies: List[Dependency] = []

    def parse(self) -> List[Dependency]:
        """Parse the build.gradle.kts file and extract dependencies."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        current_category = None
        dependencies_by_base = {}  # Track base libraries for KMP grouping

        # Extract the dependencies block
        constraints_match = re.search(r'constraints\s*\{(.*?)\}', content, re.DOTALL)
        if not constraints_match:
            return []

        constraints_block = constraints_match.group(1)
        lines = constraints_block.split('\n')

        for line in lines:
            line = line.strip()

            # Check for category comment
            if line.startswith('//'):
                category_name = line.lstrip('/').strip()
                current_category = self.CATEGORY_MAPPING.get(category_name, category_name)
                continue

            # Parse api() lines
            api_match = re.match(r'api\("([^:]+):([^:]+):([^"]+)"\)', line)
            if api_match and current_category:
                group_id = api_match.group(1)
                artifact_id = api_match.group(2)
                version = api_match.group(3)

                # Check if this is a KMP variant
                base_artifact = artifact_id
                is_variant = False
                for suffix in self.KMP_VARIANT_SUFFIXES:
                    if artifact_id.endswith(suffix):
                        base_artifact = artifact_id[:artifact_id.rfind(suffix)]
                        is_variant = True
                        break

                # Only add the base library, not variants
                if not is_variant:
                    dep = Dependency(
                        artifact_id=artifact_id,
                        version=version,
                        category=current_category,
                        group_id=group_id
                    )
                    dependencies_by_base[artifact_id] = dep
                elif base_artifact not in dependencies_by_base:
                    # If we encounter a variant before the base, add the base
                    dep = Dependency(
                        artifact_id=base_artifact,
                        version=version,
                        category=current_category,
                        group_id=group_id
                    )
                    dependencies_by_base[base_artifact] = dep

        # Preserve order by re-parsing and keeping only base libraries
        result = []
        current_category = None

        for line in lines:
            line = line.strip()

            if line.startswith('//'):
                category_name = line.lstrip('/').strip()
                current_category = self.CATEGORY_MAPPING.get(category_name, category_name)
                continue

            api_match = re.match(r'api\("([^:]+):([^:]+):([^"]+)"\)', line)
            if api_match and current_category:
                artifact_id = api_match.group(2)

                # Check if this is a base library (not a variant)
                is_base = True
                for suffix in self.KMP_VARIANT_SUFFIXES:
                    if artifact_id.endswith(suffix):
                        is_base = False
                        break

                if is_base and artifact_id in dependencies_by_base:
                    result.append(dependencies_by_base[artifact_id])

        return result


class ChangelogParser:
    """Parser for CHANGELOG.md file."""

    def __init__(self, filepath: str):
        self.filepath = filepath

    def parse_latest_version(self) -> Tuple[Optional[str], Dict[str, ChangelogEntry]]:
        """Parse the latest version section and return version number and entries."""
        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the [Unreleased] section first
        unreleased_match = re.search(r'\n## \[Unreleased\]', content)
        if not unreleased_match:
            return None, {}

        # Find the first version section after [Unreleased]
        search_start = unreleased_match.end()
        version_match = re.search(r'\n## \[(\d{4}\.\d{2}\.\d{2})\]', content[search_start:])
        if not version_match:
            return None, {}

        version = version_match.group(1)

        # Extract the section content until the next ## or end of file
        section_start = search_start + version_match.end()
        next_section = re.search(r'\n## \[', content[section_start:])
        if next_section:
            section_end = section_start + next_section.start()
        else:
            # Look for the reference links section
            refs_match = re.search(r'\n\[Unreleased\]:', content[section_start:])
            if refs_match:
                section_end = section_start + refs_match.start()
            else:
                section_end = len(content)

        section_content = content[section_start:section_end]

        # Parse the table
        entries = {}
        lines = section_content.split('\n')
        in_table = False
        current_category = ""

        for line in lines:
            if line.startswith('|') and '---' in line:
                in_table = True
                continue

            if in_table and line.startswith('|'):
                # Parse table row
                cells = [cell.strip() for cell in line.split('|')[1:-1]]
                if len(cells) >= 2:
                    name = cells[0].strip()

                    # Check if this is a category header
                    if '**' in name:
                        current_category = name
                        continue

                    # Skip empty rows
                    if not name or not cells[1].strip():
                        continue

                    dep_version = cells[1].strip('`').strip()
                    status = cells[2].strip() if len(cells) > 2 else ''
                    prev_version = cells[3].strip('`').strip() if len(cells) > 3 else ''

                    # Extract artifact name from markdown link if present
                    link_match = re.match(r'\[([^\]]+)\]', name)
                    if link_match:
                        name = link_match.group(1)

                    if name and dep_version:
                        entries[name] = ChangelogEntry(name, dep_version, status, prev_version, current_category)

        return version, entries


class VersionComparator:
    """Compare versions and determine change type."""

    @staticmethod
    def parse_version(version: str) -> Tuple[int, ...]:
        """Parse a version string into a tuple of integers."""
        try:
            return tuple(int(x) for x in version.split('.'))
        except (ValueError, AttributeError):
            return (0,)

    @staticmethod
    def get_status(old_version: str, new_version: str) -> str:
        """Determine status emoji based on semantic versioning."""
        old = VersionComparator.parse_version(old_version)
        new = VersionComparator.parse_version(new_version)

        # Pad to same length
        max_len = max(len(old), len(new))
        old = old + (0,) * (max_len - len(old))
        new = new + (0,) * (max_len - len(new))

        if new == old:
            return ""

        # Check major version (first component)
        if new[0] > old[0]:
            return "🔴"

        # Check minor version (second component)
        if len(new) > 1 and len(old) > 1 and new[1] > old[1]:
            return "🔵"

        # Otherwise it's a patch
        return "🟢"


class ChangelogGenerator:
    """Generate new changelog entries."""

    def __init__(self, filepath: str):
        self.filepath = filepath

    def generate_new_section(
        self,
        new_version: str,
        dependencies: List[Dependency],
        old_entries: Dict[str, ChangelogEntry]
    ) -> Tuple[str, bool]:
        """Generate a new version section for the changelog."""
        lines = [
            f"## [{new_version}]",
            "",
            "| Component                                       | Version | Status | Prev.<br>Version |",
            "|:------------------------------------------------|:-------:|:------:|:----------------:|"
        ]

        has_changes = False
        current_deps_names = set()

        # Build a dict of current dependencies by category for easy lookup
        deps_by_category = {}
        for dep in dependencies:
            if dep.category not in deps_by_category:
                deps_by_category[dep.category] = []
            deps_by_category[dep.category].append(dep)
            current_deps_names.add(dep.artifact_id)

        # Find removed dependencies organized by category
        removed_by_category = {}
        for name, old_entry in old_entries.items():
            if name not in current_deps_names:
                has_changes = True
                if old_entry.category not in removed_by_category:
                    removed_by_category[old_entry.category] = []
                removed_by_category[old_entry.category].append(old_entry)

        # Process each category in order (from dependencies list)
        current_category = None
        for dep in dependencies:
            # Add category header if changed
            if dep.category != current_category:
                if current_category is not None:
                    # Add removed dependencies from previous category
                    if current_category in removed_by_category:
                        for removed in removed_by_category[current_category]:
                            name = f"[{removed.name}]"
                            version = f"`{removed.version}`"
                            status = "❌"
                            prev_version = ""
                            line = f"| {name:<47} | {version:^7} | {status:^6} | {prev_version:^16} |"
                            lines.append(line)
                    lines.append("|                                                 |         |        |                  |")

                current_category = dep.category
                lines.append(f"| {current_category:<47} |         |        |                  |")

            # Determine if there's a change
            old_entry = old_entries.get(dep.artifact_id)
            status = ""
            prev_version = ""

            if old_entry:
                if old_entry.version != dep.version:
                    status = VersionComparator.get_status(old_entry.version, dep.version)
                    prev_version = f"`{old_entry.version}`"
                    has_changes = True
            else:
                # New dependency
                status = "🆕"
                has_changes = True

            # Format the line
            name = f"[{dep.artifact_id}]"
            version = f"`{dep.version}`"

            # Build the line with proper alignment
            line = f"| {name:<47} | {version:^7} | {status:^6} | {prev_version:^16} |"
            lines.append(line)

        # Add removed dependencies from last category
        if current_category and current_category in removed_by_category:
            for removed in removed_by_category[current_category]:
                name = f"[{removed.name}]"
                version = f"`{removed.version}`"
                status = "❌"
                prev_version = ""
                line = f"| {name:<47} | {version:^7} | {status:^6} | {prev_version:^16} |"
                lines.append(line)

        # Handle removed dependencies from categories that no longer exist
        for category, removed_list in removed_by_category.items():
            if category not in deps_by_category:
                lines.append("|                                                 |         |        |                  |")
                lines.append(f"| {category:<47} |         |        |                  |")
                for removed in removed_list:
                    name = f"[{removed.name}]"
                    version = f"`{removed.version}`"
                    status = "❌"
                    prev_version = ""
                    line = f"| {name:<47} | {version:^7} | {status:^6} | {prev_version:^16} |"
                    lines.append(line)

        return "\n".join(lines), has_changes

    def update_changelog(
        self,
        new_version: str,
        new_section: str,
        has_changes: bool,
        dependencies: List[Dependency],
        old_entries: Dict[str, ChangelogEntry]
    ) -> bool:
        """Update the CHANGELOG.md file with the new section."""
        if not has_changes:
            print("No changes detected between build.gradle.kts and the latest CHANGELOG version.")
            return False

        with open(self.filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Find the [Unreleased] section
        unreleased_match = re.search(r'(## \[Unreleased\]\n)', content)
        if not unreleased_match:
            print("Error: Could not find [Unreleased] section in CHANGELOG.md")
            return False

        # Insert new section after [Unreleased]
        insert_pos = unreleased_match.end()
        new_content = (
            content[:insert_pos] +
            "\n" + new_section + "\n" +
            content[insert_pos:]
        )

        # Update reference links
        new_content = self.update_reference_links(new_content, new_version, dependencies, old_entries)

        with open(self.filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

        print(f"CHANGELOG.md updated successfully with version {new_version}")
        return True

    def update_reference_links(
        self,
        content: str,
        new_version: str,
        dependencies: List[Dependency],
        old_entries: Dict[str, ChangelogEntry]
    ) -> str:
        """Update the [Unreleased] and version reference links, and add/remove dependency links."""
        # Find the reference links section
        unreleased_link_match = re.search(
            r'\[Unreleased\]: https://github\.com/([^/]+)/([^/]+)/compare/([\d.]+)\.\.\.HEAD',
            content
        )

        if not unreleased_link_match:
            return content

        org = unreleased_link_match.group(1)
        repo = unreleased_link_match.group(2)
        old_version = unreleased_link_match.group(3)

        # Update [Unreleased] link to point from new version to HEAD
        new_unreleased_link = f"[Unreleased]: https://github.com/{org}/{repo}/compare/{new_version}...HEAD"
        content = re.sub(
            r'\[Unreleased\]: https://github\.com/[^/]+/[^/]+/compare/[\d.]+\.\.\.HEAD',
            new_unreleased_link,
            content
        )

        # Add new version link after [Unreleased] link
        new_version_link = f"[{new_version}]: https://github.com/{org}/{repo}/compare/{old_version}...{new_version}"
        content = re.sub(
            r'(\[Unreleased\]: [^\n]+\n)',
            f'\\1{new_version_link}\n',
            content
        )

        # Find added and removed dependencies
        current_deps = {dep.artifact_id for dep in dependencies}
        old_deps = set(old_entries.keys())

        added_deps = current_deps - old_deps
        removed_deps = old_deps - current_deps

        # First, remove links for removed dependencies
        for dep_name in removed_deps:
            content = re.sub(
                rf'\n\[{re.escape(dep_name)}\]: https://github\.com/[^\n]+\n',
                '\n',
                content
            )

        # Extract all existing artifact links (keypop and keyple) into a dict
        existing_links = {}
        for match in re.finditer(r'\n\[((keypop|keyple)-[^\]]+)\]: ([^\n]+)\n', content):
            artifact_id = match.group(1)
            full_line = match.group(0)
            existing_links[artifact_id] = full_line

        # Build set of all dependencies we're managing
        managed_deps = set(dep.artifact_id for dep in dependencies)

        # Build the new ordered list of links based on dependencies order
        # Group by category to add blank lines between categories
        new_links_section = []
        processed_deps = set()
        previous_category = None

        for dep in dependencies:
            processed_deps.add(dep.artifact_id)

            # Add blank line between categories
            if previous_category and dep.category != previous_category:
                new_links_section.append('')

            if dep.artifact_id in existing_links:
                # Use existing link (strip the leading \n if present)
                link = existing_links[dep.artifact_id].lstrip('\n')
                new_links_section.append(link.rstrip('\n'))
            else:
                # Create new link (either because it's a new dependency or the link is missing)
                if dep.artifact_id.startswith('keypop-'):
                    org = 'eclipse-keypop'
                elif dep.artifact_id.startswith('keyple-'):
                    org = 'eclipse-keyple'
                else:
                    continue
                new_link = f"[{dep.artifact_id}]: https://github.com/{org}/{dep.artifact_id}/releases"
                new_links_section.append(new_link)

            previous_category = dep.category

        # Add any existing links that are not in current dependencies and not removed
        # (these might be from older versions still referenced in the changelog)
        orphan_links = []
        for artifact_id, link_line in existing_links.items():
            if artifact_id not in processed_deps and artifact_id not in removed_deps:
                orphan_links.append(link_line.lstrip('\n').rstrip('\n'))

        if orphan_links:
            new_links_section.append('')  # Blank line before orphan links
            new_links_section.extend(orphan_links)

        # Find the artifact links section boundaries
        first_artifact_link = re.search(r'\n\[(keypop|keyple)-[^\]]+\]: ', content)
        if first_artifact_link:
            # Find where artifact links end (before the next section or end of file)
            links_start = first_artifact_link.start()

            # Find the end of all artifact links
            last_artifact_link = None
            for match in re.finditer(r'\n\[(keypop|keyple)-[^\]]+\]: [^\n]+\n', content):
                last_artifact_link = match

            if last_artifact_link:
                links_end = last_artifact_link.end()

                # Replace the entire artifact links section with the new ordered one
                # Join with newlines and add a trailing newline
                new_links_text = '\n' + '\n'.join(new_links_section) + '\n'
                content = (
                    content[:links_start] +
                    new_links_text +
                    content[links_end:]
                )

        return content


def main():
    """Main entry point."""
    # Determine version
    if len(sys.argv) > 1:
        new_version = sys.argv[1]
        # Validate format
        if not re.match(r'^\d{4}\.\d{2}\.\d{2}$', new_version):
            print(f"Error: Invalid version format '{new_version}'. Expected YYYY.MM.DD")
            sys.exit(1)
    else:
        today = date.today()
        new_version = today.strftime("%Y.%m.%d")

    print(f"Updating CHANGELOG.md for version {new_version}...")

    # Parse build.gradle.kts
    gradle_parser = BuildGradleParser("build.gradle.kts")
    dependencies = gradle_parser.parse()
    print(f"Found {len(dependencies)} dependencies in build.gradle.kts")

    # Parse CHANGELOG.md
    changelog_parser = ChangelogParser("CHANGELOG.md")
    old_version, old_entries = changelog_parser.parse_latest_version()
    if old_version:
        print(f"Latest CHANGELOG version: {old_version}")
    else:
        print("No previous version found in CHANGELOG.md")
        old_entries = {}

    # Check if the target version already exists
    if old_version == new_version:
        print(f"Version {new_version} already exists in CHANGELOG.md. No changes needed.")
        sys.exit(0)

    # Generate new section
    generator = ChangelogGenerator("CHANGELOG.md")
    new_section, has_changes = generator.generate_new_section(
        new_version, dependencies, old_entries
    )

    # Update changelog
    success = generator.update_changelog(new_version, new_section, has_changes, dependencies, old_entries)

    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
