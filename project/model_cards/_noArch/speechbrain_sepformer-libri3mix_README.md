---
language: "en"
thumbnail:
tags:
- Source Separation
- Speech Separation
- Audio Source Separation
- Libri3Mix
- SepFormer
- Transformer 
- audio-to-audio 
- audio-source-separation
- speechbrain
license: "apache-2.0"
datasets:
- Libri3Mix
metrics:
- SI-SNRi
- SDRi

---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# SepFormer trained on Libri3Mix

This repository provides all the necessary tools to perform audio source separation with a [SepFormer](https://arxiv.org/abs/2010.13154v2) 
model, implemented with SpeechBrain, and pretrained on Libri3Mix dataset. For a better experience we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The model performance is 19.8 dB SI-SNRi on the test set of Libri3Mix dataset.

| Release | Test-Set SI-SNRi | Test-Set SDRi |
|:-------------:|:--------------:|:--------------:|
| 16-09-22 | 19.0dB | 19.4dB |


## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Perform source separation on your own audio file

```python
from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio

model = separator.from_hparams(source="speechbrain/sepformer-libri3mix", savedir='pretrained_models/sepformer-libri3mix')

est_sources = model.separate_file(path='speechbrain/sepformer-wsj03mix/test_mixture_3spks.wav') 

torchaudio.save("source1hat.wav", est_sources[:, :, 0].detach().cpu(), 8000)
torchaudio.save("source2hat.wav", est_sources[:, :, 1].detach().cpu(), 8000)
torchaudio.save("source3hat.wav", est_sources[:, :, 2].detach().cpu(), 8000)

```

The system expects input recordings sampled at 8kHz (single channel).
If your signal has a different sample rate, resample it (e.g, using torchaudio or sox) before using the interface.

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (fc2eabb7).
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
cd  recipes/LibriMix/separation
python train.py hparams/sepformer.yaml --data_folder=your_data_folder
```
Note: change num_spks to 3 in the yaml file.


You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1DN49LtAs6cq1X0jZ8tRMlh2Pj6AecClz).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

#### Referencing SpeechBrain

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


#### Referencing SepFormer
```bibtex
@inproceedings{subakan2021attention,
      title={Attention is All You Need in Speech Separation}, 
      author={Cem Subakan and Mirco Ravanelli and Samuele Cornell and Mirko Bronzi and Jianyuan Zhong},
      year={2021},
      booktitle={ICASSP 2021}
}

@misc{subakan2022sepformer
  author = {Subakan, Cem and Ravanelli, Mirco and Cornell, Samuele and Grondin, Francois and Bronzi, Mirko},
  title = {On Using Transformers for Speech-Separation},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}

```

# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/