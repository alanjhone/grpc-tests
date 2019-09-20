# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import echo_pb2 as echo__pb2


class EchoServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetMessage = channel.stream_unary(
        '/grpc.EchoService/GetMessage',
        request_serializer=echo__pb2.Request.SerializeToString,
        response_deserializer=echo__pb2.Response.FromString,
        )
    self.EchoStream = channel.stream_stream(
        '/grpc.EchoService/EchoStream',
        request_serializer=echo__pb2.Request.SerializeToString,
        response_deserializer=echo__pb2.NameResponse.FromString,
        )


class EchoServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetMessage(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def EchoStream(self, request_iterator, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_EchoServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetMessage': grpc.stream_unary_rpc_method_handler(
          servicer.GetMessage,
          request_deserializer=echo__pb2.Request.FromString,
          response_serializer=echo__pb2.Response.SerializeToString,
      ),
      'EchoStream': grpc.stream_stream_rpc_method_handler(
          servicer.EchoStream,
          request_deserializer=echo__pb2.Request.FromString,
          response_serializer=echo__pb2.NameResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'grpc.EchoService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
