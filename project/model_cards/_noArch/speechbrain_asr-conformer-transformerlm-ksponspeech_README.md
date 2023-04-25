---
language:
- ko
thumbnail:
tags:
- automatic-speech-recognition
- CTC
- Attention
- Conformer
- pytorch
- speechbrain
license: "apache-2.0"
datasets:
- ksponspeech
metrics:
- wer
- cer
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Conformer for KsponSpeech (with Transformer LM)

This repository provides all the necessary tools to perform automatic speech
recognition from an end-to-end system pretrained on KsponSpeech (Kr) within
SpeechBrain. For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). 
The performance of the model is the following:

| Release  | eval clean CER | eval other CER |    GPUs     |
| :------: | :------------: | :------------: | :---------: |
| 09-05-21 |     7.48%      |     8.38%      | 6xA100 80GB |

## Pipeline description

This ASR system is composed of 3 different but linked blocks:
- Tokenizer (unigram) that transforms words into subword units and trained with
the train transcriptions of KsponSpeech.
- Neural language model (Transformer LM) trained on the train transcriptions of KsponSpeech
- Acoustic model made of a conformer encoder and a joint decoder with CTC +
transformer. Hence, the decoding also incorporates the CTC probabilities.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *transcribe_file* if needed.

## Install SpeechBrain
First of all, please install SpeechBrain with the following command:

```
pip install speechbrain==0.5.10
```
Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).
### Transcribing your own audio files (in Korean)
```
from speechbrain.pretrained import EncoderDecoderASR
asr_model = EncoderDecoderASR.from_hparams(source="ddwkim/asr-conformer-transformerlm-ksponspeech", savedir="pretrained_models/asr-conformer-transformerlm-ksponspeech",  run_opts={"device":"cuda"})
asr_model.transcribe_file("ddwkim/asr-conformer-transformerlm-ksponspeech/record_0_16k.wav")
```

### Inference on GPU

To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

## Parallel Inference on a Batch

Please, [see this Colab notebook](https://colab.research.google.com/drive/10N98aGoeLGfh6Hu6xOCH5BbjVTVYgCyB?usp=sharing) on using the pretrained model

### Training

The model was trained with SpeechBrain (Commit hash: 'fd9826c').
To train it from scratch follow these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```bash
cd speechbrain
pip install -r requirements.txt
pip install .
```
3. Run Training:
```bash
cd recipes/KsponSpeech/ASR/transformer
python train.py hparams/conformer_medium.yaml --data_folder=your_data_folder
```
You can find our training results (models, logs, etc) at the subdirectories.

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

# Citing the model
```bibtex
@misc{returnzero,
  title = {ReturnZero Conformer Korean ASR model},
  author = {Dongwon Kim and Dongwoo Kim and Roh Jeongkyu},
  year = {2021},
  howpublished = {\url{https://huggingface.co/ddwkim/asr-conformer-transformerlm-ksponspeech}},
}
```

# Citing KsponSpeech dataset
```bibtex
@Article{app10196936,
AUTHOR = {Bang, Jeong-Uk and Yun, Seung and Kim, Seung-Hi and Choi, Mu-Yeol and Lee, Min-Kyu and Kim, Yeo-Jeong and Kim, Dong-Hyun and Park, Jun and Lee, Young-Jik and Kim, Sang-Hun},
TITLE = {KsponSpeech: Korean Spontaneous Speech Corpus for Automatic Speech Recognition},
JOURNAL = {Applied Sciences},
VOLUME = {10},
YEAR = {2020},
NUMBER = {19},
ARTICLE-NUMBER = {6936},
URL = {https://www.mdpi.com/2076-3417/10/19/6936},
ISSN = {2076-3417},
DOI = {10.3390/app10196936}
}
```
