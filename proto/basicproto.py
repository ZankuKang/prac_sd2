from proto import store_pb2
import time
import random
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
        super.__init__()

    def put(self, put_request, context):
        # We have to implement the two phase commit before
        self.storage[put_request.key] = put_request.value
        return store_pb2.PutResponse(success=True)
    