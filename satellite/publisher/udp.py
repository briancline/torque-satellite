from base import Publisher
import msgpack
import socket


class UDPPublisher(Publisher):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def publish(self, request):
        x = self.socket.sendto(msgpack.dumps(request), (self.host, self.port))
        print x
        return True

    def read(self, buffer):
        try:
            request = msgpack.loads(buffer)
        except:
            return False

        return request
