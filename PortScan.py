#O SCRIPT TEM COMO FUNÇÃO FAZER UMA SCANNER NA REDE CONFORME IP INSERIDO IDENTIFICAR QUAIS PORTAS ESTÃO ABERTAS
import os
import socket
os.system('cls') 


ip = input('Digite o IP: ')
ports = [20,21,22,23,25,26,80,2222,3306,110
,443,445,8443,8080,135,139,3306,3395,23395] # portas

for i in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.2)
    conexao = s.connect_ex((ip,i))
    if conexao == 0:
        
        print('OPEN Port (',i,')')
       
    else:
        exit
    
        
