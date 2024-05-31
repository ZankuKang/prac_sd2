from concurrent import futures
import grpc
from proto import store_pb2_grpc, store_pb2
import time
from proto.store_impl import basic_servicer
import json

storage = {}

# Loads the file to the slave and starts it
def main(port):
    basic_servicer.setStorage(storage)
    registerThisSlave(port)
    time.sleep(2)
    startService(port)
    while True:
        time.sleep(86400)


def startService(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(basic_servicer, server)
    server.add_insecure_port('localhost:' + str(port))
    server.start()
    server.wait_for_termination()


# Lets the master node know this slave is active and ready to be used, so the master
# can register it and have it in consideration for the 2PC
def registerThisSlave(port):
    channel = grpc.insecure_channel("localhost:32770")
    stub = store_pb2_grpc.KeyValueStoreStub(channel)
    store = stub.registerSlave(store_pb2.SlaveInfo(address="localhost:" + str(port)))
    master_storage = json.loads(store.store)
    for key in master_storage:
        basic_servicer.storage[key] = master_storage[key]
