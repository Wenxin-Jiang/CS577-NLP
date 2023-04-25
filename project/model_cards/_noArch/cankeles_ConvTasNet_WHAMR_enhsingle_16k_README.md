---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- Libri1Mix
- enh_single
license: cc-by-sa-4.0
---
## Asteroid model `cankeles/ConvTasNet_WHAMR_enhsingle_16k`

Description:

This model was fine tuned on a modified version of WHAMR! where the speakers were taken from audiobook recordings and reverb was added by Pedalboard, Spotify.

The initial model was taken from here: https://huggingface.co/JorisCos/ConvTasNet_Libri1Mix_enhsingle_16k

This model was trained by M. Can Keles using the WHAM recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `enh_single` task of the WHAM dataset.

Training config:

```yml
data:
  mode: min
  nondefault_nsrc: null
  sample_rate: 16000
  task: enh_single
  train_dir: wav16k/min/tr/
  valid_dir: wav16k/min/cv/
filterbank:
  kernel_size: 16
  n_filters: 512
  stride: 8
main_args:
  exp_dir: exp/tmp
  help: null
masknet:
  bn_chan: 128
  hid_chan: 512
  mask_act: relu
  n_blocks: 8
  n_repeats: 3
  n_src: 1
  skip_chan: 128
optim:
  lr: 0.001
  optimizer: adam
  weight_decay: 0.0
positional arguments: {}
training:
  batch_size: 2
  early_stop: true
  epochs: 10
  half_lr: true
  num_workers: 4
```
  

Results:
```
 'sar': 13.612368475881558,
 'sar_imp': 9.709316571584433,
 'sdr': 13.612368475881558,
 'sdr_imp': 9.709316571584433,
 'si_sdr': 12.978640274976373,
 'si_sdr_imp': 9.161273840297232,
 'sir': inf,
 'sir_imp': nan,
 'stoi': 0.9214516928197306,
 'stoi_imp': 0.11657488247668318

```

