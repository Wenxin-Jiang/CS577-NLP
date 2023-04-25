---
language: "en"
tags:
- text-to-speech
- TTS
- speech-synthesis
- Tacotron2
- speechbrain
license: "apache-2.0"
datasets:
- LJSpeech
metrics:
- mos
---

<iframe src="https://ghbtns.com/github-btn.html?user=speechbrain&repo=speechbrain&type=star&count=true&size=large&v=2" frameborder="0" scrolling="0" width="170" height="30" title="GitHub"></iframe>
<br/><br/>


# Text-to-Speech (TTS) with Tacotron2 trained on LJSpeech

This repository provides all the necessary tools for Text-to-Speech (TTS)  with SpeechBrain using a [Tacotron2](https://arxiv.org/abs/1712.05884) pretrained on [LJSpeech](https://keithito.com/LJ-Speech-Dataset/).

The pre-trained model takes in input a short text and produces a spectrogram in output. One can get the final waveform by applying a vocoder (e.g., HiFIGAN) on top of the generated spectrogram.


## Install SpeechBrain

```
pip install speechbrain
```

Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Perform Text-to-Speech (TTS)

```
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")

# Running the TTS
mel_output, mel_length, alignment = tacotron2.encode_text("Mary had a little lamb")

# Running Vocoder (spectrogram-to-waveform)
waveforms = hifi_gan.decode_batch(mel_output)

# Save the waverform
torchaudio.save('example_TTS.wav',waveforms.squeeze(1), 22050)
```

If you want to generate multiple sentences in one-shot, you can do in this way:

```
from speechbrain.pretrained import Tacotron2
tacotron2 = Tacotron2.from_hparams(source="speechbrain/TTS_Tacotron2", savedir="tmpdir")
items = [
       "A quick brown fox jumped over the lazy dog",
       "How much wood would a woodchuck chuck?",
       "Never odd or even"
     ]
mel_outputs, mel_lengths, alignments = tacotron2.encode_batch(items)

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
3. Run Training:
```bash
cd recipes/LJSpeech/TTS/tacotron2/
python train.py --device=cuda:0 --max_grad_norm=1.0 --data_folder=/your_folder/LJSpeech-1.1 hparams/train.yaml
```
You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/1PKju-_Nal3DQqd-n0PsaHK-bVIOlbf26?usp=sharing).

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
