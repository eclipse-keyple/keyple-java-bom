# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project uses a **date-based versioning scheme** (`YYYY.MM.DD`).

Legend: 🆕 New • ❌ Removed • 🟢 Patch • 🔵 Minor • 🔴 Major

## [Unreleased]

## [2026.03.16]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.1.0` |        |                  |
| [keypop-calypso-card-java-api]                  | `2.2.0` |        |                  |
| [keypop-calypso-crypto-legacysam-java-api]      | `1.0.0` |        |                  |
| [keypop-storagecard-java-api]                   | `1.1.1` |        |                  |
| [keypop-genericcard-jvm-api]                    | `1.0.0` |   🆕   |                  |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.1.0` |        |                  |
| [keyple-service-java-lib]                       | `3.4.1` |        |                  |
| [keyple-service-resource-java-lib]              | `3.1.1` |        |                  |
| [keyple-util-java-lib]                          | `2.4.1` |        |                  |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.3` |        |                  |
| [keyple-distributed-network-java-lib]           | `2.5.2` |        |                  |
| [keyple-distributed-remote-java-lib]            | `2.5.2` |        |                  |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.2.2` |        |                  |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `1.0.1` |        |                  |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.4` |        |                  |
| [keyple-card-generic-java-lib]                  | `4.0.0` |   🔴   |     `3.2.1`      |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.2.2` |        |                  |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.1` |        |                  |
| [keyple-plugin-cardresource-java-lib]           | `2.0.2` |        |                  |
| [keyple-plugin-pcsc-java-lib]                   | `2.6.2` |        |                  |
| [keyple-plugin-stub-java-lib]                   | `2.2.2` |        |                  |

## [2026.02.20]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.1.0` |        |                  |
| [keypop-calypso-card-java-api]                  | `2.2.0` |        |                  |
| [keypop-calypso-crypto-legacysam-java-api]      | `1.0.0` |        |                  |
| [keypop-storagecard-java-api]                   | `1.1.1` |   🔵   |     `1.0.0`      |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.1.0` |   🔵   |     `1.0.0`      |
| [keyple-service-java-lib]                       | `3.4.1` |   🟢   |     `3.4.0`      |
| [keyple-service-resource-java-lib]              | `3.1.1` |   🟢   |     `3.1.0`      |
| [keyple-util-java-lib]                          | `2.4.1` |   🟢   |     `2.4.0`      |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.3` |   🟢   |     `2.5.2`      |
| [keyple-distributed-network-java-lib]           | `2.5.2` |   🟢   |     `2.5.1`      |
| [keyple-distributed-remote-java-lib]            | `2.5.2` |   🟢   |     `2.5.1`      |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.2.2` |   🟢   |     `3.2.1`      |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `1.0.1` |   🟢   |     `1.0.0`      |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.4` |   🟢   |     `0.2.3`      |
| [keyple-card-generic-java-lib]                  | `3.2.1` |   🟢   |     `3.2.0`      |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.2.2` |   🔵   |     `3.1.0`      |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.1` |   🟢   |     `2.1.0`      |
| [keyple-plugin-cardresource-java-lib]           | `2.0.2` |   🟢   |     `2.0.1`      |
| [keyple-plugin-pcsc-java-lib]                   | `2.6.2` |   🟢   |     `2.6.0`      |
| [keyple-plugin-stub-java-lib]                   | `2.2.2` |   🟢   |     `2.2.1`      |

