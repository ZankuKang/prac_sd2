from concurrent import futures
import time
import grpc
import json
from proto.basicproto import centralized_servicer
from proto import store_pb2, store_pb2_grpc
import threading

storage = {}


def main(port):
    centralized_servicer.set_storage(storage)
    # Start the server in a separate thread to avoid blocking
    server_thread = threading.Thread(target=start_server, args=(port,))
    server_thread.start()

    # Give the server time to start
    time.sleep(3)

    # Register the slave after starting the server
    register_slave("localhost", port)

    # Keep the main thread running
    server_thread.join()


def start_server(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=15))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(centralized_servicer, server)
    server_address = 'localhost:' + str(port)
    print(f"Starting server on {server_address}")
    server.add_insecure_port(server_address)
    server.start()
    server.wait_for_termination()


def register_slave(ip, port):
    master = "localhost:32770"
    slave_address = f"{ip}:{port}"
    for attempt in range(5):  # Retry 5 times
        try:
            channel = grpc.insecure_channel(master)
            stub = store_pb2_grpc.KeyValueStoreStub(channel)
            register_request = store_pb2.SlaveInfo(address=slave_address)
            response = stub.registerSlave(register_request)
            storage_receive = response.store
            storage_receive = json.loads(storage_receive)
            for key in storage_receive:
                centralized_servicer.storage[key] = storage_receive[key]
            print(f"Slave registered successfully at {slave_address}")
            return
        except grpc.RpcError as e:
            print(f"Error registering slave on attempt {attempt + 1}: {e}")
            time.sleep(2)
    raise Exception(f"Failed to register slave after multiple attempts: {slave_address}")


if __name__ == "__main__":
    ports = [32771, 32772]
    for port in ports:
        slave_thread = threading.Thread(target=main, args=(port,))
        slave_thread.start()