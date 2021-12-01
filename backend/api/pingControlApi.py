from flask_cors import cross_origin
from service.pingControlService import PingControlService
from flask import jsonify, request


@cross_origin()
def getpingInfo():
    host = request.json["host"]
    portInfoResponse = PingControlService.pingControl(host)
    print(portInfoResponse)
    return portInfoResponse
