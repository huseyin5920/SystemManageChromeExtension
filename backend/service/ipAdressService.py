import netifaces as ni


class IpAddressService():
    def getIpAddress():
        ni.ifaddresses('wlp2s0')
        ip = ni.ifaddresses('wlp2s0')[ni.AF_INET][0]['addr']
        return ip
