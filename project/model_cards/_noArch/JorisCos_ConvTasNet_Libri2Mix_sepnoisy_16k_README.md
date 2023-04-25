---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- Libri2Mix
- sep_noisy
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/ConvTasNet_Libri2Mix_sepnoisy_16k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `sep_noisy` task of the Libri2Mix dataset.

Training config:

```yml
data:
    n_src: 2
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
    n_src: 2
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


On Libri2Mix min test set :
```yml
si_sdr: 10.617130949793383
si_sdr_imp: 12.551811412989263
sdr: 11.231867464482065
sdr_imp: 13.059765009747343
sir: 24.461138352988346
sir_imp: 24.371856452307703
sar: 11.5649982725426
sar_imp: 4.662525705768228
stoi: 0.8701085138712695
stoi_imp: 0.2245418019822898

```


License notice:

This work "ConvTasNet_Libri2Mix_sepnoisy_16k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"ConvTasNet_Libri2Mix_sepnoisy_16k" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino