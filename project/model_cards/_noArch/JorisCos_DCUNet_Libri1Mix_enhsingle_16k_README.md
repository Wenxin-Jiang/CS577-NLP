---
tags:
- asteroid
- audio
- DCUNet
- audio-to-audio
datasets:
- Libri1Mix
- enh_single
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/DCUNet_Libri1Mix_enhsignle_16k`

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
  stft_n_filters: 1024
  stft_kernel_size: 1024
  stft_stride: 256
masknet:
  architecture: Large-DCUNet-20
  fix_length_mode: pad
  n_src: 1
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
si_sdr: 13.154035391645971
si_sdr_imp: 9.704254085786271
sdr: 13.568058873121435
sdr_imp: 10.065396073908367
sar: 13.568058873121435
sar_imp: 10.065396073908367
stoi: 0.9199373340235417
stoi_imp: 0.12401751048300132
```


License notice:

This work "DCUNet_Libri1Mix_enhsignle_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"DCUNet_Libri1Mix_enhsignle_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino