# test ssl cert_callback parameter

import socket
import ssl


def cert_callback(cert, depth):
    print(type(cert), len(cert) > 100, depth)
    return 0


def cert_callback_fail(cert, depth):
    print(type(cert), len(cert) > 100, depth)
    return 1


def test(peer_addr):
    s = socket.socket()
    s.connect(peer_addr)
    s = ssl.wrap_socket(s, cert_callback=cert_callback, cert_reqs=ssl.CERT_OPTIONAL)
    s.close()

    s = socket.socket()
    s.connect(peer_addr)
    try:
        s = ssl.wrap_socket(s, cert_callback=cert_callback_fail, cert_reqs=ssl.CERT_OPTIONAL)
    except OSError as e:
        print(err.args[1])
    s.close()


if __name__ == "__main__":
    test(socket.getaddrinfo("micropython.org", 443)[0][-1])
