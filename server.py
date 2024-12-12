import grpc
from concurrent import futures
from generated import service_pb2, service_pb2_grpc

# Implementación de la clase del servicio
class MyService(service_pb2_grpc.MyServiceServicer):
    def SayHello(self, request, context):
        # Lógica del método SayHello
        print(f"Recibido: {request.name}")
        return service_pb2.HelloResponse(message=f"¡Hola, {request.name}!")

# Función principal para iniciar el servidor
def serve():
    # Crear un servidor gRPC
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    # Registrar el servicio en el servidor
    service_pb2_grpc.add_MyServiceServicer_to_server(MyService(), server)
    # Escuchar en el puerto 50051
    server.add_insecure_port("[::]:50051")
    print("Servidor gRPC escuchando en el puerto 50051...")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
