# Automatic CHANGELOG Update Script

## Description

`update_changelog.py` is a Python script that **automates the update** of the `CHANGELOG.md` file based on version changes detected in `build.gradle.kts`.

## Features

- **Automatic change detection** between `build.gradle.kts` and the latest version in `CHANGELOG.md`:
  - 🆕 **New dependencies**: automatically detected
  - ❌ **Removed dependencies**: displayed in their original category with their last version
  - 🟢 **Patch**: x.y.z → x.y.(z+n)
  - 🔵 **Minor**: x.y.z → x.(y+n).z
  - 🔴 **Major**: x.y.z → (x+n).y.z
- Grouping of KMP libraries (a single line for the base library)
- Preservation of the dependencies' order as defined in `build.gradle.kts`
- **Automatic update of reference links**:
  - Version links `[Unreleased]` and `[version]`
  - Automatic addition of links for new dependencies (from organization eclipse-keypop or eclipse-keyple)
  - Automatic removal of links for dependencies that have been dropped
- Compliance with the "Keep a Changelog" format

-----

## Prerequisites

- Python 3.7 or higher
- The `build.gradle.kts` and `CHANGELOG.md` files must be located at the project root

-----

## Usage

**Important**: The script must be executed from the project root directory.

### Basic Usage (Current Date)

```bash
# On Windows
.\tools\update_changelog.bat

# On Linux/Mac
./tools/update_changelog.sh

# With Python directly (all systems)
python tools/update_changelog.py
```

This command uses the current date in the format `YYYY.MM.DD` as the version number.

### Specifying a Custom Date

```bash
# On Windows
.\tools\update_changelog.bat 2025.10.30

# On Linux/Mac
./tools/update_changelog.sh 2025.10.30

# With Python directly (all systems)
python tools/update_changelog.py 2025.10.30
```

The date format must be `YYYY.MM.DD`.

-----

## Behavior

1.  **Dependency Parsing**: The script analyzes `build.gradle.kts` and extracts all dependencies while preserving their order
2.  **Comparison**: It compares these versions with those in the latest section of `CHANGELOG.md`
3.  **Change Detection**:
  - If no changes are detected: displays a message and makes no modification
  - If changes are detected: creates a new section with the appropriate statuses
4.  **Update**: Adds the new section after `[Unreleased]` and updates the reference links

-----

## Examples

### Example 1: No Changes

```bash
$ python tools/update_changelog.py
Updating CHANGELOG.md for version 2025.10.23...
Found 23 dependencies in build.gradle.kts
Latest CHANGELOG version: 2025.10.23
No changes detected between build.gradle.kts and the latest CHANGELOG version.
```

### Example 2: With Changes

```bash
$ python tools/update_changelog.py 2025.10.30
Updating CHANGELOG.md for version 2025.10.30...
Found 23 dependencies in build.gradle.kts
Latest CHANGELOG version: 2025.10.23
CHANGELOG.md updated successfully with version 2025.10.30
```

The `CHANGELOG.md` file will be updated with:

- A new section `## [2025.10.30]`
- The statuses 🟢/🔵/🔴 for each modified component
- The "Prev. Version" column showing the old version
- Updated links:
  ```
  [Unreleased]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.10.30...HEAD
  [2025.10.30]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.10.23...2025.10.30
  ```

-----

## Generated Structure

The new section follows this format:

```markdown
## [2025.10.30]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies** |         |        |                  |
| [keypop-reader-java-api]                        | `2.0.1` |        |                  |
| ...                                             |         |        |                  |
|                                                 |         |        |                  |
| **Keyple Core** |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-service-java-lib]                       | `3.4.0` |   🔵   |     `3.3.6`      |
| [keyple-service-resource-java-lib]              | `4.0.0` |   🔴   |     `3.1.0`      |
| [keyple-test-java-lib]                          | `1.0.0` |   🆕   |                  |
| [keyple-util-java-lib]                          | `2.4.0` |   ❌   |                  |
| ...                                             |         |        |                  |
```

In this example:

- `keyple-service-java-lib`: Minor change (3.3.6 → 3.4.0) marked 🔵
- `keyple-service-resource-java-lib`: Major change (3.1.0 → 4.0.0) marked 🔴
- `keyple-test-java-lib`: New dependency marked 🆕
- `keyple-util-java-lib`: Removed dependency marked ❌

### Reference Links Update

The script also automatically updates the links at the bottom of the file:

```markdown
[Unreleased]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.10.30...HEAD
[2025.10.30]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.10.23...2025.10.30

[keypop-reader-java-api]: https://github.com/eclipse-keypop/keypop-reader-java-api/releases
...
[keyple-test-java-lib]: https://github.com/eclipse-keyple/keyple-test-java-lib/releases
...
```

- **New dependencies**: the link is automatically added in the appropriate section (eclipse-keypop or eclipse-keyple)
- **Removed dependencies**: the link is automatically removed

-----

## Notes

- The script respects the exact order of dependencies as defined in `build.gradle.kts`
- KMP libraries with variants (-jvm, -android, -iosarm64, etc.) are grouped into a single line
- Only components whose version has changed will have a status and a value in "Prev. Version"
- New dependencies (🆕) and version changes (🟢🔵🔴) appear in the order of the `build.gradle.kts` file
- Removed dependencies (❌) appear after the current dependencies of their original category
- If an entire category is removed, it appears at the end of the table with its dependencies marked ❌