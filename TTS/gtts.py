#https://pypi.python.org/pypi/gTTS
#instalar tambien pydub pip install pydub

import os
from gtts import gTTS
from pydub import AudioSegment

tts = gTTS(text='Hola esto es una prueba', lang= 'es')
tts.save("prueba.mp3")

#convertimos a wav
song = AudioSegment.from_mp3("prueba.mp3")
song.export("final.wav", format="wav")

#reproducimos el audio
os.system("aplay final.wav")