## [2025.12.12]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.1.0` |        |                  |
| [keypop-calypso-card-java-api]                  | `2.2.0` |        |                  |
| [keypop-calypso-crypto-legacysam-java-api]      | `1.0.0` |        |                  |
| [keypop-storagecard-java-api]                   | `1.0.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.0.0` |        |                  |
| [keyple-service-java-lib]                       | `3.4.0` |        |                  |
| [keyple-service-resource-java-lib]              | `3.1.0` |        |                  |
| [keyple-util-java-lib]                          | `2.4.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.2` |        |                  |
| [keyple-distributed-network-java-lib]           | `2.5.1` |        |                  |
| [keyple-distributed-remote-java-lib]            | `2.5.1` |        |                  |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.2.1` |   🟢   |     `3.2.0`      |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `1.0.0` |        |                  |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.3` |        |                  |
| [keyple-card-generic-java-lib]                  | `3.2.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.1.0` |        |                  |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.0` |        |                  |
| [keyple-plugin-cardresource-java-lib]           | `2.0.1` |        |                  |
| [keyple-plugin-pcsc-java-lib]                   | `2.6.0` |   🔵   |     `2.5.3`      |
| [keyple-plugin-stub-java-lib]                   | `2.2.1` |        |                  |

## [2025.11.21]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.1.0` |   🔵   |     `2.0.1`      |
| [keypop-calypso-card-java-api]                  | `2.2.0` |   🔵   |     `2.1.2`      |
| [keypop-calypso-crypto-legacysam-java-api]      | `1.0.0` |   🔴   |     `0.7.0`      |
| [keypop-storagecard-java-api]                   | `1.0.0` |   🔴   |     `0.3.0`      |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.0.0` |        |                  |
| [keyple-service-java-lib]                       | `3.4.0` |   🔵   |     `3.3.7`      |
| [keyple-service-resource-java-lib]              | `3.1.0` |        |                  |
| [keyple-util-java-lib]                          | `2.4.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.2` |        |                  |
| [keyple-distributed-network-java-lib]           | `2.5.1` |        |                  |
| [keyple-distributed-remote-java-lib]            | `2.5.1` |        |                  |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.2.0` |   🔵   |     `3.1.9`      |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `1.0.0` |   🔴   |     `0.9.1`      |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.3` |        |                  |
| [keyple-card-generic-java-lib]                  | `3.2.0` |   🔵   |     `3.1.3`      |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.1.0` |        |                  |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.0` |        |                  |
| [keyple-plugin-cardresource-java-lib]           | `2.0.1` |        |                  |
| [keyple-plugin-pcsc-java-lib]                   | `2.5.3` |        |                  |
| [keyple-plugin-stub-java-lib]                   | `2.2.1` |        |                  |

## [2025.11.13]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.0.1` |        |                  |
| [keypop-calypso-card-java-api]                  | `2.1.2` |        |                  |
| [keypop-calypso-crypto-legacysam-java-api]      | `0.7.0` |        |                  |
| [keypop-storagecard-java-api]                   | `0.3.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.0.0` |        |                  |
| [keyple-service-java-lib]                       | `3.3.7` |   🟢   |     `3.3.6`      |
| [keyple-service-resource-java-lib]              | `3.1.0` |        |                  |
| [keyple-util-java-lib]                          | `2.4.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.2` |        |                  |
| [keyple-distributed-network-java-lib]           | `2.5.1` |        |                  |
| [keyple-distributed-remote-java-lib]            | `2.5.1` |        |                  |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.1.9` |        |                  |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `0.9.1` |   🟢   |     `0.9.0`      |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.3` |        |                  |
| [keyple-card-generic-java-lib]                  | `3.1.3` |        |                  |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.1.0` |        |                  |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.0` |        |                  |
| [keyple-plugin-cardresource-java-lib]           | `2.0.1` |        |                  |
| [keyple-plugin-pcsc-java-lib]                   | `2.5.3` |        |                  |
| [keyple-plugin-stub-java-lib]                   | `2.2.1` |        |                  |

## [2025.11.12]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.0.1` |        |                  |
| [keypop-calypso-card-java-api]                  | `2.1.2` |        |                  |
| [keypop-calypso-crypto-legacysam-java-api]      | `0.7.0` |        |                  |
| [keypop-storagecard-java-api]                   | `0.3.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.0.0` |        |                  |
| [keyple-service-java-lib]                       | `3.3.6` |        |                  |
| [keyple-service-resource-java-lib]              | `3.1.0` |        |                  |
| [keyple-util-java-lib]                          | `2.4.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.2` |        |                  |
| [keyple-distributed-network-java-lib]           | `2.5.1` |        |                  |
| [keyple-distributed-remote-java-lib]            | `2.5.1` |        |                  |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.1.9` |        |                  |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `0.9.0` |        |                  |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.3` |        |                  |
| [keyple-card-generic-java-lib]                  | `3.1.3` |   🟢   |     `3.1.2`      |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.1.0` |        |                  |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.0` |        |                  |
| [keyple-plugin-cardresource-java-lib]           | `2.0.1` |        |                  |
| [keyple-plugin-pcsc-java-lib]                   | `2.5.3` |        |                  |
| [keyple-plugin-stub-java-lib]                   | `2.2.1` |        |                  |

## [2025.10.24]

