import shutil


class BasicDiskInfoService():
    def getBasicDiskInfo():
        total, used, free = shutil.disk_usage("/")
        # print("Total: %d GiB" % (total // (2**30)))
        # print("Used: %d GiB" % (used // (2**30)))
        # print("Free: %d GiB" % (free // (2**30)))
        dict = {"total": total // (2**30), "used": used // (2**30), "free": free // (2**30)}
        return dict
