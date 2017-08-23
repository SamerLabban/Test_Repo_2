package NetworkAutomationCourse

import NetworkAutomationCourse.buildTypes.*
import jetbrains.buildServer.configs.kotlin.v10.*
import jetbrains.buildServer.configs.kotlin.v10.Project
import jetbrains.buildServer.configs.kotlin.v10.projectFeatures.VersionedSettings
import jetbrains.buildServer.configs.kotlin.v10.projectFeatures.VersionedSettings.*
import jetbrains.buildServer.configs.kotlin.v10.projectFeatures.versionedSettings

object Project : Project({
    uuid = "5292ab8b-61b0-4dc5-8e86-e25cdee869f7"
    extId = "NetworkAutomationCourse"
    parentId = "_Root"
    name = "Network Automation Course"

    buildType(NetworkAutomationCourse_Build)

    features {
        versionedSettings {
            id = "PROJECT_EXT_6"
            mode = VersionedSettings.Mode.ENABLED
            buildSettingsMode = VersionedSettings.BuildSettingsMode.USE_CURRENT_SETTINGS
            rootExtId = "NetworkAutomationCourse_HttpsGithubComSamerLabbanNetworkAutomationCourseRefsHead"
            showChanges = false
            settingsFormat = VersionedSettings.Format.KOTLIN
            param("credentialsStorageType", "credentialsJSON")
        }
    }
})
