import os

class JournalctlService:
    def readJournalctl():
        os.system("journalctl -r --since '1 hour ago' > /home/huseyin/Documents/DEVELOPMENT/SystemManageChromeExtension/reportService/service/journal.txt")
        f = open("/home/huseyin/Documents/DEVELOPMENT/SystemManageChromeExtension/reportService/service/journal.txt", "r")
        a = f.read()
        a = a.split("\n")
        asd = {}
        asd["sonuc"] = a
        print(len(a))
        f.close()
        return asd