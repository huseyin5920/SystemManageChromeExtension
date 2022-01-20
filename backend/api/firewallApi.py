from flask_cors import cross_origin
from service.firewallService import FirewallService


@cross_origin()
def getFirewallStatus():
    firewallStatusResponse = FirewallService.firewallStatus()
    return firewallStatusResponse


@cross_origin()
def getFirewallDisable():
    firewallDisableResponse = FirewallService.firewallDisable()
    return firewallDisableResponse


@cross_origin()
def getFirewallEnable():
    firewallEnableResponse = FirewallService.firewallEnable()
    return firewallEnableResponse
