---
tags:
- tensorflowtts
- audio
- text-to-speech
- text-to-mel
language: eng
license: apache-2.0
datasets:
- LJSpeech
widget:
- text: "How are you?"
---

# FastSpeech trained on LJSpeech (Eng)
This repository provides a pretrained [FastSpeech](https://arxiv.org/abs/1905.09263) trained on LJSpeech dataset (ENG). For a detail of the model, we encourage you to read more about
[TensorFlowTTS](https://github.com/TensorSpeech/TensorFlowTTS). 


## Install TensorFlowTTS
First of all, please install TensorFlowTTS with the following command:
```
pip install TensorFlowTTS
```

### Converting your Text to Mel Spectrogram
```python
import numpy as np
import soundfile as sf
import yaml

import tensorflow as tf

from tensorflow_tts.inference import AutoProcessor
from tensorflow_tts.inference import TFAutoModel

processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech-ljspeech-en")
fastspeech = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech-ljspeech-en")

text = "How are you?"

input_ids = processor.text_to_sequence(text)

mel_before, mel_after, duration_outputs = fastspeech.inference(
    input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
    speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
    speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
)
```

#### Referencing FastSpeech
```
@article{DBLP:journals/corr/abs-1905-09263,
  author    = {Yi Ren and
               Yangjun Ruan and
               Xu Tan and
               Tao Qin and
               Sheng Zhao and
               Zhou Zhao and
               Tie{-}Yan Liu},
  title     = {FastSpeech: Fast, Robust and Controllable Text to Speech},
  journal   = {CoRR},
  volume    = {abs/1905.09263},
  year      = {2019},
  url       = {http://arxiv.org/abs/1905.09263},
  archivePrefix = {arXiv},
  eprint    = {1905.09263},
  timestamp = {Wed, 11 Nov 2020 08:48:07 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1905-09263.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
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