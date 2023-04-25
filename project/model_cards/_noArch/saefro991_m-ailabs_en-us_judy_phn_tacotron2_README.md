---
tags:
- espnet
- audio
- text-to-speech
language: en
datasets:
- m_ailabs
license: cc-by-4.0
---

## ESPnet2 TTS model 

### `saefro991/m-ailabs_en-us_judy_phn_tacotron2`

This model was trained by Takaaki-Saeki using m_ailabs recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

Follow the [ESPnet installation instructions](https://espnet.github.io/espnet/installation.html)
if you haven't done that already.

```bash
cd espnet
git checkout 32b0f75b4491b71e88deac62bfc431cfcc9d7143
pip install -e .
cd egs2/m_ailabs/tts1
./run.sh --skip_data_prep false --skip_train true --download_model saefro991/m-ailabs_en-us_judy_phn_tacotron2
```



## TTS config

<details><summary>expand</summary>

```
config: conf/train.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_raw_phn_tacotron_g2p_en
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
max_epoch: 200
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
create_graph_in_tensorboard: false
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
batch_bins: 5120000
valid_batch_bins: null
train_shape_file:
- exp/tts_stats_raw_phn_tacotron_g2p_en/train/text_shape.phn
- exp/tts_stats_raw_phn_tacotron_g2p_en/train/speech_shape
valid_shape_file:
- exp/tts_stats_raw_phn_tacotron_g2p_en/valid/text_shape.phn
- exp/tts_stats_raw_phn_tacotron_g2p_en/valid/speech_shape
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
-   - dump/raw/tr_no_dev/text
    - text
    - text
-   - dump/raw/tr_no_dev/wav.scp
    - speech
    - sound
valid_data_path_and_name_and_type:
-   - dump/raw/dev/text
    - text
    - text
-   - dump/raw/dev/wav.scp
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
- ''
- AH0
- T
- N
- D
- R
- S
- L
- DH
- IH1
- K
- EH1
- M
- Z
- AE1
- W
- IH0
- AH1
- ','
- B
- IY1
- ER0
- UW1
- P
- HH
- AY1
- F
- V
- AA1
- AO1
- .
- EY1
- IY0
- OW1
- NG
- G
- Y
- AW1
- SH
- CH
- ER1
- UH1
- TH
- JH
- OW0
- OY1
- '?'
- '!'
- EH0
- EY2
- IH2
- ''''
- AY2
- AA0
- EH2
- UW0
- AA2
- AH2
- AE0
- OW2
- AO2
- UW2
- AE2
- ZH
- AW2
- AY0
- IY2
- AO0
- UH0
- UH2
- OY2
- AW0
- ER2
- EY0
- OY0
- <sos/eos>
odim: null
model_conf: {}
use_preprocessor: true
token_type: phn
bpemodel: null
non_linguistic_symbols: null
cleaner: tacotron
g2p: g2p_en
feats_extract: fbank
feats_extract_conf:
    n_fft: 1024
    hop_length: 256
    win_length: null
    fs: 16000
    fmin: 80
    fmax: 7600
    n_mels: 80
normalize: global_mvn
normalize_conf:
    stats_file: exp/tts_stats_raw_phn_tacotron_g2p_en/train/feats_stats.npz
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
version: '202209'
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
