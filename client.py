import grpc
from generated import service_pb2, service_pb2_grpc

# Función para crear una conexión con el servidor gRPC
def run():
    # Establecer conexión con el servidor gRPC
    with grpc.insecure_channel('localhost:50051') as channel:
        # Crear un stub (cliente) para el servicio
        stub = service_pb2_grpc.MyServiceStub(channel)
        
        # Crear una solicitud para el método SayHello
        request = service_pb2.HelloRequest(name="Mundo")
        
        # Hacer la llamada al servidor
        response = stub.SayHello(request)
        
        # Mostrar la respuesta del servidor
        print(f"Respuesta del servidor: {response.message}")

if __name__ == "__main__":
    run()
