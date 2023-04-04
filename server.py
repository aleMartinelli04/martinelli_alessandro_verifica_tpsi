from socket import socket, SOCK_STREAM, AF_INET

import jsonschema

import json
from config import SERVER_HOST, SERVER_PORT


class TCPServer:
    def __init__(self, ip: str, port: int, action: callable = lambda msg: msg):
        self.ip = ip
        self.port = port

        self.action = action

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(self.address)

    @property
    def address(self) -> tuple:
        return self.ip, self.port

    def start(self):
        self.socket.listen(1)
        print(f"Socket listening on {self.address}")

        while True:
            connection, address = self.socket.accept()
            print(f"Accepted connection with {address}")

            while True:
                data = connection.recv(2048)
                print(f"Received data from {address}: {data}")

                if not data:
                    break

                res: str = self.action(data.decode())

                print(f"RES: {res}")

                connection.send(res.encode())

            connection.close()
            print(f"Closed connection with {address}")


if __name__ == '__main__':
    def edit_msg(msg: str) -> str:
        json_file = json.loads(msg)

        print(json_file)

        with open('json/schema.json', 'r') as schema_file:
            schema = json.load(schema_file)

        try:
            jsonschema.validate(json_file, schema)

            utenti = json_file['utenti']

            giovane = None
            vecchio = None

            for utente in utenti:
                if not giovane:
                    giovane = utente

                if not vecchio:
                    vecchio = utente

                if vecchio['eta'] < utente['eta']:
                    vecchio = utente

                if giovane['eta'] > utente['eta']:
                    giovane = utente

            return json.dumps({
                "giovane": giovane,
                "vecchio": vecchio
            }, indent=4)

        except Exception as e:
            return str(e)


    TCPServer(SERVER_HOST, SERVER_PORT, edit_msg).start()
