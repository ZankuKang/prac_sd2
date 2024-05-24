from centralized import Master, Slave
import threading


def start_master():
    master = threading.Thread(target=Master.main())
    master.start()


def start_slaves():
    ports = [32771, 32772]
    num_slaves = len(ports)
    for i in range(num_slaves):
        slave_th = threading.Thread(target=Slave.main(ports[i]))
        slave_th.start()


start_slaves()
start_master()
while True:
    pass

