from concurrent import futures
import grpc
from proto import store_pb2_grpc, store_pb2

quorum_read = 2
quorum_write = 3
neighbours = ["localhost:32770", "localhost:32771", "localhost:32772"]


def askVotePut(put_request, size):
    votes = size
    stubs = []
    for neigh in neighbours:
        try:
            channel = grpc.insecure_channel(neigh)
            stub = store_pb2_grpc.KeyValueStoreStub(channel)
            response = stub.votePut(put_request)
            if response.success:
                votes += response.size
            stubs.append(stub)
        except grpc.RpcError:
            continue

    if votes >= quorum_write:
        try:
            for stub in stubs:
                response = stub.doCommit(store_pb2.CommitRequest(key=put_request.key, value=put_request.value))
                if not response.success:
                    return False
            return True
        except grpc.RpcError:
            return False


def askVoteGet(get_request, value, size):
    votes = {value: size}
    for neigh in neighbours:
        try:
            channel = grpc.insecure_channel(neigh)
            stub = store_pb2_grpc.KeyValueStoreStub(channel)
            response = stub.voteGet(store_pb2.voteGetRequest(key=get_request.key))
            if response.success:
                if response.value in votes:
                    votes[response.value] += response.size
                else:
                    votes[response.value] = response.size
        except grpc.RpcError:
            continue

    max_val = max(votes.keys(), key=lambda y: votes[y])
    max_votes = votes[max_val]
    if max_votes >= quorum_read:
        return max_val
    else:
        return None


def main(port):
    from proto.store_impl import descen_servicer
    descen_servicer.setPort(port)
    descen_servicer.loadStorageDes()
    if port == 32771:
        descen_servicer.setVote(2)
    else:
        descen_servicer.setVote(1)
    for neigh in neighbours:
        ip, node_port = neigh.split(":")
        if port == node_port:
            neighbours.remove(port)
            break
    startService(port)


def startService(port):
    from proto.store_impl import descen_servicer
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=5))
    store_pb2_grpc.add_KeyValueStoreServicer_to_server(descen_servicer, server)
    server.add_insecure_port('localhost:' + str(port))
    server.start()
    server.wait_for_termination()
