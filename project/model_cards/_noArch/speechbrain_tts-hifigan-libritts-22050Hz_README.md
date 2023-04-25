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
- LibriTTS
---

# Vocoder with HiFIGAN trained on LibriTTS

This repository provides all the necessary tools for using a [HiFIGAN](https://arxiv.org/abs/2010.05646) vocoder trained with [LibriTTS](https://www.openslr.org/60/) (with multiple speakers). The sample rate used for the vocoder is 22050 Hz.

The pre-trained model takes in input a spectrogram and produces a waveform in output. Typically, a vocoder is used after a TTS model that converts an input text into a spectrogram.

Alternatives to this models are the following:
- [tts-hifigan-libritts-16kHz](https://huggingface.co/speechbrain/tts-hifigan-libritts-16kHz/) (same model trained on the same dataset, but for a sample rate of 16000 Hz)
- [tts-hifigan-ljspeech](https://huggingface.co/speechbrain/tts-hifigan-ljspeech)  (same model trained on LJSpeech for a sample rate of 22050 Hz).

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
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-libritts-22050Hz", savedir="tmpdir")
mel_specs = torch.rand(2, 80,298)

# Running Vocoder (spectrogram-to-waveform)
waveforms = hifi_gan.decode_batch(mel_specs)
```

### Using the Vocoder with the TTS
```python
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="speechbrain/tts-tacotron2-ljspeech", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-libritts-22050Hz", savedir="tmpdir_vocoder")

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
cd recipes/LibriTTS/vocoder/hifigan/
python train.py hparams/train.yaml --data_folder=/path/to/LibriTTS_data_destination --sample_rate=22050
```

To change the sample rate for model training go to the `"recipes/LibriTTS/vocoder/hifigan/hparams/train.yaml"` file and change the value for `sample_rate` as required.
The training logs and checkpoints are available [here](https://drive.google.com/drive/folders/1cImFzEonNYhetS9tmH9R_d0EFXXN0zpn?usp=sharing).