# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x63ommon/transaction.proto\x12\x06shared\"D\n\x0bTransaction\x12\n\n\x02id\x18\x01 \x02(\t\x12\x14\n\x0coperation_id\x18\x02 \x02(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x02(\t\"\'\n\tOperation\x12\n\n\x02id\x18\x01 \x02(\t\x12\x0e\n\x06status\x18\x02 \x02(\t')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'common.transaction_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_TRANSACTION']._serialized_start=36
  _globals['_TRANSACTION']._serialized_end=104
  _globals['_OPERATION']._serialized_start=106
  _globals['_OPERATION']._serialized_end=145
# @@protoc_insertion_point(module_scope)
