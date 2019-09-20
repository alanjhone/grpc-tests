import grpc
from concurrent import futures
import time

import hello_pb2 as hello 
import hello_pb2_grpc as rpc

class HelloService(rpc.HelloServiceServicer):

    def __init__(self):
        self.prev_request = []

    def BidiHello(self, request_iterator, context):
        for request in request_iterator:
            print(request)
            self.prev_request.append(request)
            response = hello.HelloResponse(
                message=request.message
            )
            yield response

    def RequestStream(self, request_iterator, context):
        lastindex = 0
        while True:
            while len(self.prev_request) > lastindex:
                n = self.prev_request[lastindex]
                lastindex += 1
                yield n

if __name__ == '__main__':

    port = 50051
    
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    rpc.add_HelloServiceServicer_to_server(HelloService(), server)

    print('Starting server. Listening...')
    server.add_insecure_port('[::]:' + str(port))
    server.start()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop(0)