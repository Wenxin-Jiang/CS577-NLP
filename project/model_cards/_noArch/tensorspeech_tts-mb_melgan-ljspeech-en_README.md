---
tags:
- tensorflowtts
- audio
- text-to-speech
- mel-to-wav
language: en
license: apache-2.0
datasets:
- ljspeech
widget:
- text: "Hello, how are you doing?"
---

# Multi-band MelGAN trained on LJSpeech (En)
This repository provides a pretrained [Multi-band MelGAN](https://arxiv.org/abs/2005.05106) trained on LJSpeech dataset (Eng). For a detail of the model, we encourage you to read more about
[TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS). 


## Install TensorFlowTTS
First of all, please install TensorFlowTTS with the following command:
```
pip install TensorFlowTTS
```

### Converting your Text to Wav
```python
import soundfile as sf
import numpy as np

import tensorflow as tf

from tensorflow_tts.inference import AutoProcessor
from tensorflow_tts.inference import TFAutoModel

processor = AutoProcessor.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en")
tacotron2 = TFAutoModel.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en")
mb_melgan = TFAutoModel.from_pretrained("tensorspeech/tts-mb_melgan-ljspeech-en")

text = "This is a demo to show how to use our model to generate mel spectrogram from raw text."

input_ids = processor.text_to_sequence(text)

# tacotron2 inference (text-to-mel)
decoder_output, mel_outputs, stop_token_prediction, alignment_history = tacotron2.inference(
    input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
    input_lengths=tf.convert_to_tensor([len(input_ids)], tf.int32),
    speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
)

# melgan inference (mel-to-wav)
audio = mb_melgan.inference(mel_outputs)[0, :, 0]

# save to file
sf.write('./audio.wav', audio, 22050, "PCM_16")
```

#### Referencing Multi-band MelGAN
```
@misc{yang2020multiband,
      title={Multi-band MelGAN: Faster Waveform Generation for High-Quality Text-to-Speech}, 
      author={Geng Yang and Shan Yang and Kai Liu and Peng Fang and Wei Chen and Lei Xie},
      year={2020},
      eprint={2005.05106},
      archivePrefix={arXiv},
      primaryClass={cs.SD}
}
```

#### Referencing TensorFlowTTS
```
@misc{TFTTS,
    author = {Minh Nguyen, Alejandro Miguel Velasquez, Erogol, Kuan Chen, Dawid Kobus, Takuya Ebata, 
    Trinh Le and Yunchao He},
    title = {TensorflowTTS},
    year = {2020},
    publisher = {GitHub},
    journal = {GitHub repository},
    howpublished = {\\url{https://github.com/TensorSpeech/TensorFlowTTS}},
  }
```