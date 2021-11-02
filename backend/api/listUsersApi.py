from flask_cors import cross_origin
from service.listUsersService import ListUsersService


@cross_origin()
def topCommandByCurrentUser():
    topCurrentUserResponse = ListUsersService.currentUser()
    return topCurrentUserResponse


@cross_origin()
def topCommandListUsers():
    topCurrentUserResponse = ListUsersService.listUsers()
    return topCurrentUserResponse
