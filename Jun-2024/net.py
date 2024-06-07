import socket
import time
import json

def handle_client(conn):
    try:
        # Receiving data from the client
        data = conn.recv(1024).decode('utf-8')
        print("Received message:", data)
        
        # Simulate processing time of 5 seconds
        time.sleep(5)
        
        # Prepare response message based on the provided format
        response = {
            "msg_type": "resp_prepay",
            "src_id": "Team1",
            "dst_id": "Team9",
            "msg_content": {
                "item_code": "01",
                "item_num": "1",
                "availability": "T"
            }
        }
        
        # Send the response message
        conn.send(json.dumps(response).encode('utf-8'))
        print("Sent response:", response)
    finally:
        conn.close()

def start_server():
    # Create a socket and bind to port 9999
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.bind(('127.0.0.1', 9999))
        server.listen()
        print("Server listening on port 9999...")
        
        while True:
            conn, addr = server.accept()
            print(f"Connected by {addr}")
            handle_client(conn)

# Run the server
if __name__ == "__main__":
    start_server()
