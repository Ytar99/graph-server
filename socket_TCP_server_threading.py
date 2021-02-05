import socketserver

class ThreadingTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

class EchoTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        data = self.request.recv(1024).strip()
        print('From [{0}]: {1}'.format(self.client_address[0], data.decode()))
        self.request.sendall(data)

if __name__ == '__main__':
    with ThreadingTCPServer(('',8888), EchoTCPHandler) as server:
        server.serve_forever()
