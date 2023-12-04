#!/usr/bin/env python3

from paramiko import *

IP = "158.193.152.167"
PORT = 22
USER = "admin"
PASS = "Admin123"

ssh_client = SSHClient()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(hostname=IP, port=PORT, username=USER, password=PASS)
(stdin, stdout, stderr) = ssh_client.exec_command("/ip addr print terse")
vystup = list()
counter = 0
for line in stdout:
    line_list = line.strip("\n").strip("\r").split(" ")
    if len(line_list) < 2:
        continue
    vystup.append({"interface": line_list[3].split("=")[1], "ip": line_list[1].split("=")[1]})
print(vystup)


# (stdin, stdout, stderr) = ssh_client.exec_command("conf t")
# (stdin, stdout, stderr) = ssh_client.exec_command("int lo100")
# (stdin, stdout, stderr) = ssh_client.exec_command("ip add 1.1.1.1 255.255.255.255")

