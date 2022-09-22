
#O script tem como função realizar download dos video do youtube no formato MP4 e converter para MP3 também 
#ATENÇÃO PARA FUNCIONAR BASTA EXECUTAR O CODIGO EM UMA IDE DE SUA PREFERENCIA.

from tkinter import mainloop
import youtube_dl
import os
os.system('cls')

 
print("\n Escolha opção desejada!!\n ")
print(" 1-Fazer Download do video MP4")
print(" 2-Fazer Download video convertido para MP3")

opção = input("\n Digite número da operação (1/2/): ")


link = input(' Copie e cole a URL do video: ')


if opção == '1':

    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})


elif opção == '2':

    ydl = youtube_dl.YoutubeDL({
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
})


with ydl:
    result = ydl.extract_info(link, download=True) 


if 'entries' in result:
    video = result['entradas'][0] 

else: 
    video = result


