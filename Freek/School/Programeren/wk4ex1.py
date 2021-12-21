# Programmeren I, Practicum 4
# Bestandsnaam: wk4ex1.py
# Naam: Freek van Witzenburg
# Probleemomschrijving: Geluidsbewerking

import time
import random
import math
from audio import *
# een functie zodat we kunnen beginnen met een opfrisser
# over list comprehensions...
def three_ize(L):
 """three_ize is a function that accepts a list and
 returns a list of elements each three times as large.
 """
 # dit is een voorbeeld van een list comprehension
 lc = [3 * x for x in L]
 return lc
# Te schrijven functie #1: scale
def scale(L, scale_factor):
 lc = [scale_factor * x for x in L]
 return lc
# hier is een voorbeeld van hoe je op een andere
# manier de functie three_ize kan schrijven:
def three_ize_by_index(L):
 """three_ize_by_index has the same behavior as three_ize
 but it uses the INDEX of each element, instead of
 using the elements themselves -- this is much more flexible!
 """
 # nog een voorbeeld van een list comprehension
 n = len(L)
 lc = [3 * L[i] for i in range(n)]
 return lc
# Te schrijven functie #2: add_2
def add_2(L, m):
 n = min(len(L), len(m))
 return [L[i] + m[i] for i in range (n)]
# Te schrijven functie #3: add_3
def add_3(L, m, p):
 n = min(len(L), len(m), len(p))
 return [L[i] + m[i] + p[i] for i in range (n)]
# Te schrijven functie #4: add_scale_2
def add_scale_2(L, m, L_scale, m_scale):
 n = min(len(L), len(m))
 return [L[i] * L_scale + m[i] * m_scale for i in range (n)]
# Hulpfunctie: randomize
def randomize(x, chance_of_replacing):
 """randomize accepts an original value, x
 and a fraction named chance_of_replacing.
 With the "chance_of_replacing" chance, it
 should return a random float from -32767 to 32767.
 Otherwise, it should return x (not replacing it)."""
 r = random.uniform(0, 1)
 if r < chance_of_replacing:
    return random.uniform(-32768, 32767)
 else:
    return x
# Te schrijven functie #5: replace_some
def replace_some(L, chance_of_replacing):
 return [randomize(x, chance_of_replacing) for x in L]
#
# de functies hieronder betreffen geluidsbewerking...
#
# een functie om te zorgen dat alles werkt
def test():
 """A test function that plays swfaith.wav
 You'll need swfaith.wav in this folder.
 """
 play('swfaith.wav')
# De voorbeeldfunctie change_speed
def change_speed(filename, newsr):
 """change_speed allows the user to change an audio file's speed.
 Arguments: filename, the name of the original file
 newsr, the new sampling rate in samples per second
 Result: no return value, but
 this creates the sound file 'out.wav'
 and plays it
 """
 print("Het originele geluid afspelen...")
 play(filename)
 sound_data = [0, 0] # een "lege" lijst
 read_wav(filename, sound_data) # laad gegevens IN sound_data
 samps = sound_data[0] # de samples van de ruwe geluidsgolven
 print("De eerste 10 geluidsdruksamples zijn\n", samps[:10])
 sr = sound_data[1] # de sampling rate, sr
 print("Het aantal samples per seconde is", sr)
 # deze regel is niet echt nodig, maar staat hier voor de consistentie...
 newsamps = samps # dezelfde samples als eerder
 new_sound_data = [newsamps, newsr] # nieuwe geluidsgegevens
 write_wav(new_sound_data, "out.wav") # sla de gegevens op naar out.wav
 print("\nNieuw geluid afspelen...")
 play('out.wav') # speel het nieuwe bestand 'out.wav' af
def flipflop(filename):
 """flipflop swaps the halves of an audio file
 Argument: filename, the name of the original file
 Result: no return value, but
 this creates the sound file 'out.wav'
 and plays it
 """
 print("Het originele geluid afspelen...")
 play(filename)

 print("Geluidsgegevens inlezen...")
 sound_data = [0, 0]
 read_wav(filename, sound_data)
 samps = sound_data[0]
 sr = sound_data[1]
 print("Nieuw geluid berekenen...")
 # dit bepaalt het middelpunt en noemt dat x
 x = len(samps)//2
 newsamps = samps[x:] + samps[:x]
 newsr = sr
 new_sound_data = [newsamps, newsr]
 print("De nieuwe geluidsgegevens opslaan...")
 write_wav(new_sound_data, "out.wav") # schrijf gegevens naar out.wav
 print("Nieuw geluid afspelen...")
 play('out.wav')
