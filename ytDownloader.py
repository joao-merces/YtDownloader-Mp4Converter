import Mp4ToMp3
from pytube import YouTube
from moviepy.editor import *

baixarMais='s'

while(baixarMais=='s'):
    link=input("Insira o link do video: ")
    yt=YouTube(link)    
    print("Baixando", yt.title)
    yt = yt.streams. get_highest_resolution()
    yt.download()

    baixarMais=str(input("Deseja baixar mais? "))

    if baixarMais!='s':
        if baixarMais!='n':
            print("Opção invalida.")
            
    elif baixarMais=='n':
        print("Saindo...")
