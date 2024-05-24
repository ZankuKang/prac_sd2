from concurrent import futures
import time
import grpc
import json
from proto.basicproto import centralized_servicer
from proto import store_pb2, store_pb2_grpc

storage = {}

def main(port):
    centralized_servicer.set_storage(storage)
    register_slave("localhost", port)


def start_server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(centralized_servicer, server)
    server.add_insecure_port('localhost'+str(port))
    server.start()
    server.wait_for_termination()

def register_slave(ip, port):
    master = "localhost:32770"
    channel = grpc.insecure_channel(master)
    stub = store_pb2_grpc.KeyValueStoreStub(channel)
    register_request = store_pb2.SlaveInfo(address=str(ip) + str(port))
    response = stub.registerSlave(register_request)
    storage_receive = response.store
    storage_receive = json.loads(storage_receive)
    for key in storage_receive:
        centralized_servicer.storage[key] = storage_receive[key]
