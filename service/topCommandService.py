import subprocess
import re
from io import StringIO
import pandas as pd
from utils.sliceData import SliceData
from flask import request


class TopCommandService:

    @staticmethod
    def memoryFunc():
        #output = subprocess.check_output(['top', "-bn1", "-o", "%MEM"])
        output = subprocess.check_output(['top', "-b", "-n1", "-o", "%MEM"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

        #header = match[1]
        data = match[2]

        df = pd.read_fwf(
            StringIO(data),
            colspecs=[(0, 7),  # PID
                      (7, 16),  # USER
                      (16, 20),  # PR
                      (19, 22),  # NI
                      (25, 32),  # VIRT
                      (32, 39),  # RES
                      (40, 46),  # SHR
                      (48, 56),  # CPU
                      (57, 61),  # MEM
                      (61, 70),  # TIME
                      (71, 999)],  # COMMAND
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', '%CPU', '%MEM', 'TIME+', 'COMMAND'])

        # print(df)
        # print(df.to_dict(orient='index'))
        # print(df.to_dict(orient='index'))
        # print(len(df.to_dict(orient='index')))

        responseDataByMemory = SliceData.sliceFirstTenData(df)
        return responseDataByMemory

    @staticmethod
    def cpuFunc():
        #output = subprocess.check_output(['top', "-bn1", "-o", "%MEM"])
        output = subprocess.check_output(['top', "-b", "-n1", "-o", "%CPU"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

        #header = match[1]
        data = match[2]

        df = pd.read_fwf(
            StringIO(data),
            colspecs=[(0, 7),  # PID
                      (7, 16),  # USER
                      (16, 20),  # PR
                      (19, 22),  # NI
                      (25, 32),  # VIRT
                      (32, 39),  # RES
                      (40, 46),  # SHR
                      (48, 56),  # CPU
                      (57, 61),  # MEM
                      (61, 70),  # TIME
                      (71, 999)],  # COMMAND
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', '%CPU', '%MEM', 'TIME+', 'COMMAND'])

        # print(df)
        # print(df.to_dict(orient='index'))
        # print(df.to_dict(orient='index'))
        # print(len(df.to_dict(orient='index')))

        responseDataByMemory = SliceData.sliceFirstTenData(df)
        return responseDataByMemory

    @staticmethod
    def listByUserCpu(user):
        #output = subprocess.check_output(['top', "-bn1", "-o", "%MEM"])
        output = subprocess.check_output(['top', "-u", user, "-b", "-n1", "-o", "%CPU"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

        #header = match[1]
        data = match[2]

        df = pd.read_fwf(
            StringIO(data),
            colspecs=[(0, 7),  # PID
                      (7, 16),  # USER
                      (16, 20),  # PR
                      (19, 22),  # NI
                      (25, 32),  # VIRT
                      (32, 39),  # RES
                      (40, 46),  # SHR
                      (48, 56),  # CPU
                      (57, 61),  # MEM
                      (61, 70),  # TIME
                      (71, 999)],  # COMMAND
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', '%CPU', '%MEM', 'TIME+', 'COMMAND'])

        responseDataByUserCpu = SliceData.sliceFirstTenData(df)
        return responseDataByUserCpu

    @staticmethod
    def listByUserMemory(user):
        #output = subprocess.check_output(['top', "-bn1", "-o", "%MEM"])
        output = subprocess.check_output(['top', "-u", user, "-b", "-n1", "-o", "%MEM"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

        #header = match[1]
        data = match[2]

        df = pd.read_fwf(
            StringIO(data),
            colspecs=[(0, 7),  # PID
                      (7, 16),  # USER
                      (16, 20),  # PR
                      (19, 22),  # NI
                      (25, 32),  # VIRT
                      (32, 39),  # RES
                      (40, 46),  # SHR
                      (48, 56),  # CPU
                      (57, 61),  # MEM
                      (61, 70),  # TIME
                      (71, 999)],  # COMMAND
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', '%CPU', '%MEM', 'TIME+', 'COMMAND'])

        responseDataByUserMemory = SliceData.sliceFirstTenData(df)
        return responseDataByUserMemory
