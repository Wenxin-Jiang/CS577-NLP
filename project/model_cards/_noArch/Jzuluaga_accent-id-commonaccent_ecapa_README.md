---
language:
- en
thumbnail:
tags:
- audio-classification
- speechbrain
- embeddings
- Accent
- Identification
- pytorch
- ECAPA-TDNN
- TDNN
- CommonAccent
license: "mit"
datasets:
- CommonVoice
metrics:
- Accuracy
widget:
- example_title: Africa-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/african_1.wav
- example_title: Australia-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/australia_1.wav
- example_title: India-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/indian_1.wav
- example_title: Ireland-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/ireland_1.wav
- example_title: Malaysia-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/malaysia_1.wav
- example_title: Canada-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/canada_1.wav
- example_title: SouthAtlantic-English
  src: https://huggingface.co/Jzuluaga/accent-id-commonaccent_ecapa/resolve/main/data/southatlantic_1.wav
---


<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Accent Identification from Speech Recordings with ECAPA-TDNN embeddings on CommonAccent


**Abstract**: The recognition of accented speech still remains a dominant problem in Automatic Speech Recognition (ASR) systems. We approach the classification of accented English speech through the Emphasized Channel Attention, Propagation and Aggregation Time Delay Neural Network (ECAPA-TDNN) architecture which has been shown to perform well on a variety of speech tasks. Three models are proposed: one trained from scratch, another two models (one using data augmentation and a baseline model) fine-tuned from the checkpoints of speechbrain/spkrec-ecapa-voxceleb (VoxCeleb). Our results show that the model fine-tuned with data augmentation yield the best results. Most of the misclassifications were structured and expected due to accent similarities, such as the American and Canadian accents. We also explored the internal categorization of embeddings through t-SNE, a dimensionality reduction technique, and found that there was a level of clustering based on phonological similarity. For future work, we would like to explore the implementation of this accent classification system in our suggested framework to improve ASR performance by making it more inclusive to accented speech. 


This repository provides all the necessary tools to perform accent identification from speech recordings with [SpeechBrain](https://github.com/speechbrain/speechbrain).
The system uses a model pretrained on the CommonAccent dataset in English (16 accents). This system is based on the CommonLanguage Recipe located here: https://github.com/speechbrain/speechbrain/tree/develop/recipes/CommonLanguage


The provided system can recognize the following 16 accents from short speech recordings in English (EN):

```
african
australia
bermuda
canada
england
hongkong
indian
ireland
malaysia
newzealand
philippines
scotland
singapore
southatlandtic
us
wales
```

<a href="https://github.com/JuanPZuluaga/accent-recog-slt2022"> <img alt="GitHub" src="https://img.shields.io/badge/GitHub-Open%20source-green"> </a> Github repository link: https://github.com/JuanPZuluaga/accent-recog-slt2022


For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The given model performance on the test set is:

| Release (dd/mm/yyyy) | Accuracy (%)
|:-------------:|:--------------:|
| 01-08-2023 (this model) | 87 | 
| 01-08-2023 (this model trained without data augmentation) | 85 | 
| 01-08-2023 (this model trained from scratch, no paremeter transfer) | 82 | 


## Pipeline description
This system is composed of an ECAPA model coupled with statistical pooling. A classifier, trained with Categorical Cross-Entropy Loss, is applied on top of that.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *classify_file* if needed. Make sure your input tensor is compliant with the expected sampling rate if you use *encode_batch* and *classify_batch*.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Perform Accent Identification from Speech Recordings

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="Jzuluaga/accent-id-commonaccent_ecapa", savedir="pretrained_models/accent-id-commonaccent_ecapa")
# Irish Example
out_prob, score, index, text_lab = classifier.classify_file('Jzuluaga/accent-id-commonaccent_ecapa/data/ireland_1.wav')
print(text_lab)

# Malaysia Example
out_prob, score, index, text_lab = classifier.classify_file('Jzuluaga/accent-id-commonaccent_ecapa/data/malaysia_1.wav')
print(text_lab)
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training

The model was trained with SpeechBrain.

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

3. Clone our repository in https://github.com/JuanPZuluaga/accent-recog-slt2022:

```bash
git clone https://github.com/JuanPZuluaga/accent-recog-slt2022
cd CommonAccent/accent_id
python train.py hparams/train_ecapa_tdnn.yaml
```

You can find our training results (models, logs, etc) in this repository's `Files and versions` page.

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

#### Referencing ECAPA

```@inproceedings{DBLP:conf/interspeech/DesplanquesTD20,
  author    = {Brecht Desplanques and
               Jenthe Thienpondt and
               Kris Demuynck},
  editor    = {Helen Meng and
               Bo Xu and
               Thomas Fang Zheng},
  title     = {{ECAPA-TDNN:} Emphasized Channel Attention, Propagation and Aggregation
               in {TDNN} Based Speaker Verification},
  booktitle = {Interspeech 2020},
  pages     = {3830--3834},
  publisher = {{ISCA}},
  year      = {2020},
}
```


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