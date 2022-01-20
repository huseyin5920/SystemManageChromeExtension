from flask_cors import cross_origin
from service.userDelCreService import CreateUserService
from flask import jsonify, request


@cross_origin()
def createUser():
    name = request.json["name"]
    username = request.json["username"]
    password = request.json["password"]
    responseCreateUserService = CreateUserService.createUser(name, username, password)
    return responseCreateUserService


@cross_origin()
def deleteUser():
    username = request.json["username"]
    responseDeleteUserService = CreateUserService.deleteUser(username)
    return responseDeleteUserService
