from flask_cors import cross_origin
from flask import request, jsonify, Blueprint
from service.showOpenWindowsService import ShowOpenWindowsService


@cross_origin()
def showOpenWindow():
    showOpenWindowResponse = ShowOpenWindowsService.showOpenWindow()
    return jsonify(showOpenWindowResponse)
