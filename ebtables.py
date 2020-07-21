import os

def ebtables(device_ip, src):
    src_ip_list = get_src_ips(src)
    for ip in src_ip_list:
        try:
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(ip, dev_ip))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(dev_ip, ip))
        except:
            return("Blocking new IP failed")
        return("Successfully blocked IP: {}".format(src_ip))

def get_src_ips(src):
    src_ip_list = []
    f = open('{}.txt'.format(src), "r")
    for ip in f:
        src_ip_list.append(ip)
    return src_ip_list
    