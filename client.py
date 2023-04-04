from socket import SOCK_STREAM, AF_INET, socket

import json
from config import SERVER_PORT, SERVER_HOST


class TCPClient:
    def __init__(self, ip: str, port: int):
        self.ip = ip
        self.port = port

        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(self.address)

    @property
    def address(self):
        return self.ip, self.port

    def send(self, msg: str) -> str:
        self.socket.send(msg.encode())

        data = self.socket.recv(2048)

        return data.decode()


if __name__ == '__main__':
    client = TCPClient(SERVER_HOST, SERVER_PORT)

    with open('json/utenti.json', 'r') as file:
        json_data = json.load(file)

    res = client.send(json.dumps(json_data))

    if res[0] == '{':
        with open('json/result.json', 'w') as file:
            file.write(res)

    print(res)
