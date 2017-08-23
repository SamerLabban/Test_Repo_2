package NetworkAutomationCourse

import NetworkAutomationCourse.buildTypes.*
import jetbrains.buildServer.configs.kotlin.v10.*
import jetbrains.buildServer.configs.kotlin.v10.Project

object Project : Project({
    uuid = "5292ab8b-61b0-4dc5-8e86-e25cdee869f7"
    extId = "NetworkAutomationCourse"
    parentId = "_Root"
    name = "Network Automation Course"

    buildType(NetworkAutomationCourse_Build)
})
