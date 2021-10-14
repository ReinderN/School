# Programmeren I, Practicum 4 "Klinkt goed"
# Auteur: Trevor Fung, 2016
# Probleemomschrijving: Geluidsbewerking
#
# Opmerkingen voor als deze module stuk gaat:
#  - De module wordt in wk4ex1.py aangeroepen via play(filename).
#  - De volgende aanroep is naar read_wav(filename), en die maakt op zijn beurt twee aanroepen:
#     - get_data(filename), die de paramters en ruwe frames uit het geluidsbestand leest
#     - Die worden dan doorgegeven aan tr(params, rf), die de lijst met floats oplevert
#       (sound_data) waarop wk4ex1.py zijn list comprehensions uitvoert
#  - De volgende aanroep is naar write_wav(sound_data, desired filename), die deze aanroepen maakt:
#     - tri(params, data), die de lijst floats omzet naar een aantal bytes
#     - write_wav(params, rawframesstring, filename) die de bytes meekrijgt en omzet naar een
#       geluidsbestand

import os
import wave
wave.big_endian = 0


def print_params(params):
    print('Parameters:')
    print('  nchannels:', params[0])
    print('  sampwidth:', params[1])
    print('  framerate:', params[2])
    print('  nframes  :', params[3])
    print('  comptype :', params[4])
    print('  compname :', params[5])


def tr(params, rf):
    """tr transforms raw frames to floating-point samples"""
    samps = [x for x in rf]    # omzetten naar numerieke bytes
    # parameters betere namen geven
    nchannels = params[0]
    sampwidth = params[1]
    nsamples = params[3]
    if sampwidth == 1:

        for i in range(nsamples):
            if samps[i] < 128:
                samps[i] *= 256.0       # omzetten naar 16-bit getallen
            else:
                samps[i] = (samps[i] - 256) * 256.0

    elif sampwidth == 2:
        newsamps = nsamples * nchannels * [0]
        for i in range(nsamples * nchannels):
            # De module wav geeft ons de gegevens in z'n eigen
            # "endinan-ness". Het indexeren met wave.big_endian zorgt dat
            # we de bytes in de goede volgorde "uitpakken".
            sampval = samps[2*i + 1 - wave.big_endian] * 256 + samps[2*i + wave.big_endian]
            if sampval >= 32768:
                sampval -= 65536
            newsamps[i] = float(sampval)
        samps = newsamps
    else:
        print('Het sampleformaat', params[1], 'wordt niet ondersteund.')
        print('We geven stilte terug.')
        samps = nsamples * [0.0]

    if nchannels == 2:
        # Mixen naar mono
        newsamps = nsamples * [0]
        for i in range(nsamples):
            newsamps[i] = (samps[2 * i] + samps[2 * i + 1]) / 2.0
        samps = newsamps
    return samps


def tri(params, samps):
    """tri is tr inverse, i.e. from samples to rawframes"""
    if params[1] == 1:                 # één byte per sample
        samps = [int(x+127.5) for x in samps]
        rf = [chr(x) for x in samps]
    elif params[1] == 2:               # twee bytes per sample
        bytesamps = (2*params[3])*[0]  # met nullen beginnen
        for i in range(params[3]):
            # misschien een andere afrondstrategie in de toekomst?
            intval = int(samps[i])
            if intval > 32767:
                intval = 32767
            if intval < -32767:
                intval = -32767  # zou -32768 kunnen zijn
            if intval < 0:
                intval += 65536  # Negatieve getallen verwerken
            # De module wav wil de gegevens in z'n eigen "endian-ness" hebben.
            # Het indexeren met wave.big_endian zorgt dat we de bytes in de
            # goede volgorde "inpakken".
            bytesamps[2*i + 1 - wave.big_endian] = intval // 256
            bytesamps[2*i + wave.big_endian] = intval % 256
        samps = bytesamps
        rf = [chr(x).encode("latin-1") for x in samps]
    return b''.join(rf)


def get_data(filename):
    """The file needs to be in .wav format.
       There are lots of conversion programs online, however,
       that can create .wav from .mp3 and other formats.
    """
    # dit geeft een foutmelding als het bestand niet bestaat!
    fin = wave.open(filename, 'rb')
    params = fin.getparams()
    raw_frames = fin.readframes(params[3])
    # we hoeven maar één geluidskanaal in het goede formaat te lezen...
    fin.close()
    return params, raw_frames


def readwav(filename):
    """readwav returns the audio data from the file
       named filename, which must be a .wav file.

       Call this function as follows:

       samps, sr = readwav(filename)

       samps will be a list of the raw sound samples (floats)
       sr will be the sampling rate for that list (integer)
    """
    sound_data = [0, 0]
    read_wav(filename, sound_data)
    samps = sound_data[0]
    sr = sound_data[1]
    if not isinstance(samps, list):
        samps = [42]  # defaultwaarde
    return samps, sr


