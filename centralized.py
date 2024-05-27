import threading
import time

from CentralizedDir import Master, Slave

master_th = threading.Thread(target=Master.main)
master_th.start()

time.sleep(3)
slave_th1 = threading.Thread(target=Slave.main, args=(32771, ))
slave_th1.start()

slave_th2 = threading.Thread(target=Slave.main, args=(32772, ))
slave_th2.start()

while True:
    # THE most literal "do nothing" ever written
    pass