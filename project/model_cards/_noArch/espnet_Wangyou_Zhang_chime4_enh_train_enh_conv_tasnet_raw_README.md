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

### `espnet/Wangyou_Zhang_chime4_enh_train_enh_conv_tasnet_raw`

This model was trained by Wangyou Zhang using chime4 recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet

pip install -e .
cd egs2/chime4/enh1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/Wangyou_Zhang_chime4_enh_train_enh_conv_tasnet_raw
```



## ENH config

<details><summary>expand</summary>

```
config: conf/tuning/train_enh_conv_tasnet.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: chunk
output_dir: exp/enh_train_enh_conv_tasnet_raw
ngpu: 1
seed: 0
num_workers: 4
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: 2
dist_rank: 0
local_rank: 0
dist_master_addr: localhost
dist_master_port: 57680
dist_launcher: null
multiprocessing_distributed: true
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
collect_stats: false
write_collected_feats: false
max_epoch: 100
patience: 4
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
grad_clip: 5.0
grad_clip_type: 2.0
grad_noise: false
accum_grad: 1
no_forward_run: false
resume: true
train_dtype: float32
use_amp: false
log_interval: null
unused_parameters: false
use_tensorboard: true
use_wandb: false
wandb_project: null
wandb_id: null
pretrain_path: null
init_param: []
freeze_param: []
num_iters_per_epoch: null
batch_size: 8
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/enh_stats_16k/train/speech_mix_shape
- exp/enh_stats_16k/train/speech_ref1_shape
valid_shape_file:
- exp/enh_stats_16k/valid/speech_mix_shape
- exp/enh_stats_16k/valid/speech_ref1_shape
batch_type: folded
valid_batch_type: null
fold_length:
- 80000
- 80000
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 32000
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/tr05_simu_isolated_1ch_track/wav.scp
    - speech_mix
    - sound
-   - dump/raw/tr05_simu_isolated_1ch_track/spk1.scp
    - speech_ref1
    - sound
valid_data_path_and_name_and_type:
-   - dump/raw/dt05_simu_isolated_1ch_track/wav.scp
    - speech_mix
    - sound
-   - dump/raw/dt05_simu_isolated_1ch_track/spk1.scp
    - speech_ref1
    - sound
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.001
    eps: 1.0e-08
    weight_decay: 1.0e-05
scheduler: reducelronplateau
scheduler_conf:
    mode: min
    factor: 0.5
    patience: 3
init: xavier_uniform
model_conf:
    loss_type: si_snr
use_preprocessor: false
encoder: conv
encoder_conf:
    channel: 256
    kernel_size: 20
    stride: 10
separator: tcn
separator_conf:
    num_spk: 1
    layer: 8
    stack: 4
    bottleneck_dim: 256
    hidden_dim: 512
    kernel: 3
    causal: false
    norm_type: gLN
    nonlinear: relu
decoder: conv
decoder_conf:
    channel: 256
    kernel_size: 20
    stride: 10
required:
- output_dir
version: 0.9.7
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
