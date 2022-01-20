import psutil


class ProcessControlService():

    def checkProcessStatus(process_name):
        """
        Return status of process based on process name.
        """
        processList = {}
        processCount = 0
        process_status = [proc for proc in psutil.process_iter() if proc.name() == process_name]
        if process_status:
            for current_process in process_status:
                eachProcess = "Process id is %s, name is %s, status is %s" % (
                    current_process.pid, current_process.name(), current_process.status())
                processList[processCount] = eachProcess
                # print("Process id is %s, name is %s, status is %s" %
                #       (current_process.pid, current_process.name(), current_process.status()))
                # print(processList)
                processCount += 1
            return processList

        else:
            # print("Process name not valid", process_name)
            return "Process name not valid" + process_name
