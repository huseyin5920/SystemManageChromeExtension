import os
import pwd
import grp
import json


class ListUsersService:
    def currentUser():
        # print(pwd.getpwuid(os.getuid())[0])
        # print(pwd.getpwuid(os.getuid()))
        return pwd.getpwuid(os.getuid())[0]

    def listUsers():
        dict = {}
        for p in pwd.getpwall():
            #print(p[0], grp.getgrgid(p[3])[0])
            dict[p[0]] = grp.getgrgid(p[3])[0]
        # print(dict)
        return dict
