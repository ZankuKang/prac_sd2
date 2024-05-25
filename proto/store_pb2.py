# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/store.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11proto/store.proto\x12\x10\x64istributedstore\"(\n\nPutRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"\x1e\n\x0bPutResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x19\n\nGetRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\"+\n\x0bGetResponse\x12\r\n\x05value\x18\x01 \x01(\t\x12\r\n\x05\x66ound\x18\x02 \x01(\x08\"\"\n\x0fSlowDownRequest\x12\x0f\n\x07seconds\x18\x01 \x01(\x05\"#\n\x10SlowDownResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x10\n\x0eRestoreRequest\"\"\n\x0fRestoreResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"+\n\rCommitRequest\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"!\n\x0e\x43ommitResponse\x12\x0f\n\x07success\x18\x01 \x01(\x08\"\x1c\n\tSlaveInfo\x12\x0f\n\x07\x61\x64\x64ress\x18\x01 \x01(\t\"*\n\x08Response\x12\r\n\x05store\x18\x01 \x01(\t\x12\x0f\n\x07success\x18\x02 \x01(\x08\"\x07\n\x05\x45mpty2\xa3\x04\n\rKeyValueStore\x12\x42\n\x03put\x12\x1c.distributedstore.PutRequest\x1a\x1d.distributedstore.PutResponse\x12\x42\n\x03get\x12\x1c.distributedstore.GetRequest\x1a\x1d.distributedstore.GetResponse\x12Q\n\x08slowDown\x12!.distributedstore.SlowDownRequest\x1a\".distributedstore.SlowDownResponse\x12N\n\x07restore\x12 .distributedstore.RestoreRequest\x1a!.distributedstore.RestoreResponse\x12N\n\tcanCommit\x12\x1f.distributedstore.CommitRequest\x1a .distributedstore.CommitResponse\x12M\n\x08\x64oCommit\x12\x1f.distributedstore.CommitRequest\x1a .distributedstore.CommitResponse\x12H\n\rregisterSlave\x12\x1b.distributedstore.SlaveInfo\x1a\x1a.distributedstore.Responseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'proto.store_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_PUTREQUEST']._serialized_start=39
  _globals['_PUTREQUEST']._serialized_end=79
  _globals['_PUTRESPONSE']._serialized_start=81
  _globals['_PUTRESPONSE']._serialized_end=111
  _globals['_GETREQUEST']._serialized_start=113
  _globals['_GETREQUEST']._serialized_end=138
  _globals['_GETRESPONSE']._serialized_start=140
  _globals['_GETRESPONSE']._serialized_end=183
  _globals['_SLOWDOWNREQUEST']._serialized_start=185
  _globals['_SLOWDOWNREQUEST']._serialized_end=219
  _globals['_SLOWDOWNRESPONSE']._serialized_start=221
  _globals['_SLOWDOWNRESPONSE']._serialized_end=256
  _globals['_RESTOREREQUEST']._serialized_start=258
  _globals['_RESTOREREQUEST']._serialized_end=274
  _globals['_RESTORERESPONSE']._serialized_start=276
  _globals['_RESTORERESPONSE']._serialized_end=310
  _globals['_COMMITREQUEST']._serialized_start=312
  _globals['_COMMITREQUEST']._serialized_end=355
  _globals['_COMMITRESPONSE']._serialized_start=357
  _globals['_COMMITRESPONSE']._serialized_end=390
  _globals['_SLAVEINFO']._serialized_start=392
  _globals['_SLAVEINFO']._serialized_end=420
  _globals['_RESPONSE']._serialized_start=422
  _globals['_RESPONSE']._serialized_end=464
  _globals['_EMPTY']._serialized_start=466
  _globals['_EMPTY']._serialized_end=473
  _globals['_KEYVALUESTORE']._serialized_start=476
  _globals['_KEYVALUESTORE']._serialized_end=1023
# @@protoc_insertion_point(module_scope)
