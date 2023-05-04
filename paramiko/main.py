import paramiko

def sendCommand(command):
    stdin, stdout, stderr = ssh.exec_command(command)
    cmd_output = stdout.read()
    print("<<", cmd_output.decode())

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip = "10.10.0.5"
port = 22
username = "msfadmin"
password = "msfadmin"

ssh.connect(ip, port = port, username = username, password = password)

command = "whoami"

while command.lower().strip() != "quit":
    if(command != ""):
        sendCommand(command)
    command = input(">>")

