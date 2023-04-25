---
language:
- ar
- eu
- br
- ca
- cv
- cs
- dv
- nl
- en
- eo
- et
- fr
- fy
- ka
- de
- el
- cnh
- id
- ia
- it
- ja
- kab
- rw
- ky
- lv
- mt
- mn
- fa
- pl
- pt
- ro
- rm
- ru
- sah
- sl
- es
- sv
- ta
- tt
- tr
- uk
- cy
language_bcp47:
- zh-CH
- zh-HK
- zh-TW
thumbnail:
tags:
- audio-classification
- speechbrain
- embeddings
- Language
- Identification
- pytorch
- ECAPA-TDNN
- TDNN
- CommonLanguage
license: "apache-2.0"
datasets:
- Urbansound8k
metrics:
- Accuracy
widget:
- example_title: English Sample
  src: https://cdn-media.huggingface.co/speech_samples/LibriSpeech_61-70968-0000.flac
---


<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Language Identification from Speech Recordings with ECAPA embeddings on CommonLanguage

This repository provides all the necessary tools to perform language identification from speech recordings with SpeechBrain.
The system uses a model pretrained on the CommonLanguage dataset (45 languages).
You can download the dataset [here](https://zenodo.org/record/5036977#.YNzDbXVKg5k)
The provided system can recognize the following 45 languages from short speech recordings:

```
Arabic, Basque, Breton, Catalan, Chinese_China, Chinese_Hongkong, Chinese_Taiwan, Chuvash, Czech, Dhivehi, Dutch, English, Esperanto, Estonian, French, Frisian, Georgian, German, Greek, Hakha_Chin, Indonesian, Interlingua, Italian, Japanese, Kabyle, Kinyarwanda, Kyrgyz, Latvian, Maltese, Mongolian, Persian, Polish, Portuguese, Romanian, Romansh_Sursilvan, Russian, Sakha, Slovenian, Spanish, Swedish, Tamil, Tatar, Turkish, Ukrainian, Welsh
```

For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The given model performance on the test set is:

| Release | Accuracy (%)
|:-------------:|:--------------:|
| 30-06-21 | 85.0 | 


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

### Perform Language  Identification from Speech Recordings

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/lang-id-commonlanguage_ecapa", savedir="pretrained_models/lang-id-commonlanguage_ecapa")
# Italian Example
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/lang-id-commonlanguage_ecapa/example-it.wav')
print(text_lab)

# French Example
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/lang-id-commonlanguage_ecapa/example-fr.wav')
print(text_lab)
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (a02f860e).
To train it from scratch follow these steps:
1. Clone SpeechBrain:
```bash
git clone https://github.com/speechbrain/speechbrain/
```
2. Install it:
```
cd speechbrain
pip install -r requirements.txt
pip install -e .
```

3. Run Training:
```
cd recipes/CommonLanguage/lang_id
python train.py hparams/train_ecapa_tdnn.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1sD2u0MhSmJlx_3RRgwsYzevX81RM8-WE?usp=sharing).

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
