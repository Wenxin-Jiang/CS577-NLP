---
tags:
- espnet
- audio
- audio-to-audio
language: 
datasets:
- chime4
license: cc-by-4.0
---

## ESPnet2 ENH model 

### `espnet/Wangyou_Zhang_wsj0_2mix_enh_dc_crn_mapping_snr_raw`

This model was trained by Wangyou Zhang using chime4 recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet

pip install -e .
cd egs2/chime4/enh1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/Wangyou_Zhang_wsj0_2mix_enh_dc_crn_mapping_snr_raw
```



## ENH config

<details><summary>expand</summary>

```
config: conf/tuning/train_enh_dc_crn_mapping_snr.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: chunk
output_dir: exp/enh_train_enh_dc_crn_mapping_snr_raw
ngpu: 1
seed: 0
num_workers: 4
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
patience: 10
val_scheduler_criterion:
- valid
- loss
early_stopping_criterion:
- valid
- loss
- min
best_model_criterion:
-   - valid
    - si_snr
    - max
-   - valid
    - loss
    - min
keep_nbest_models: 1
nbest_averaging_interval: 0
grad_clip: 5
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
num_iters_per_epoch: null
batch_size: 16
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/enh_stats_8k/train/speech_mix_shape
- exp/enh_stats_8k/train/speech_ref1_shape
- exp/enh_stats_8k/train/speech_ref2_shape
valid_shape_file:
- exp/enh_stats_8k/valid/speech_mix_shape
- exp/enh_stats_8k/valid/speech_ref1_shape
- exp/enh_stats_8k/valid/speech_ref2_shape
batch_type: folded
valid_batch_type: null
fold_length:
- 80000
- 80000
- 80000
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 32000
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/tr_min_8k/wav.scp
    - speech_mix
    - sound
-   - dump/raw/tr_min_8k/spk1.scp
    - speech_ref1
    - sound
-   - dump/raw/tr_min_8k/spk2.scp
    - speech_ref2
    - sound
valid_data_path_and_name_and_type:
-   - dump/raw/cv_min_8k/wav.scp
    - speech_mix
    - sound
-   - dump/raw/cv_min_8k/spk1.scp
    - speech_ref1
    - sound
-   - dump/raw/cv_min_8k/spk2.scp
    - speech_ref2
    - sound
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.001
    eps: 1.0e-08
    weight_decay: 1.0e-07
    amsgrad: true
scheduler: steplr
scheduler_conf:
    step_size: 2
    gamma: 0.98
init: xavier_uniform
model_conf:
    stft_consistency: false
    loss_type: mask_mse
    mask_type: null
criterions:
-   name: si_snr
    conf:
        eps: 1.0e-07
    wrapper: pit
    wrapper_conf:
        weight: 1.0
use_preprocessor: false
encoder: stft
encoder_conf:
    n_fft: 256
    hop_length: 128
separator: dc_crn
separator_conf:
    num_spk: 2
    input_channels:
    - 2
    - 16
    - 32
    - 64
    - 128
    - 256
    enc_hid_channels: 8
    enc_layers: 5
    glstm_groups: 2
    glstm_layers: 2
    glstm_bidirectional: true
    glstm_rearrange: false
    mode: mapping
decoder: stft
decoder_conf:
    n_fft: 256
    hop_length: 128
required:
- output_dir
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

@inproceedings{li2021espnetse,
  title={{ESPnet-SE}: End-to-End Speech Enhancement and Separation Toolkit Designed for {ASR} Integration},
  author={Li, Chenda and Shi, Jing and Zhang, Wangyou and Subramanian, Aswin Shanmugam and Chang, Xuankai and Kamo, Naoyuki and Hira, Moto and Hayashi, Tomoki and Boeddeker, Christoph and Chen, Zhuo and Watanabe, Shinji},
  booktitle={Proc. IEEE Spoken Language Technology Workshop (SLT)},
  pages={785--792},
  year={2021},
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

@inproceedings{li2021espnetse,
  title={{ESPnet-SE}: End-to-End Speech Enhancement and Separation Toolkit Designed for {ASR} Integration},
  author={Li, Chenda and Shi, Jing and Zhang, Wangyou and Subramanian, Aswin Shanmugam and Chang, Xuankai and Kamo, Naoyuki and Hira, Moto and Hayashi, Tomoki and Boeddeker, Christoph and Chen, Zhuo and Watanabe, Shinji},
  year={2020},
  eprint={2011.03706},
  archivePrefix={arXiv},
  primaryClass={eess.AS}
}
```
