---
language:
- en
thumbnail: null
tags:
- automatic-speech-recognition
- CTC
- Attention
- pytorch
- speechbrain
license: "apache-2.0"
datasets:
- switchboard
metrics:
- wer
- cer

---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# CRDNN with CTC/Attention trained on Switchboard (No LM)

This repository provides all the necessary tools to perform automatic speech recognition from an end-to-end system pretrained on Switchboard (EN) within SpeechBrain. 
For a better experience we encourage you to learn more about [SpeechBrain](https://speechbrain.github.io). 

The performance of the model is the following:

| Release  | Swbd CER | Callhome CER | Eval2000 CER | Swbd WER | Callhome WER | Eval2000 WER | GPUs        |
|:--------:|:--------:|:------------:|:------------:|:--------:|:------------:|:------------:|:-----------:|
| 17-09-22 |  9.89   |  16.30       |  13.17       |  16.01     |  25.12     |  20.71       | 1xA100 40GB |


## Pipeline description

This ASR system is composed with 2 different but linked blocks:
- Tokenizer (unigram) that transforms words into subword units trained on
the training transcriptions of the Switchboard and Fisher corpus.
- Acoustic model (CRDNN + CTC/Attention). The CRDNN architecture is made of
N blocks of convolutional neural networks with normalisation and pooling on the
frequency domain. Then, a bidirectional LSTM is connected to a final DNN to obtain
the final acoustic representation that is given to the CTC and attention decoders.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling `transcribe_file` if needed.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Note that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

## Transcribing Your Own Audio Files

```python
from speechbrain.pretrained import EncoderDecoderASR

asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-crdnn-switchboard", savedir="pretrained_models/speechbrain/asr-crdnn-switchboard")
asr_model.transcribe_file('speechbrain/asr-crdnn-switchboard/example.wav')

```

## Inference on GPU

To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

## Parallel Inference on a Batch

Please, [see this Colab notebook](https://colab.research.google.com/drive/1hX5ZI9S4jHIjahFCZnhwwQmFoGAi3tmu?usp=sharing) to figure out how to transcribe in parallel a batch of input sentences using a pre-trained model.

## Training

The model was trained with SpeechBrain (commit hash: `70904d0`).
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
cd recipes/Switchboard/ASR/seq2seq
python train.py hparams/train_BPE_2000.yaml --data_folder=your_data_folder
```

## Limitations

The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets. 

## Credits

This model was trained with resources provided by the [THN Center for AI](https://www.th-nuernberg.de/en/kiz). 

# About SpeechBrain

SpeechBrain is an open-source and all-in-one speech toolkit. It is designed to be simple, extremely flexible, and user-friendly. 
Competitive or state-of-the-art performance is obtained in various domains.

- Website: https://speechbrain.github.io/
- GitHub: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/

# Citing SpeechBrain

Please cite SpeechBrain if you use it for your research or business.

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
