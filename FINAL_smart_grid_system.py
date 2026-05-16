
import socket
import threading
import random
import time

HOST = "127.0.0.1"
PORT = 5000

def handle_client(conn, addr):
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(1024).decode()

        if not data:
            break

        value = int(data)
        print(f"Received Energy Usage: {value} MW")

        if value > 80:
            print("Warning: High Energy Consumption Detected")

    conn.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print("Smart Grid Monitoring Server Started")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()

def sector_node():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))

    while True:
        energy = random.randint(20, 100)
        client.send(str(energy).encode())
        time.sleep(2)

if __name__ == "__main__":
    server_thread = threading.Thread(target=start_server)
    server_thread.start()

    time.sleep(2)

    sector_node()
