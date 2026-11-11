import socket

class Client:
    def __init__(self):
        # temporary
        self.SERVER_IP = socket.gethostbyname(socket.gethostname()) 
        self.SERVER_PORT = 5050
        self.soc = socket.socket()
        self.init_connection()



    def init_connection(self):
        self.soc.connect((self.SERVER_IP, self.SERVER_PORT))
        print("succesfully connected")

def main():
    client = Client()
    while True:
        pass

if __name__ == "__main__":
    main()