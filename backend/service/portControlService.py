import subprocess
import socket


class PortControlService:
    def portControl(port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(2)  # 2 Second Timeout
        result = sock.connect_ex(('127.0.0.1', port))
        if result == 0:
            #print('port OPEN')
            return str(1)
        else:
            #print('port CLOSE')
            return str(0)
