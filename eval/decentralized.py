import threading

ports = [32770, 32771, 32772]

# Creates the nodes concurrently
from DescentralizedDir import DesNode
for port in ports:
    thread = threading.Thread(target=DesNode.main, args=(port,))
    thread.start()

while True:
    pass
