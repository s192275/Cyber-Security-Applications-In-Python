from scapy.all import *

conf.checkIPaddr = False

ether = Ether(dst = "ff:ff:ff:ff:ff:ff")
ip = IP(src = "0.0.0.0", dst = "255.255.255.255")
udp = UDP(sport = 68, dport = 67)
bootp= BOOTP(op =1 , chaddr = RandMAC())
dhcp = DHCP(options=[("message-type","discover"),"end"])
dhcp_discover = ether/ip/udp/bootp/dhcp

#ans, unans = srp(dhcp_discover, iface = "eth0", verbose = False)

		#p[0].show()
		#p[1].show()
sendp(dhcp_discover, iface='eth0', verbose = False, loop = 1)
