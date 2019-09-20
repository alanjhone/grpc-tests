import grpc
from concurrent import futures
import time

import echo_pb2 as echo 
import echo_pb2_grpc as rpc

class EchoService(rpc.EchoServiceServicer):

    def __init__(self):
        self.chats = []

    def GetMessage(self, request, context):
        metadata = dict(context.invocation_metadata())
        print(metadata)
        response.message = echo.Response(request.name + request.lastName)
        return echo.Response(response)

    def EchoStream(self, request, context):
        
        for req in request:
            response = echo.Response(
                req.name + req.lastName
            )
            yield echo.NameResponse(response=response)


if __name__ == '__main__':

    port = 50051
    
    # create a gRPC server
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_EchoServiceServicer_to_server(EchoService(), server)

    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()

    # Server starts in background (another thread) so keep waiting
    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)