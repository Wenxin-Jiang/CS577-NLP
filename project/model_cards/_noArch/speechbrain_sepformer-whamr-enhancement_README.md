---
language: "en"
thumbnail:
tags:
- audio-to-audio 
- Speech Enhancement
- WHAMR!
- SepFormer
- Transformer 
- pytorch
- speechbrain
license: "apache-2.0"
datasets:
- WHAMR!
metrics:
- SI-SNR
- PESQ

---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# SepFormer trained on WHAMR! for speech enhancement (8k sampling frequency)
This repository provides all the necessary tools to perform speech enhancement (denoising + dereverberation) with a [SepFormer](https://arxiv.org/abs/2010.13154v2) model, implemented with SpeechBrain, and pretrained on [WHAMR!](http://wham.whisper.ai/) dataset with 8k sampling frequency, which is basically a version of WSJ0-Mix dataset with environmental noise and reverberation in 8k. For a better experience we encourage you to learn more about [SpeechBrain](https://speechbrain.github.io). The given model performance is 10.59 dB SI-SNR on the test set of WHAMR! dataset.


| Release | Test-Set SI-SNR | Test-Set PESQ |
|:-------------:|:--------------:|:--------------:|
| 01-12-21 | 10.59 | 2.84 |


## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about [SpeechBrain](https://speechbrain.github.io).

### Perform speech enhancement on your own audio file

```python
from speechbrain.pretrained import SepformerSeparation as separator
import torchaudio

model = separator.from_hparams(source="speechbrain/sepformer-whamr-enhancement", savedir='pretrained_models/sepformer-whamr-enhancement')

# for custom file, change path
est_sources = model.separate_file(path='speechbrain/sepformer-whamr-enhancement/example_whamr.wav') 

torchaudio.save("enhanced_whamr.wav", est_sources[:, :, 0].detach().cpu(), 8000)

```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The training script is currently being worked on an ongoing pull-request. 

We will update the model card as soon as the PR is merged. 

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1V0KwkEfWwomZ0Vjox0BTnQ694_uxgu8G).

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
```

# **About SpeechBrain**
- Website: https://speechbrain.github.io/
- Code: https://github.com/speechbrain/speechbrain/
- HuggingFace: https://huggingface.co/speechbrain/