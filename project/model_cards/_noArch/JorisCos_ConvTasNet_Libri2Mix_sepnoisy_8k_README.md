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

## Asteroid model `JorisCos/ConvTasNet_Libri2Mix_sepnoisy_8k`
Imported from [Zenodo](https://zenodo.org/record/3874420#.X9I6NcLjJH4)

Description:

This model was trained by Joris Cosentino using the librimix recipe in [Asteroid](https://github.com/asteroid-team/asteroid).
It was trained on the `sep_noisy` task of the Libri2Mix  dataset.

Training config:

```yml
data:
    n_src: 2
    sample_rate: 8000
    segment: 3
    task: sep_noisy
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
    num_workers: 4
```
  

Results:

On Libri2Mix min test set :
```yml
si_sdr: 9.944424856077259
si_sdr_imp: 11.939395359731192
sdr: 10.701526190782072
sdr_imp: 12.481757547845662
sir: 22.633644975545575
sir_imp: 22.45666740833025
sar: 11.131644100944868
sar_imp: 4.248489589311784
stoi: 0.852048619949357
stoi_imp: 0.2071994899565506
```


License notice:

This work "ConvTasNet_Libri2Mix_sepnoisy_8k" is a derivative of [LibriSpeech ASR corpus](http://www.openslr.org/12) by Vassil Panayotov,
used under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/); of The WSJ0 Hipster Ambient Mixtures 
dataset by [Whisper.ai](http://wham.whisper.ai/), used under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/) (Research only). 
"ConvTasNet_Libri2Mix_sepnoisy_8k" is licensed under A[Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/) by Joris Cosentino