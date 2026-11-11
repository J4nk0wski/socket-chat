import socket

class Server:
    def __init__(self, port=5050):
        self.PORT = port
        self.IP = socket.gethostbyname(socket.gethostname()) # temporary
        self.server_socket = socket.socket() # temporarily default parameters
        self.clients = [] # contains tuples (client_conn, client_addr)

        self.setup()

    def setup(self, max_connections_count=10):
        self.server_socket.bind((self.IP, self.PORT))
        self.server_socket.listen(max_connections_count)

    def clients_count(self):
        return len(self.clients)

    def wait_for_connections(self):
        print("waiting for clients")
        while True:
            conn, client_addr = self.server_socket.accept()
            print(f"client {client_addr} has connected")



def main():
    server = Server()
    server.wait_for_connections()


if __name__ == "__main__":
    main()
    