from flask_cors import cross_origin
from service.systemdServiceReport import SystemdService
from service.journalctl1Hour import JournalctlService

@cross_origin()
def cpuRe():
    firewallStatusResponse = SystemdService.getListOfProcessSortedByMemory()
    return firewallStatusResponse

@cross_origin()
def journalctlReport():
    firewallStatusResponse = JournalctlService.readJournalctl()
    return firewallStatusResponse

