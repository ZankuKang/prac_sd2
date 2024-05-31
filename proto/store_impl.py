from proto import store_pb2
import time
import json

# Basic class that will implement the store.proto functions
# In particular, this one will implement the methods required for
# centralized slaves
class StorageBasicService:

    # Builder
    def __init__(self):
        self.storage = {}
        self.slow_secs = 0

    # Setters
    def setStorage(self, storage):
        self.storage = storage

    # Base API functions
    def slowDown(self, slow_down_request, context):
        self.slow_secs = slow_down_request.seconds
        return store_pb2.SlowDownResponse(success=True)

    def restore(self, restore_request, context):
        self.slow_secs = 0
        return store_pb2.RestoreResponse(success=True)

    def get(self, get_request, context):
        time.sleep(self.slow_secs)
        val = self.storage.get(get_request.key)
        if val is None:
            return store_pb2.GetResponse(value="", found=False)
        return store_pb2.GetResponse(value=val, found=True)

    # Turns out we still have to define this function here, because the tests will try
    # to run the put function without looking if it is a slave or not
    def put(self, put_request, context):
        return store_pb2.PutResponse(success=False)

    # Just like the put function, we still have to implement the "illegal" functions for
    # the slaves
    def registerSlave(self, slave_info, context):
        return store_pb2.Response(store="", success=False)

    # 2PC functions
    def canCommit(self, commit_request, context):
        time.sleep(self.slow_secs)
        return store_pb2.SlowDownResponse(success=True)

    def doCommit(self, commit_request, context):
        self.storage[commit_request.key] = commit_request.value
        return store_pb2.CommitResponse(success=True)

    # Persistence functions
    def loadStorage(self):
        try:
            store = open("database.txt", "r")
            pairs = store.readlines()
            for pair in pairs:
                pair = pair.strip()
                key, value = pair.split(":")
                self.storage[key] = value
            store.close()
        except FileNotFoundError:
            store = open("database.txt", 'w')
            store.close()

    def saveStorage(self, key, value):
        try:
            store = open("database.txt", 'w')
            store.write(key + ":" + value + "\n")
            store.close()
        except FileNotFoundError:
            print("Unable to write to storage")


# This class will inherit the previous functions while overriding
# some methods, like put()
class MasterStorageService(StorageBasicService):

    def __init__(self):
        super().__init__()
        self.registered_slaves = []

    def setSlaves(self, registered_slaves):
        self.registered_slaves = registered_slaves

    def getSlaves(self):
        return self.registered_slaves

    def put(self, put_request, context):
        from CentralizedDir import Master
        if Master.Two_PC(put_request):
            self.storage[put_request.key] = put_request.value
            self.saveStorage(put_request.key, put_request.value)
            return store_pb2.PutResponse(success=True)
        else:
            return store_pb2.PutResponse(success=False)

    def registerSlave(self, slave_info, context):
        self.registered_slaves.append(slave_info.address)
        return store_pb2.Response(store=(json.dumps(self.storage)), success=True)


# Like the previous class, but this one implements the methods required for the
# decentralized nodes
class DecentralizedService(StorageBasicService):

    def __init__(self):
        super().__init__()
        # The node's vote size, initialized to 4 as a placeholder
        self.size = 4
        # The node's port, initialized to 53 because we like DNS
        self.port = 53
        from DescentralizedDir import DesNode
        self.desnode = DesNode

    def setVote(self, size):
        self.size = size

    def setPort(self, port):
        self.port = port

    def getPort(self):
        return self.port

    # This method will require askVoteGet (implemented in DescentralizedDir.Desnode.py)
    # to perform the quorum voting
    def get(self, get_request, context):
        local_val = self.storage.get(get_request.key)
        value = self.desnode.askVoteGet(get_request, local_val, self.size)
        if value is not None:
            return store_pb2.GetResponse(value=value, found=True)
        else:
            return store_pb2.GetResponse(value="", found=False)

    # Ths will be called when some has received a get petition
    def voteGet(self, vote_request, context):
        time.sleep(self.slow_secs)
        value = self.storage.get(vote_request.key)
        if value is not None:
            return store_pb2.voteGetResponse(success=True, value=value, size=self.size)
        else:
            return store_pb2.voteGetResponse(success=False, value=value, size=self.size)

    def put(self, put_request, context):
        if self.desnode.askVotePut(put_request, self.size):
            self.storage[put_request.key] = put_request.value
            self.saveStorageDes(put_request.key, put_request.value)
            return store_pb2.PutResponse(success=True)
        else:
            return store_pb2.PutResponse(success=False)

    def votePut(self, put_request, context):
        time.sleep(self.slow_secs)
        return store_pb2.votePutResponse(success=True, size=self.size)

    # We create different files for the different nodes
    def loadStorageDes(self):
        try:
            store = open("storage" + str(self.port) + ".txt", "r")
            pairs = store.readlines()
            for pair in pairs:
                pair = pair.strip()
                key, value = pair.split(":")
                self.storage[key] = value
            store.close()
        except FileNotFoundError:
            store = open("storage" + str(self.port) + ".txt", 'w')
            store.close()

    def saveStorageDes(self, key, value):
        try:
            store = open("storage" + str(self.port) + ".txt", 'w')
            store.write(key + ":" + value + "\n")
            store.close()
        except FileNotFoundError:
            print("Unable to write to storage")


basic_servicer = StorageBasicService()
master_servicer = MasterStorageService()
descen_servicer = DecentralizedService()
