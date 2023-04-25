---
tags:
- asteroid
- audio
- DPTNet
- audio-to-audio
datasets:
- Libri1Mix
- enh_single
license: cc-by-sa-4.0
---
## Asteroid model `cankeles/DPTNet_WHAMR_enhsignle_16k`

Description:

This model was trained by M. Can Keleş using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `enh_single` task of the Libri1Mix  dataset.

Training config:

```yml
data:
  mode: min
  nondefault_nsrc: null
  sample_rate: 16000
  segment: 2.0
  task: enh_single
  train_dir: wav16k/min/tr/
  valid_dir: wav16k/min/cv/
filterbank:
  kernel_size: 16
  n_filters: 64
  stride: 8
main_args:
  exp_dir: exp/tmp
  help: null
masknet:
  bidirectional: true
  chunk_size: 100
  dropout: 0
  ff_activation: relu
  ff_hid: 256
  hop_size: 50
  in_chan: 64
  mask_act: sigmoid
  n_repeats: 2
  n_src: 1
  norm_type: gLN
  out_chan: 64
optim:
  lr: 0.001
  optimizer: adam
  weight_decay: 1.0e-05
positional arguments: {}
scheduler:
  d_model: 64
  steps_per_epoch: 10000
training:
  batch_size: 4
  early_stop: true
  epochs: 60
  gradient_clipping: 5
  half_lr: true
  num_workers: 4
```
  

Results:

On custom min test set :
```yml
'sar': 12.853384266251018,
 'sar_imp': 8.950332361953906,
 'sdr': 12.853384266251018,
 'sdr_imp': 8.950332361953906,
 'si_sdr': 12.247012621312548,
 'si_sdr_imp': 8.429646186633407,
 'sir': inf,
 'sir_imp': nan,
 'stoi': 0.9022338865380519,
 'stoi_imp': 0.09735707619500522
 ```
