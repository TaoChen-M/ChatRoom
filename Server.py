# coding: utf-8

import socket
import select

from util import Queue
from AESEncrypt import encryptMsg,decrptMsg


class Server:
    def __init__(self, host, port):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_socket.bind((host, port))
        self.server_socket.listen(5)
        self.server_socket.setblocking(False)

        self.epoll = select.epoll()
        self.epoll.register(self.server_socket.fileno(), select.EPOLLIN)

        self.connections = {self.server_socket.fileno(): self.server_socket}
        self.addresses = {}
        self.message_queues = {}

    def start(self):
        while True:
            events = self.epoll.poll(timeout=10)
            if not events:
                continue
            print("Start processing", len(events), "event(s)...")

            for fd, event in events:
                socket = self.connections[fd]
                if socket == self.server_socket:
                    # New connection
                    connection, address = self.server_socket.accept()
                    print("Connected from", address)
                    connection.setblocking(False)
                    conn_fd = connection.fileno()
                    self.epoll.register(conn_fd, select.EPOLLIN)

                    self.connections[conn_fd] = connection
                    self.addresses[conn_fd] = address
                    self.message_queues[conn_fd] = Queue()

                elif event & select.EPOLLIN:
                    # Read
                    data = self.connections[fd].recv(1024)
                    if not data:
                        self.remove(fd)
                    else:
                        message = ("%s<%s> say: " % (self.addresses[fd][0], str(self.addresses[fd][1]))).encode() + \
                                  data.strip()

                        for key in self.connections:
                            if key not in [fd, self.server_socket.fileno()]:
                                self.message_queues[key].put(message)
                                self.epoll.modify(key, select.EPOLLOUT)

                elif event & select.EPOLLOUT:
                    # Write
                    while not self.message_queues[fd].is_empty():
                        self.connections[fd].send(self.message_queues[fd].get())
                    self.epoll.modify(fd, select.EPOLLIN)

                elif event & select.EPOLLHUP:
                    self.remove(fd)

    def remove(self, fd):
        print('Client close')
        self.epoll.unregister(fd)
        self.connections[fd].close()
        del self.connections[fd]
        del self.addresses[fd]
        del self.message_queues[fd]

    def __del__(self):
        self.epoll.unregister(self.server_socket.fileno())
        self.epoll.close()
        self.server_socket.close()


if __name__ == '__main__':
    Server(host='0.0.0.0', port=34321).start()
