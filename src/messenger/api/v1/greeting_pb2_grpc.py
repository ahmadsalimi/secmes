# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from messenger.api.v1 import greeting_pb2 as messenger_dot_api_dot_v1_dot_greeting__pb2


class GreetingServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SayHello = channel.unary_unary(
                '/v1.GreetingService/SayHello',
                request_serializer=messenger_dot_api_dot_v1_dot_greeting__pb2.GreetingRequest.SerializeToString,
                response_deserializer=messenger_dot_api_dot_v1_dot_greeting__pb2.GreetingResponse.FromString,
                )


class GreetingServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def SayHello(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_GreetingServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SayHello': grpc.unary_unary_rpc_method_handler(
                    servicer.SayHello,
                    request_deserializer=messenger_dot_api_dot_v1_dot_greeting__pb2.GreetingRequest.FromString,
                    response_serializer=messenger_dot_api_dot_v1_dot_greeting__pb2.GreetingResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'v1.GreetingService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class GreetingService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def SayHello(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/v1.GreetingService/SayHello',
            messenger_dot_api_dot_v1_dot_greeting__pb2.GreetingRequest.SerializeToString,
            messenger_dot_api_dot_v1_dot_greeting__pb2.GreetingResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)