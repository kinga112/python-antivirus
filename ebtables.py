import os

def ebtables(device_ip, dev):
    f = open('devices/{}.txt'.format(dev), "r")
    for ip in f:
        ip.rstrip('\n')
        try:
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(ip, device_ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(device_ip, ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} -j DROP".format(device_ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst {} -j DROP".format(device_ip))
            print("Successfully addded rules for Device: {}".format(device_ip))
        except:
            print("Adding rules for new device failed")
    