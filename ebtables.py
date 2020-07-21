import subprocess

def add_rule(device_ip, dev):
    f = open('devices/{}.txt'.format(dev), "r")
    try:
        for ip in f:
            ip = ip.replace('\n', '')
            print("sudo ebtables -A FORWARD -p IPv4 --ip-src {} --ip-dst {} -j ACCEPT".format(device_ip, ip))
            subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src",device_ip,"--ip-dst",ip,"-j","ACCEPT"], stdout=subprocess.PIPE)
            subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src",ip,"--ip-dst",device_ip,"-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src",device_ip,"-j","DROP"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst",device_ip,"-j","DROP"], stdout=subprocess.PIPE)
        return 'Ebtables successfully (probably not) added new rules'
    except:
        return 'Error: Ebtables not updated'

def delete_rule(device_ip, dev):
    f = open('devices/{}.txt'.format(device_ip), "r")
    try:
        for ip in f:
            ip = ip.replace('\n', '')
            subprocess.Popen(["sudo","ebtables","-D","FORWARD","-p","IPv4","--ip-src",device_ip,"--ip-dst",ip,"-j","ACCEPT"], stdout=subprocess.PIPE)
            subprocess.Popen(["sudo","ebtables","-D","FORWARD","-p","IPv4","--ip-src",ip,"--ip-dst",device_ip,"-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-D","FORWARD","-p","IPv4","--ip-src",device_ip,"-j","DROP"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-D","FORWARD","-p","IPv4","--ip-dst",device_ip,"-j","DROP"], stdout=subprocess.PIPE)
        return 'Ebtables successfully (probably not) deleted rules'
    except:
        return 'Error: Ebtables not updated'