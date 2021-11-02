from flask_cors import cross_origin
from service.ipAdressService import IpAddressService


@cross_origin()
def getIpAddress():
    ipAddressResponse = IpAddressService.getIpAddress()
    return ipAddressResponse
