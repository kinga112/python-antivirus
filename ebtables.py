import subprocess

def ebtables(device_ip, dev):
    f = open('devices/{}.txt'.format(dev), "r")
    for ip in f:
        ip.rstrip('\n')
        try:
            subprocess.call("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(ip, device_ip))
            subprocess.call("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(device_ip, ip))
            subprocess.call("sudo ebtables -A FORWARD -p IPv4 --ip-src {} -j DROP".format(device_ip))
            subprocess.call("sudo ebtables -A FORWARD -p IPv4 --ip-dst {} -j DROP".format(device_ip))
            return 'Ebtables Successfully (probably not) updated'
        except:
            return 'Error: Ebtables not updated'
