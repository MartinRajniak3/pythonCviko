#!/usr/bin/env python3

from netmiko import ConnectHandler

IP = "158.193.152.166"
PORT = 22
USER = "admin"
PASS = "Admin123"

connection = ConnectHandler(device_type="cisco_ios", host=IP, username=USER, password=PASS)
vystup = connection.send_command("show ip int brief")
print(vystup)
loop_config = ["int lo14", "ip add 1.1.1.14 255.255.255.255", "no shut"]
connection.send_config_set(loop_config)
vystup = connection.send_command("show ip int brief")
print(vystup)