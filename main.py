#! /usr/bin/python
from pprint import pprint

from scapy.all import *

from attack import run_ssh_attack


def is_open(target, port):
    """
    Send a SYNC packet and see, if the target will return with SYN-ACK => open, else the port is close
    :param target: host or ip.
            port : service port, EX 22 for SSH.
    :return: 1 if ssh port is open, 0 else.
    """
    rep, no_rep = sr(IP(dst=target) / TCP(dport=port, flags="S"), timeout=5)
    for elem in rep:
        if 'SA' in str(elem[1].flags):  #  SYN-ACK
            print('OPEN');
            return 1
    print('CLOSE');
    return 0


def ping(target):
    """
    ping a traget | send ICMP packet(type=echo-request) and verify response type ?=  echo-replay
    :param target: host or ip
    :return: 1 if the target is UP,  0 if DOWN
    """
    rep, no_rep = sr(IP(dst=target) / ICMP(), timeout=5)
    for elem in rep:  # elem représente un couple (paquet émis, paquet reçu)
        if elem[1].type == 0:  # 0 <=> echo-reply
            return 1
    return 0


def scan_all_ports(target, ports):
    """
    scan all ports in port list
    :param target: host or ip
    :param ports: port's list
    :return: open ports, ex {'ssh',22, 'ftp':21, ...}
    """
    open_ports = {}
    for protocol, port in ports.items():
        if is_open(target, port):
            open_ports[protocol] = port
    return open_ports


def main():
    """
    if ping('192.168.1.10'):
        print("OKAY")
    else:
        print("KO")
    """
    is_open('192.168.1.6', 21)
    ports = {'tftp': 20, 'ftp': 21, 'ssh': 22, 'telnet': 23, 'smtp': 25, 'dns': 53, 'dhcp': 67, 'dhcp1': 68, 'http': 80,
             'pop3': 110, 'nfs': 111, 'nfs1': 2049, 'samba': 137, 'samba2': 139, 'imap': 143, 'snmp': 161,
             'snmptrap': 162,
             'https': 443, 'samba1': 445, 'smtpauth': 587, 'heartbeat': 694, 'imap1': 995, 'mysql': 3306,
             'webmin': 10000}

    scan_all_ports('192.168.1.6', ports=ports)


if __name__ == "__main__":
    # main()
    user = 'yacine'
    host = 'localhost'
    port = 22
    passwords = ['secret10', 'linux00', 'pass010', '123test', 'azerty', '1010ree', 'tt120', '2020ml', '45m1ui', 'h12jh', 'j15mkj',
                 'aze0101kl']
    run_ssh_attack(host=host, user=user, users=None, port=port, passwords=passwords, nb_thread=3)

