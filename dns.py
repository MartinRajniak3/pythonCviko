#!/usr/bin/env python3

import socket
import struct

DNS_ADDR = "8.8.8.8"
DNS_PORT = 53
SRC_PORT = 50000


class DNS():
    def __init__(self):
        self.id = 0x1234
        self.flags = 0x0100  # standard query
        self.questions = 1
        self.answers = 0
        self.authority = 0
        self.additional = 0
        self.payload = list()

    def add_payload(self, payload):
        self.payload.append(payload)

    def to_bytes(self):
        payload_bytes = bytes()
        for payload in self.payload:
            payload_bytes += payload.to_bytes()
        return struct.pack("!6H", self.id, self.flags, self.questions, self.answers, self.authority,
                           self.additional) + payload_bytes


class DNS_question():
    def __init__(self, query):
        self.query = bytes()
        list_labels = query.split(".")
        for label in list_labels:
            label_bytes = label.encode()
            self.query += bytes([len(label_bytes)])
            self.query += label_bytes
        self.query += bytes([0x00])


        self.query += struct.pack("!HH", 0x001, 0x001)
    def to_bytes(self):
        return self.query


query = "www.dls.sk"
query = input("Enter dns query")
dns = DNS()
dns.add_payload(DNS_question(query))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.sendto(dns.to_bytes(), (DNS_ADDR, DNS_PORT))
while True:
    [response, addr] = sock.recvfrom(200)

    if addr[0] != DNS_ADDR:
        continue
    if addr[1] != DNS_PORT:
        continue
    if response[0:2] != struct.pack("!H", 0x1234):
        continue
    if response[2:4] != struct.pack("!H", 0x8180):
        continue

    ip_resp = socket.inet_ntoa(response[-4:])
    print("Query {} has IPv4: {}".format(query, ip_resp))
    break;
sock.close()