# Te schrijven geluidsfunctie #1: reverse
def reverse(filename):
 print("Het originele geluid afspelen...")
 play(filename)
 print("Geluidsgegevens inlezen...")
 sound_data = [0, 0]
 read_wav(filename, sound_data)
 samps = sound_data[0]
 sr = sound_data[1]
 print("Nieuw geluid berekenen...")
 newsamps = samps[::-1]
 newsr = sr
 new_sound_data = [newsamps, newsr]
 print("De nieuwe geluidsgegevens opslaan...")
 write_wav(new_sound_data, "out.wav") # schrijf gegevens naar out.wav
 print("Nieuw geluid afspelen...")
 play('out.wav')
# Te schrijven geluidsfunctie #2: volume
def volume(filename, scale_factor):
 sound_data = [0, 0]
 read_wav(filename, sound_data)
 samps = sound_data[0]
 sr = sound_data[1]
 newsamps = scale(samps, scale_factor)
 newsr = sr
 new_sound_data = [newsamps, newsr]
 write_wav(new_sound_data, "out.wav")
 play('out.wav')
# Te schrijven geluidsfunctie #3: static
def static(filename, probability_of_static):
 sound_data = [0, 0]
 read_wav(filename, sound_data)
 samps = sound_data[0]
 sr = sound_data[1]


 newsamps = replace_some(samps, probability_of_static)
 newsr = sr
 new_sound_data = [newsamps, newsr]
 write_wav(new_sound_data, "out.wav")
 play('out.wav')
# Te schrijven geluidsfunctie #4: overlay
def overlay(filename1, filename2):
 sound_data = [0, 0]
 read_wav(filename1, sound_data)
 samps = sound_data[0]
 sr = sound_data[1]
 sound_data1 = [0, 0]
 read_wav(filename2, sound_data1)
 samps1 = sound_data1[0]
 sr1 = sound_data1[1]
 new_sound_data = add_scale_2(samps, samps1, 0.5, 0.5)
 new_sound_data = [new_sound_data, sr]
 write_wav(new_sound_data, "out.wav")
 play('out.wav')
# Te schrijven geluidsfunctie #5: echo

def echo(filename, time_delay):
 sound_data = [0, 0]
 read_wav(filename, sound_data)
 samps = sound_data[0]
 sr = sound_data[1]
 samps2 = [0] * 42 + samps
 new_sound_data = add_scale_2(samps, samps2, 0.5, 0)
 new_sound_data = [new_sound_data, sr]
 write_wav(new_sound_data, "out.wav")
 play("out.wav")
# Hulpfunctie om pure tonen te genereren
def gen_pure_tone(freq, seconds, sound_data):
 """pure_tone returns the y-values of a cosine wave
 whose frequency is freq Hertz.
 It returns nsamples values, taken once every 1/44100 of a second.
 Thus, the sampling rate is 44100 hertz.
 0.5 second (22050 samples) is probably enough.
 """
 if sound_data != [0, 0]:
    print("De waarde van sound_data moet [0, 0] zijn.")

 return
 sampling_rate = 22050
 # hoeveel samples we moeten genereren
 nsamples = int(seconds*sampling_rate) # naar beneden afgerond
 # de factor f om de frequentie te schalen
 f = 2*math.pi/sampling_rate # omrekenen van samples naar Hz
 # de factor a om de amplitude te schalen
 a = 32767.0
 sound_data[0] = [a * math.sin(f*n*freq) for n in range(nsamples)]
 sound_data[1] = sampling_rate
 return sound_data
def pure_tone(freq, time_in_seconds):

 """Generates and plays a pure tone of the given frequence."""
 print("Toon genereren...")
 sound_data = [0, 0]
 gen_pure_tone(freq, time_in_seconds, sound_data)
 print("De nieuwe geluidsgegevens opslaan...")
 write_wav(new_sound_data, "out.wav") # schrijf gegevens naar out.wav
 print("Nieuw geluid afspelen...")
 play('out.wav')
# Te schrijven geluidsfunctie #6: chord
