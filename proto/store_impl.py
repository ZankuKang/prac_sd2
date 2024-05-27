from proto import store_pb2
import time
import json


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


basic_servicer = StorageBasicService()
master_servicer = MasterStorageService()