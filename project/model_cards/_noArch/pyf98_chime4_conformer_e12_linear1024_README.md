---
tags:
- espnet
- audio
- automatic-speech-recognition
language: en
datasets:
- chime4
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `pyf98/chime4_conformer_e12_linear1024`

This model was trained by Yifan Peng using chime4 recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

Follow the [ESPnet installation instructions](https://espnet.github.io/espnet/installation.html)
if you haven't done that already.

```bash
cd espnet
git checkout ad91279f0108d54bd22abe29671b376f048822c5
pip install -e .
cd egs2/chime4/asr1
./run.sh --skip_data_prep false --skip_train true --download_model pyf98/chime4_conformer_e12_linear1024
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Wed Dec 28 15:49:24 EST 2022`
- python version: `3.9.15 (main, Nov 24 2022, 14:31:59)  [GCC 11.2.0]`
- espnet version: `espnet 202211`
- pytorch version: `pytorch 1.12.1`
- Git hash: `f9a8009aef6ff9ba192a78c19b619ae4a9f3b9d2`
  - Commit date: `Wed Dec 28 00:30:54 2022 -0500`

## asr_train_asr_conformer_e12_linear1024_raw_en_char_sp
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/dt05_real_beamformit_5mics|1640|27119|92.8|5.8|1.5|0.6|7.8|56.5|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/dt05_simu_beamformit_5mics|1640|27120|91.3|6.7|2.0|0.8|9.5|60.5|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/et05_real_beamformit_5mics|1320|21409|88.6|9.2|2.1|1.2|12.5|63.8|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/et05_simu_beamformit_5mics|1320|21416|86.5|10.4|3.1|1.3|14.8|70.9|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/dt05_real_beamformit_5mics|1640|160390|96.9|1.6|1.5|0.7|3.8|56.5|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/dt05_simu_beamformit_5mics|1640|160400|96.0|2.0|2.0|1.0|4.9|60.5|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/et05_real_beamformit_5mics|1320|126796|94.8|2.8|2.3|1.2|6.4|63.9|
|decode_asr_lm_lm_train_lm_transformer_en_char_valid.loss.ave_asr_model_valid.acc.ave/et05_simu_beamformit_5mics|1320|126812|93.1|3.4|3.4|1.5|8.4|70.9|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|

## ASR config

<details><summary>expand</summary>

```
config: conf/tuning/train_asr_conformer_e12_linear1024.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_conformer_e12_linear1024_raw_en_char_sp
ngpu: 1
seed: 2022
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
max_epoch: 60
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
    - acc
    - max
keep_nbest_models: 10
nbest_averaging_interval: 0
grad_clip: 5.0
grad_clip_type: 2.0
grad_noise: false
accum_grad: 1
no_forward_run: false
resume: true
train_dtype: float32
use_amp: true
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
num_iters_per_epoch: null
batch_size: 20
valid_batch_size: null
batch_bins: 15000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_en_char_sp/train/speech_shape
- exp/asr_stats_raw_en_char_sp/train/text_shape.char
valid_shape_file:
- exp/asr_stats_raw_en_char_sp/valid/speech_shape
- exp/asr_stats_raw_en_char_sp/valid/text_shape.char
batch_type: numel
valid_batch_type: null
fold_length:
- 80000
- 150
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 500
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/tr05_multi_noisy_si284_sp/wav.scp
    - speech
    - kaldi_ark
-   - dump/raw/tr05_multi_noisy_si284_sp/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/dt05_multi_isolated_1ch_track/wav.scp
    - speech
    - kaldi_ark
-   - dump/raw/dt05_multi_isolated_1ch_track/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.001
    weight_decay: 1.0e-06
scheduler: warmuplr
scheduler_conf:
    warmup_steps: 25000
token_list:
- <blank>
- <unk>
- <space>
- E
- T
- A
- N
- I
- O
- S
- R
- H
- L
- D
- C
- U
- M
- P
- F
- G
- Y
- W
- B
- V
- K
- .
- X
- ''''
- J
- Q
- Z
- ','
- '-'
- '"'
- <NOISE>
- '*'
- ':'
- (
- )
- '?'
- '&'
- ;
- '!'
- /
- '{'
- '}'
- '1'
- '2'
- '0'
- $
- '8'
- '9'
- '6'
- '3'
- '5'
- '7'
- '4'
- '~'
- '`'
- _
- <*IN*>
- <*MR.*>
- \
- ^
- <sos/eos>
init: null
input_size: null
ctc_conf:
    dropout_rate: 0.0
    ctc_type: builtin
    reduce: true
    ignore_nan_grad: null
    zero_infinity: true
joint_net_conf: null
use_preprocessor: true
token_type: char
bpemodel: null
non_linguistic_symbols: data/nlsyms.txt
cleaner: null
g2p: null
speech_volume_normalize: null
rir_scp: null
rir_apply_prob: 1.0
noise_scp: null
noise_apply_prob: 1.0
noise_db_range: '13_15'
short_noise_thres: 0.5
frontend: default
frontend_conf:
    n_fft: 512
    win_length: 400
    hop_length: 160
    fs: 16k
specaug: specaug
specaug_conf:
    apply_time_warp: true
    time_warp_window: 5
    time_warp_mode: bicubic
    apply_freq_mask: true
    freq_mask_width_range:
    - 0
    - 27
    num_freq_mask: 2
    apply_time_mask: true
    time_mask_width_ratio_range:
    - 0.0
    - 0.05
    num_time_mask: 2
normalize: global_mvn
normalize_conf:
    stats_file: exp/asr_stats_raw_en_char_sp/train/feats_stats.npz
model: espnet
model_conf:
    ctc_weight: 0.3
    lsm_weight: 0.1
    length_normalized_loss: false
preencoder: null
preencoder_conf: {}
encoder: conformer
encoder_conf:
    output_size: 256
    attention_heads: 4
    linear_units: 1024
    num_blocks: 12
    dropout_rate: 0.1
    positional_dropout_rate: 0.1
    attention_dropout_rate: 0.1
    input_layer: conv2d
    normalize_before: true
    macaron_style: true
    rel_pos_type: latest
    pos_enc_layer_type: rel_pos
    selfattention_layer_type: rel_selfattn
    activation_type: swish
    use_cnn_module: true
    cnn_module_kernel: 31
postencoder: null
postencoder_conf: {}
decoder: transformer
decoder_conf:
    attention_heads: 4
    linear_units: 2048
    num_blocks: 6
    dropout_rate: 0.1
    positional_dropout_rate: 0.1
    self_attention_dropout_rate: 0.1
    src_attention_dropout_rate: 0.1
preprocessor: default
preprocessor_conf: {}
required:
- output_dir
- token_list
version: '202211'
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