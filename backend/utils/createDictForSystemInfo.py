import json
from flask import jsonify


class CreateDictForSystemInfo:
    def createJsonObjectForSystemInfo(uname):
        systemInfoDict = {}
        systemInfoDict["System"] = uname.system
        systemInfoDict["Node Name"] = uname.node
        systemInfoDict["Release"] = uname.release
        systemInfoDict["Version"] = uname.version
        systemInfoDict["Machine"] = uname.machine
        systemInfoDict["Processor"] = uname.processor
        json_dump = json.dumps(systemInfoDict)
        json_object = json.loads(json_dump)
        return json_object

    def createJsonObjectForCpuInfo(physicalCores, totalCores, maxFrequency, minFrequency, currentFrequency):
        systemCpuInfoDict = {}
        currentFrequencyFormat = format(currentFrequency, '.2f')
        maxFrequencyFormat = format(maxFrequency, '.2f')
        minFrequencyFormat = format(minFrequency, '.2f')
        systemCpuInfoDict["physicalCores"] = physicalCores
        systemCpuInfoDict["totalCores"] = totalCores
        systemCpuInfoDict["maxFrequency"] = maxFrequencyFormat + "Mhz"
        systemCpuInfoDict["minFrequency"] = minFrequencyFormat + "Mhz"
        systemCpuInfoDict["currentFrequency"] = currentFrequencyFormat + "Mhz"
        json_dump = json.dumps(systemCpuInfoDict)
        json_object = json.loads(json_dump)
        return json_object

    def createJsonObjectForLiveCpuInfo(cores, totalCpu):
        systemLiveCpuInfoDict = {}
        systemLiveCpuInfoDict["cores"] = cores
        systemLiveCpuInfoDict["totalCpu"] = totalCpu
        json_dump = json.dumps(systemLiveCpuInfoDict)
        json_object = json.loads(json_dump)
        return json_object

    def createJsonObjectForNetworkInfo(ifAddrs):
        systemNetworkInfoDict = {}
        systemNetworkInfoList = []
        for interface_name, interface_addresses in ifAddrs.items():
            for address in interface_addresses:
                if str(address.family) == 'AddressFamily.AF_INET':

                    systemNetworkInfoDict["address"] = address.address
                    systemNetworkInfoDict["netmask"] = address.netmask
                    systemNetworkInfoDict["broadcast"] = address.broadcast
                    dictCopyNetworkInfo = systemNetworkInfoDict.copy()
                    systemNetworkInfoList.append(dictCopyNetworkInfo)
        return jsonify(systemNetworkInfoList)

    def createJsonObjectForGpuInfo(gpus):
        systemGpuInfoDict = {}
        systemGpuInfoList = []
        for gpu in gpus:
            systemGpuInfoDict["gpId"] = gpu.id
            systemGpuInfoDict["gpuName"] = gpu.name
            systemGpuInfoDict["gpuLoad"] = gpu.load*100
            systemGpuInfoDict["gpuFreeMemory"] = gpu.memoryFree
            systemGpuInfoDict["gpuUsedMemory"] = gpu.memoryUsed
            systemGpuInfoDict["gpuTotalTemory"] = gpu.memoryTotal
            systemGpuInfoDict["gpuTemperature"] = gpu.temperature
            systemGpuInfoDict["gpuUuid"] = gpu.uuid
            dictCopyGpuInfo = systemGpuInfoDict.copy()
            systemGpuInfoList.append(dictCopyGpuInfo)
        return jsonify(systemGpuInfoList)
