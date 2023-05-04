import socket
ip = "10.0.2.15"

for port in range(1,100):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(2.0)
		s.connect((ip,port))
		response = s.recv(1024)
		print(str(port)," is open: Banner : ",response.decode())
	except socket.timeout as t:
		if(port == 80):
			httpMessage = "GET / HTTP/1.0\r\n\r\n"
			s.send(httpMessage.encode())
			httpRcv = s.recv(1024)
			print(str(port), "open : Banner : ", httpRcv.decode())
		else:
			print(str(port) ,"use different method.")
	except Exception as e:
		print(str(port) ,"is closed. Reason : ",str(e))
		pass
	finally:
		s.close()