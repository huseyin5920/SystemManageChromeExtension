import psutil



class KillPidService():
    def killPidApp(pid):
        p = psutil.Process(pid)
        p.terminate() 
        return "killed"
