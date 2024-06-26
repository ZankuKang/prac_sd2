from concurrent import futures
import grpc
from proto import store_pb2_grpc, store_pb2
import time
from proto.store_impl import master_servicer

storage = {}
slaves = []

# Loads the file to the master node and starts it
def main():
    master_servicer.setStorage(storage)
    master_servicer.loadStorage()
    master_servicer.setSlaves(slaves)
    startService()
    while True:
        time.sleep(86400)


def startService():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(master_servicer, server)
    server.add_insecure_port('localhost:32770')
    server.start()
    server.wait_for_termination()


# 2PC's algorithm implementation
def Two_PC(put_request):
    channels = []
    stubs = []
    commit_pet = store_pb2.CommitRequest(key=put_request.key, value=put_request.value)
    try:
        for slave in slaves:
            channel = grpc.insecure_channel(slave)
            stub = store_pb2_grpc.KeyValueStoreStub(channel)
            channels.append(channel)
            stubs.append(stub)

        for stub in stubs:
            can_com = stub.canCommit(commit_pet)
            if not can_com.success:
                return False

        for stub in stubs:
            do_com = stub.doCommit(store_pb2.CommitRequest(key=put_request.key, value=put_request.value))
            if not do_com.success:
                return False
        return True
    except:
        return False
