import os
import sys
import random
import time

#windows(10,8,7)


banner1 = (''' 	
    
    
 /$$      /$$ /$$  /$$$$$$  /$$       /$$   /$$                     /$$      
| $$  /$ | $$|__/ /$$__  $$|__/      | $$  | $$                    | $$      
| $$ /$$$| $$ /$$| $$  \__/ /$$      | $$  | $$  /$$$$$$   /$$$$$$$| $$   /$$
| $$/$$ $$ $$| $$| $$$$    | $$      | $$$$$$$$ |____  $$ /$$_____/| $$  /$$/
| $$$$_  $$$$| $$| $$_/    | $$      | $$__  $$  /$$$$$$$| $$      | $$$$$$/ 
| $$$/ \  $$$| $$| $$      | $$      | $$  | $$ /$$__  $$| $$      | $$_  $$ 
| $$/   \  $$| $$| $$      | $$      | $$  | $$|  $$$$$$$|  $$$$$$$| $$ \  $$
|__/     \__/|__/|__/      |__/      |__/  |__/ \_______/ \_______/|__/  \__/
                                                                             
    .:| Author : Security77 Github:Security77 Twiter: @iAmHere96509046  |:.                                      
                                                                             

    
    
    ''')
banner2 = ('''

 @@@  @@@  @@@ @@@ @@@@@@@@ @@@      @@@  @@@  @@@@@@   @@@@@@@ @@@  @@@
 @@!  @@!  @@! @@! @@!      @@!      @@!  @@@ @@!  @@@ !@@      @@!  !@@
 @!!  !!@  @!@ !!@ @!!!:!   !!@      @!@!@!@! @!@!@!@! !@!      @!@@!@! 
  !:  !!:  !!  !!: !!:      !!:      !!:  !!! !!:  !!! :!!      !!: :!! 
   ::.:  :::   :    :       :         :   : :  :   : :  :: :: :  :   :::

    .:| Author : Security77 Github:Security77 Twiter: @iAmHere96509046  |:.                                                                    

        ''')
    

choi = (banner1, banner2)
print (random.choice(choi))
time.sleep(0.6)
def perangkat():
    print'''
    +===============+
    |___Perangkat___|
    |     Kali      |
    |    Windows    |
    +===============+'''
        
    terminal = raw_input('->')

    if terminal == 'Kali':
        kali()

    elif terminal == 'Windows':
       helpCmd()
       mainCmd()

    elif terminal == 'cmd':
        helpCmd()
        mainCmd()

    elif terminal == exit:
        os.system('exit')
    
    elif terminal == 'kali':
        kali()

    elif terminal == 'windows':
        helpCmd()
        mainCmd()

def module():
    main = raw_input('Wifi->')

    if main == 'wifi':
        kali-wifi()

    elif main == 'ip':
        os.system('ifconfig')

    elif main == 'nmap':
        nmap-kali()

    elif main == 'arp':
        arp-kali()
    
    elif main == 'netdiscover':
        net-kali()

    


def mainCmd():
    cek = raw_input('Wifi->')

    if cek == 'wifi':
        wifi()
    
    elif cek == 'Ip':
        ifconfig()

    elif cek == 'arp':
        arp()
    elif cek == 'exit':
        exit()

    elif cek == 'help':
        helpCmd()

    else:
        print '[?]Perintah Tidak Ditemukan.!'
        print '[!]Mohon perhatikan besar kecilnya huruf'
        mainCmd()
def exit():
    print '[+]Terimakasih Telah Menggunakan <(-_-)> '
    time.sleep(1.20)
    os.system('exit')

def arp():
    print 'Coming Soon'
    os.system('exit')

def ifconfig():
    os.system('ipconfig')
    mainCmd()

def wifi():
    os.system('netsh wlan show profiles')
    ssid = raw_input('Nama Wifi :')
    os.system('netsh wlan show profiles '     + ssid + ' key=clear')
    mainCmd()
    

def helpCmd():
    print '''
    +------------------------+
    |________Perintah________|
    |          Ip            |
    |         wifi           |
    |          arp           |
    |         exit           |
    +------------------------+

    '''
    mainCmd()

def kali():
    print ''' 
    +========================+
    |_______Perintah_________|
    |         ip             |
    |        wifi            |
    |      netdiscover       |
    |         arp            |
    |        nmap            |
    |       snifing          |
    +------------------------+
    '''
    module()

perangkat()

