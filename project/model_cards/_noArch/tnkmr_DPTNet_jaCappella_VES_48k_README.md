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

# DPTNet trained with the jaCappella corpus for vocal ensemble separation

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
  seq_dur: 5.046
  source_augmentations:
  - gain
  sources:
  - vocal_percussion
  - bass
  - alto
  - tenor
  - soprano
  - lead_vocal
filterbank:
  kernel_size: 32
  n_filters: 64
  stride: 16
masknet:
  bidirectional: true
  chunk_size: 174
  dropout: 0
  ff_activation: relu
  ff_hid: 256
  hop_size: 128
  in_chan: 64
  mask_act: sigmoid
  n_repeats: 8
  n_src: 6
  norm_type: gLN
  out_chan: 64
optim:
  lr: 0.005
  optimizer: adam
  weight_decay: 1.0e-05
training:
  batch_size: 1
  early_stop: true
  epochs: 600
  gradient_clipping: 5
  half_lr: true
  loss_func: pit_sisdr
```
# Results (SI-SDR [dB]) on vocal ensemble separation

|     Method      |   Lead vocal   |    Soprano     |      Alto      |     Tenor      |      Bass      |Vocal percussion|
|:---------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|
|     DPTNet      |       8.9      |       8.5      |      11.9      |      14.9      |      19.7      |      21.9      |
