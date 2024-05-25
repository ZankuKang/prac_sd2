import time

from centralizedDir import Master, Slave
import threading


def start_master():
    master = threading.Thread(target=Master.main)
    master.start()


def start_slaves():
    slave_th = threading.Thread(target=Slave.main, args=(32771,))
    slave_th.start()
    slave_th2 = threading.Thread(target=Slave.main, args=(32772,))
    slave_th2.start()


start_master()
time.sleep(3)
start_slaves()
while True:
    pass
