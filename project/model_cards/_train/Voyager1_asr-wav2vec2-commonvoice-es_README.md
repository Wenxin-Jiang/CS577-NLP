---
language:
- es
thumbnail: null
pipeline_tag: automatic-speech-recognition
tags:
- CTC
- pytorch
- speechbrain
- Transformer
- hf-asr-leaderboard
license: afl-3.0
datasets:
- commonvoice
metrics:
- wer
- cer
model-index:
- name: asr-wav2vec2-commonvoice-es
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: CommonVoice 7.0 (Spanish)
      type: mozilla-foundation/common_voice_7_0
      config: es
      split: test
      args:
        language: es
    metrics:
    - name: Test WER
      type: wer
      value: '7.68'
---



<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# wav2vec 2.0 with CTC trained on CommonVoice Spanish (No LM)

This repository provides all the necessary tools to perform automatic speech
recognition from an end-to-end system pretrained on CommonVoice (Spanish Language) within
SpeechBrain. For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io).

The performance of the model is the following:

| Release | Test CER | Test WER | GPUs |
|:-------------:|:--------------:|:--------------:| :--------:|
| 16-01-23 | 2.27 | 7.68 | 3xRTX2080Ti 12GB |

## Pipeline description

This ASR system is composed of 2 different but linked blocks:
- Tokenizer (char) that transforms words into chars and trained with
the train transcriptions (train.tsv) of CommonVoice (ES).  
- Acoustic model (wav2vec2.0 + CTC). A pretrained wav2vec 2.0 model ([wav2vec2-large-xlsr-53-spanish](https://huggingface.co/facebook/wav2vec2-large-xlsr-53-spanish)) is combined with two DNN layers and finetuned on CommonVoice ES. 
The obtained final acoustic representation is given to the CTC decoder.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

## Install SpeechBrain

First of all, please install tranformers and SpeechBrain with the following command:

```
pip install speechbrain transformers
```

Please notice that we encourage you to read tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Transcribing your own audio files (in Spanish)

```python
from speechbrain.pretrained import EncoderASR

asr_model = EncoderASR.from_hparams(source="Voyager1/asr-wav2vec2-commonvoice-es", savedir="pretrained_models/asr-wav2vec2-commonvoice-es")
asr_model.transcribe_file("Voyager1/asr-wav2vec2-commonvoice-es/example-es.wav")

```
### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.


### Limitations
We do not provide any warranty on the performance achieved by this model when used on other datasets.


# **Citations**

```bibtex

@article{lopez2022tid,
  title={TID Spanish ASR system for the Albayzin 2022 Speech-to-Text Transcription Challenge},
  author={L{\'o}pez, Fernando and Luque, Jordi},
  journal={Proc. IberSPEECH 2022},
  pages={271--275},
  year={2022}
}

@misc{https://doi.org/10.48550/arxiv.2210.15226,
  doi = {10.48550/ARXIV.2210.15226},
  url = {https://arxiv.org/abs/2210.15226},
  author = {López, Fernando and Luque, Jordi},
  title = {Iterative pseudo-forced alignment by acoustic CTC loss for self-supervised ASR domain adaptation},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}

@misc{speechbrain,
  title={{SpeechBrain}: A General-Purpose Speech Toolkit},
  author={Mirco Ravanelli and Titouan Parcollet and Peter Plantinga and Aku Rouhe and Samuele Cornell and Loren Lugosch and Cem Subakan and Nauman Dawalatabad and Abdelwahab Heba and Jianyuan Zhong and Ju-Chieh Chou and Sung-Lin Yeh and Szu-Wei Fu and Chien-Feng Liao and Elena Rastorgueva and François Grondin and William Aris and Hwidong Na and Yan Gao and Renato De Mori and Yoshua Bengio},
  year={2021},
  eprint={2106.04624},
  archivePrefix={arXiv},
  primaryClass={eess.AS},
  note={arXiv:2106.04624}
}
```
