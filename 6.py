#Printing the current time from the internet time server

import ntplib
from time import ctime

#Network Time Protocol (NTP) adalah sebuah protokol yang digunakan untuk pengsinkronan waktu[1] di dalam sebuah jaringan
#NTP sendiri berada di 2 sisi yaitu sisi klien dan sisi server, 
#Kegunaan layanan di ntp adalah untuk mempaskan atau menyesuaikan waktu yang ada sesuai regional di mana mesin komputer itu berada.

def print_time():

    #Membuat client NTP
    ntp_client = ntplib.NTPClient()

    #Meminta akses ke server ntp
    #pool.ntp.org adalah kumpulan server waktu virtual besar yang menyediakan layanan NTP andal yang mudah digunakan untuk jutaan klien.
    response = ntp_client.request('pool.ntp.org')
    print (ctime(response.tx_time))
if __name__ == '__main__':
    print_time()