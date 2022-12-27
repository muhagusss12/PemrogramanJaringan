import socket

#Setting and getting the default socket timeout
#Mengatur dan mendapatkan waktu habis default dari timeout

def socketTimeout():
    while True:
        print('Menu Aplikasi')
        print('1. Lihat Default Socket Timeout')
        print('2. Set Default Socket Timeout')
        print('3. Hentikan aplikasi')
        pilihan = int(input('Pilihan    : '))

        if pilihan == 1:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            print('Default socket timeout: {}'.format(s.gettimeout()))
            print('----------------------------')
        elif pilihan == 2:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            waktu_habis = int(input('Masukan waktu habis : '))
            s.settimeout(waktu_habis)
            print('Current socket timeout: {}'.format(s.gettimeout()))
            print('----------------------------')
        elif pilihan == 3:
            break
        else:
            print('Inputan tidak tersedia')

if __name__ == '__main__':
    socketTimeout()