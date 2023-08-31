import grpc
import sys
sys.path.append('/Users/magzhanzhumabaev/Desktop/smallgay/testauth')
import autorizer_pb2 as grpc1
import autorizer_pb2_grpc as grpc2

def get_access_token(email, password):
    # Open a gRPC channel
    channel = grpc.insecure_channel('localhost:50051', options=(('grpc.enable_http_proxy', 0),))

    # Create a stub (client)
    stub = grpc2.AuthServiceStub(channel)

    # Create a valid request message
    request = grpc1.AuthRequest(email=email, password=password)

    try:
        # Make the call
        response = stub.GetAccessToken(request)
        return response.access_token
    except grpc.RpcError as e:
        print(f"Error calling gRPC service: {e}")
        print(f"Details: {e.details()}")
        return None
# import grpc
# import sys
# sys.path.append('/Users/magzhanzhumabaev/Desktop/smallgay/testauth') 
# # import the generated classes
# import autorizer_pb2 as gprc1
# import autorizer_pb2_grpc as grpc2
# # open a gRPC channel
# channel = grpc.insecure_channel('localhost:50051')

# # create a stub (client)
# stub = grpc2.AuthServiceStub(channel)

# # create a valid request message
# request = gprc1.AuthRequest(email="nurlannurlanov612@gmail.com", password="magzhan2005")

# # make the call
# response = stub.GetAccessToken(request)

# # et voilà
# print(response.access_token)

# import grpc
# import sys
# sys.path.append('/Users/magzhanzhumabaev/Desktop/smallgay/testauth') 
# # import the generated classes
# import autorizer_pb2 as gprc1
# import autorizer_pb2_grpc as grpc2
# # open a gRPC channel
# # def get_access_token(email, password):
# channel = grpc.insecure_channel('localhost:50051')

# # create a stub (client)

# stub = grpc2.AuthServiceStub(channel)
# # create a valid request message
# request = gprc1.AuthRequest(email="nurlannurlanov@gmail.com", password="magzhan2005")
# # request = gprc1.AuthRequest(email=email, password=password)

# # make the call
# response = stub.GetAccessToken(request)

# # et voilà
# print(response.access_token)
#     # return response.access_token

# # get_access_token(email="nurlannurlanov@gmail.com", password="magzhan2005")