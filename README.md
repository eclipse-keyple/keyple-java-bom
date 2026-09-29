[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=eclipse-keyple_keyple-java-bom&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=eclipse-keyple_keyple-java-bom)
[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=eclipse-keyple_keyple-java-bom&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=eclipse-keyple_keyple-java-bom)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=eclipse-keyple_keyple-java-bom&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=eclipse-keyple_keyple-java-bom)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=eclipse-keyple_keyple-java-bom&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=eclipse-keyple_keyple-java-bom)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=eclipse-keyple_keyple-java-bom&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=eclipse-keyple_keyple-java-bom)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=eclipse-keyple_keyple-java-bom&metric=coverage)](https://sonarcloud.io/summary/new_code?id=eclipse-keyple_keyple-java-bom)

# Keyple Java BOM

**Eclipse Keyple™ Project**  
A Bill of Materials (BOM) for Java/Kotlin applications to manage the versions of all Keyple artifacts.

---

## 👁️ Overview

The **Keyple Java BOM** provides a centralized way to manage the versions of all Keyple artifacts for Java and Kotlin
applications. It ensures that projects using multiple Keyple libraries stay consistent and compatible without requiring
explicit version declarations for each dependency.

🔎 Note: The BOM also includes the versions of the [Keypop](https://keypop.org/) dependencies required by Keyple, so you
don’t need to manage them separately.

## 📖 Documentation & Contribution Guide

The full documentation, including the **user guide**, **download information** and **contribution guide**, is available
on the Keyple website [keyple.org](https://keyple.org).

## 🚀 Usage

### With **Maven**

Add the Keyple BOM to your `<dependencyManagement>` section:

```xml
<dependencyManagement>
  <dependencies>
    <dependency>
      <groupId>org.eclipse.keyple</groupId>
      <artifactId>keyple-java-bom</artifactId>
      <version>2025.09.12</version>
      <type>pom</type>
      <scope>import</scope>
    </dependency>
  </dependencies>
</dependencyManagement>
```

Then declare the Keyple dependencies without versions:

```xml
<dependencies>
  <!-- Keypop APIs -->
  <dependency>
    <groupId>org.eclipse.keypop</groupId>
    <artifactId>keypop-reader-java-api</artifactId>
  </dependency>
  ...
  <!-- Keyple components -->
  <dependency>
    <groupId>org.eclipse.keyple</groupId>
    <artifactId>keyple-common-java-api</artifactId>
  </dependency>
  <dependency>
    <groupId>org.eclipse.keyple</groupId>
    <artifactId>keyple-service-java-lib</artifactId>
  </dependency>
  ...
</dependencies>
```

### With **Gradle**

Import the BOM as a platform:

```kotlin
dependencies {
  implementation(platform("org.eclipse.keyple:keyple-java-bom:2025.09.12"))
  // Keypop APIs
  implementation("org.eclipse.keypop:keypop-reader-java-api")
  ...
  // Keyple components
  implementation("org.eclipse.keyple:keyple-common-java-api")
  implementation("org.eclipse.keyple:keyple-service-java-lib")
  ...
}
```

## 📝 Versioning

This project follows a date-based versioning scheme:
- **Format**: `YYYY.MM.DD` (year, month, day).
- **Release cadence**: A new version is released whenever one or more Keyple artifacts are updated.
- **Interpretation**: The version number indicates the release date, not the compatibility level.
  → Users should check the release notes to see which artifacts were updated.

### Keyple Distributed libraries

The three libraries of the **Keyple Distributed** solution
([keyple-distributed-network-java-lib](https://github.com/eclipse-keyple/keyple-distributed-network-java-lib),
[keyple-distributed-local-java-lib](https://github.com/eclipse-keyple/keyple-distributed-local-java-lib) and
[keyple-distributed-remote-java-lib](https://github.com/eclipse-keyple/keyple-distributed-remote-java-lib)) form a
single component split into several artifacts and rely on internal contracts of each other. Their versions are aligned
according to the following rules:
- The three libraries always share the same **major** and **minor** version numbers (e.g. `2.6.x`), and are released
  together for each new major or minor version.
- **Patch** versions are independent (e.g. `keyple-distributed-local-java-lib` `2.6.1` with
  `keyple-distributed-network-java-lib` `2.6.0`).

Each version of this BOM therefore references the three Keyple Distributed libraries with the same major and minor
version numbers. Applications importing the BOM automatically get a consistent set; applications declaring the versions
explicitly must follow the same rule.

## 🤖 Continuous Integration

This project uses **GitHub Actions** for continuous integration. Every push and pull request triggers automated builds
and checks to ensure code quality and maintain compatibility with the defined specifications.
