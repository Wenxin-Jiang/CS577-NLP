---
language: "en"
tags:
- audio-to-audio 
- speech-enhancement
- PyTorch
- speechbrain
license: "apache-2.0"
datasets:
- Voicebank
- DEMAND
metrics:
- PESQ
- STOI
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# MetricGAN-trained model for Enhancement

This repository provides all the necessary tools to perform enhancement with
SpeechBrain. For a better experience we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The model performance is:

| Release | Test PESQ | Test STOI |
|:-----------:|:-----:| :-----:|
| 21-04-27 | 3.15 | 93.0 |

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
import torch
import torchaudio
from speechbrain.pretrained import SpectralMaskEnhancement

enhance_model = SpectralMaskEnhancement.from_hparams(
    source="speechbrain/metricgan-plus-voicebank",
    savedir="pretrained_models/metricgan-plus-voicebank",
)

# Load and add fake batch dimension
noisy = enhance_model.load_audio(
    "speechbrain/metricgan-plus-voicebank/example.wav"
).unsqueeze(0)

# Add relative length tensor
enhanced = enhance_model.enhance_batch(noisy, lengths=torch.tensor([1.]))

# Saving enhanced signal on disk
torchaudio.save('enhanced.wav', enhanced.cpu(), 16000)
```

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *enhance_file* if needed. Make sure your input tensor is compliant with the expected sampling rate if you use *enhance_batch* as in the example.

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (d0accc8).
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
cd  recipes/Voicebank/enhance/MetricGAN
python train.py hparams/train.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1fcVP52gHgoMX9diNN1JxX_My5KaRNZWs?usp=sharing).

### Limitations
The SpeechBrain team does not provide any warranty on the performance achieved by this model when used on other datasets.

## Referencing MetricGAN+

If you find MetricGAN+ useful, please cite:

```
@article{fu2021metricgan+,
  title={MetricGAN+: An Improved Version of MetricGAN for Speech Enhancement},
  author={Fu, Szu-Wei and Yu, Cheng and Hsieh, Tsun-An and Plantinga, Peter and Ravanelli, Mirco and Lu, Xugang and Tsao, Yu},
  journal={arXiv preprint arXiv:2104.03538},
  year={2021}
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