---
language: el
datasets:
- aesdd
tags:
- audio
- audio-classification
- speech
license: apache-2.0
---


~~~
# requirement packages
!pip install git+https://github.com/huggingface/datasets.git
!pip install git+https://github.com/huggingface/transformers.git
!pip install torchaudio
!pip install librosa
!git clone https://github.com/m3hrdadfi/soxan
cd soxan
~~~


# prediction
~~~
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchaudio
from transformers import AutoConfig, Wav2Vec2FeatureExtractor

import librosa
import IPython.display as ipd
import numpy as np
import pandas as pd
~~~

~~~
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_name_or_path = "Bagus/wav2vec2-xlsr-greek-speech-emotion-recognition"
config = AutoConfig.from_pretrained(model_name_or_path)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained(model_name_or_path)
sampling_rate = feature_extractor.sampling_rate
model = Wav2Vec2ForSpeechClassification.from_pretrained(model_name_or_path).to(device)
~~~

~~~
def speech_file_to_array_fn(path, sampling_rate):
    speech_array, _sampling_rate = torchaudio.load(path)
    resampler = torchaudio.transforms.Resample(_sampling_rate)
    speech = resampler(speech_array).squeeze().numpy()
    return speech


def predict(path, sampling_rate):
    speech = speech_file_to_array_fn(path, sampling_rate)
    inputs = feature_extractor(speech, sampling_rate=sampling_rate, return_tensors="pt", padding=True)
    inputs = {key: inputs[key].to(device) for key in inputs}

    with torch.no_grad():
        logits = model(**inputs).logits

    scores = F.softmax(logits, dim=1).detach().cpu().numpy()[0]
    outputs = [{"Emotion": config.id2label[i], "Score": f"{round(score * 100, 3):.1f}%"} for i, score in enumerate(scores)]
    return outputs
~~~

# prediction
~~~
# path for a sample
path = '/data/jtes_v1.1/wav/f01/ang/f01_ang_01.wav'   
outputs = predict(path, sampling_rate)
~~~

~~~
[{'Emotion': 'anger', 'Score': '98.3%'},
 {'Emotion': 'disgust', 'Score': '0.0%'},
 {'Emotion': 'fear', 'Score': '0.4%'},
 {'Emotion': 'happiness', 'Score': '0.7%'},
 {'Emotion': 'sadness', 'Score': '0.5%'}]
 ~~~