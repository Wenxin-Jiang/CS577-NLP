---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- libri1mix
- enh_single
license: cc-by-sa-4.0
---

## Asteroid model `mhu-coder/ConvTasNet_Libri1Mix_enhsingle`
Imported from [Zenodo](https://zenodo.org/record/4301955#.X9cj98Jw0bY)

### Description:
This model was trained by Mathieu Hu using the librimix/ConvTasNet recipe in
[Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `enh_single` task of the Libri1Mix dataset. 

### Training config:
```yaml
data:
    n_src: 1
    sample_rate: 16000
    segment: 3
    task: enh_single
    train_dir: data/wav16k/min/train-100
    valid_dir: data/wav16k/min/dev
filterbank:
    kernel_size: 16
    n_filters: 512
    stride: 8
main_args:
    exp_dir: exp/train_convtasnet_f34664b9
    help: None
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
positional arguments:
training:
    batch_size: 2
    early_stop: True
    epochs: 200
    half_lr: True
    num_workers: 4
```

### Results:
```yaml
si_sdr: 13.938355526049932
si_sdr_imp: 10.488574220190232
sdr: 14.567380104207393
sdr_imp: 11.064717304994337
sir: inf
sir_imp: nan
sar: 14.567380104207393
sar_imp: 11.064717304994337
stoi: 0.9201010933251715
stoi_imp: 0.1241812697846321 
```

### License notice:
This work "ConvTasNet_Libri1Mx_enhsingle" is a derivative of [CSR-I (WSJ0) Complete](https://catalog.ldc.upenn.edu/LDC93S6A)
by [LDC](https://www.ldc.upenn.edu/), used under [LDC User Agreement for 
Non-Members](https://catalog.ldc.upenn.edu/license/ldc-non-members-agreement.pdf) (Research only). 
"ConvTasNet_Libri1Mix_enhsingle" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
by Mathieu Hu.
