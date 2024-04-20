# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: raft.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nraft.proto\"\x0e\n\x0c\x45mptyMessage\"\x1a\n\x07Message\x12\x0f\n\x07message\x18\x01 \x01(\t\"\x19\n\nMessageKey\x12\x0b\n\x03key\x18\x01 \x01(\t\"-\n\x0fMessageKeyValue\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t\"2\n\x0bPeerMessage\x12\x12\n\ntermNumber\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"h\n\x12PeerRequestMessage\x12\x12\n\ntermNumber\x18\x01 \x01(\x05\x12\x13\n\x0b\x63\x61ndidateId\x18\x02 \x01(\x05\x12\x14\n\x0clastLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0blastLogTerm\x18\x04 \x01(\x05\"\x8b\x01\n\x11PeerAppendMessage\x12\x12\n\ntermNumber\x18\x01 \x01(\x05\x12\x10\n\x08leaderId\x18\x02 \x01(\x05\x12\x14\n\x0cprevLogIndex\x18\x03 \x01(\x05\x12\x13\n\x0bprevLogTerm\x18\x04 \x01(\x05\x12\x0f\n\x07\x65ntries\x18\x05 \x01(\t\x12\x14\n\x0cleaderCommit\x18\x06 \x01(\x05\"4\n\x0fMessageResponse\x12\x10\n\x08received\x18\x01 \x01(\x08\x12\x0f\n\x07message\x18\x02 \x01(\t\" \n\x11\x44\x65leteTaskRequest\x12\x0b\n\x03key\x18\x01 \x01(\t2\xd7\x02\n\x06Server\x12\x34\n\x0bRequestVote\x12\x13.PeerRequestMessage\x1a\x10.MessageResponse\x12\x35\n\rAppendEntries\x12\x12.PeerAppendMessage\x1a\x10.MessageResponse\x12,\n\tGetLeader\x12\r.EmptyMessage\x1a\x10.MessageResponse\x12%\n\x07Suspend\x12\x08.Message\x1a\x10.MessageResponse\x12,\n\x06SetVal\x12\x10.MessageKeyValue\x1a\x10.MessageResponse\x12\'\n\x06GetVal\x12\x0b.MessageKey\x1a\x10.MessageResponse\x12\x34\n\nDeleteTask\x12\x12.DeleteTaskRequest\x1a\x10.MessageResponse\"\x00\x62\x06proto3')



_EMPTYMESSAGE = DESCRIPTOR.message_types_by_name['EmptyMessage']
_MESSAGE = DESCRIPTOR.message_types_by_name['Message']
_MESSAGEKEY = DESCRIPTOR.message_types_by_name['MessageKey']
_MESSAGEKEYVALUE = DESCRIPTOR.message_types_by_name['MessageKeyValue']
_PEERMESSAGE = DESCRIPTOR.message_types_by_name['PeerMessage']
_PEERREQUESTMESSAGE = DESCRIPTOR.message_types_by_name['PeerRequestMessage']
_PEERAPPENDMESSAGE = DESCRIPTOR.message_types_by_name['PeerAppendMessage']
_MESSAGERESPONSE = DESCRIPTOR.message_types_by_name['MessageResponse']
_DELETETASKREQUEST = DESCRIPTOR.message_types_by_name['DeleteTaskRequest']
EmptyMessage = _reflection.GeneratedProtocolMessageType('EmptyMessage', (_message.Message,), {
  'DESCRIPTOR' : _EMPTYMESSAGE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:EmptyMessage)
  })
_sym_db.RegisterMessage(EmptyMessage)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)

MessageKey = _reflection.GeneratedProtocolMessageType('MessageKey', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEKEY,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:MessageKey)
  })
_sym_db.RegisterMessage(MessageKey)

MessageKeyValue = _reflection.GeneratedProtocolMessageType('MessageKeyValue', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGEKEYVALUE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:MessageKeyValue)
  })
_sym_db.RegisterMessage(MessageKeyValue)

PeerMessage = _reflection.GeneratedProtocolMessageType('PeerMessage', (_message.Message,), {
  'DESCRIPTOR' : _PEERMESSAGE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:PeerMessage)
  })
_sym_db.RegisterMessage(PeerMessage)

PeerRequestMessage = _reflection.GeneratedProtocolMessageType('PeerRequestMessage', (_message.Message,), {
  'DESCRIPTOR' : _PEERREQUESTMESSAGE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:PeerRequestMessage)
  })
_sym_db.RegisterMessage(PeerRequestMessage)

PeerAppendMessage = _reflection.GeneratedProtocolMessageType('PeerAppendMessage', (_message.Message,), {
  'DESCRIPTOR' : _PEERAPPENDMESSAGE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:PeerAppendMessage)
  })
_sym_db.RegisterMessage(PeerAppendMessage)

MessageResponse = _reflection.GeneratedProtocolMessageType('MessageResponse', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGERESPONSE,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:MessageResponse)
  })
_sym_db.RegisterMessage(MessageResponse)

DeleteTaskRequest = _reflection.GeneratedProtocolMessageType('DeleteTaskRequest', (_message.Message,), {
  'DESCRIPTOR' : _DELETETASKREQUEST,
  '__module__' : 'raft_pb2'
  # @@protoc_insertion_point(class_scope:DeleteTaskRequest)
  })
_sym_db.RegisterMessage(DeleteTaskRequest)

_SERVER = DESCRIPTOR.services_by_name['Server']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _EMPTYMESSAGE._serialized_start=14
  _EMPTYMESSAGE._serialized_end=28
  _MESSAGE._serialized_start=30
  _MESSAGE._serialized_end=56
  _MESSAGEKEY._serialized_start=58
  _MESSAGEKEY._serialized_end=83
  _MESSAGEKEYVALUE._serialized_start=85
  _MESSAGEKEYVALUE._serialized_end=130
  _PEERMESSAGE._serialized_start=132
  _PEERMESSAGE._serialized_end=182
  _PEERREQUESTMESSAGE._serialized_start=184
  _PEERREQUESTMESSAGE._serialized_end=288
  _PEERAPPENDMESSAGE._serialized_start=291
  _PEERAPPENDMESSAGE._serialized_end=430
  _MESSAGERESPONSE._serialized_start=432
  _MESSAGERESPONSE._serialized_end=484
  _DELETETASKREQUEST._serialized_start=486
  _DELETETASKREQUEST._serialized_end=518
  _SERVER._serialized_start=521
  _SERVER._serialized_end=864
# @@protoc_insertion_point(module_scope)
