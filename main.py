from socketserver import UDPServer, BaseRequestHandler


class EchoUdpRequestHandler(BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]

        print(f"{self.client_address[0]}:{self.client_address[1]} wrote: {data}")  # For demo purpose

        socket.sendto(data, self.client_address)


if __name__ == "__main__":
    HOST, PORT = "127.0.0.1", 7070  # Could be defined from args but hey, demo.

    with UDPServer((HOST, PORT), EchoUdpRequestHandler) as server:
        print(f"Server started at {HOST}:{PORT}")
        server.serve_forever()
