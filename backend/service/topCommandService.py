import subprocess
import re
from io import StringIO
import pandas as pd
from utils.sliceData import SliceData
import json
import ast
from collections import Counter
from flask import jsonify, request

class TopCommandService:

    @staticmethod
    def memoryFunc():
        output = subprocess.check_output(['top', "-b", "-n1", "-o", "%MEM"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

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
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])


        responseDataByMemory = SliceData.sliceFirstTenData(df)
        print(re)
        return responseDataByMemory

    @staticmethod
    def cpuFunc():
        output = subprocess.check_output(['top', "-bn1", "-o", "%CPU"])
        #print(output.decode())
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

                # df = pd.read_fwf(
                # StringIO(data),
                # colspecs=[(0, 7),  # PID
                #           (7, 16),  # USER
                #           (16, 20),  # PR
                #           (19, 22),  # NI
                #           (25, 32),  # VIRT
                #           (32, 39),  # RES
                #           (40, 46),  # SHR
                #           (48, 56),  # CPU
                #           (57, 61),  # MEM
                #           (61, 70),  # TIME
                #           (71, 999)],  # COMMAND
                # names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])


        df = pd.read_fwf( StringIO(output.decode())
            , colspecs=[(0, 7),  # PID
                        (7, 16),  # USER
                        (16, 20),  # PR
                        (19, 22),  # NI
                        (25, 32),  # VIRT
                        (32, 39),  # RES
                        (40, 46),  # SHR
                        (48, 56),  # CPU
                        (57, 61),  # MEM
                        (61, 70),  # TIME
                        (71, 999)]
            , names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])

        #print(df.to_dict(orient='index'))
        result = df.to_dict(orient='index')
        result = SliceData.sliceFirstTenData(result)
        return json.dumps(result)

    @staticmethod
    def listByUserCpu(user):
        output = subprocess.check_output(['top', "-u", user, "-b", "-n1", "-o", "%CPU"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

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
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])

        responseDataByUserCpu = SliceData.sliceFirstTenData(df)
        return responseDataByUserCpu

    @staticmethod
    def listByUserMemory(user):
        output = subprocess.check_output(['top', "-u", user, "-b", "-n1", "-o", "%MEM"])
        match = re.match(r'^[\w\W]*?\n( +PID.*COMMAND)\n([\w\W]*)', output.decode())

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
            names=['PID', 'USER', 'PR', 'NI', 'VIRT', 'RES', 'SHR', 'CPU', 'MEM', 'TIME', 'COMMAND'])

        responseDataByUserMemory = SliceData.sliceFirstTenData(df)
        return responseDataByUserMemory
