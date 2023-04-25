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

# MelGAN trained on LJSpeech (En)
This repository provides a pretrained [MelGAN](https://arxiv.org/abs/1910.06711) trained on LJSpeech dataset (Eng). For a detail of the model, we encourage you to read more about
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
melgan = TFAutoModel.from_pretrained("tensorspeech/tts-melgan-ljspeech-en")

text = "This is a demo to show how to use our model to generate mel spectrogram from raw text."

input_ids = processor.text_to_sequence(text)

# tacotron2 inference (text-to-mel)
decoder_output, mel_outputs, stop_token_prediction, alignment_history = tacotron2.inference(
    input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
    input_lengths=tf.convert_to_tensor([len(input_ids)], tf.int32),
    speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
)

# melgan inference (mel-to-wav)
audio = melgan.inference(mel_outputs)[0, :, 0]

# save to file
sf.write('./audio.wav', audio, 22050, "PCM_16")
```

#### Referencing MelGAN
```
@misc{kumar2019melgan,
      title={MelGAN: Generative Adversarial Networks for Conditional Waveform Synthesis}, 
      author={Kundan Kumar and Rithesh Kumar and Thibault de Boissiere and Lucas Gestin and Wei Zhen Teoh and Jose Sotelo and Alexandre de Brebisson and Yoshua Bengio and Aaron Courville},
      year={2019},
      eprint={1910.06711},
      archivePrefix={arXiv},
      primaryClass={eess.AS}
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