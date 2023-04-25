---
tags:
- tensorflowtts
- audio
- text-to-speech
- text-to-mel
language: vi
license: apache-2.0
datasets:
- infore
---
# Install TensorFlowTTS
```
pip install TensorFlowTTS
```
## Converting your Text to Mel Spectrogram
```python
import numpy as np
import soundfile as sf
import yaml
import IPython.display as ipd

import tensorflow as tf

from tensorflow_tts.inference import AutoProcessor
from tensorflow_tts.inference import TFAutoModel

processor = AutoProcessor.from_pretrained("MarcNg/fastspeech2-vi-infore")
fastspeech2 = TFAutoModel.from_pretrained("MarcNg/fastspeech2-vi-infore")

text = "xin chào đây là một ví dụ về chuyển đổi văn bản thành giọng nói"

input_ids = processor.text_to_sequence(text)

mel_before, mel_after, duration_outputs, _, _ = fastspeech2.inference(
    input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
    speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
    speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
    f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
    energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
)
```

## Bonus: Convert Mel Spectrogram to Speech
```python
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")

audio_before = mb_melgan.inference(mel_before)[0, :, 0]
audio_after = mb_melgan.inference(mel_after)[0, :, 0]

sf.write("audio_before.wav", audio_before, 22050, "PCM_16")
sf.write("audio_after.wav", audio_after, 22050, "PCM_16")

ipd.Audio('audio_after.wav')
```
#### Referencing FastSpeech2
```
@misc{ren2021fastspeech,
      title={FastSpeech 2: Fast and High-Quality End-to-End Text to Speech}, 
      author={Yi Ren and Chenxu Hu and Xu Tan and Tao Qin and Sheng Zhao and Zhou Zhao and Tie-Yan Liu},
      year={2021},
      eprint={2006.04558},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
}
```