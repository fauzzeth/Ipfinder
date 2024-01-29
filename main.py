import random
from pystyle import *
import time
import subprocess


def ping_ip(ip_address):
    process = subprocess.Popen(["ping", "-n", "1", ip_address], stdout=subprocess.PIPE)
    output = process.communicate()[0]
    return output


print(Colorate.Horizontal(Colors.red_to_green, "made by fau??eth"))


while True:
    first = random.randint(1, 255)
    second = random.randint(1, 255)
    third = random.randint(1, 255)
    fourth = random.randint(1, 255)
    ip = f"{first}.{second}.{third}.{fourth}"
    print(Colorate.Horizontal(Colors.red_to_green, f"Trying to ping {ip}..."))
    result = ping_ip(ip)
    result = f"{result.decode()}"
    if "Request timed out." in result:
        print(Colorate.Horizontal(Colors.red_to_green, "Request timed out. Writing in timeout.txt"))
        f = open("timeout.txt", 'a')

        f = open("timeout.txt", "r")
        if ip in str(f.read()):
            print(Colorate.Horizontal(Colors.red_to_green, "It is already written."))
        else:
            f = open("timeout.txt", 'a')
            f.write(ip + '\n')

    elif "transmit failed." in result:
        print(Colorate.Horizontal(Colors.red_to_green, "Transmit failed. Writing in transmitfailed.txt"))
        f = open("transmitfailed.txt", 'a')

        f = open("transmitfailed.txt", 'r')
        if ip in str(f.read()):
            print(Colorate.Horizontal(Colors.red_to_green, "It is already written."))
        else:
            f = open("transmitfailed.txt", 'a')
            f.write(ip + '\n')


    elif "Reply from" in result:
        print(Colorate.Horizontal(Colors.red_to_green, "Got reply! Writing in replied.txt"))
        f = open("replied.txt", 'a')

        f = open("replied.txt", "r")
        if ip in str(f.read()):
            print(Colorate.Horizontal(Colors.red_to_green, "It is already written."))
        else:
            f = open("replied.txt", 'a')
            f.write(ip + '\n')
    else:
        print(Colorate.Horizontal(Colors.red_to_green, "Error while analyzing! Writing in unknown.txt"))
        f = open("unknown.txt", 'a')

        f = open("unknown.txt", "r")
        if ip in str(f.read()):
            print(Colorate.Horizontal(Colors.red_to_green, "It is already written."))
        else:
            f = open("unknown.txt", 'a')
            f.write('\n\n' + result + '\n\n')
            f.write(ip + '\n')
            f.write("__________________________________________")

