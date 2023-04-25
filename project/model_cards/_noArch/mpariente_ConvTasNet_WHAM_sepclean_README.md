---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- wham
- sep_clean
license: cc-by-sa-4.0
widget:
- example_title: Librispeech sample 1
  src: https://cdn-media.huggingface.co/speech_samples/sample1.flac
---

## Asteroid model `mpariente/ConvTasNet_WHAM_sepclean`
Imported from [Zenodo](https://zenodo.org/record/3862942)

### Description:
This model was trained by Manuel Pariente 
using the wham/ConvTasNet recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `sep_clean` task of the WHAM! dataset.

### Training config:
```yaml
data:
    n_src: 2
    mode: min
    nondefault_nsrc: None
    sample_rate: 8000
    segment: 3
    task: sep_clean
    train_dir: data/wav8k/min/tr/
    valid_dir: data/wav8k/min/cv/
filterbank:
    kernel_size: 16
    n_filters: 512
    stride: 8
main_args:
    exp_dir: exp/wham
    gpus: -1
    help: None
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
positional arguments:
training:
    batch_size: 24
    early_stop: True
    epochs: 200
    half_lr: True
    num_workers: 4
```

### Results:
```yaml
si_sdr: 16.21326632846293
si_sdr_imp: 16.21441705664987
sdr: 16.615180021738933
sdr_imp: 16.464137807433435
sir: 26.860503975131923
sir_imp: 26.709461760826414
sar: 17.18312813480803
sar_imp: -131.99332048277296
stoi: 0.9619940905157323
stoi_imp: 0.2239480672473015
```

### License notice:
This work "ConvTasNet_WHAM!_sepclean" is a derivative of [CSR-I (WSJ0) Complete](https://catalog.ldc.upenn.edu/LDC93S6A)
by [LDC](https://www.ldc.upenn.edu/), used under [LDC User Agreement for 
Non-Members](https://catalog.ldc.upenn.edu/license/ldc-non-members-agreement.pdf) (Research only). 
"ConvTasNet_WHAM!_sepclean" is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
by Manuel Pariente.