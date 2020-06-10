#! /usr/bin/python

from scapy.all import *


def ping(target):
    """
    ping a traget | send ICMP packet(type=echo-request) and verify response type ?=  echo-replay
    :param target: host or ip
    :return: 1 if the target is UP,  0 if DOWN
    """
    rep, no_rep = sr(IP(dst=target) / ICMP(), timeout=0.5)
    for elem in rep:  # elem représente un couple (paquet émis, paquet reçu)
        if elem[1].type == 0:  # 0 <=> echo-reply
            return 1
    return 0


def main():
    if ping('192.168.1.10'):
        print("OKAY")
    else:
        print("KO")


if __name__ == "__main__":
    main()
