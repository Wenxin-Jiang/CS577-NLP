---
language: "en"
thumbnail:
tags:
- automatic-speech-recognition
- CTC
- Attention
- Transformers
- wav2vec2
- pytorch
- speechbrain
license: "apache-2.0"
datasets:
- aishell
metrics:
- wer
- cer
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Transformer for AISHELL + wav2vec2 (Mandarin Chinese)

This repository provides all the necessary tools to perform automatic speech
recognition from an end-to-end system pretrained on AISHELL +wav2vec2 (Mandarin Chinese)
within SpeechBrain. For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io).

The performance of the model is the following:

| Release | Dev CER | Test CER | GPUs | Full Results |
|:-------------:|:--------------:|:--------------:|:--------:|:--------:|
| 05-03-21 | 5.19 | 5.58 | 2xV100 32GB | [Google Drive](https://drive.google.com/drive/folders/1zlTBib0XEwWeyhaXDXnkqtPsIBI18Uzs?usp=sharing)|



## Pipeline description

This ASR system is composed of 2 different but linked blocks:
- Tokenizer (unigram) that transforms words into subword units and trained with
the train transcriptions of LibriSpeech.
- Acoustic model made of a wav2vec2 encoder and a joint decoder with CTC +
transformer. Hence, the decoding also incorporates the CTC probabilities.

To Train this system from scratch, [see our SpeechBrain recipe](https://github.com/speechbrain/speechbrain/tree/develop/recipes/AISHELL-1/ASR/transformer).

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Transcribing your own audio files (in English)

```python
from speechbrain.pretrained import EncoderDecoderASR
asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-wav2vec2-transformer-aishell", savedir="pretrained_models/asr-wav2vec2-transformer-aishell")
asr_model.transcribe_file("speechbrain/asr-wav2vec2-transformer-aishell/example_mandarin.wav")
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

## Parallel Inference on a Batch
Please, [see this Colab notebook](https://colab.research.google.com/drive/1hX5ZI9S4jHIjahFCZnhwwQmFoGAi3tmu?usp=sharing) to figure out how to transcribe in parallel a batch of input sentences using a pre-trained model.

### Training
The model was trained with SpeechBrain (Commit hash: '480dde87').
To train it from scratch follow these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```bash
cd speechbrain
pip install -r requirements.txt
pip install -e .
```

3. Run Training:
```bash
cd recipes/AISHELL-1/ASR/transformer/
python train.py hparams/train_ASR_transformer_with_wav2vect.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1P3w5BnwLDxMHFQrkCZ5RYBZ1WsQHKFZr?usp=sharing).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.


# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/


# **Citing SpeechBrain**
Please, cite SpeechBrain if you use it for your research or business.

```bibtex
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