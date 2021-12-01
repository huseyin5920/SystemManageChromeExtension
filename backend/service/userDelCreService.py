import crypt
import os

import subprocess
import sys


class CreateUserService():
    def createUser(name, username, password):
        try:
            encPass = crypt.crypt(password, "22")
            os.system(
                "sudo useradd -p " + encPass + " -s " + "/bin/bash " + "-d " + "/home/" + username + " -m " + " -c \"" + name +
                "\" " + username)
            return "successful"

        except Exception as e:
            print(e)
            return "error"

    def deleteUser(username):
        try:
            output = subprocess.run(['userdel', username])
            if output.returncode == 0:
                print("User successfully deleted with given credentials")
                return "successful"
            else:
                return "error"

        except:
            print(f"Failed to delete user.")
            sys.exit(1)
