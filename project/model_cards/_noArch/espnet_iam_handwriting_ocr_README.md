---
tags:
- espnet
- image-to-text
- ocr
- handwriting-recognition
language: en
datasets:
- iam
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `espnet/iam_handwriting_ocr`

This model was trained by kenzheng99 using iam recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

Follow the [ESPnet installation instructions](https://espnet.github.io/espnet/installation.html)
if you haven't done that already.

```bash
cd espnet
git checkout 2169367022b8939d22005e8cf45a65bb20bc0768
pip install -e .
cd egs2/iam/ocr1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/iam_handwriting_ocr
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Mon Nov  7 13:40:17 EST 2022`
- python version: `3.7.13 (default, Mar 29 2022, 02:18:16)  [GCC 7.5.0]`
- espnet version: `espnet 202209`
- pytorch version: `pytorch 1.10.0`
- Git hash: `2169367022b8939d22005e8cf45a65bb20bc0768`
  - Commit date: `Thu Nov 3 20:38:03 2022 -0400`

## asr_train_asr_conformer_extracted_en_char
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|inference_asr_model_valid.acc.ave/test|2915|25932|80.5|17.3|2.2|0.8|20.3|72.8|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|inference_asr_model_valid.acc.ave/test|2915|125616|94.0|4.2|1.8|0.7|6.7|72.8|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|

## ASR config

<details><summary>expand</summary>

```
config: conf/train_asr_conformer.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_conformer_extracted_en_char
ngpu: 1
seed: 0
num_workers: 1
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: 4
dist_rank: 0
local_rank: 0
dist_master_addr: localhost
dist_master_port: 35197
dist_launcher: null
multiprocessing_distributed: true
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
batch_size: 64
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_extracted_en_char/train/speech_shape
- exp/asr_stats_extracted_en_char/train/text_shape.char
valid_shape_file:
- exp/asr_stats_extracted_en_char/valid/speech_shape
- exp/asr_stats_extracted_en_char/valid/text_shape.char
batch_type: folded
valid_batch_type: null
fold_length:
- 800
- 150
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 500
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/extracted/train/feats.scp
    - speech
    - kaldi_ark
-   - dump/extracted/train/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/extracted/valid/feats.scp
    - speech
    - kaldi_ark
-   - dump/extracted/valid/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.002
    weight_decay: 1.0e-06
scheduler: warmuplr
scheduler_conf:
    warmup_steps: 15000
token_list:
- <blank>
- <unk>
- <space>
- e
- t
- a
- o
- n
- i
- r
- s
- h
- l
- d
- c
- u
- m
- f
- p
- g
- y
- w
- b
- .
- ','
- v
- k
- '-'
- T
- ''''
- M
- I
- A
- '"'
- S
- P
- H
- B
- C
- W
- N
- G
- x
- R
- E
- L
- F
- '0'
- D
- '1'
- j
- O
- q
- U
- K
- '!'
- '3'
- '9'
- (
- z
- )
- ':'
- V
- ;
- '5'
- '2'
- J
- '8'
- Y
- '4'
- '6'
- '?'
- '#'
- '&'
- '7'
- /
- '*'
- Q
- X
- Z
- +
- <sos/eos>
init: xavier_uniform
input_size: 100
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
non_linguistic_symbols: null
cleaner: null
g2p: null
speech_volume_normalize: null
rir_scp: null
rir_apply_prob: 1.0
noise_scp: null
noise_apply_prob: 1.0
noise_db_range: '13_15'
short_noise_thres: 0.5
frontend: null
frontend_conf: {}
specaug: null
specaug_conf: {}
normalize: global_mvn
normalize_conf:
    stats_file: exp/asr_stats_extracted_en_char/train/feats_stats.npz
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
required:
- output_dir
- token_list
version: '202209'
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