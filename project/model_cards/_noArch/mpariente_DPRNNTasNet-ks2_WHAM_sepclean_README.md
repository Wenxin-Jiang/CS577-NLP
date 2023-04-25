---
tags:
- asteroid
- audio
- DPRNNTasNet
- audio-to-audio
datasets:
- wham
- sep_clean
license: cc-by-sa-4.0
---

## Asteroid model `mpariente/DPRNNTasNet-ks2_WHAM_sepclean`
Imported from [Zenodo](https://zenodo.org/record/3862942)

### Description:
This model was trained by Manuel Pariente 
using the wham/DPRNN recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `sep_clean` task of the WHAM! dataset.

### Training config:
```yaml
data:
    mode: min
    nondefault_nsrc: None
    sample_rate: 8000
    segment: 2.0
    task: sep_clean
    train_dir: data/wav8k/min/tr
    valid_dir: data/wav8k/min/cv
filterbank:
    kernel_size: 2
    n_filters: 64
    stride: 1
main_args:
    exp_dir: exp/train_dprnn_new/
    gpus: -1
    help: None
masknet:
    bidirectional: True
    bn_chan: 128
    chunk_size: 250
    dropout: 0
    hid_size: 128
    hop_size: 125
    in_chan: 64
    mask_act: sigmoid
    n_repeats: 6
    n_src: 2
    out_chan: 64
optim:
    lr: 0.001
    optimizer: adam
    weight_decay: 1e-05
positional arguments:
training:
    batch_size: 3
    early_stop: True
    epochs: 200
    gradient_clipping: 5
    half_lr: True
    num_workers: 8
```

### Results:
```yaml
si_sdr: 19.316743490695334
si_sdr_imp: 19.317895273889842
sdr: 19.68085347190952
sdr_imp: 19.5298092932871
sir: 30.362213998701232
sir_imp: 30.21116982007881
sar: 20.15553251343315
sar_imp: -129.02091762351188
stoi: 0.97772664309074
stoi_imp: 0.23968091518217424
```

### License notice:
This work "DPRNNTasNet-ks2_WHAM_sepclean" is a derivative of [CSR-I (WSJ0) Complete](https://catalog.ldc.upenn.edu/LDC93S6A)
by [LDC](https://www.ldc.upenn.edu/), used under [LDC User Agreement for 
Non-Members](https://catalog.ldc.upenn.edu/license/ldc-non-members-agreement.pdf) (Research only). 
"DPRNNTasNet-ks2_WHAM_sepclean" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
by Manuel Pariente.
