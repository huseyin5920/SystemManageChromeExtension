import json
from utils.createDictForSystemInfo import CreateDictForSystemInfo

import psutil
import platform
from datetime import datetime
import GPUtil
from tabulate import tabulate


class SystemInfoService:
    def systemInformation():
        uname = platform.uname()
        systemInfoResponse = CreateDictForSystemInfo.createJsonObjectForSystemInfo(uname)
        return systemInfoResponse

    def bootTime():
        boot_time_timestamp = psutil.boot_time()
        bt = datetime.fromtimestamp(boot_time_timestamp)
        return f"{bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}"

    def cpuInfo():
        cpufreq = psutil.cpu_freq()
        systemCpuInfoResponse = CreateDictForSystemInfo.createJsonObjectForCpuInfo(psutil.cpu_count(
            logical=False), psutil.cpu_count(logical=True), cpufreq.max, cpufreq.min, cpufreq.current)
        return systemCpuInfoResponse

    def cpuInfoLive():
        cpuInfoLıveList = []
        for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
            cpuInfoLıveList.append(percentage)

        totalCpuUsage = psutil.cpu_percent()
        systemLiveCpuInfoResponse = CreateDictForSystemInfo.createJsonObjectForLiveCpuInfo(
            cpuInfoLıveList, totalCpuUsage)
        return systemLiveCpuInfoResponse

    def networkInformation():
        if_addrs = psutil.net_if_addrs()
        systemLiveCpuInfoResponse = CreateDictForSystemInfo.createJsonObjectForNetworkInfo(if_addrs)
        return systemLiveCpuInfoResponse

    def gpuDetails():
        gpus = GPUtil.getGPUs()
        systemGpuInfoResponse = CreateDictForSystemInfo.createJsonObjectForGpuInfo(gpus)
        return systemGpuInfoResponse
