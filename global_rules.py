import subprocess

def globalRules():
    try:
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","ARP","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","8.8.8.8","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","8.8.8.8","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","224.0.0.22","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","224.0.0.22","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","224.0.0.1","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","224.0.0.1","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","224.0.0.251","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","224.0.0.251","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","239.255.255.250","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","239.255.255.250","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","10.0.0.0/8","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","10.0.0.0/8","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","172.16.0.0/12","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","172.16.0.0/12","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-src","192.168.0.0/16","-j","ACCEPT"], stdout=subprocess.PIPE)
        subprocess.Popen(["sudo","ebtables","-A","FORWARD","-p","IPv4","--ip-dst","192.168.0.0/16","-j","ACCEPT"], stdout=subprocess.PIPE)
    except:
        return("setting global rules failed")
    return("Successfully set global rules")