from ftplib import FTP
import os

def uploadFile(paths):
    ftp=FTP('')
    print('starting')
    ftp.connect('192.168.43.124',2121)
    print('connecting')
    ftp.login('nicat','access2ftp')
    print('loged in')
    ftp.cwd('')
    ftp.retrlines('LIST')
    path_s = os.path.split(os.path.abspath(paths))
    ftp.storbinary('STOR '+ path_s[1],open(paths,'rb'))
    ftp.quit()
