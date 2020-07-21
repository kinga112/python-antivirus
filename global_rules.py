import os

def globalRules():
    try:
        os.system("sudo ebtables -A FORWARD -p ARP -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 8.8.8.8 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 8.8.8.8 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 224.0.0.22 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 224.0.0.22 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 224.0.0.1 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 224.0.0.1 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 244.0.0.251 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 244.0.0.251 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 239.255.255.250 -j ACCEPT")
        os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 239.255.255.250 -j ACCEPT")
        range1 = 8
        while range1 < 33:
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 10.0.0.0/{} -j ACCEPT".format(range1))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 10.0.0.0/{} -j ACCEPT".format(range1))
            range1 += 1
        range2 = 12
        while range2 < 33:
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 172.16.0.0/{} -j ACCEPT".format(range2))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 172.16.0.0/{} -j ACCEPT".format(range2))
            range2 += 1
        range3 = 16
        while range3 < 33:
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-src 192.168.0.0/{} -j ACCEPT".format(range3))
            os.system("sudo ebtables -A FORWARD -p IPv4 --ip-dst 192.168.0.0/{} -j ACCEPT".format(range3))
            range3 += 1
    except:
        return("setting global rules failed")
    return("Successfully set global rules")