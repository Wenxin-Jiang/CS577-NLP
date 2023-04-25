---
tags:
- tensorflowtts
- audio
- text-to-speech
- text-to-mel
language: chinese
license: apache-2.0
datasets:
- Baker
widget:
- text: "这是一个开源的端到端中文语音合成系统"
---

# FastSpeech2 trained on Baker (Chinese)
This repository provides a pretrained [FastSpeech2](https://arxiv.org/abs/2006.04558) trained on Baker dataset (Ch). For a detail of the model, we encourage you to read more about
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

processor = AutoProcessor.from_pretrained("tensorspeech/tts-fastspeech2-baker-ch")
fastspeech2 = TFAutoModel.from_pretrained("tensorspeech/tts-fastspeech2-baker-ch")

text = "这是一个开源的端到端中文语音合成系统"

input_ids = processor.text_to_sequence(text, inference=True)

mel_before, mel_after, duration_outputs, _, _ = fastspeech2.inference(
    input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
    speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
    speed_ratios=tf.convert_to_tensor([1.0], dtype=tf.float32),
    f0_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
    energy_ratios =tf.convert_to_tensor([1.0], dtype=tf.float32),
)
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