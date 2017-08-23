package NetworkAutomationCourse.buildTypes

import jetbrains.buildServer.configs.kotlin.v10.*
import jetbrains.buildServer.configs.kotlin.v10.triggers.VcsTrigger
import jetbrains.buildServer.configs.kotlin.v10.triggers.VcsTrigger.*
import jetbrains.buildServer.configs.kotlin.v10.triggers.vcs

object NetworkAutomationCourse_Build : BuildType({
    uuid = "9743d336-e7b7-41d7-b8ac-60be10d782b8"
    extId = "NetworkAutomationCourse_Build"
    name = "Building888"

    vcs {
        root("NetworkAutomationCourse_HttpsGithubComSamerLabbanNetworkAutomationCourseRefsHead")

    }

    triggers {
        vcs {
        }
    }
})
