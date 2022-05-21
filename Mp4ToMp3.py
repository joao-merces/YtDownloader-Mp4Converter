
from pytube import YouTube
from moviepy.editor import *
import os
import glob
import ytDownloader

lista_mp4=glob.glob("*.mp4")

for video in lista_mp4:
    print("Lendo arquivos mp4")

    mp4=VideoFileClip(os.path.join(video))
    nome_mp3=video[:-4]+".mp3"
    print("Convertendo")
    mp4.audio.write_audiofile(os.path.join(nome_mp3))

    print("Convertido mp4 "+video+"para mp3"+nome_mp3)
    