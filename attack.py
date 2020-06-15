#! /usr/bin/python
from multiprocessing import Process, Queue
from pprint import  pprint

def bruteForceSSH(host, user, user_list, password_file):
    """

    :param host:
    :param user:
    :param user_file:
    :param password_file:
    :return:
    """

    if user:
        for

def findPassword(host, user, passwords, queue):
    """
    Find just the password
    :param host:
    :param user:
    :param password:
    :return:
    """
    for password in passwords:
        if tryConnect(host, user, password):
            queue.put((user, password))
            return (user, password)
            break

def findUserAndPassword(host, users, passwords):
    """
    Find the user and password
    :param host: str
    :param users:  set
    :param password: set
    :return: (user, password)
    """

    for user in users:
        for password in password:
            if tryConnect(host, user, password):
                return (user, password)
                break


def tryConnect(host, user, password):
    """
    test user and password connection
    :param host: str
    :param user: str
    :param password: str
    :return:
    """
    if user:
        return True

def run(number_process):
    # http://www.python-simple.com/python-modules-autres/multiprocessing.php
    queue = Queue
    user = 'root'
    passwords = ['root', 'toor', 'azerty', '123test']
    process = []
    for i in number_process:
        p = Process(target=findPassword, args=(host, user, passwords, queue))
        p.start()
        process.append(p)

    for p in process:
        if p.exitcode == 0 # le statut de retour quand le process est fini (0 si ok)
            # un des process  a pu trouver le user/password
            result = queue.get()
            pprint(result)



