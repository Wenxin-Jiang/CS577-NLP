---
language: "lg"
tags:
- text-to-speech
- TTS
- speech-synthesis
- Tacotron2
- speechbrain
license: "apache-2.0"
datasets:
- SALT-TTS
metrics:
- mos
---

# Sunbird AI Text-to-Speech (TTS) model trained on Luganda text 

### Text-to-Speech (TTS) with Tacotron2 trained on Professional Studio Recordings

This repository provides all the necessary tools for Text-to-Speech (TTS)  with SpeechBrain.

The pre-trained model takes in input a short text and produces a spectrogram in output. One can get the final waveform by applying a vocoder (e.g., HiFIGAN) on top of the generated spectrogram.


### Install SpeechBrain

```
pip install speechbrain
```


### Perform Text-to-Speech (TTS)

```
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="/Sunbird/sunbird-lug-tts", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")

# Running the TTS
mel_output, mel_length, alignment = tacotron2.encode_text("Mbagaliza Christmass Enungi Nomwaka Omugya Gubaberere Gwamirembe")

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
       "Nsanyuse okukulaba",
       "Erinnya lyo ggwe ani?",
       "Mbagaliza Christmass Enungi Nomwaka Omugya Gubaberere Gwamirembe"
     ]
mel_outputs, mel_lengths, alignments = tacotron2.encode_batch(items)

```

### Inference on GPU
To perform inference on the GPU, add  `run_opts={"device":"cuda"}`  when calling the `from_hparams` method.