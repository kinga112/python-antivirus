import logging
import re
import requests
import socket
import struct
import textwrap

def main():
    logging.basicConfig(filename='log.log', filemode='a', level=logging.INFO)

    host = socket.gethostbyname(socket.gethostname()) # windows
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_IP) # mac and windows
    # s = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3)) # linux
    s.bind((host, 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)

    while True:
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON) # windows
        raw_data, addr = s.recvfrom(2048)
        s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)

        dest_mac, src_mac, eth_proto, data = ethernet_frame(raw_data)
        print('\nEthernet Frame:')
        print('Destination: {}, Source: {}, Protocol: {}'.format(dest_mac, src_mac, eth_proto))
        version, header_length, ttl, proto, src, target, data = ipv4_packet(data)
        print('Destination: {}, Source: {}, Protocol: {}'.format(target, src, proto))
        
        # if eth_proto == 8:
        #     version, header_length, ttl, proto, src, target, data = ipv4_packet(data)
        #     print('Destination: {}, Source: {}, Protocol: {}'.format(target, source, proto))
        
        # data = check_ip(addr[0])

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('! 6s 6s H', data[:14])
    return get_mac_addr(dest_mac), get_mac_addr(src_mac), socket.htons(proto), data[14:]

def get_mac_addr(bytes_addr):
    """retrurns readable mac address (AA:BB:CC:DD:EE:FF)"""
    bytes_str = map('{:02x}'.format, bytes_addr)
    mac_addr = ':'.join(bytes_str).upper()
    return mac_addr

def ipv4_packet(data):
    version_header_length = data[0]
    version = version_header_length >> 4
    header_length = (version_header_length & 15) * 4
    ttl, proto, src, target = struct.unpack('! 8x B B 2x 4s 4s', data[:20])
    return version, header_length, ttl, proto, ipv4(src), ipv4(target), data[header_length:]

def ipv4(addr):
    return '.'.join(map(str, addr))

def check_ip(ip):
    bad_ips = get_bad_ips()
    if ip in bad_ips:
        print('IP Scanned: BAD IP DETECTED')
        logging.info('IP {} was scanned, BAD IP DETECTED'.format(ip))
    else:
        print('IP Scanned: No Issues Found')
        logging.info('IP {} was scanned, no issues found'.format(ip))

def get_bad_ips():
    resp = requests.get('https://isc.sans.edu/api/threatlist')
    data = resp.text
    bad_ip_list = re.findall(r'<ipv4>(.+?)</ipv4>', data)
    return bad_ip_list

if __name__ == "__main__":
    main()
    