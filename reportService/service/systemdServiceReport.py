import psutil
from flask import jsonify
class SystemdService():

    def getListOfProcessSortedByMemory():
        '''
        Get list of running process sorted by Memory Usage
        '''
        listOfProcObjects = []
        # Iterate over the list
        for proc in psutil.process_iter():
            try:
                # Fetch process details as dict
                pinfo = proc.as_dict(attrs=['pid', 'name', 'username', 'cpu_percent', 'memory_percent', 'create_time',
])
                pinfo['vms'] = proc.memory_info().vms / (1024 * 1024)
                # Append dict to list
                if pinfo['cpu_percent'] > 0:
                    listOfProcObjects.append(pinfo);
                    if pinfo['cpu_percent'] > 80:
                        print(pinfo)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        # Sort list of dict by key vms i.e. memory usage
        listOfProcObjects = sorted(listOfProcObjects, key=lambda procObj: procObj['cpu_percent'], reverse=True)
        return jsonify(listOfProcObjects)


# import requests

# url = 'https://www.w3schools.com/python/demopage.php'
# myobj = {'somekey': 'somevalue'}

# x = requests.post(url, data = myobj)

# print(x.text)