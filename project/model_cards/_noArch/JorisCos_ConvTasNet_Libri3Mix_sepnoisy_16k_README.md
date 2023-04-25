---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- Libri3Mix
- sep_noisy
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/ConvTasNet_Libri3Mix_sepnoisy_16k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `sep_noisy` task of the Libri3Mix  dataset.

Training config:

```yml
data:
  n_src: 3
  sample_rate: 16000
  segment: 3
  task: sep_noisy
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
  n_src: 3
  skip_chan: 128
optim:
  lr: 0.001
  optimizer: adam
  weight_decay: 0.0
training:
  batch_size: 8
  early_stop: true
  epochs: 200
  half_lr: true
  num_workers: 4
```
  

Results:

On Libri3Mix min test set :
```yml
si_sdr: 5.926151147554517
si_sdr_imp: 10.282912158535625
sdr: 6.700975236867358
sdr_imp: 10.882972447337504
sir: 15.364110064569388
sir_imp: 18.574476587171688
sar: 7.918866830474568
sar_imp: -0.9638973409971135
stoi: 0.7713777027310713
stoi_imp: 0.2078696167973911
```


License notice:

This work "ConvTasNet_Libri3Mix_sepnoisy_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). 
"ConvTasNet_Libri3Mix_sepnoisy_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino