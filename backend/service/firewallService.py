import subprocess
import re


class FirewallService:
    def firewallStatus():
        firewallStatusOutput = subprocess.check_output(["sudo", "ufw", "status"])
        print(firewallStatusOutput[:14])
        if firewallStatusOutput[:14].decode() == "Status: inactive":
            return "inactive"
        else:
            return "active"
        # return firewallStatusOutput.decode()

    def firewallDisable():
        firewallOutput = subprocess.check_output(["sudo", "ufw", "disable"])
        return firewallOutput.decode()

    def firewallEnable():
        firewallOutput = subprocess.check_output(["sudo", "ufw", "enable"])
        return firewallOutput.decode()
