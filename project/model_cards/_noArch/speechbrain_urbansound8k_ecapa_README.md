---
language: "en"
thumbnail:
tags:
- speechbrain
- embeddings
- Sound
- Keywords
- Keyword Spotting
- pytorch
- ECAPA-TDNN
- TDNN
- Command Recognition
- audio-classification
license: "apache-2.0"
datasets:
- Urbansound8k
metrics:
- Accuracy

---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Sound Recognition with ECAPA embeddings on UrbanSoudnd8k

This repository provides all the necessary tools to perform sound recognition with SpeechBrain using a model pretrained on UrbanSound8k.
You can download the dataset [here](https://urbansounddataset.weebly.com/urbansound8k.html)
The provided system can recognize the following 10 keywords:

```
dog_bark, children_playing, air_conditioner, street_music, gun_shot, siren, engine_idling, jackhammer, drilling, car_horn
```

For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The given model performance on the test set is:

| Release | Accuracy 1-fold (%)
|:-------------:|:--------------:|
| 04-06-21 | 75.5 | 


## Pipeline description
This system is composed of a ECAPA model coupled with statistical pooling. A classifier, trained with Categorical Cross-Entropy Loss, is applied on top of that.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Perform Sound Recognition

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/urbansound8k_ecapa", savedir="pretrained_models/gurbansound8k_ecapa")
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/urbansound8k_ecapa/dog_bark.wav')
print(text_lab)
```
The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *classify_file* if needed. Make sure your input tensor is compliant with the expected sampling rate if you use *encode_batch* and *classify_batch*.

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (8cab8b0c).
To train it from scratch follows these steps:
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
cd recipes/UrbanSound8k/SoundClassification
python train.py hparams/train_ecapa_tdnn.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1sItfg_WNuGX6h2dCs8JTGq2v2QoNTaUg?usp=sharing).

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

#### Referencing UrbanSound
```@inproceedings{Salamon:UrbanSound:ACMMM:14,
    Author = {Salamon, J. and Jacoby, C. and Bello, J. P.},
    Booktitle = {22nd {ACM} International Conference on Multimedia (ACM-MM'14)},
    Month = {Nov.},
    Pages = {1041--1044},
    Title = {A Dataset and Taxonomy for Urban Sound Research},
    Year = {2014}}
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