| Component                                       | Version | Status | Prev.<br>Version |
|:------------------------------------------------|:-------:|:------:|:----------------:|
| **Keypop Dependencies**                         |         |        |                  |
| [keypop-reader-java-api]                        | `2.0.1` |        |                  |
| [keypop-calypso-card-java-api]                  | `2.1.2` |        |                  |
| [keypop-calypso-crypto-legacysam-java-api]      | `0.7.0` |        |                  |
| [keypop-storagecard-java-api]                   | `0.3.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Core**                                 |         |        |                  |
| [keyple-common-java-api]                        | `2.0.2` |        |                  |
| [keyple-plugin-storagecard-java-api]            | `1.0.0` |        |                  |
| [keyple-service-java-lib]                       | `3.3.6` |   🟢   |     `3.3.5`      |
| [keyple-service-resource-java-lib]              | `3.1.0` |        |                  |
| [keyple-util-java-lib]                          | `2.4.0` |        |                  |
|                                                 |         |        |                  |
| **Keyple Distributed**                          |         |        |                  |
| [keyple-distributed-local-java-lib]             | `2.5.2` |        |                  |
| [keyple-distributed-network-java-lib]           | `2.5.1` |        |                  |
| [keyple-distributed-remote-java-lib]            | `2.5.1` |        |                  |
|                                                 |         |        |                  |
| **Keyple Interop**                              |         |        |                  |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |        |                  |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |        |                  |
|                                                 |         |        |                  |
| **Keyple Card Extensions**                      |         |        |                  |
| [keyple-card-calypso-java-lib]                  | `3.1.9` |        |                  |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `0.9.0` |        |                  |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.3` |        |                  |
| [keyple-card-generic-java-lib]                  | `3.1.2` |        |                  |
|                                                 |         |        |                  |
| **Keyple Reader Plugins**                       |         |        |                  |
| [keyple-plugin-android-nfc-java-lib]            | `3.1.0` |        |                  |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.0` |        |                  |
| [keyple-plugin-cardresource-java-lib]           | `2.0.1` |        |                  |
| [keyple-plugin-pcsc-java-lib]                   | `2.5.3` |   🟢   |     `2.5.2`      |
| [keyple-plugin-stub-java-lib]                   | `2.2.1` |        |                  |

## [2025.09.12]
First publication of the **Keyple Java BOM**.  
This release defines a consistent set of versions for **Keyple** and **Keypop** artifacts.

| Component                                       | Version | Status |
|:------------------------------------------------|:-------:|:------:|
| **Keypop Dependencies**                         |         |        |
| [keypop-reader-java-api]                        | `2.0.1` |   🆕   |
| [keypop-calypso-card-java-api]                  | `2.1.2` |   🆕   |
| [keypop-calypso-crypto-legacysam-java-api]      | `0.7.0` |   🆕   |
| [keypop-storagecard-java-api]                   | `0.3.0` |   🆕   |
|                                                 |         |        |
| **Keyple Core**                                 |         |        |
| [keyple-common-java-api]                        | `2.0.2` |   🆕   |
| [keyple-plugin-storagecard-java-api]            | `1.0.0` |   🆕   |
| [keyple-service-java-lib]                       | `3.3.5` |   🆕   |
| [keyple-service-resource-java-lib]              | `3.1.0` |   🆕   |
| [keyple-util-java-lib]                          | `2.4.0` |   🆕   |
|                                                 |         |        |
| **Keyple Distributed**                          |         |        |
| [keyple-distributed-local-java-lib]             | `2.5.2` |   🆕   |
| [keyple-distributed-network-java-lib]           | `2.5.1` |   🆕   |
| [keyple-distributed-remote-java-lib]            | `2.5.1` |   🆕   |
|                                                 |         |        |
| **Keyple Interop**                              |         |        |
| [keyple-interop-jsonapi-client-kmp-lib]         | `0.1.6` |   🆕   |
| [keyple-interop-localreader-nfcmobile-kmp-lib]  | `0.1.6` |   🆕   |
|                                                 |         |        |
| **Keyple Card Extensions**                      |         |        |
| [keyple-card-calypso-java-lib]                  | `3.1.9` |   🆕   |
| [keyple-card-calypso-crypto-legacysam-java-lib] | `0.9.0` |   🆕   |
| [keyple-card-calypso-crypto-pki-java-lib]       | `0.2.3` |   🆕   |
| [keyple-card-generic-java-lib]                  | `3.1.2` |   🆕   |
|                                                 |         |        |
| **Keyple Reader Plugins**                       |         |        |
| [keyple-plugin-android-nfc-java-lib]            | `3.1.0` |   🆕   |
| [keyple-plugin-android-omapi-java-lib]          | `2.1.0` |   🆕   |
| [keyple-plugin-cardresource-java-lib]           | `2.0.1` |   🆕   |
| [keyple-plugin-pcsc-java-lib]                   | `2.5.2` |   🆕   |
| [keyple-plugin-stub-java-lib]                   | `2.2.1` |   🆕   |

[Unreleased]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2026.03.16...HEAD
[2026.03.16]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2026.02.20...2026.03.16
[2026.02.20]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.12.12...2026.02.20
[2025.12.12]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.11.21...2025.12.12
[2025.11.21]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.11.13...2025.11.21
[2025.11.13]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.11.12...2025.11.13
[2025.11.12]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.10.24...2025.11.12
[2025.10.24]: https://github.com/eclipse-keyple/keyple-java-bom/compare/2025.09.12...2025.10.24
[2025.09.12]: https://github.com/eclipse-keyple/keyple-java-bom/releases/tag/2025.09.12

[keypop-reader-java-api]: https://github.com/eclipse-keypop/keypop-reader-java-api/releases
[keypop-calypso-card-java-api]: https://github.com/eclipse-keypop/keypop-calypso-card-java-api/releases
[keypop-calypso-crypto-legacysam-java-api]: https://github.com/eclipse-keypop/keypop-calypso-crypto-legacysam-java-api/releases
[keypop-storagecard-java-api]: https://github.com/eclipse-keypop/keypop-storagecard-java-api/releases
[keypop-genericcard-jvm-api]: https://github.com/eclipse-keypop/keypop-genericcard-jvm-api/releases

[keyple-common-java-api]: https://github.com/eclipse-keyple/keyple-common-java-api/releases
[keyple-plugin-storagecard-java-api]: https://github.com/eclipse-keyple/keyple-plugin-storagecard-java-api/releases
[keyple-service-java-lib]: https://github.com/eclipse-keyple/keyple-service-java-lib/releases
[keyple-service-resource-java-lib]: https://github.com/eclipse-keyple/keyple-service-resource-java-lib/releases
[keyple-util-java-lib]: https://github.com/eclipse-keyple/keyple-util-java-lib/releases

[keyple-distributed-local-java-lib]: https://github.com/eclipse-keyple/keyple-distributed-local-java-lib/releases
[keyple-distributed-network-java-lib]: https://github.com/eclipse-keyple/keyple-distributed-network-java-lib/releases
[keyple-distributed-remote-java-lib]: https://github.com/eclipse-keyple/keyple-distributed-remote-java-lib/releases

[keyple-interop-jsonapi-client-kmp-lib]: https://github.com/eclipse-keyple/keyple-interop-jsonapi-client-kmp-lib/releases
[keyple-interop-localreader-nfcmobile-kmp-lib]: https://github.com/eclipse-keyple/keyple-interop-localreader-nfcmobile-kmp-lib/releases

[keyple-card-calypso-java-lib]: https://github.com/eclipse-keyple/keyple-card-calypso-java-lib/releases
[keyple-card-calypso-crypto-legacysam-java-lib]: https://github.com/eclipse-keyple/keyple-card-calypso-crypto-legacysam-java-lib/releases
[keyple-card-calypso-crypto-pki-java-lib]: https://github.com/eclipse-keyple/keyple-card-calypso-crypto-pki-java-lib/releases
[keyple-card-generic-java-lib]: https://github.com/eclipse-keyple/keyple-card-generic-java-lib/releases

[keyple-plugin-android-nfc-java-lib]: https://github.com/eclipse-keyple/keyple-plugin-android-nfc-java-lib/releases
[keyple-plugin-android-omapi-java-lib]: https://github.com/eclipse-keyple/keyple-plugin-android-omapi-java-lib/releases
[keyple-plugin-cardresource-java-lib]: https://github.com/eclipse-keyple/keyple-plugin-cardresource-java-lib/releases
[keyple-plugin-pcsc-java-lib]: https://github.com/eclipse-keyple/keyple-plugin-pcsc-java-lib/releases
[keyple-plugin-stub-java-lib]: https://github.com/eclipse-keyple/keyple-plugin-stub-java-lib/releases
