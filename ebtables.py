import os

def ebtables(device_ip, src_ip):
    try:
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(src_ip, dev_ip))
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(dev_ip, src_ip))
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} -j DROP".format(device_ip))
    except:
        return("Blocking new IP failed")
    return("Successfully blocked IP: {}".format(src_ip))
