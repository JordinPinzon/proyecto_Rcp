import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "generated")))

from generated import service_pb2, service_pb2_grpc
from service_pb2 import HelloRequest, HelloResponse
from service_pb2_grpc import MyService


print("¡Código generado correctamente!")
