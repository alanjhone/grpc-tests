# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: calculator.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='calculator.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x10\x63\x61lculator.proto\"\x17\n\x06Number\x12\r\n\x05value\x18\x01 \x01(\x02\".\n\x07Number2\x12\t\n\x01x\x18\x01 \x01(\x02\x12\t\n\x01y\x18\x02 \x01(\x02\x12\r\n\x05value\x18\x03 \x01(\x02\"\x16\n\x07Message\x12\x0b\n\x03msg\x18\x01 \x01(\t2o\n\nCalculator\x12 \n\nSquareRoot\x12\x07.Number\x1a\x07.Number\"\x00\x12\x1b\n\x03Sum\x12\x08.Number2\x1a\x08.Number2\"\x00\x12\"\n\nHelloWorld\x12\x08.Message\x1a\x08.Message\"\x00\x62\x06proto3')
)




_NUMBER = _descriptor.Descriptor(
  name='Number',
  full_name='Number',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Number.value', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=20,
  serialized_end=43,
)


_NUMBER2 = _descriptor.Descriptor(
  name='Number2',
  full_name='Number2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='Number2.x', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='y', full_name='Number2.y', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='Number2.value', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=45,
  serialized_end=91,
)


_MESSAGE = _descriptor.Descriptor(
  name='Message',
  full_name='Message',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='msg', full_name='Message.msg', index=0,
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
  serialized_start=93,
  serialized_end=115,
)

DESCRIPTOR.message_types_by_name['Number'] = _NUMBER
DESCRIPTOR.message_types_by_name['Number2'] = _NUMBER2
DESCRIPTOR.message_types_by_name['Message'] = _MESSAGE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Number = _reflection.GeneratedProtocolMessageType('Number', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number)
  })
_sym_db.RegisterMessage(Number)

Number2 = _reflection.GeneratedProtocolMessageType('Number2', (_message.Message,), {
  'DESCRIPTOR' : _NUMBER2,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Number2)
  })
_sym_db.RegisterMessage(Number2)

Message = _reflection.GeneratedProtocolMessageType('Message', (_message.Message,), {
  'DESCRIPTOR' : _MESSAGE,
  '__module__' : 'calculator_pb2'
  # @@protoc_insertion_point(class_scope:Message)
  })
_sym_db.RegisterMessage(Message)



_CALCULATOR = _descriptor.ServiceDescriptor(
  name='Calculator',
  full_name='Calculator',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=117,
  serialized_end=228,
  methods=[
  _descriptor.MethodDescriptor(
    name='SquareRoot',
    full_name='Calculator.SquareRoot',
    index=0,
    containing_service=None,
    input_type=_NUMBER,
    output_type=_NUMBER,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Sum',
    full_name='Calculator.Sum',
    index=1,
    containing_service=None,
    input_type=_NUMBER2,
    output_type=_NUMBER2,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='HelloWorld',
    full_name='Calculator.HelloWorld',
    index=2,
    containing_service=None,
    input_type=_MESSAGE,
    output_type=_MESSAGE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_CALCULATOR)

DESCRIPTOR.services_by_name['Calculator'] = _CALCULATOR

# @@protoc_insertion_point(module_scope)
