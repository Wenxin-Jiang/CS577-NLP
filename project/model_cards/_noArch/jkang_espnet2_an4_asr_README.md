---
tags:
- espnet
- audio
- automatic-speech-recognition
language: en
datasets:
- an4
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `jkang/espnet2_an4_asr`

This model was trained by jaekookang using an4 recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout 48422215e272812feb9bbac9d7cf4aae6a316bca
pip install -e .
cd egs2/an4/asr1
./run.sh --skip_data_prep false --skip_train true --download_model jkang/espnet2_an4_asr
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Tue Feb  1 13:22:35 KST 2022`
- python version: `3.9.7 (default, Sep 16 2021, 13:09:58)  [GCC 7.5.0]`
- espnet version: `espnet 0.10.6a1`
- pytorch version: `pytorch 1.10.1`
- Git hash: `48422215e272812feb9bbac9d7cf4aae6a316bca`
  - Commit date: `Fri Jan 28 17:25:31 2022 +0000`

## asr_train_asr_transformer_raw_en_bpe30_sp
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_en_bpe30_valid.loss.ave_asr_model_valid.acc.ave/test|130|773|91.5|6.5|2.1|0.6|9.2|38.5|
|decode_asr_lm_lm_train_lm_en_bpe30_valid.loss.ave_asr_model_valid.acc.ave/train_dev|100|591|88.8|7.4|3.7|0.7|11.8|41.0|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_en_bpe30_valid.loss.ave_asr_model_valid.acc.ave/test|130|2565|96.6|1.2|2.2|1.0|4.4|38.5|
|decode_asr_lm_lm_train_lm_en_bpe30_valid.loss.ave_asr_model_valid.acc.ave/train_dev|100|1915|94.0|1.7|4.3|0.4|6.4|41.0|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_en_bpe30_valid.loss.ave_asr_model_valid.acc.ave/test|130|2695|96.8|1.1|2.1|0.9|4.2|38.5|
|decode_asr_lm_lm_train_lm_en_bpe30_valid.loss.ave_asr_model_valid.acc.ave/train_dev|100|2015|94.3|1.6|4.1|0.4|6.1|41.0|

## ASR config

<details><summary>expand</summary>

```
config: conf/train_asr_transformer.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_transformer_raw_en_bpe30_sp
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
batch_size: 64
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_en_bpe30_sp/train/speech_shape
- exp/asr_stats_raw_en_bpe30_sp/train/text_shape.bpe
valid_shape_file:
- exp/asr_stats_raw_en_bpe30_sp/valid/speech_shape
- exp/asr_stats_raw_en_bpe30_sp/valid/text_shape.bpe
batch_type: folded
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
-   - dump/raw/train_nodev_sp/wav.scp
    - speech
    - sound
-   - dump/raw/train_nodev_sp/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/train_dev/wav.scp
    - speech
    - sound
-   - dump/raw/train_dev/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.001
scheduler: warmuplr
scheduler_conf:
    warmup_steps: 2500
token_list:
- <blank>
- <unk>
- ▁
- T
- E
- O
- R
- Y
- A
- H
- U
- S
- I
- F
- B
- L
- P
- D
- G
- M
- C
- V
- X
- J
- K
- Z
- W
- N
- Q
- <sos/eos>
init: xavier_uniform
input_size: null
ctc_conf:
    dropout_rate: 0.0
    ctc_type: builtin
    reduce: true
    ignore_nan_grad: true
joint_net_conf: null
model_conf:
    ctc_weight: 0.3
    lsm_weight: 0.1
    length_normalized_loss: false
use_preprocessor: true
token_type: bpe
bpemodel: data/en_token_list/bpe_unigram30/bpe.model
non_linguistic_symbols: null
cleaner: null
g2p: null
speech_volume_normalize: null
rir_scp: null
rir_apply_prob: 1.0
noise_scp: null
noise_apply_prob: 1.0
noise_db_range: '13_15'
frontend: default
frontend_conf:
    fs: 16k
specaug: null
specaug_conf: {}
normalize: global_mvn
normalize_conf:
    stats_file: exp/asr_stats_raw_en_bpe30_sp/train/feats_stats.npz
preencoder: null
preencoder_conf: {}
encoder: transformer
encoder_conf:
    output_size: 256
    attention_heads: 4
    linear_units: 2048
    num_blocks: 12
    dropout_rate: 0.1
    positional_dropout_rate: 0.1
    attention_dropout_rate: 0.0
    input_layer: conv2d
    normalize_before: true
postencoder: null
postencoder_conf: {}
decoder: transformer
decoder_conf:
    attention_heads: 4
    linear_units: 2048
    num_blocks: 6
    dropout_rate: 0.1
    positional_dropout_rate: 0.1
    self_attention_dropout_rate: 0.0
    src_attention_dropout_rate: 0.0
required:
- output_dir
- token_list
version: 0.10.6a1
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
