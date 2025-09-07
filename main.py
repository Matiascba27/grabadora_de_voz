import sounddevice
from scipy.io.wavfile import write
fs=44100 #sample_rate
second=int(input("Ingrese la duracion en segunddos: ")) # Ingresar duracion en segundos
print("Grabando...\n")
record_voice=sounddevice.rec(int(second * fs), samplerate=fs, channels=2)
sounddevice.wait() # Esperar hasta que se complete la grabacion
write("out.wav", fs, record_voice) # Guardar como archivo wav
print("Grabacion Finalizada...\nPorfavor Revisar el archivo out.wav")