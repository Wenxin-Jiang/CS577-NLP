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
## Asteroid model `Awais/Audio_Source_Separation`
Imported from [Zenodo](https://zenodo.org/record/3873572#.X9M69cLjJH4)

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid). 
It was trained on the `sep_clean` task of the Libri2Mix dataset.

Training config:
```yaml
data:
    n_src: 2
    sample_rate: 8000
    segment: 3
    task: sep_clean
    train_dir: data/wav8k/min/train-360
    valid_dir: data/wav8k/min/dev
filterbank:
    kernel_size: 16
    n_filters: 512
    stride: 8
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
    batch_size: 24
    early_stop: True
    epochs: 200
    half_lr: True
    num_workers: 2
```


Results :

On Libri2Mix min test set :
```yaml
si_sdr: 14.764543634468069
si_sdr_imp: 14.764029375607246
sdr: 15.29337970745095
sdr_imp: 15.114146605113111
sir: 24.092904661115366
sir_imp: 23.913669683141528
sar: 16.06055906916849
sar_imp: -51.980784441287454
stoi: 0.9311142440593033
stoi_imp: 0.21817376142710482
```

License notice:

This work "ConvTasNet_Libri2Mix_sepclean_8k" 
is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "ConvTasNet_Libri2Mix_sepclean_8k" 
is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Cosentino Joris.
