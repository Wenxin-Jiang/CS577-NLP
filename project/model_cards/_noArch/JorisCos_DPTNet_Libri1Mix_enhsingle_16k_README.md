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

## Asteroid model `JorisCos/DPTNet_Libri1Mix_enhsignle_16k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `enh_single` task of the Libri1Mix  dataset.

Training config:

```yml
data:
  n_src: 1
  sample_rate: 16000
  segment: 3
  task: enh_single
  train_dir: data/wav16k/min/train-360
  valid_dir: data/wav16k/min/dev
filterbank:
  kernel_size: 16
  n_filters: 64
  stride: 8
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
scheduler:
  d_model: 64
  steps_per_epoch: 10000
training:
  batch_size: 4
  early_stop: true
  epochs: 200
  gradient_clipping: 5
  half_lr: true
  num_workers: 4
```
  

Results:

On Libri1Mix min test set :
```yml
si_sdr: 14.829670037349064
si_sdr_imp: 11.379888731489366
sdr: 15.395712644737149
sdr_imp: 11.893049845524112
sir: Infinity
sir_imp: NaN
sar: 15.395712644737149
sar_imp: 11.893049845524112
stoi: 0.9301948391058859
stoi_imp: 0.13427501556534832
```


License notice:

This work "DPTNet_Libri1Mix_enhsignle_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"DPTNet_Libri1Mix_enhsignle_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino