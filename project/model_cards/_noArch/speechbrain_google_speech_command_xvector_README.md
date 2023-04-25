---
language: "en"
thumbnail:
tags: 
- speechbrain
- embeddings
- Commands
- Keywords
- Keyword Spotting
- pytorch
- xvectors
- TDNN
- Command Recognition
- audio-classification
license: "apache-2.0"
datasets:
- google speech commands
metrics:
- Accuracy
widget:
- example_title: Speech Commands "down"
  src: https://cdn-media.huggingface.co/speech_samples/keyword_spotting_down.wav
- example_title: Speech Commands "go"
  src: https://cdn-media.huggingface.co/speech_samples/keyword_spotting_go.wav

---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>

# Command Recognition with xvector embeddings on Google Speech Commands

This repository provides all the necessary tools to perform command recognition with SpeechBrain using a model pretrained on Google Speech Commands.
You can download the dataset [here](https://www.tensorflow.org/datasets/catalog/speech_commands)
The dataset provides small training, validation, and test sets useful for detecting single keywords in short audio clips. The provided system can recognize the following 12 keywords:
```
'yes', 'no', 'up', 'down', 'left', 'right', 'on', 'off', 'stop', 'go', 'unknown', 'silence'
```

For a better experience, we encourage you to learn more about
[SpeechBrain](https://speechbrain.github.io). The given model performance on the test set is:

| Release | Accuracy(%) 
|:-------------:|:--------------:|
| 06-02-21 | 98.14 | 


## Pipeline description
This system is composed of a TDNN model coupled with statistical pooling. A classifier, trained with Categorical Cross-Entropy Loss, is applied on top of that.

The system is trained with recordings sampled at 16kHz (single channel).
The code will automatically normalize your audio (i.e., resampling + mono channel selection) when calling *classify_file* if needed.

## Install SpeechBrain

First of all, please install SpeechBrain with the following command:

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Perform Command Recognition

```python
import torchaudio
from speechbrain.pretrained import EncoderClassifier
classifier = EncoderClassifier.from_hparams(source="speechbrain/google_speech_command_xvector", savedir="pretrained_models/google_speech_command_xvector")
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/google_speech_command_xvector/yes.wav')
print(text_lab)
out_prob, score, index, text_lab = classifier.classify_file('speechbrain/google_speech_command_xvector/stop.wav')
print(text_lab)
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.

### Training
The model was trained with SpeechBrain (b7ff9dc4).
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
cd recipes/Google-speech-commands
python train.py hparams/xvect.yaml --data_folder=your_data_folder
```

You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1BKwtr1mBRICRe56PcQk2sCFq63Lsvdpc?usp=sharing).

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

#### Referencing Google Speech Commands
```@article{speechcommands,
   author = { {Warden}, P.},
    title = "{Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition}",
  journal = {ArXiv e-prints},
  archivePrefix = "arXiv",
  eprint = {1804.03209},
  primaryClass = "cs.CL",
  keywords = {Computer Science - Computation and Language, Computer Science - Human-Computer Interaction},
    year = 2018,
    month = apr,
    url = {https://arxiv.org/abs/1804.03209},
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
