---
tags:
- tensorflowtts
- audio
- text-to-speech
- text-to-mel
language: ko
license: apache-2.0
datasets:
- kss
widget:
- text: "신은 우리의 수학 문제에는 관심이 없다. 신은 다만 경험적으로 통합할 뿐이다."
---

# Tacotron 2 with Guided Attention trained on KSS (Korean)
This repository provides a pretrained [Tacotron2](https://arxiv.org/abs/1712.05884) trained with [Guided Attention](https://arxiv.org/abs/1710.08969) on KSS dataset (KO). For a detail of the model, we encourage you to read more about
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

processor = AutoProcessor.from_pretrained("tensorspeech/tts-tacotron2-kss-ko")
tacotron2 = TFAutoModel.from_pretrained("tensorspeech/tts-tacotron2-kss-ko")

text = "신은 우리의 수학 문제에는 관심이 없다. 신은 다만 경험적으로 통합할 뿐이다."

input_ids = processor.text_to_sequence(text)

decoder_output, mel_outputs, stop_token_prediction, alignment_history = tacotron2.inference(
    input_ids=tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
    input_lengths=tf.convert_to_tensor([len(input_ids)], tf.int32),
    speaker_ids=tf.convert_to_tensor([0], dtype=tf.int32),
)

```

#### Referencing Tacotron 2
```
@article{DBLP:journals/corr/abs-1712-05884,
  author    = {Jonathan Shen and
               Ruoming Pang and
               Ron J. Weiss and
               Mike Schuster and
               Navdeep Jaitly and
               Zongheng Yang and
               Zhifeng Chen and
               Yu Zhang and
               Yuxuan Wang and
               R. J. Skerry{-}Ryan and
               Rif A. Saurous and
               Yannis Agiomyrgiannakis and
               Yonghui Wu},
  title     = {Natural {TTS} Synthesis by Conditioning WaveNet on Mel Spectrogram
               Predictions},
  journal   = {CoRR},
  volume    = {abs/1712.05884},
  year      = {2017},
  url       = {http://arxiv.org/abs/1712.05884},
  archivePrefix = {arXiv},
  eprint    = {1712.05884},
  timestamp = {Thu, 28 Nov 2019 08:59:52 +0100},
  biburl    = {https://dblp.org/rec/journals/corr/abs-1712-05884.bib},
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