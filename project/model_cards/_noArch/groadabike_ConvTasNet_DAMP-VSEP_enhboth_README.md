---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- DAMP-VSEP
license: cc-by-sa-4.0
---

## Asteroid model `groadabike/ConvTasNet_DAMP-VSEP_enhboth`
Imported from [Zenodo](https://zenodo.org/record/3994193)

### Description:
This model was trained by Gerardo Roa Dabike using Asteroid. It was trained on the enh_both task of the DAMP-VSEP dataset.

### Training config:
```yaml
data:
    channels: 1
    n_src: 2
    root_path: data
    sample_rate: 16000
    samples_per_track: 10
    segment: 3.0
    task: enh_both
filterbank:
    kernel_size: 20
    n_filters: 256
    stride: 10
main_args:
    exp_dir: exp/train_convtasnet
    help: None
masknet:
    bn_chan: 256
    conv_kernel_size: 3
    hid_chan: 512
    mask_act: relu
    n_blocks: 8
    n_repeats: 4
    n_src: 2
    norm_type: gLN
    skip_chan: 256
optim:
    lr: 0.0003
    optimizer: adam
    weight_decay: 0.0
positional arguments:
training:
   batch_size: 12
    early_stop: True
    epochs: 50
    half_lr: True
    num_workers: 12
```

### Results:
```yaml
si_sdr: 14.018196157142519
si_sdr_imp: 14.017103133809577
sdr: 14.498517291333885
sdr_imp: 14.463389151567865
sir: 24.149634529133372
sir_imp: 24.11450638936735
sar: 15.338597389045935
sar_imp: -137.30634122401517
stoi: 0.7639416744417206
stoi_imp: 0.1843383526963759
```

### License notice:
This work "ConvTasNet_DAMP-VSEP_enhboth" is a derivative of DAMP-VSEP: Smule Digital Archive of Mobile Performances - Vocal Separation (Version 1.0.1) by Smule, Inc, used under Smule's Research Data License Agreement (Research only). "ConvTasNet_DAMP-VSEP_enhboth" is licensed under Attribution-ShareAlike 3.0 Unported by Gerardo Roa Dabike.
