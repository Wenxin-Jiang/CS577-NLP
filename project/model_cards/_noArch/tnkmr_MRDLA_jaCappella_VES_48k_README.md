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

# MRDLA trained with the jaCappella corpus for vocal ensemble separation

This model was trained by Tomohiko Nakamura using [the codebase](https://github.com/TomohikoNakamura/asteroid_jaCappella)).
It was trained on the vocal ensemble separation task of [the jaCappella dataset](https://tomohikonakamura.github.io/jaCappella_corpus/).

# License
See [the jaCappella dataset page](https://tomohikonakamura.github.io/jaCappella_corpus/).

# Citation
See [the jaCappella dataset page](https://tomohikonakamura.github.io/jaCappella_corpus/).

For MRDLA, please cite the following paper.
```
@article{TNakamura202104IEEEACMTASLP,
 author={Nakamura, Tomohiko and Kozuka, Shihori and Saruwatari, Hiroshi},
 journal = {IEEE/ACM Transactions on Audio, Speech, and Language Processing},
 title = {Time-domain audio source separation with neural networks based on multiresolution analysis},
 year=2021,
 doi={10.1109/TASLP.2021.3072496},
 month=apr,
 volume=29,
 pages={1687--1701},
}
```

# Configuration

```yaml
data:
  in_memory: true
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
loss_func:
  lambda_t: 10.0
  lambda_f: 1.0
  band: high
model:
  C_dec: 64
  C_enc: 64
  C_mid: 768
  L: 12
  activation: GELU
  context: false
  f_dec: 21
  f_enc: 21
  input_length: 288000
  padding_type: reflect
  signal_ch: 1
  wavelet: haar
optim:
  lr: 0.0001
  lr_decay_gamma: 0.3
  lr_decay_patience: 50
  optimizer: adam
  patience: 1000
  weight_decay: 0.0
training:
  batch_size: 16
  epochs: 1000
```

# Results (SI-SDR [dB]) on vocal ensemble separation

|     Method      |   Lead vocal   |    Soprano     |      Alto      |     Tenor      |      Bass      |Vocal percussion|
|:---------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|:--------------:|
|     MRDLA       |       8.7      |      11.8      |      14.7      |      11.3      |      10.2      |      22.1      |
