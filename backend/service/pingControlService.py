import os


class PingControlService():

    def pingControl(host):
        response = os.system("ping -c 1 " + host)
        if response == 0:
            return "Up"
        else:
            return "Down"
