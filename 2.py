import sys
import socket
import argparse

#Handling socket errors gracefully

def main():
    #Modul argparse memudahkan untuk menulis antarmuka baris perintah yang mudah digunakan.
    #Program menentukan argumen apa yang diperlukan, dan argparse akan mencari cara untuk menguraikannya
    #Modul argparse juga secara otomatis menghasilkan pesan bantuan dan penggunaan. 
    #Modul juga akan mengeluarkan kesalahan saat pengguna memberikan argumen yang tidak valid pada program.
    parser = argparse.ArgumentParser(description='Socket Error Examples')

    parser.add_argument('--host', action='store', dest='host', required=False)
    parser.add_argument('--port', action='store', dest='port', type=int, required=False)
    parser.add_argument('--file', action='store', dest='file', required=False)

    given_args = parser.parse_args()
    host = given_args.host
    port = given_args.port
    filename = given_args.file

    #Blok try memungkinkan Anda menguji blok kode untuk kesalahan. 
    #Blok except memungkinkan Anda menangani kesalahan.
    #Python tidak akan memberi tahu Anda tentang kesalahan seperti kesalahan sintaksis (kesalahan tata bahasa), melainkan akan berhenti secara tiba-tiba.

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as e:
        print('Error creating socket: %s' % e)
        sys.exit(1)

    try:
        s.connect((host,port))
    except socket.gaierror as e:
        print('Connection error: %s' % e)
        sys.exit(1)
    
    try:
        msg = 'GET %s HTTP/1.0\r\n\r\n' % filename
        s.sendall(msg.encode('utf-8'))
    except socket.error as e:
        print('Error sending data: %s' % e)
        sys.exit(1)
    
    while 1:
        try:
            buf = s.recv(2048)
        except socket.error as e:
            print('Error receiving data: %s' % e)
            sys.exit(1)

        if not len(buf):
            break
        sys.stdout.write(buf.decode('utf-8'))

if __name__ == '__main__':
    main()