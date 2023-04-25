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

## Asteroid model `JorisCos/ConvTasNet_Libri3Mix_sepclean_8k`

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid). 
It was trained on the `sep_clean` task of the Libri3Mix dataset.

Training config:
```yml
data:
    n_src: 3
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
    n_src: 3
    skip_chan: 128
optim:
    lr: 0.001
    optimizer: adam
    weight_decay: 0.0
training:
  batch_size: 24
  early_stop: true
  epochs: 200
  half_lr: true
  num_workers: 4
```

Results :

On Libri3Mix min test set :
```yaml
si_sdr: 8.581797049575108
si_sdr_imp: 11.977037288467368
sdr' 9.305885208641385
sdr_imp: 12.3943409734845
sir: 16.42030534048559
sir_imp: 19.508759460400984
sar: 10.641943911079238
sar_imp: -56.4345187842095
stoi: 0.8365148408724333
stoi_imp: 0.24401766199806396
```

License notice:

This work "ConvTasNet_Libri3Mix_sepclean_8k" 
is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). "ConvTasNet_Libri3Mix_sepclean_8k" 
is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Cosentino Joris.