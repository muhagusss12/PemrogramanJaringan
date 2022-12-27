#Modifying a socket's send/receive buffer size

import socket

SEND_BUF_SIZE = 4096
RECV_BUF_SIZE = 4096

def modify_buff_size():
    #Membuat socket
    sock = socket.socket( socket.AF_INET, socket.SOCK_STREAM )
    
    #Memberikan ukuran buffer dengan getsockopt() yang terdiri atas 3 parameter
    #1. socket.SOL_TCP gunakan konstanta ini sebagai argumen level ke getsockopt
    #2. socket.SO_SNDBUF gunakan ini untuk mengatur ukuran buffer yang akan dikirimkan
    #3. ukuran atau size dari buffer
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    print ("Buffer size [Before]:%d" %bufsize)

    #setockopt() menyediakan sarana untuk mengontrol perilaku soket.
    #setockopt() untuk mengalokasikan ruang penyangga, mengontrol waktu tunggu habis, atau mengizinkan siaran data soket.
    sock.setsockopt(socket.SOL_TCP,socket.TCP_NODELAY, 1)

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, SEND_BUF_SIZE)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, RECV_BUF_SIZE)
    
    bufsize = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
    
    print ("Buffer size [After]:%d" %bufsize)

if __name__ == '__main__':
    modify_buff_size()