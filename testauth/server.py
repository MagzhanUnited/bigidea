import grpc
from concurrent import futures
import time

# import the generated classes
import autorizer_pb2
import autorizer_pb2_grpc


# import the original calculator.py
import auth

# create a class to define the server functions, derived from
# autorizer_pb2_grpc.AuthServiceServicer
class AuthServiceServicer(autorizer_pb2_grpc.AuthServiceServicer):

    # calculator.square_root is exposed here
    # the request and response are of the data type
    # autorizer_pb2.AuthResponse
    def GetAccessToken(self, request, context):
        response = autorizer_pb2.AuthResponse()
        response.access_token = auth.get_access_token(request.email, request.password)
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_AuthServiceServicer_to_server`
# to add the defined class to the server
autorizer_pb2_grpc.add_AuthServiceServicer_to_server(
        AuthServiceServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)