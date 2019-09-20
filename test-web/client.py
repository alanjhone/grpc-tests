import grpc

# import the generated classes
import calculator_pb2
import calculator_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a stub (client)
stub = calculator_pb2_grpc.CalculatorStub(channel)

# create a valid request message
msg = calculator_pb2.Message(msg="Alan")

# create a valid request message
number = calculator_pb2.Number(value=16)

# make the call
response = stub.HelloWorld(msg)

print(response.msg)

response = stub.SquareRoot(number)

print(response.value)


number2 = calculator_pb2.Number2(x=16, y=4)

# make the call
response = stub.Sum(number2)

print(response)