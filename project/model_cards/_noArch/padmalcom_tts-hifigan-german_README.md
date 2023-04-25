---
language: "de"
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
- custom
---

# Vocoder with HiFIGAN trained on custom German dataset

This repository provides all the necessary tools for using a [HiFIGAN](https://arxiv.org/abs/2010.05646) vocoder trained on a generated German dataset using [mp3_to_training_data](https://github.com/padmalcom/mp3_to_training_data).

The pre-trained model (8 epochs so far) takes in input a spectrogram and produces a waveform in output. Typically, a vocoder is used after a TTS model that converts an input text into a spectrogram.


## How to use

Install speechbrain.

```bash
pip install speechbrain
```

Use a TTS model (e.g. [tts-tacotron-german](https://huggingface.co/padmalcom/tts-tacotron2-german)), generate a spectrogram and convert it to audio.

```python
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

tacotron2 = Tacotron2.from_hparams(source="padmalcom/tts-tacotron2-german", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="padmalcom/tts-hifigan-german", savedir="tmpdir_vocoder")

mel_output, mel_length, alignment = tacotron2.encode_text("Mary had a little lamb")

waveforms = hifi_gan.decode_batch(mel_output)

torchaudio.save('example_TTS.wav',waveforms.squeeze(1), 22050)
```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.