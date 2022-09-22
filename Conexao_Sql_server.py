#O SRCRIPT TEM COMO OBJETIVO REALIZAR UMA PONTE COM SQL-SERVE TRAZENDO AS TABELAS CONFORME BANCO DE DADOS ESCOLHICO 
#ATENÇÃO PARA FUNCIONAR EXECUTE EM UMA IDE DE SUA PREFERENCIA 

import pyodbc
import os 
os.system('cls')


def retornar_conexao_sql():
    server = "TI-02\SQLEXPRESS"
    database = "JDBCPrimeiraConexao"
    
    string_conexao = 'Driver={SQL Server Native Client 11.0};Server='+server+';Database='+database+';Trusted_Connection=yes;'
    conexao = pyodbc.connect(string_conexao)
    return conexao.cursor()


cursor = retornar_conexao_sql()
cursor.execute("select* from Tbl_Usuario order by 1")
linha = cursor.fetchone()
res = []
while linha:
    for coluna in linha:
        res.append(coluna)
    print(res)
    res = []
    linha = cursor.fetchone()
