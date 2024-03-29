# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: echo.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='echo.proto',
  package='grpc',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\necho.proto\x12\x04grpc\"\x07\n\x05\x45mpty\"\x1b\n\x08Response\x12\x0f\n\x07message\x18\x01 \x01(\t\"0\n\x0cNameResponse\x12 \n\x08response\x18\x01 \x03(\x0b\x32\x0e.grpc.Response\")\n\x07Request\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08lastName\x18\x02 \x01(\t2q\n\x0b\x45\x63hoService\x12-\n\nGetMessage\x12\r.grpc.Request\x1a\x0e.grpc.Response(\x01\x12\x33\n\nEchoStream\x12\r.grpc.Request\x1a\x12.grpc.NameResponse(\x01\x30\x01\x62\x06proto3')
)




_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='grpc.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=20,
  serialized_end=27,
)


_RESPONSE = _descriptor.Descriptor(
  name='Response',
  full_name='grpc.Response',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='message', full_name='grpc.Response.message', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=56,
)


_NAMERESPONSE = _descriptor.Descriptor(
  name='NameResponse',
  full_name='grpc.NameResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='grpc.NameResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=106,
)


_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='grpc.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='grpc.Request.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='lastName', full_name='grpc.Request.lastName', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=149,
)

_NAMERESPONSE.fields_by_name['response'].message_type = _RESPONSE
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY
DESCRIPTOR.message_types_by_name['Response'] = _RESPONSE
DESCRIPTOR.message_types_by_name['NameResponse'] = _NAMERESPONSE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), {
  'DESCRIPTOR' : _EMPTY,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Empty)
  })
_sym_db.RegisterMessage(Empty)

Response = _reflection.GeneratedProtocolMessageType('Response', (_message.Message,), {
  'DESCRIPTOR' : _RESPONSE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Response)
  })
_sym_db.RegisterMessage(Response)

NameResponse = _reflection.GeneratedProtocolMessageType('NameResponse', (_message.Message,), {
  'DESCRIPTOR' : _NAMERESPONSE,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.NameResponse)
  })
_sym_db.RegisterMessage(NameResponse)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), {
  'DESCRIPTOR' : _REQUEST,
  '__module__' : 'echo_pb2'
  # @@protoc_insertion_point(class_scope:grpc.Request)
  })
_sym_db.RegisterMessage(Request)



_ECHOSERVICE = _descriptor.ServiceDescriptor(
  name='EchoService',
  full_name='grpc.EchoService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=151,
  serialized_end=264,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetMessage',
    full_name='grpc.EchoService.GetMessage',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_RESPONSE,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='EchoStream',
    full_name='grpc.EchoService.EchoStream',
    index=1,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_NAMERESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ECHOSERVICE)

DESCRIPTOR.services_by_name['EchoService'] = _ECHOSERVICE

# @@protoc_insertion_point(module_scope)
