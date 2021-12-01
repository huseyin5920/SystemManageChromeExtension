from flask_cors import cross_origin
from service.processControlService import ProcessControlService
from flask import jsonify, request


@cross_origin()
def getProcessInfo():
    processName = request.json["processName"]
    processInfoResponse = ProcessControlService.checkProcessStatus(processName)
    # print(processInfoResponse)
    return processInfoResponse
