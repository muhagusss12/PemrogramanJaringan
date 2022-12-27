import socket

#Setting and getting the default socket timeout
#Mengatur dan mendapatkan waktu habis default dari timeout

def socketTimeout():
    #Socket adalah titik komunikasi dari lalu lintas komunikasi antar proses di dalam sebuah jaringan komputer.
    #Socket terdiri atas parameter domain dan protokol
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print('Default socket timeout: {}'.format(s.gettimeout()))
    s.settimeout(100)
    print('Current socket timeout: {}'.format(s.gettimeout()))

if __name__ == '__main__':
    socketTimeout()