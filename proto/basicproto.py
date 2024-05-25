from proto import store_pb2
import time
from centralizedDir import Master
import json


class BasicAPIService:
    def __init__(self):
        self.storage = {}
        self.slowdown = 0

    def set_storage(self, storage):
        self.storage = storage

    def get(self, get_request, context):
        value_to_find = get_request.key
        val = self.storage.get(value_to_find)
        time.sleep(self.slowdown)
        if val is not None:
            return store_pb2.GetResponse(value=val, found=True)
        else:
            return store_pb2.GetResponse(value=None, found=False)

    def put(self, put_request, context):
        return store_pb2.PutResponse(success=False)

    def slowDown(self, slow_down_request, context):
        self.slowdown = slow_down_request.seconds
        return store_pb2.SlowDownResponse(success=True)

    def restore(self, restore_request, context):
        self.slowdown = 0
        return store_pb2.RestoreResponse(success=True)

    def canCommit(self, commit_request, context):
        time.sleep(self.slowdown)
        return store_pb2.CommitResponse(success=True)

    def doCommit(self, commit_request, context):
        key = commit_request.key
        val = commit_request.value
        self.storage[key] = val
        return store_pb2.CommitResponse(success=True)

    def registerSlave(self, slave_info, context):
        return store_pb2.Response(success=False)


class MasterNodeService(BasicAPIService):
    def __init__(self):
        super().__init__()
        self.dis_queue = []

    def put(self, put_request, context):
        if Master.Two_PC(put_request, context):
            self.storage[put_request.key] = put_request.value
            return store_pb2.PutResponse(success=True)
        else:
            return store_pb2.PutResponse(success=False)

    def setDicoverQueue(self, dis_queue):
        self.dis_queue = dis_queue

    def registerSlave(self, slave_info, context):
        self.dis_queue.append(slave_info.address)  # IP:Port
        storageReplication = json.dumps(self.storage)
        return store_pb2.Response(store=storageReplication, success=True)

    def getDiscoverQueue(self):
        return self.dis_queue


centralized_servicer = BasicAPIService()
master_servicer = MasterNodeService()
