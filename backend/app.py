from flask import Flask
from constants import constants
from api import topCommandApi, ipAddressApi, portControlApi, listUsersApi, firewallApi, systemInfoApi

app = Flask('app')
app.add_url_rule('/memory', view_func=topCommandApi.topCommandByMemory, methods=["GET"])
app.add_url_rule('/cpu', view_func=topCommandApi.topCommandByCpu, methods=["GET"])
app.add_url_rule('/listUsers', view_func=listUsersApi.topCommandListUsers, methods=["GET"])
app.add_url_rule('/currentUser', view_func=listUsersApi.topCommandByCurrentUser, methods=["GET"])
app.add_url_rule('/listByUserCpu', view_func=topCommandApi.topCommandListByUserCpu, methods=["POST"])
app.add_url_rule('/listByUserMemory', view_func=topCommandApi.topCommandListByUserMemory, methods=["POST"])
app.add_url_rule('/getIp', view_func=ipAddressApi.getIpAddress, methods=["GET"])
app.add_url_rule('/portControl', view_func=portControlApi.getPortInfo, methods=["POST"])
app.add_url_rule('/firewallStatus', view_func=firewallApi.getFirewallStatus, methods=["GET"])
app.add_url_rule('/firewallDisable', view_func=firewallApi.getFirewallDisable, methods=["GET"])
app.add_url_rule('/firewallEnable', view_func=firewallApi.getFirewallEnable, methods=["GET"])
app.add_url_rule('/systemInfo', view_func=systemInfoApi.getSystemInfo, methods=["GET"])
app.add_url_rule('/systemBootInfo', view_func=systemInfoApi.getBootTime, methods=["GET"])
app.add_url_rule('/systemCpuInfo', view_func=systemInfoApi.getSystemCpuInfo, methods=["GET"])
app.add_url_rule('/systemLiveCpuInfo', view_func=systemInfoApi.getSystemLiveCpuInfo, methods=["GET"])
app.add_url_rule('/systemNetworkInfo', view_func=systemInfoApi.getSystemNetworkInfo, methods=["GET"])
app.add_url_rule('/systemGpuInfo', view_func=systemInfoApi.getSystemGpuInfo, methods=["GET"])

if __name__ == '__main__':
    app.run(constants.FLASK_HOST, constants.FLASK_PORT, debug=True)
