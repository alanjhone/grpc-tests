import logging

import grpc

import hello_pb2 as hello
import hello_pb2_grpc as hello_grpc


def make_request(message):
    return hello.HelloRequest(
        	message=message
        )


def generate_messages():
    messages = [
        make_request("First message"),
        make_request("Second message"),
        make_request("Third message"),
        make_request("Fourth message"),
        make_request("Fifth message"),
    ]

    for msg in messages:
        print("Sending message: %s" % (msg.message))

        yield msg


def getBidiHelloResponse(stub):
    responses = stub.BidiHello(generate_messages())
    print(responses)
    for response in responses:
        print("Received message %s" % (response.message))


def run():

    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_grpc.HelloServiceStub(channel)
        print("-------------- BidirectionalHello --------------")
        getBidiHelloResponse(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()