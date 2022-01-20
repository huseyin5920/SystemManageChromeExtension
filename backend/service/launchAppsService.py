import os


class LaunchAppsService():
    def launchVsCode(appName):
        os.system(appName)
        return "successful"
