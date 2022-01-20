from flask_cors import cross_origin
from service.launchAppsService import LaunchAppsService
from flask import jsonify, request


@cross_origin()
def launchApp():
    appName = request.json["appName"]
    launchAppResponse = LaunchAppsService.launchVsCode(appName)
    return launchAppResponse
