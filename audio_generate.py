import os
from gtts import gTTS
import random

test_output_folder = './audio_test_data'
validation_output_folder = './validation_test_data'

test_data_count = 10000
validation_data_count = 100

length = 8

symbols_file = './symbols.txt'

def generate_audios(symbols, output_folder, count):
    i = 0
    while True:
        text = ''.join(random.choices(symbols, k=length))
        filename = text + '.mp3'
        filepath = os.path.join(output_folder, filename)

        print(f'${output_folder}: ${i}')

        if os.path.exists(filepath):
            continue

        tts = gTTS(text)
        tts.save(filepath)

        i += 1
        if i >= count:
            break

if not os.path.exists(test_output_folder):
    os.mkdir(test_output_folder)

if not os.path.exists(validation_output_folder):
    os.mkdir(validation_output_folder)

symbols = None

with open(symbols_file) as file:
    symbols = [c for c in file.read().strip()]

generate_audios(symbols, test_output_folder, test_data_count)
generate_audios(symbols, validation_output_folder, validation_data_count)
