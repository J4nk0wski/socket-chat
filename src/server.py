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
        print(f"waiting for clients on {self.IP}:{self.PORT}")
        try:
            while True:
                conn, client_addr = self.server_socket.accept()
                self.clients.append((conn, client_addr))
                print(f"client {client_addr} has connected")
                print(f"total number of client: {self.clients_count()}")
        except KeyboardInterrupt:
            print("\nShutting down the server...")
        finally:
            self.shutdown()
    def shutdown(self):
        for conn,_ in self.clients:
            conn.close()
        self.clients.clear()
        self.server_socket.close()


        


def main():
    server = Server()
    server.wait_for_connections()


if __name__ == "__main__":
    main()
    