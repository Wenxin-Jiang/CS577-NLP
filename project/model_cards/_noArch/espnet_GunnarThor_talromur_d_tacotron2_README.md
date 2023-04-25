---
tags:
- espnet
- audio
- text-to-speech
language: en
datasets:
- talromur
license: cc-by-4.0
---

## ESPnet2 TTS model 

### `espnet/GunnarThor_talromur_d_tacotron2`

This model was trained by Gunnar Thor using talromur recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout 49a284e69308d81c142b89795de255b4ce290c54
pip install -e .
cd egs2/talromur/tts1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/GunnarThor_talromur_d_tacotron2
```



## TTS config

<details><summary>expand</summary>

```
config: ./conf/tuning/train_tacotron2.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/d/tts_train_tacotron2_raw_phn_none
ngpu: 1
seed: 0
num_workers: 1
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: 2
dist_rank: 0
local_rank: 0
dist_master_addr: localhost
dist_master_port: 41629
dist_launcher: null
multiprocessing_distributed: true
unused_parameters: false
sharded_ddp: false
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
collect_stats: false
write_collected_feats: false
max_epoch: 100
patience: null
val_scheduler_criterion:
- valid
- loss
early_stopping_criterion:
- valid
- loss
- min
best_model_criterion:
-   - valid
    - loss
    - min
-   - train
    - loss
    - min
keep_nbest_models: 5
nbest_averaging_interval: 0
grad_clip: 1.0
grad_clip_type: 2.0
grad_noise: false
accum_grad: 1
no_forward_run: false
resume: true
train_dtype: float32
use_amp: false
log_interval: null
use_matplotlib: true
use_tensorboard: true
use_wandb: false
wandb_project: null
wandb_id: null
wandb_entity: null
wandb_name: null
wandb_model_log_interval: -1
detect_anomaly: false
pretrain_path: null
init_param: []
ignore_init_mismatch: false
freeze_param: []
num_iters_per_epoch: 500
batch_size: 20
valid_batch_size: null
batch_bins: 2560000
valid_batch_bins: null
train_shape_file:
- exp/d/tts_stats_raw_phn_none/train/text_shape.phn
- exp/d/tts_stats_raw_phn_none/train/speech_shape
valid_shape_file:
- exp/d/tts_stats_raw_phn_none/valid/text_shape.phn
- exp/d/tts_stats_raw_phn_none/valid/speech_shape
batch_type: numel
valid_batch_type: null
fold_length:
- 150
- 204800
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 500
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/train_d_phn/text
    - text
    - text
-   - dump/raw/train_d_phn/wav.scp
    - speech
    - sound
valid_data_path_and_name_and_type:
-   - dump/raw/dev_d_phn/text
    - text
    - text
-   - dump/raw/dev_d_phn/wav.scp
    - speech
    - sound
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.001
    eps: 1.0e-06
    weight_decay: 0.0
scheduler: null
scheduler_conf: {}
token_list:
- <blank>
- <unk>
- ','
- .
- r
- t
- n
- a0
- s
- I0
- D
- l
- Y0
- m
- v
- h
- E1
- k
- a:1
- E:1
- j
- f
- T
- G
- a1
- p
- c
- au:1
- i:1
- O:1
- E0
- I:1
- r_0
- I1
- t_h
- k_h
- Y1
- i0
- ei1
- u:1
- ou:1
- ei:1
- O1
- N
- l_0
- '91'
- ou0
- ai0
- n_0
- au1
- O0
- ou1
- ai:1
- ei0
- '9:1'
- ai1
- i1
- c_h
- '90'
- au0
- x
- C
- p_h
- u0
- 9i:1
- Y:1
- 9i1
- J
- u1
- 9i0
- N_0
- m_0
- J_0
- Oi1
- Yi0
- Yi1
- Oi0
- '9:0'
- au:0
- E:0
- <sos/eos>
odim: null
model_conf: {}
use_preprocessor: true
token_type: phn
bpemodel: null
non_linguistic_symbols: null
cleaner: null
g2p: null
feats_extract: fbank
feats_extract_conf:
    n_fft: 1024
    hop_length: 256
    win_length: null
    fs: 22050
    fmin: 80
    fmax: 7600
    n_mels: 80
normalize: global_mvn
normalize_conf:
    stats_file: exp/d/tts_stats_raw_phn_none/train/feats_stats.npz
tts: tacotron2
tts_conf:
    embed_dim: 512
    elayers: 1
    eunits: 512
    econv_layers: 3
    econv_chans: 512
    econv_filts: 5
    atype: location
    adim: 512
    aconv_chans: 32
    aconv_filts: 15
    cumulate_att_w: true
    dlayers: 2
    dunits: 1024
    prenet_layers: 2
    prenet_units: 256
    postnet_layers: 5
    postnet_chans: 512
    postnet_filts: 5
    output_activation: null
    use_batch_norm: true
    use_concate: true
    use_residual: false
    dropout_rate: 0.5
    zoneout_rate: 0.1
    reduction_factor: 1
    spk_embed_dim: null
    use_masking: true
    bce_pos_weight: 5.0
    use_guided_attn_loss: true
    guided_attn_loss_sigma: 0.4
    guided_attn_loss_lambda: 1.0
pitch_extract: null
pitch_extract_conf: {}
pitch_normalize: null
pitch_normalize_conf: {}
energy_extract: null
energy_extract_conf: {}
energy_normalize: null
energy_normalize_conf: {}
required:
- output_dir
- token_list
version: 0.10.7a1
distributed: true
```

</details>



### Citing ESPnet

```BibTex
@inproceedings{watanabe2018espnet,
  author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson Yalta and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
  title={{ESPnet}: End-to-End Speech Processing Toolkit},
  year={2018},
  booktitle={Proceedings of Interspeech},
  pages={2207--2211},
  doi={10.21437/Interspeech.2018-1456},
  url={http://dx.doi.org/10.21437/Interspeech.2018-1456}
}




@inproceedings{hayashi2020espnet,
  title={{Espnet-TTS}: Unified, reproducible, and integratable open source end-to-end text-to-speech toolkit},
  author={Hayashi, Tomoki and Yamamoto, Ryuichi and Inoue, Katsuki and Yoshimura, Takenori and Watanabe, Shinji and Toda, Tomoki and Takeda, Kazuya and Zhang, Yu and Tan, Xu},
  booktitle={Proceedings of IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={7654--7658},
  year={2020},
  organization={IEEE}
}
```

or arXiv:

```bibtex
@misc{watanabe2018espnet,
  title={ESPnet: End-to-End Speech Processing Toolkit}, 
  author={Shinji Watanabe and Takaaki Hori and Shigeki Karita and Tomoki Hayashi and Jiro Nishitoba and Yuya Unno and Nelson Yalta and Jahn Heymann and Matthew Wiesner and Nanxin Chen and Adithya Renduchintala and Tsubasa Ochiai},
  year={2018},
  eprint={1804.00015},
  archivePrefix={arXiv},
  primaryClass={cs.CL}
}
```
