---
language: ru
tags:
- audio-classification
- audio
- emotion
- emotion-recognition
- emotion-classification
- speech
license: mit
datasets:
- Aniemore/resd
model-index:
- name: XLS-R Wav2Vec2 For Russian Speech Emotion Classification by Nikita Davidchuk
  results:
  - task:
      name: Audio Emotion Recognition
      type: audio-emotion-recognition
    dataset:
      name: Russian Emotional Speech Dialogs
      type: Aniemore/resd
      args: ru
    metrics:
    - name: accuracy
      type: accuracy
      value: 72%
---

# Prepare and importing

```python
import torch
import torch.nn as nn
import torch.nn.functional as F
import torchaudio
from transformers import AutoConfig, AutoModel, Wav2Vec2FeatureExtractor

import librosa
import numpy as np


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
        logits = model_(**inputs).logits

    scores = F.softmax(logits, dim=1).detach().cpu().numpy()[0]
    outputs = [{"Emotion": config.id2label[i], "Score": f"{round(score * 100, 3):.1f}%"} for i, score in enumerate(scores)]
    return outputs
```

# Evoking:

```python
TRUST = True

config = AutoConfig.from_pretrained('Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition', trust_remote_code=TRUST)
model_ = AutoModel.from_pretrained("Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition", trust_remote_code=TRUST)
feature_extractor = Wav2Vec2FeatureExtractor.from_pretrained("Aniemore/wav2vec2-xlsr-53-russian-emotion-recognition")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model_.to(device)
```

# Use case

```python
result = predict("/path/to/russian_audio_speech.wav", 16000)
print(result)
```

```python
# outputs
[{'Emotion': 'anger', 'Score': '0.0%'},
 {'Emotion': 'disgust', 'Score': '100.0%'},
 {'Emotion': 'enthusiasm', 'Score': '0.0%'},
 {'Emotion': 'fear', 'Score': '0.0%'},
 {'Emotion': 'happiness', 'Score': '0.0%'},
 {'Emotion': 'neutral', 'Score': '0.0%'},
 {'Emotion': 'sadness', 'Score': '0.0%'}]
```

# Results

|              | precision | recall | f1-score | support |
|--------------|-----------|--------|----------|---------|
| anger        | 0.97      | 0.86   | 0.92     | 44      |
| disgust      | 0.71      | 0.78   | 0.74     | 37      |
| enthusiasm   | 0.51      | 0.80   | 0.62     | 40      |
| fear         | 0.80      | 0.62   | 0.70     | 45      |
| happiness    | 0.66      | 0.70   | 0.68     | 44      |
| neutral      | 0.81      | 0.66   | 0.72     | 38      |
| sadness      | 0.79      | 0.59   | 0.68     | 32      |
| accuracy     |           |        | 0.72     | 280     |
| macro avg    | 0.75      | 0.72   | 0.72     | 280     |
| weighted avg | 0.75      | 0.72   | 0.73     | 280     |

# Citations
```
@misc{Aniemore,
  author = {Артем Аментес, Илья Лубенец, Никита Давидчук},
  title = {Открытая библиотека искусственного интеллекта для анализа и выявления эмоциональных оттенков речи человека},
  year = {2022},
  publisher = {Hugging Face},
  journal = {Hugging Face Hub},
  howpublished = {\url{https://huggingface.com/aniemore/Aniemore}},
  email = {hello@socialcode.ru}
}
```