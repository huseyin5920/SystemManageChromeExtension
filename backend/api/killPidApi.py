from flask_cors import cross_origin
from service.killPid import KillPidService
from flask import jsonify, request


@cross_origin()
def killPid():
    pid = request.json["pid"]
    pidKillResponse = KillPidService.killPidApp(pid)
    return pidKillResponse
