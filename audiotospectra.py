import os
import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile,join

path="/audio"
dest = "/audiospectra"

for audio in [f for f in listdir(path) if isfile(join(path,f))]:
    x, sr = librosa.load(os.path.join(path, audio))
    plt.figure(figsize=(1.28, .64), dpi=100)
    plt.axis('off')
    plt.axes([0., 0., 1., 1., ], frameon=False, xticks=[], yticks=[])
    S = librosa.feature.melspectrogram(y=x, sr=sr)
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max))
    plt.savefig(os.path.join(dest, os.path.splitext(audio)[0]+'.png'), bbox_inches=None, pad_inches=0)
    plt.close()