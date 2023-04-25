---
language: "en"
tags:
- Robust ASR
- audio-to-audio 
- speech-enhancement
- PyTorch
- speechbrain
license: "apache-2.0"
datasets:
- Voicebank
- DEMAND
metrics:
- WER
- PESQ
- COVL
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# ResNet-like model

This repository provides all the necessary tools to perform enhancement and
robust ASR training (EN) within
SpeechBrain. For a better experience we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The model performance is:

| Release | Test PESQ | Test COVL | Valid WER | Test WER |
|:--------:|:----:|:----:|:----:|:----:|
| 22-06-21 | 3.05 | 3.74 | 2.89 | 2.80 |

Works with SpeechBrain v0.5.12

## Pipeline description

The mimic loss training system consists of three steps:

1. A perceptual model is pre-trained on clean speech features, the
same type used for the enhancement masking system.
2. An enhancement model is trained with mimic loss, using the
pre-trained perceptual model.
3. A large ASR model pre-trained on LibriSpeech is fine-tuned
using the enhancement front-end.

The enhancement and ASR models can be used together or
independently.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

## Pretrained Usage

To use the mimic-loss-trained model for enhancement, use the following simple code:

```python
import torchaudio
from speechbrain.pretrained import WaveformEnhancement

enhance_model = WaveformEnhancement.from_hparams(
    source="speechbrain/mtl-mimic-voicebank",
    savedir="pretrained_models/mtl-mimic-voicebank",
)
enhanced = enhance_model.enhance_file("speechbrain/mtl-mimic-voicebank/example.wav")

# Saving enhanced signal on disk
torchaudio.save('enhanced.wav', enhanced.unsqueeze(0).cpu(), 16000)
```

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *enhance_file* if needed. Make sure your input tensor is compliant with the expected sampling rate if you use *enhance_batch* as in the example.


### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (150e1890).
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
cd  recipes/Voicebank/MTL/ASR_enhance
python train.py hparams/enhance_mimic.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1HaR0Bq679pgd1_4jD74_wDRUq-c3Wl4L?usp=sharing).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

## Referencing Mimic Loss

If you find mimic loss useful, please cite:

```
@inproceedings{bagchi2018spectral,
title={Spectral Feature Mapping with Mimic Loss for Robust Speech Recognition},
author={Bagchi, Deblin and Plantinga, Peter and Stiff, Adam and Fosler-Lussier, Eric},
booktitle={IEEE Conference on Audio, Speech, and Signal Processing (ICASSP)},
year={2018}
}
```

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