def read_wav(filename, sound_data):
    """read_wav returns the audio data from the file
       named filename (the first input) in the list
       named sound_data (the second input)

       If the file exists and is the correct .wav format,
       then after this call sound_data will be a list of two
       elements:

       sound_data[0] will be a list of the raw sound samples
       sound_data[1] will be the sampling rate for that list

       That is, sound_data will be the following:

           [[d0, d1, d2, ...], samplingrate]

       where each d0, d1, d2, ... is a floating-point value
       and sampling rate is an integer, representing the
       frequency with which audio samples were taken.

       No value is returned from this function!
    """
    if not isinstance(sound_data, list):
        print("""
            read_wav was called with a second input,
            sound_data, that was _not_ of type list.

            That input needs to be a list, e.g., []
            """)
        return  # niets
    # sound_data is een lijst: we zorgen dat de eerste twee elementen bestaan
    if len(sound_data) < 1:
        sound_data.append(0)
    if len(sound_data) < 2:
        sound_data.append(0)
    # er zijn nu ten minste twee elementen, die geven we nu een standaard waarde
    sound_data[0] = 42
    sound_data[1] = 42
    try:
        params, rf = get_data(filename)
        samps = tr(params, rf)
    except:
        print("Er is een probleem met het bestand", filename)
        print("Je kan kijken of het wel bestaat en of")
        print("het het juiste formaat (.wav) heeft... ")
        return  # niets

    numchannels = params[0]
    datawidth = params[1]
    framerate = params[2]
    numsamples = params[3]
    print()
    print('Je hebt', filename, 'geopend en het heeft')
    print('   ', numsamples, 'geluidssamples, genomen op')
    print('   ', framerate, 'hertz (samples per seconde).')
    print()
    sound_data[0] = samps
    sound_data[1] = framerate
    return  # niets


def write_data(params=None, raw_frames=None, filename="out.wav"):
    """Write data out to .wav format"""

    fout = wave.open(filename, 'wb')
    if params:
        fout.setparams(params)
        if raw_frames:
            fout.writeframes(raw_frames)
        else:
            print('geen frames')
    else:
        print('geen params')
    fout.close()


def write_wav(sound_data, filename="out.wav"):
    """write_wav creates a .wav file whose contents are sound_data.
       sound_data is [audio data, srate] as a list.

       The second parameter is the output file name.
       If no name is specified, this parameter defaults to 'out.wav'.
    """
    # zorg eerst dat de sampling rate een int is...
    sound_data[1] = int(sound_data[1])

    # nog wat andere controles
    if not isinstance(sound_data, list) or \
       len(sound_data) < 2 or \
       not isinstance(sound_data[0], list) or \
       not isinstance(sound_data[1], int):
        print("""
            write_wav is aangeroepen met een de eerste parameter,
            sound_data, die _niet_ een geschikte lijst is.

            Die parameter moet een lijst zijn waarbij
            sound_data[0] de ruwe geluidssamples zijn en
            sound_data[1] de sampling rate is, e.g.,

                [[d0, d1, d2, ...], sampling_rate]

            waarbij de getallen d0, d1, d2, ... floating-pointgetallen zijn
            en de sampling rate een integer is, die de frequentie voorstelt
            waarmee de geluidssamples genomen zijn.
            """)
        return  # niets
    # benoem de twee elementen sound_data
    data = sound_data[0]
    samplingrate = sound_data[1]
    # stel het bestand samen...
    framerate = int(samplingrate)
    if framerate < 0:
        framerate = -framerate
    if framerate < 1:
        framerate = 1
    # altijd 1 kanaal en 2 uitvoerbytes per sample
    params = [1, 2, framerate, len(data), "NONE", "No compression"]
    # omzetten naar ruwe frames
    rawframesstring = tri(params, data)
    write_data(params, rawframesstring, filename)
    print()
    print('Je hebt het bestand', filename, 'opgeslagen met')
    print('   ', len(data), 'geluidssamples, genomen op')
    print('   ', samplingrate, 'hertz.')
    print()
    return  # niets


def play(filename):
    """Play a .wav file for Windows, Linux, or Mac.
    """
    if not isinstance(filename, str):
        raise TypeError('filename moet een string zijn')
    if os.name == 'nt':
        import winsound
        winsound.PlaySound(filename, winsound.SND_FILENAME)
    elif os.uname()[0] == 'Linux':
        os.system('/usr/bin/play ' + filename + ' || /usr/bin/aplay ' + filename)
    # ga ervanuit dat als het geen Windows of Linux is dat het een Mac is
    # als je een ander OS gebruikt moet je dit aanpassen...
    else:
        os.system(('/usr/bin/afplay ' + filename))
