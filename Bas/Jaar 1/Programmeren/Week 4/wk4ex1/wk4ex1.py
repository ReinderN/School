# Programmeren I, Practicum 4
# Bestandsnaam: wk4ex1.py
# Naam: Bas Mellens
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
    """scale returns the list (L) with a scaled factor of scale_factor
    L: the list you want to have scaled
    scale_factor: the amount you want it to be scaled by
    """
    lc = [scale_factor*x for x in L]
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
    """add_2 returns the item that is indexed at the same position on both lists added together"""
    n = min(len(L), len(m))
    lc = [L[i] + m[i] for i in range(n)]
    return lc

# Te schrijven functie #3: add_3
def add_3(L, m, p):
    """add_3 returns the item that is indexed at the same position on all lists added together"""    
    n = min(len(L), len(m), len(p))
    lc = [L[i] + m[i] + p[i] for i in range(n)]
    return lc

# Te schrijven functie #4: add_scale_2
def add_scale_2(L, m, L_scale, m_scale):
    """add_scale_2 returns values from a list multiplied by their scale and than added together with an item at the same position as another list"""
    n = min(len(L), len(m))
    lc = [L[i] * L_scale + m[i] * m_scale for i in range(n)]
    return lc

def add_scale_3(L, m, p, L_scale, m_scale, p_scale):
    """add_scale_3 returns values from a list multiplied by their scale and than added together with an item at the same position as other lists"""
    n = min(len(L), len(m), len(p))
    lc = [L[i] * L_scale + m[i] * m_scale + p[i] * p_scale for i in range(n)]
    return lc

# Hulpfunctie: randomize

def randomize(x, chance_of_replacing):
    """randomize accepts an original value, x
       and a fraction named chance_of_replacing.

       With the "chance_of_replacing" chance, it
       should return a random float from -32767 to 32767.

       Otherwise, it should return x (not replacing it).
    """
    r = random.uniform(0, 1)
    if r < chance_of_replacing:
        return random.uniform(-32768, 32767)
    return x


# Te schrijven functie #5: replace_some
def replace_some(L, chance_of_replacing):
    """replace_some returns a list with some random values of L changed based on the chance_of_replacing (0-1)"""
    lc = [randomize(L[i], chance_of_replacing) for i in range(len(L))]
    return lc

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

    sound_data = [0, 0]             # een "lege" lijst
    read_wav(filename, sound_data)  # laad gegevens IN sound_data

    samps = sound_data[0]           # de samples van de ruwe geluidsgolven

    print("De eerste 10 geluidsdruksamples zijn\n", samps[:10])
    sr = sound_data[1]              # de sampling rate, sr

    print("Het aantal samples per seconde is", sr)

    # deze regel is niet echt nodig, maar staat hier voor de consistentie...
    newsamps = samps                      # dezelfde samples als eerder
    new_sound_data = [newsamps, newsr]    # nieuwe geluidsgegevens
    write_wav(new_sound_data, "out.wav")  # sla de gegevens op naar out.wav
    print("\nNieuw geluid afspelen...")
    play('out.wav')   # speel het nieuwe bestand 'out.wav' af


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
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #1: reverse
def reverse(filename):
    """This reverses the audiofile
    filename: the file you want to reverse
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
    newsamps = samps[::-1]
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')

# Te schrijven geluidsfunctie #2: volume
def volume(filename, scale_factor):
    """volume changes the volume of a file by a scale of scale_factor
    filename: the file that needs it volume to be higher
    scale_factor: the factor at wich the volume needs to be upped or lowered
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
    newsamps = scale(samps, scale_factor)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')

# Te schrijven geluidsfunctie #3: static
def static(filename, probability_of_static):
    """static adds static noise on filename with a probability of becoming more static using probabliity_of_static
    filename: the file that needs to have static noise added to it
    probability_of_static: the amount of static you want to add to the file
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
    newsamps = replace_some(samps, probability_of_static)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')    

# Te schrijven geluidsfunctie #4: overlay
def overlay(filename1, filename2):
    """overlay combines 2 files toghether to have them be played at the same time
    filename1: one of the files to play
    filename2: the other file to be played
    """
    print("Het originele geluid afspelen...")
    play(filename1)
    play(filename2)

    print("Geluidsgegevens inlezen...")
    sound_data1 = [0, 0]
    read_wav(filename1, sound_data1)
    samps1 = sound_data1[0]
    sound_data2 = [0, 0]
    read_wav(filename2, sound_data2)
    samps2 = sound_data2[0]
    sr = sound_data2[1]

    print("Nieuw geluid berekenen...")
    # dit bepaalt het middelpunt en noemt dat x
    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')       

# Te schrijven geluidsfunctie #5: echo
def echo(filename, time_delay):
    """echo gives a reverb to a file using a delay
    filename: the file to add reverb to
    time_delay: the amount of delay before the reverb starts
    """
    print("Het originele geluid afspelen...")
    play(filename)

    print("Geluidsgegevens inlezen...")
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps1 = sound_data[0]
    sr = sound_data[1]
    samps2 = [0] * int(sr * time_delay) + samps1

    print("Nieuw geluid berekenen...")
    # dit bepaalt het middelpunt en noemt dat x
    newsamps = add_scale_2(samps1, samps2, 0.5, 0.5)
    newsr = sr
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')      

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
    nsamples = int(seconds*sampling_rate)  # naar beneden afgerond
    # de factor f om de frequentie te schalen
    f = 2*math.pi/sampling_rate   # omrekenen van samples naar Hz
    # de factor a om de amplitude te schalen
    a = 32767.0
    sound_data[0] = [a * math.sin(f*n*freq) for n in range(nsamples)]
    sound_data[1] = sampling_rate
    return sound_data


def pure_tone(freq, time_in_seconds):
    """Generates and plays a pure tone of the given frequence."""
    print("Toon genereren...")
    sound_data = [0, 0]
    new_sound_data = gen_pure_tone(freq, time_in_seconds, sound_data)

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play('out.wav')


# Te schrijven geluidsfunctie #6: chord
def chord(f1, f2, f3, time_in_seconds):
    """chord plays different tones after one another for a certain amount of time
    f1: the first tone to play
    f2: the second tone to play
    f3: the third tone to play
    time_in_seconds: the amount of time that the sound plays
    """
    samps1, sr1 = gen_pure_tone(f1, time_in_seconds, [0, 0])
    samps2, sr2 = gen_pure_tone(f2, time_in_seconds, [0, 0])
    samps3, sr3 = gen_pure_tone(f3, time_in_seconds, [0, 0])

    samps1 = samps1 + [0] * int(sr1*2)
    samps2 = [0] * int(sr1) + samps2 + [0] * int(sr1)
    samps3 = [0] * int(sr1*2) + samps3

    newsamps = add_scale_3(samps1,samps2,samps3, .1,.1,.1)
    newsr = (sr1+sr2+sr3)/3
    new_sound_data = [newsamps, newsr]

    print("De nieuwe geluidsgegevens opslaan...")
    write_wav(new_sound_data, "out.wav")  # schrijf gegevens naar out.wav

    print("Nieuw geluid afspelen...")
    play("out.wav")