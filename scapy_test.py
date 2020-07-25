import pyshark
import subprocess

packet_count_pyshark = 0
packet_count_tshark = 0

tsharkCall = ["tshark", "-i", "Wi-Fi", "-w", "tshark_capture" + ".pcap"]
print("Starting Shark")
tshark_process = subprocess.Popen(tsharkCall, stderr=subprocess.DEVNULL)
print("Starting Pyshark")
capture = pyshark.LiveCapture(interface='Wi-Fi')
for packet in capture.sniff_continuously():
    packet_count_pyshark += 1
    print("Pyshark : ", packet_count_pyshark)