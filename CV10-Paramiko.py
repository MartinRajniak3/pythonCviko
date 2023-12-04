#!/usr/bin/env python3

from paramiko import *

IP = "158.193.152.166"
PORT = 22
USER = "admin"
PASS = "Admin123"

ssh_client = SSHClient()
ssh_client.set_missing_host_key_policy(AutoAddPolicy())
ssh_client.connect(hostname=IP, port=PORT, username=USER, password=PASS)
# (stdin, stdout, stderr) = ssh_client.exec_command("sh ip int brief")
# vystup = list()
# counter = 0
# for line in stdout:
#     counter += 1
#     if counter < 3:
#         continue
#     riadok_list = line.strip("\n").strip("\r").split(" ")
#     while "" in riadok_list:
#         riadok_list.remove("")
#     vystup.append({"interface": riadok_list[0], "ip": riadok_list[1]})
# print(vystup)

(stdin, stdout, stderr) = ssh_client.exec_command("conf t")
(stdin, stdout, stderr) = ssh_client.exec_command("int lo100")
(stdin, stdout, stderr) = ssh_client.exec_command("ip add 1.1.1.1 255.255.255.255")

