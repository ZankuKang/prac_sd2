# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from proto import store_pb2 as proto_dot_store__pb2


class KeyValueStoreStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.put = channel.unary_unary(
                '/distributedstore.KeyValueStore/put',
                request_serializer=proto_dot_store__pb2.PutRequest.SerializeToString,
                response_deserializer=proto_dot_store__pb2.PutResponse.FromString,
                )
        self.get = channel.unary_unary(
                '/distributedstore.KeyValueStore/get',
                request_serializer=proto_dot_store__pb2.GetRequest.SerializeToString,
                response_deserializer=proto_dot_store__pb2.GetResponse.FromString,
                )
        self.slowDown = channel.unary_unary(
                '/distributedstore.KeyValueStore/slowDown',
                request_serializer=proto_dot_store__pb2.SlowDownRequest.SerializeToString,
                response_deserializer=proto_dot_store__pb2.SlowDownResponse.FromString,
                )
        self.restore = channel.unary_unary(
                '/distributedstore.KeyValueStore/restore',
                request_serializer=proto_dot_store__pb2.RestoreRequest.SerializeToString,
                response_deserializer=proto_dot_store__pb2.RestoreResponse.FromString,
                )


class KeyValueStoreServicer(object):
    """Missing associated documentation comment in .proto file."""

    def put(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def get(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def slowDown(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def restore(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'put': grpc.unary_unary_rpc_method_handler(
                    servicer.put,
                    request_deserializer=proto_dot_store__pb2.PutRequest.FromString,
                    response_serializer=proto_dot_store__pb2.PutResponse.SerializeToString,
            ),
            'get': grpc.unary_unary_rpc_method_handler(
                    servicer.get,
                    request_deserializer=proto_dot_store__pb2.GetRequest.FromString,
                    response_serializer=proto_dot_store__pb2.GetResponse.SerializeToString,
            ),
            'slowDown': grpc.unary_unary_rpc_method_handler(
                    servicer.slowDown,
                    request_deserializer=proto_dot_store__pb2.SlowDownRequest.FromString,
                    response_serializer=proto_dot_store__pb2.SlowDownResponse.SerializeToString,
            ),
            'restore': grpc.unary_unary_rpc_method_handler(
                    servicer.restore,
                    request_deserializer=proto_dot_store__pb2.RestoreRequest.FromString,
                    response_serializer=proto_dot_store__pb2.RestoreResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'distributedstore.KeyValueStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class KeyValueStore(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def put(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/put',
            proto_dot_store__pb2.PutRequest.SerializeToString,
            proto_dot_store__pb2.PutResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def get(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/get',
            proto_dot_store__pb2.GetRequest.SerializeToString,
            proto_dot_store__pb2.GetResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def slowDown(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/slowDown',
            proto_dot_store__pb2.SlowDownRequest.SerializeToString,
            proto_dot_store__pb2.SlowDownResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def restore(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/distributedstore.KeyValueStore/restore',
            proto_dot_store__pb2.RestoreRequest.SerializeToString,
            proto_dot_store__pb2.RestoreResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
