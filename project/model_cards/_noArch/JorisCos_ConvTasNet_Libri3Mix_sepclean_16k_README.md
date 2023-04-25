---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- Libri3Mix
- sep_clean
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/ConvTasNet_Libri3Mix_sepclean_16k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid). 
It was trained on the `sep_clean` task of the Libri3Mix dataset.

Training config:
```yaml
data:
    n_src: 3
    sample_rate: 16000
    segment: 3
    task: sep_clean
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


Results :

On Libri3Mix min test set :
```yaml
si_sdr: 8.932601610824145
si_sdr_imp: 12.299341066588594
sdr: 9.557260814240447
sdr_imp: 12.76957128385349
sir: 17.387646884037455
sir_imp: 20.599955591768484
sar: 10.686885056960504
sar_imp: -55.8894643263213
stoi: 0.8481258332025354
stoi_imp: 0.25528367853750356
```

License notice:

This work "ConvTasNet_Libri3Mix_sepclean_16k" 
is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "ConvTasNet_Libri3Mix_sepclean_16k" 
is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Cosentino Joris.