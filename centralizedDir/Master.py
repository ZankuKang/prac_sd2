from proto import store_pb2, store_pb2, store_pb2_grpc
import time
import grpc
from concurrent.futures import ThreadPoolExecutor
from concurrent import futures
from proto.basicproto import master_servicer

# Basic features
storage = {}
registeredNodes = []


def start_service():
    # creates the grpc server on master node
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(master_servicer, server)
    # Defines where the server will listen
    server.add_insecure_port('localhost:32770')
    server.start()
    server.wait_for_termination()


def Two_PC(put_request, context):
    # We get the nodes that are registered in master
    registeredNodes = master_servicer.getDiscoverQueue()
    for node in registeredNodes:
        channel = grpc.insecure_channel(node)  # node = IP:PORT
        stub = store_pb2_grpc.KeyValueStoreStub(channel)
        request = store_pb2.CommitRequest(key=put_request.key, value=put_request.value)
        can_node_commit = stub.canCommit(request)
        if not can_node_commit.success:
            return False
    for node in registeredNodes:
        channel = grpc.insecure_channel(node)
        stub = store_pb2_grpc.KeyValueStoreStub(channel)
        commit = store_pb2.CommitRequest(key=put_request.key, value=put_request.value)
        have_commited = stub.doCommit(commit)
        if not have_commited.success:
            return False
    return True


def main():
    master_servicer.set_storage(storage)
    master_servicer.setDicoverQueue(registeredNodes)

    start_service()

    while True:
        time.sleep(100000)
