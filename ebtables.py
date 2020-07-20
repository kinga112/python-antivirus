import os

def ebtables(device_ip, src_ip):
    try:
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(src_ip, dev_ip))
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(dev_ip, src_ip))
        range1 = 8
        while range1 < 33
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 10.0.0.0/{} --ip-dst {} -j ACCEPT".format(range1, dev_ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst 10.0.0.0/{} -j ACCEPT".format(dev_ip, range1))
            range1 += 1
        range2 = 12
        while range2 < 33
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 172.16.0.0/{} --ip-dst {} -j ACCEPT".format(range2, dev_ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst 172.16.0.0/{} -j ACCEPT".format(dev_ip, range2))
            range2 += 1
        range3 = 16
        while range3 < 33
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 192.168.0.0/{} --ip-dst {} -j ACCEPT".format(range3, dev_ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst 192.168.0.0/{} -j ACCEPT".format(dev_ip, range3))
            range3 += 1
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} -j DROP".format(dev_ip))
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst {} -j DROP".format(dev_ip))
    except:
        return("Blocking new IP failed")
    return("Successfully blocked IP: {}".format(src_ip))
