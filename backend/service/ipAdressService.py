import netifaces as ni


class IpAddressService():
    def getIpAddress():
        ni.ifaddresses('wlp0s20f3')
        ip = ni.ifaddresses('wlp0s20f3')[ni.AF_INET][0]['addr']
        return ip
