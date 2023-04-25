---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- Libri2Mix
- sep_clean
license: cc-by-sa-4.0
---

## Asteroid model `JorisCos/ConvTasNet_Libri2Mix_sepclean_16k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid). 
It was trained on the `sep_clean` task of the Libri2Mix dataset.

Training config:
```yaml
data:
    n_src: 2
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


Results :

On Libri2Mix min test set :
```yaml
si_sdr: 15.243671356901526
si_sdr_imp: 15.243034178473609
sdr: 15.668108919568112
sdr_imp: 15.578229918028036
sir: 25.295100756629957
sir_imp: 25.205219921301754
sar: 16.307682590197313
sar_imp: -51.64989963759405
stoi: 0.9394951175291422
stoi_imp: 0.22640192740016568
```

License notice:

This work "ConvTasNet_Libri2Mix_sepclean_16k" 
is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "ConvTasNet_Libri2Mix_sepclean_16k" 
is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Cosentino Joris.