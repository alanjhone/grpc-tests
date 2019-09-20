import logging

import threading

import grpc
import time
import sys

import hello_pb2 as hello
import hello_pb2_grpc as hello_grpc

address = 'localhost'
port = 50051


class Client:

    def __init__(self):
        channel = grpc.insecure_channel(address + ':' + str(port))
        self.stub = hello_grpc.HelloServiceStub(channel)
        t = threading.Thread(target=self.__listen_for_messages)
        t.start()

    def __listen_for_messages(self):
        for response in self.stub.RequestStream(hello.Empty()):
            print("[Received]: {}".format(response.message))

    def make_request(self, message):
        return hello.HelloRequest(
                message=message
            )


    def generate_messages(self):
        messages = [
            self.make_request("First message"),
            self.make_request("Second message"),
            self.make_request("Third message"),
            self.make_request("Fourth message"),
            self.make_request("Fifth message"),
        ]

        for msg in messages:
            print("Sending message: %s" % (msg.message))

            yield msg


    def getBidiHelloResponse(self):
        responses = self.stub.BidiHello(self.generate_messages())
        print(responses)
        for response in responses:
            print("Received message %s" % (response.message))


    def run(self):
        print("-------------- BidirectionalHello --------------")
        self.getBidiHelloResponse()

if __name__ == '__main__':
    client = Client()
    client.run()
