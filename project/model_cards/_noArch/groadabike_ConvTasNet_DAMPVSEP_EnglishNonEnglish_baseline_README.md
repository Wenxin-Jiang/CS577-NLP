---
tags:
- asteroid
- audio
- ConvTasNet
- audio-to-audio
datasets:
- DAMP-VSEP
- Singing/Accompaniment Separation
license: cc-by-sa-4.0
---


## Description:
This model was trained by Gerardo Roa using the dampvsep recipe in Asteroid.
It was trained on the `singing/accompaniment` task of the `DAMP-VSEP` dataset.


## Training config:
```yaml
data:
  channels: 1
  emb_model: 'no'
  metadata_path: metadata
  mixture: remix
  root_path: /fastdata/acp13gr/DAMP/DAMP-VSEP
  sample_rate: 16000
  train_set: english_nonenglish
filterbank:
  kernel_size: 20
  n_filters: 256
  stride: 10
main_args:
  exp_dir: exp/train_convtasnet_remix-no-0.0-english_nonenglish-0.0005-jade
  help: null
masknet:
  bn_chan: 256
  conv_kernel_size: 3
  hid_chan: 512
  mask_act: relu
  n_blocks: 10
  n_repeats: 4
  n_src: 2
  norm_type: gLN
  skip_chan: 256
optim:
  lr: 0.0005
  optimizer: adam
  weight_decay: 0.0
positional arguments: {}
training:
  batch_size: 7
  early_stop: true
  epochs: 50
  half_lr: true
  loss_alpha: 0.0
  num_workers: 10
```


## Results:
```yaml
"si_sdr": 15.111802516750586,
"si_sdr_imp": 15.178209807687663,
"si_sdr_s0": 12.160261214703553,
"si_sdr_s0_imp": 17.434593619085675,
"si_sdr_s1": 18.063343818797623,
"si_sdr_s1_imp": 12.92182599628965,
"sdr": 15.959722569460281,
"sdr_imp": 14.927002467087567,
"sdr_s0": 13.270412028426595,
"sdr_s0_imp": 16.45867572657551,
"sdr_s1": 18.64903311049397,
"sdr_s1_imp": 13.39532920759962,
"sir": 23.935932341084754,
"sir_imp": 22.903212238712012,
"sir_s0": 22.30777879911744,
"sir_s0_imp": 25.49604249726635,
"sir_s1": 25.56408588305207,
"sir_s1_imp": 20.310381980157665,
"sar": 17.174899162445882,
"sar_imp": -134.47377304178818,
"sar_s0": 14.268071153965913,
"sar_s0_imp": -137.38060105026818,
"sar_s1": 20.081727170925856,
"sar_s1_imp": -131.56694503330817,
"stoi": 0.7746496376326059,
"stoi_imp": 0.19613735629114643,
"stoi_s0": 0.6611376621212413,
"stoi_s0_imp": 0.21162695175464794,
"stoi_s1": 0.8881616131439705,
"stoi_s1_imp": 0.1806477608276449
```


## License notice:

** This is important, please fill it, if you need help, you can ask on Asteroid's slack.**

This work "ConvTasNet_DAMPVSEP_EnglishNonEnglish_baseline"
is a derivative of [DAMP-VSEP corpus](https://zenodo.org/record/3553059) by
[Smule, Inc](https://www.smule.com/),
used under [Restricted License](https://zenodo.org/record/3553059)(Research only).
"ConvTasNet_DAMPVSEP_EnglishNonEnglish_baseline"
is licensed under [Attribution-ShareAlike 3.0 Unported](https://creativecommons.org/licenses/by-sa/3.0/)
by Gerardo Roa.
