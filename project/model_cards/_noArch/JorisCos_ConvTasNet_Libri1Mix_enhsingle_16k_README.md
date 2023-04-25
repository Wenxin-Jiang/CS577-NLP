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

## Asteroid model `JorisCos/ConvTasNet_Libri1Mix_enhsignle_16k`

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
  kernel_size: 32
  n_filters: 512
  stride: 16
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
training:
  batch_size: 6
  early_stop: true
  epochs: 200
  half_lr: true
  num_workers: 4

```
  

Results:

On Libri1Mix min test set :
```yml
si_sdr: 14.743051006476085
si_sdr_imp: 11.293269700616385
sdr: 15.300522933671061
sdr_imp: 11.797860134458015
sir: Infinity
sir_imp: NaN
sar: 15.300522933671061
sar_imp: 11.797860134458015
stoi: 0.9310514162434267
stoi_imp: 0.13513159270288563
```


License notice:

This work "ConvTasNet_Libri1Mix_enhsignle_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"ConvTasNet_Libri1Mix_enhsignle_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino