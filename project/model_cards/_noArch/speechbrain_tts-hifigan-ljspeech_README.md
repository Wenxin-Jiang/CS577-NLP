---
language: "en"
inference: false
tags:
- Vocoder
- HiFIGAN
- text-to-speech
- TTS
- speech-synthesis
- speechbrain
license: "apache-2.0"
datasets:
- LJSpeech
---

# Vocoder with HiFIGAN trained on LJSpeech

This repository provides all the necessary tools for using a [HiFIGAN](https://arxiv.org/abs/2010.05646) vocoder trained with [LJSpeech](https://keithito.com/LJ-Speech-Dataset/). 

The pre-trained model takes in input a spectrogram and produces a waveform in output. Typically, a vocoder is used after a TTS model that converts an input text into a spectrogram.

The sampling frequency is 22050 Hz.


## Install SpeechBrain

```bash
pip install speechbrain
```


Please notice that we encourage you to read our tutorials and learn more about
[SpeechBrain](https://speechbrain.github.io).

### Using the Vocoder

```python
import torch
from speechbrain.pretrained import HIFIGAN
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir")
mel_specs = torch.rand(2, 80,298)
waveforms = hifi_gan.decode_batch(mel_specs)
```
### Using the Vocoder with the TTS
```python
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
cd recipes/LJSpeech/TTS/vocoder/hifi_gan/
python train.py hparams/train.yaml --data_folder /path/to/LJspeech
```
You can find our training results (models, logs, etc) [here](https://drive.google.com/drive/folders/19sLwV7nAsnUuLkoTu5vafURA9Fo2WZgG?usp=sharing).