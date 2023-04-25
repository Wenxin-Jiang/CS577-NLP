---
language: "en"
thumbnail:
tags:
- embeddings
- Speaker
- Verification
- Identification
- pytorch
- xvectors
- TDNN
- speechbrain
- audio-classification
license: "apache-2.0"
datasets:
- voxceleb
metrics:
- EER
- min_dct
widget:
- example_title: VoxCeleb Speaker id10003
  src: https://cdn-media.huggingface.co/speech_samples/VoxCeleb1_00003.wav
- example_title: VoxCeleb Speaker id10004
  src: https://cdn-media.huggingface.co/speech_samples/VoxCeleb_00004.wav
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Speaker Verification with xvector embeddings on Voxceleb

This repository provides all the necessary tools to extract speaker embeddings with a pretrained TDNN model using SpeechBrain. 
The system is trained on Voxceleb 1+ Voxceleb2 training data. 

For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The given model performance on Voxceleb1-test set (Cleaned) is:

| Release | EER(%) 
|:-------------:|:--------------:|
| 05-03-21 | 3.2 | 


## Pipeline description
This system is composed of a TDNN model coupled with statistical pooling. The system is trained with Categorical Cross-Entropy Loss.  

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Compute your speaker embeddings

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/spkrec-xvect-voxceleb", savedir="pretrained_models/spkrec-xvect-voxceleb")
signal, fs =torchaudio.load('tests/samples/ASR/spk1_snt1.wav')
embeddings = classifier.encode_batch(signal)
```

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *classify_file* if needed. Make sure your input tensor is compliant with the expected sampling rate if you use *encode_batch* and *classify_batch*.

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (aa018540).
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
cd  recipes/VoxCeleb/SpeakerRec/
python train_speaker_embeddings.py hparams/train_x_vectors.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1RtCBJ3O8iOCkFrJItCKT9oL-Q1MNCwMH?usp=sharing).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

#### Referencing xvectors
```@inproceedings{DBLP:conf/odyssey/SnyderGMSPK18,
  author    = {David Snyder and
               Daniel Garcia{-}Romero and
               Alan McCree and
               Gregory Sell and
               Daniel Povey and
               Sanjeev Khudanpur},
  title     = {Spoken Language Recognition using X-vectors},
  booktitle = {Odyssey 2018},
  pages     = {105--111},
  year      = {2018},
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
