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

### `espnet/GunnarThor_talromur_h_fastspeech2`

This model was trained by Gunnar Thor using talromur recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout 49a284e69308d81c142b89795de255b4ce290c54
pip install -e .
cd egs2/talromur/tts1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/GunnarThor_talromur_h_fastspeech2
```



## TTS config

<details><summary>expand</summary>

```
config: conf/tuning/train_fastspeech2.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/h/tts_train_fastspeech2_raw_phn_none
ngpu: 1
seed: 0
num_workers: 1
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: null
dist_rank: null
local_rank: 0
dist_master_addr: null
dist_master_port: null
dist_launcher: null
multiprocessing_distributed: false
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
accum_grad: 8
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
num_iters_per_epoch: 800
batch_size: 20
valid_batch_size: null
batch_bins: 2500000
valid_batch_bins: null
train_shape_file:
- exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/text_shape.phn
- exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/speech_shape
valid_shape_file:
- exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/valid/text_shape.phn
- exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/valid/speech_shape
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
-   - dump/raw/train_h_phn/text
    - text
    - text
-   - exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/train_h_phn/durations
    - durations
    - text_int
-   - dump/raw/train_h_phn/wav.scp
    - speech
    - sound
valid_data_path_and_name_and_type:
-   - dump/raw/dev_h_phn/text
    - text
    - text
-   - exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/dev_h_phn/durations
    - durations
    - text_int
-   - dump/raw/dev_h_phn/wav.scp
    - speech
    - sound
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 1.0
scheduler: noamlr
scheduler_conf:
    model_size: 384
    warmup_steps: 4000
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
- f
- G
- j
- T
- a1
- p
- c
- au:1
- i:1
- O:1
- I:1
- E0
- I1
- r_0
- t_h
- k_h
- Y1
- ei1
- i0
- ou:1
- ei:1
- u:1
- O1
- N
- l_0
- '91'
- ai0
- au1
- ou0
- n_0
- ei0
- O0
- ou1
- ai:1
- '9:1'
- ai1
- i1
- '90'
- au0
- c_h
- x
- 9i:1
- C
- p_h
- u0
- Y:1
- J
- 9i1
- u1
- 9i0
- N_0
- m_0
- J_0
- Oi1
- Yi0
- Yi1
- Oi0
- au:0
- '9:0'
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
    stats_file: exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/feats_stats.npz
tts: fastspeech2
tts_conf:
    adim: 384
    aheads: 2
    elayers: 4
    eunits: 1536
    dlayers: 4
    dunits: 1536
    positionwise_layer_type: conv1d
    positionwise_conv_kernel_size: 3
    duration_predictor_layers: 2
    duration_predictor_chans: 256
    duration_predictor_kernel_size: 3
    postnet_layers: 5
    postnet_filts: 5
    postnet_chans: 256
    use_masking: true
    use_scaled_pos_enc: true
    encoder_normalize_before: true
    decoder_normalize_before: true
    reduction_factor: 1
    init_type: xavier_uniform
    init_enc_alpha: 1.0
    init_dec_alpha: 1.0
    transformer_enc_dropout_rate: 0.2
    transformer_enc_positional_dropout_rate: 0.2
    transformer_enc_attn_dropout_rate: 0.2
    transformer_dec_dropout_rate: 0.2
    transformer_dec_positional_dropout_rate: 0.2
    transformer_dec_attn_dropout_rate: 0.2
    pitch_predictor_layers: 5
    pitch_predictor_chans: 256
    pitch_predictor_kernel_size: 5
    pitch_predictor_dropout: 0.5
    pitch_embed_kernel_size: 1
    pitch_embed_dropout: 0.0
    stop_gradient_from_pitch_predictor: true
    energy_predictor_layers: 2
    energy_predictor_chans: 256
    energy_predictor_kernel_size: 3
    energy_predictor_dropout: 0.5
    energy_embed_kernel_size: 1
    energy_embed_dropout: 0.0
    stop_gradient_from_energy_predictor: false
pitch_extract: dio
pitch_extract_conf:
    fs: 22050
    n_fft: 1024
    hop_length: 256
    f0max: 400
    f0min: 80
    reduction_factor: 1
pitch_normalize: global_mvn
pitch_normalize_conf:
    stats_file: exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/pitch_stats.npz
energy_extract: energy
energy_extract_conf:
    fs: 22050
    n_fft: 1024
    hop_length: 256
    win_length: null
    reduction_factor: 1
energy_normalize: global_mvn
energy_normalize_conf:
    stats_file: exp/h/tts_train_tacotron2_raw_phn_none/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/energy_stats.npz
required:
- output_dir
- token_list
version: 0.10.7a1
distributed: false
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
