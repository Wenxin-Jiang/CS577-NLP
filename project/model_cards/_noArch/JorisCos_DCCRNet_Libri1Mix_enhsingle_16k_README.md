---
tags:
- asteroid
- audio
- DCCRNet
- audio-to-audio
- speech-enhancement
datasets:
- Libri1Mix
- enh_single
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/DCCRNet_Libri1Mix_enhsignle_16k`

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
  stft_kernel_size: 400
  stft_n_filters: 512
  stft_stride: 100
masknet:
  architecture: DCCRN-CL
  n_src: 1
optim:
  lr: 0.001
  optimizer: adam
  weight_decay: 1.0e-05
training:
  batch_size: 12
  early_stop: true
  epochs: 200
  gradient_clipping: 5
  half_lr: true
  num_workers: 4
```
  

Results:

On Libri1Mix min test set :
```yml
si_sdr: 13.329767398333798
si_sdr_imp: 9.879986092474098
sdr: 13.87279932997016
sdr_imp: 10.370136530757103
sir: Infinity
sir_imp: NaN
sar: 13.87279932997016
sar_imp: 10.370136530757103
stoi: 0.9140907015623948
stoi_imp: 0.11817087802185405
```


License notice:

This work "DCCRNet_Libri1Mix_enhsignle_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"DCCRNet_Libri1Mix_enhsignle_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino