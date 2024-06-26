# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/store.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/store.proto\x12\x10\x64istributedstore\x1a\x1bgoogle/protobuf/empty.proto\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1e\n\x0bPutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"+\n\x0bGetResponse\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05\x66ound\x18\x02 \x01(\x08\"\"\n\x0fSlowDownRequest\x12\x0f\n\x07seconds\x18\x01 \x01(\x05\"#\n\x10SlowDownResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x10\n\x0eRestoreRequest\"\"\n\x0fRestoreResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"+\n\rCommitRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"!\n\x0e\x43ommitResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1c\n\tSlaveInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"*\n\x08Response\x12\r\n\x05store\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x1d\n\x0evoteGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"?\n\x0fvoteGetResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\r\n\x05value\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\"0\n\x0fvotePutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0c\n\x04size\x18\x02 \x01(\x05\"\x07\n\x05\x45mpty2\xbf\x05\n\rKeyValueStore\x12\x42\n\x03put\x12\x1c.distributedstore.PutRequest\x1a\x1d.distributedstore.PutResponse\x12\x42\n\x03get\x12\x1c.distributedstore.GetRequest\x1a\x1d.distributedstore.GetResponse\x12Q\n\x08slowDown\x12!.distributedstore.SlowDownRequest\x1a\".distributedstore.SlowDownResponse\x12N\n\x07restore\x12 .distributedstore.RestoreRequest\x1a!.distributedstore.RestoreResponse\x12N\n\tcanCommit\x12\x1f.distributedstore.CommitRequest\x1a .distributedstore.CommitResponse\x12M\n\x08\x64oCommit\x12\x1f.distributedstore.CommitRequest\x1a .distributedstore.CommitResponse\x12H\n\rregisterSlave\x12\x1b.distributedstore.SlaveInfo\x1a\x1a.distributedstore.Response\x12N\n\x07voteGet\x12 .distributedstore.voteGetRequest\x1a!.distributedstore.voteGetResponse\x12J\n\x07votePut\x12\x1c.distributedstore.PutRequest\x1a!.distributedstore.votePutResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.store_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_PUTREQUEST']._serialized_start=68
  _globals['_PUTREQUEST']._serialized_end=108
  _globals['_PUTRESPONSE']._serialized_start=110
  _globals['_PUTRESPONSE']._serialized_end=140
  _globals['_GETREQUEST']._serialized_start=142
  _globals['_GETREQUEST']._serialized_end=167
  _globals['_GETRESPONSE']._serialized_start=169
  _globals['_GETRESPONSE']._serialized_end=212
  _globals['_SLOWDOWNREQUEST']._serialized_start=214
  _globals['_SLOWDOWNREQUEST']._serialized_end=248
  _globals['_SLOWDOWNRESPONSE']._serialized_start=250
  _globals['_SLOWDOWNRESPONSE']._serialized_end=285
  _globals['_RESTOREREQUEST']._serialized_start=287
  _globals['_RESTOREREQUEST']._serialized_end=303
  _globals['_RESTORERESPONSE']._serialized_start=305
  _globals['_RESTORERESPONSE']._serialized_end=339
  _globals['_COMMITREQUEST']._serialized_start=341
  _globals['_COMMITREQUEST']._serialized_end=384
  _globals['_COMMITRESPONSE']._serialized_start=386
  _globals['_COMMITRESPONSE']._serialized_end=419
  _globals['_SLAVEINFO']._serialized_start=421
  _globals['_SLAVEINFO']._serialized_end=449
  _globals['_RESPONSE']._serialized_start=451
  _globals['_RESPONSE']._serialized_end=493
  _globals['_VOTEGETREQUEST']._serialized_start=495
  _globals['_VOTEGETREQUEST']._serialized_end=524
  _globals['_VOTEGETRESPONSE']._serialized_start=526
  _globals['_VOTEGETRESPONSE']._serialized_end=589
  _globals['_VOTEPUTRESPONSE']._serialized_start=591
  _globals['_VOTEPUTRESPONSE']._serialized_end=639
  _globals['_EMPTY']._serialized_start=641
  _globals['_EMPTY']._serialized_end=648
  _globals['_KEYVALUESTORE']._serialized_start=651
  _globals['_KEYVALUESTORE']._serialized_end=1354
# @@protoc_insertion_point(module_scope)
