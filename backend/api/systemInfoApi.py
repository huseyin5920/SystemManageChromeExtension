from flask_cors import cross_origin
from service.systemInfoService import SystemInfoService


@cross_origin()
def getSystemInfo():
    systemInformationResponse = SystemInfoService.systemInformation()
    return systemInformationResponse


@cross_origin()
def getBootTime():
    bootTimeInfoResponse = SystemInfoService.bootTime()
    return bootTimeInfoResponse


@cross_origin()
def getSystemCpuInfo():
    systemCpuInfoResponse = SystemInfoService.cpuInfo()
    return systemCpuInfoResponse


@cross_origin()
def getSystemLiveCpuInfo():
    systemLiveCpuInfoResponse = SystemInfoService.cpuInfoLive()
    return systemLiveCpuInfoResponse


@cross_origin()
def getSystemNetworkInfo():
    systemNetworkInfoResponse = SystemInfoService.networkInformation()
    return systemNetworkInfoResponse


@cross_origin()
def getSystemGpuInfo():
    systemGpuInfoResponse = SystemInfoService.gpuDetails()
    return systemGpuInfoResponse
