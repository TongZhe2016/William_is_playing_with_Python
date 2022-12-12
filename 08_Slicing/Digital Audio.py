import sys
import soundfile

samples = soundfile.read('i_like_big_cars.wav')

samples = samples[0*44100:3*44100]

soundfile.play(samples)
