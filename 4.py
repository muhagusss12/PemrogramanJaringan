#Changing a socket to the blocking/non-blocking mode

import socket
def test_socket_modes():
    #Membuat socket
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    #Setel soket ke pemblokiran (benar) atau non-pemblokiran (salah).   
    #setblocking(True) sama dengan settimeout(None)
    #setblocking(False) setara dengan settimeout(0.0).
    s.setblocking(1)
    s.settimeout(0.5)
    s.bind(("127.0.0.1", 0))
    socket_address = s.getsockname()
    print ("Trivial Server launched onsocket: %s" %str(socket_address))
    while(1):
        s.listen(1)
if __name__ == '__main__':
    test_socket_modes()