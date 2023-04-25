---
tags:
- asteroid
- audio
- DPRNNTasNet
- audio-to-audio
datasets:
- Libri1Mix
- enh_single
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/DPRNNTasNet_Libri1Mix_enhsignle_16k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `enh_single` task of the Libri1Mix  dataset.

Training config:

```yml
data:
  n_src: 1
  sample_rate: 16000
  segment: 1
  task: enh_single
  train_dir: data/wav16k/min/train-360
  valid_dir: data/wav16k/min/dev
filterbank:
  kernel_size: 2
  n_filters: 64
  stride: 1
masknet:
  bidirectional: true
  bn_chan: 128
  chunk_size: 250
  dropout: 0
  hid_size: 128
  hop_size: 125
  in_chan: 64
  mask_act: sigmoid
  n_repeats: 6
  n_src: 1
  out_chan: 64
optim:
  lr: 0.001
  optimizer: adam
  weight_decay: 1.0e-05
training:
  batch_size: 2
  early_stop: true
  epochs: 200
  gradient_clipping: 5
  half_lr: true
  num_workers: 4
```
  

Results:

On Libri1Mix min test set :
```yml
si_sdr: 14.7228101708889
si_sdr_imp: 11.2730288650292
sdr: 15.35661405197161
sdr_imp: 11.853951252758595
sir: Infinity
sir_imp: NaN
sar: 15.35661405197161
sar_imp: 11.853951252758595
stoi: 0.9300461826351578
stoi_imp: 0.13412635909461715
```


License notice:

This work "DPRNNTasNet_Libri1Mix_enhsignle_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"DPRNNTasNet_Libri1Mix_enhsignle_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino