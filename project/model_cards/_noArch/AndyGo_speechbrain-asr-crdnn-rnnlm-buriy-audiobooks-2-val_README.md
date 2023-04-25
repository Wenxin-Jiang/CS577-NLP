---
language: "ru"
thumbnail:
tags:
- automatic-speech-recognition
- CTC
- Attention
- pytorch
- speechbrain
license: "apache-2.0"
datasets:
- buriy-audiobooks-2-val
metrics:
- wer
- cer
---

| Release | Test WER | GPUs |
|:-------------:|:--------------:| :--------:|
| 22-05-11 | - | 1xK80 24GB |

after  9 epochs training - valid %WER: 4.09e+02
after 12 epochs training - valid %WER: 2.07e+02, test WER: 1.78e+02

## Pipeline description
(by SpeechBrain text)

This ASR system is composed with 3 different but linked blocks:
- Tokenizer (unigram) that transforms words into subword units and trained with
the train transcriptions of LibriSpeech.
- Neural language model (RNNLM) trained on the full (380K) words dataset.
- Acoustic model (CRDNN + CTC/Attention). The CRDNN architecture is made of
N blocks of convolutional neural networks with normalisation and pooling on the
frequency domain. Then, a bidirectional LSTM is connected to a final DNN to obtain
the final acoustic representation that is given to the CTC and attention decoders.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that SpeechBrain encourage you to read tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Transcribing your own audio files (in Russian)

```python
from speechbrain.pretrained import EncoderDecoderASR
asr_model = EncoderDecoderASR.from_hparams(source="AndyGo/speechbrain-asr-crdnn-rnnlm-buriy-audiobooks-2-val", savedir="pretrained_models/speech-brain-asr-crdnn-rnnlm-buriy-audiobooks-2-val")
asr_model.transcribe_file('speechbrain-asr-crdnn-rnnlm-buriy-audiobooks-2-val/example.wav')
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Russian Speech Datasets
Russian Speech Datasets are provided by Microsoft Corporation with CC BY-NC license.
Instructions by downloading - https://github.com/snakers4/open_stt
The CC BY-NC license requires that the original copyright owner be listed as the author and the work be used only for non-commercial purposes
We used buriy-audiobooks-2-val dataset

## About SpeechBrain
Website: https://speechbrain.github.io/
Code: https://github.com/speechbrain/speechbrain/
HuggingFace: https://huggingface.co/speechbrain/

## Citing SpeechBrain
Please, cite SpeechBrain if you use it for your research or business.

@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}