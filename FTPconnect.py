from ftplib import FTP

ftp_host = "host"
ftp_username = "username"
ftp_password = "password"

def connect_ftp(host, username, password):
       ftp = FTP(host)
       ftp.login(username, password)
       print(f'Успешное подключение к ftp серверу!')

       set_passive_mode(ftp)

       return ftp
def set_passive_mode(ftp):
       ftp.set_pasv(True)

def execute_ftp_command(ftp, command):
       result = ""

       if command.upper() == "QUIT":
              ftp.quit()
              print('Соединение с ftp сервером было разорвано.')
              exit()
       elif command.upper() == "LIST":
              result = ftp.retrlines("LIST")
              print(f'Result of executing "LIST" command: \n{result}')
       else:
              result = ftp.sendcmd(command)
              print(f'Result of executing "{command}": {result}')

              return result
       
ftp_connection = connect_ftp(ftp_host, ftp_username, ftp_password)

while True:
       user_input = input('Введите команду для сервера FTP (QUIT чтобы выйти): ')
       execute_ftp_command(ftp_connection, user_input)