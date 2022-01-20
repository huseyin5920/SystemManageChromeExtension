from flask_cors import cross_origin
from service.portControlService import PortControlService
from flask import jsonify, request


@cross_origin()
def getPortInfo():
    port = request.json["port"]
    portInfoResponse = PortControlService.portControl(port)
    return portInfoResponse
