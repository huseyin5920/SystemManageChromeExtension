from flask_cors import cross_origin
from flask import Flask, jsonify, request
from service.topCommandService import TopCommandService
from service.listUsersService import ListUsersService


@cross_origin()
def topCommandByMemory():
    topMemoryResponse = TopCommandService.memoryFunc()
    return topMemoryResponse


@cross_origin()
def topCommandByCpu():
    topCpuResponse = TopCommandService.cpuFunc()
    print(type(topCpuResponse))
    return jsonify(topCpuResponse)


@cross_origin()
def topCommandListByUserCpu():
    user = request.json["user"]
    topCurrentUserResponse = TopCommandService.listByUserCpu(user)
    return topCurrentUserResponse


@cross_origin()
def topCommandListByUserMemory():
    user = request.json["user"]
    topCurrentUserResponse = TopCommandService.listByUserMemory(user)
    return topCurrentUserResponse


@cross_origin()
def topCommandByCurrentUser():
    topCurrentUserResponse = ListUsersService.currentUser()
    return topCurrentUserResponse


@cross_origin()
def topCommandListUsers():
    topCurrentUserResponse = ListUsersService.listUsers()
    return topCurrentUserResponse
