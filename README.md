# gRPC Python Application

This is a simple gRPC-based application with a client-server architecture. The server provides a `SayHello` method which sends a greeting message to the client.

## Requirements

Before running the application, make sure you have the following:

- Python 3.10 or higher
- `grpcio` and `grpcio-tools` libraries installed

## Installation and Running

### Option 1: Run Locally

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/JordinPinzon/proyecto_Rcp.git
    cd proyect_Rcp
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate  # On Windows
    source venv/bin/activate  # On macOS/Linux
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Generate the gRPC code from the `.proto` file:

    ```bash
    python -m grpc_tools.protoc -I./protos --python_out=./generated --grpc_python_out=./generated ./protos/service.proto
    ```

5. Run the server:

    ```bash
    python server.py
    ```

    The server will be available at `localhost:50051` for incoming gRPC requests.

6. In another terminal, run the client:

    ```bash
    python client.py
    ```

    You should see the greeting message returned from the server.
