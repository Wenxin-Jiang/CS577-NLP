---
language: "sw"
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

This repository provides all the necessary tools for using a [ALLFA Public](https://github.com/getalp/ALFFA_PUBLIC/tree/master/ASR/SWAHILI). 

The pre-trained model takes in input a spectrogram and produces a waveform in output. Typically, a vocoder is used after a TTS model that converts an input text into a spectrogram.


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
hifi_gan = HIFIGAN.from_hparams(source="aioxlabs/hifigan-swahili", savedir="tmpdir")
mel_specs = torch.rand(2, 80,298)
waveforms = hifi_gan.decode_batch(mel_specs)
```
### Using the Vocoder with the TTS
```python
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="aioxlabs/tacotron-swahili", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="aioxlabs/hifigan-swahili", savedir="tmpdir_vocoder")

# Running the TTS
mel_output, mel_length, alignment = tacotron2.encode_text("raisi wa jumhuri ya tanzania")

# Running Vocoder (spectrogram-to-waveform)
waveforms = hifi_gan.decode_batch(mel_output)

# Save the waverform
torchaudio.save('example_TTS.wav',waveforms.squeeze(1), 16000)
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