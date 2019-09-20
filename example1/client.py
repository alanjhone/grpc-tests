import grpc

# import the generated classes
import echo_pb2 as echo
import echo_pb2_grpc as echo_service

channel = grpc.insecure_channel('localhost:50051')
try:
    grpc.channel_ready_future(channel).result(timeout=10)
except grpc.FutureTimeoutError:
    sys.exit('Error connecting to server')
else:
    stub = echo_service.UsersStub(channel)


response = stub.CreateUser(
    echo.CreateUserRequest(username='tom'),
    metadata=metadata,
)

if response:
    print("User created:", response.user.username)


request = echo.Request(
    response=[echo.Request(name="alexa", lastName="brito"),
          echo.Request(username="christie", user_id=1)]
)


response = echo_service.EchoStream(request)
for resp in response:
    print(resp)