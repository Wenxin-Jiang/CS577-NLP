---
language: "de"
tags:
- text-to-speech
- TTS
- speech-synthesis
- Tacotron2
- speechbrain
license: "apache-2.0"
---

Text-to-Speech (TTS) with Tacotron2 trained on a custom german dataset with 12 days voice using speechbrain.

Trained for 39 epochs (english speechbrain models are trained for 750 epochs) so there is room for improvement and the model is most likely to be updated soon. The hifigan vocoder can fortunately be used language-independently.

## How to use
Install speechbrain.

```
pip install speechbrain
```

Generate spectrogram (line 17) and generate wav using hifigan (line 18).

```
import torchaudio
from speechbrain.pretrained import Tacotron2
from speechbrain.pretrained import HIFIGAN

# Intialize TTS (tacotron2) and Vocoder (HiFIGAN)
tacotron2 = Tacotron2.from_hparams(source="padmalcom/tts-tacotron2-german", savedir="tmpdir_tts")
hifi_gan = HIFIGAN.from_hparams(source="speechbrain/tts-hifigan-ljspeech", savedir="tmpdir_vocoder")

# Running the TTS
mel_output, mel_length, alignment = tacotron2.encode_text("Die Sonne schien den ganzen Tag.")

# Running Vocoder (spectrogram-to-waveform)
waveforms = hifi_gan.decode_batch(mel_output)

# Save the waverform
torchaudio.save('example_TTS.wav',waveforms.squeeze(1), 22050)
```