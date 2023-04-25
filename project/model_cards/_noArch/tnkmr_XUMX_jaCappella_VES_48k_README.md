---
license: cc-by-nc-4.0
language:
- ja
tags:
- music
- speech
- audio
- audio-to-audio
- a cappella
datasets:
- jaCappella
metrics:
- SI-SDR
---

# X-UMX trained with the jaCappella corpus for vocal ensemble separation

This model was trained by Tomohiko Nakamura using [the codebase](https://github.com/TomohikoNakamura/asteroid_jaCappella)).
It was trained on the vocal ensemble separation task of [the jaCappella dataset](https://tomohikonakamura.github.io/jaCappella_corpus/).

# License
See [the jaCappella dataset page](https://tomohikonakamura.github.io/jaCappella_corpus/).

# Citation
See [the jaCappella dataset page](https://tomohikonakamura.github.io/jaCappella_corpus/).

# Configuration

```yaml
data:
  num_workers: 12
  sample_rate: 48000
  samples_per_track: 13
  seed: 42
  seq_dur: 6.0
  source_augmentations:
  - gain
  sources:
  - vocal_percussion
  - bass
  - alto
  - tenor
  - soprano
  - lead_vocal
model:
  bandwidth: 16000
  bidirectional: true
  hidden_size: 512
  in_chan: 4096
  nb_channels: 1
  nhop: 1024
  pretrained: null
  spec_power: 1
  window_length: 4096
optim:
  lr: 0.001
  lr_decay_gamma: 0.3
  lr_decay_patience: 80
  optimizer: adam
  patience: 1000
  weight_decay: 1.0e-05
training:
  batch_size: 16
  epochs: 1000
  loss_combine_sources: true
  loss_use_multidomain: true
  mix_coef: 10.0
  val_dur: 80.0
```

# Results (SI-SDR [dB]) on vocal ensemble separation


|     Method      |   Lead vocal   |    Soprano     |      Alto      |     Tenor      |      Bass      |Vocal percussion|
|:---------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|
|     X-UMX       |       7.5      |      10.7      |      13.5      |      10.2      |       9.1      |      21.0      |