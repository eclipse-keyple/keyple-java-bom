///////////////////////////////////////////////////////////////////////////////
//  GRADLE CONFIGURATION
///////////////////////////////////////////////////////////////////////////////

if (project.hasProperty("releaseTag")) {
  project.version = project.property("releaseTag") as String
  println("Release mode: version set to ${project.version}")
} else {
  println("Development mode: version is ${project.version}")
}

plugins {
  `java-platform`
  `maven-publish`
  signing
  id("com.diffplug.spotless") version "6.25.0"
}

javaPlatform { allowDependencies() }

///////////////////////////////////////////////////////////////////////////////
//  APP CONFIGURATION
///////////////////////////////////////////////////////////////////////////////

dependencies {
  constraints {
    // Keypop
    api("org.eclipse.keypop:keypop-reader-java-api:2.0.1")
    api("org.eclipse.keypop:keypop-calypso-card-java-api:2.1.2")
    api("org.eclipse.keypop:keypop-calypso-crypto-legacysam-java-api:0.7.0")
    api("org.eclipse.keypop:keypop-storagecard-java-api:0.3.0")
    // Keyple core
    api("org.eclipse.keyple:keyple-common-java-api:2.0.2")
    api("org.eclipse.keyple:keyple-plugin-storagecard-java-api:1.0.0")
    api("org.eclipse.keyple:keyple-service-java-lib:3.3.5")
    api("org.eclipse.keyple:keyple-service-resource-java-lib:3.1.0")
    api("org.eclipse.keyple:keyple-util-java-lib:2.4.0")
    // Keyple distributed
    api("org.eclipse.keyple:keyple-distributed-local-java-lib:2.5.2")
    api("org.eclipse.keyple:keyple-distributed-network-java-lib:2.5.1")
    api("org.eclipse.keyple:keyple-distributed-remote-java-lib:2.5.1")
    // Keyple interop
    api("org.eclipse.keyple:keyple-interop-jsonapi-client-kmp-lib:0.1.6")
    api("org.eclipse.keyple:keyple-interop-jsonapi-client-kmp-lib-jvm:0.1.6")
    api("org.eclipse.keyple:keyple-interop-jsonapi-client-kmp-lib-android:0.1.6")
    api("org.eclipse.keyple:keyple-interop-jsonapi-client-kmp-lib-iosarm64:0.1.6")
    api("org.eclipse.keyple:keyple-interop-jsonapi-client-kmp-lib-iossimulatorarm64:0.1.6")
    api("org.eclipse.keyple:keyple-interop-jsonapi-client-kmp-lib-iosx64:0.1.6")
    api("org.eclipse.keyple:keyple-interop-localreader-nfcmobile-kmp-lib:0.1.6")
    api("org.eclipse.keyple:keyple-interop-localreader-nfcmobile-kmp-lib-jvm:0.1.6")
    api("org.eclipse.keyple:keyple-interop-localreader-nfcmobile-kmp-lib-android:0.1.6")
    api("org.eclipse.keyple:keyple-interop-localreader-nfcmobile-kmp-lib-iosarm64:0.1.6")
    api("org.eclipse.keyple:keyple-interop-localreader-nfcmobile-kmp-lib-iossimulatorarm64:0.1.6")
    api("org.eclipse.keyple:keyple-interop-localreader-nfcmobile-kmp-lib-iosx64:0.1.6")
    // Keyple card extensions
    api("org.eclipse.keyple:keyple-card-calypso-java-lib:3.1.9")
    api("org.eclipse.keyple:keyple-card-calypso-crypto-legacysam-java-lib:0.9.0")
    api("org.eclipse.keyple:keyple-card-calypso-crypto-pki-java-lib:0.2.3")
    api("org.eclipse.keyple:keyple-card-generic-java-lib:3.1.2")
    // Keyple reader plugins
    api("org.eclipse.keyple:keyple-plugin-android-nfc-java-lib:3.1.0")
    api("org.eclipse.keyple:keyple-plugin-android-omapi-java-lib:2.1.0")
    api("org.eclipse.keyple:keyple-plugin-cardresource-java-lib:2.0.1")
    api("org.eclipse.keyple:keyple-plugin-pcsc-java-lib:2.5.2")
    api("org.eclipse.keyple:keyple-plugin-stub-java-lib:2.2.1")
  }
}

///////////////////////////////////////////////////////////////////////////////
//  STANDARD CONFIGURATION FOR BOM PROJECTS
///////////////////////////////////////////////////////////////////////////////

tasks {
  spotless {
    kotlinGradle {
      target("**/*.kts")
      ktfmt()
    }
  }
}

publishing {
  publications {
    create<MavenPublication>("bom") {
      from(components["javaPlatform"])
      pom {
        name.set(project.findProperty("title") as String)
        description.set(project.findProperty("description") as String)
        url.set(project.findProperty("project.url") as String)
        licenses {
          license {
            name.set(project.findProperty("license.name") as String)
            url.set(project.findProperty("license.url") as String)
            distribution.set(project.findProperty("license.distribution") as String)
          }
        }
        developers {
          developer {
            name.set(project.findProperty("developer.name") as String)
            email.set(project.findProperty("developer.email") as String)
          }
        }
        organization {
          name.set(project.findProperty("organization.name") as String)
          url.set(project.findProperty("organization.url") as String)
        }
        scm {
          connection.set(project.findProperty("scm.connection") as String)
          developerConnection.set(project.findProperty("scm.developerConnection") as String)
          url.set(project.findProperty("scm.url") as String)
        }
        ciManagement {
          system.set(project.findProperty("ci.system") as String)
          url.set(project.findProperty("ci.url") as String)
        }
        properties.set(mapOf("project.build.sourceEncoding" to "UTF-8"))
      }
    }
  }
  repositories {
    maven {
      if (project.hasProperty("sonatypeURL")) {
        url = uri(project.property("sonatypeURL") as String)
        credentials {
          username = project.property("sonatypeUsername") as String
          password = project.property("sonatypePassword") as String
        }
      }
    }
  }
}

signing {
  if (project.hasProperty("releaseTag")) {
    useGpgCmd()
    sign(publishing.publications["javaPlatform"])
  }
}
