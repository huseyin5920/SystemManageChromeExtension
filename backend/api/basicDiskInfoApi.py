from flask_cors import cross_origin
from service.basicDiskInfoService import BasicDiskInfoService


@cross_origin()
def basicDiskInfo():
    firewallStatusResponse = BasicDiskInfoService.getBasicDiskInfo()
    print(firewallStatusResponse)
    return firewallStatusResponse
