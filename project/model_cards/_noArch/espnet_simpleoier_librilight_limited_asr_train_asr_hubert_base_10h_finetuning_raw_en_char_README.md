---
tags:
- espnet
- audio
- automatic-speech-recognition
language: en
datasets:
- librilight_limited
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `simpleoier/simpleoier_librilight_limited_asr_train_asr_hubert_base_10h_finetuning_raw_en_char`

This model was trained by simpleoier using librilight_limited recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

Follow the [ESPnet installation instructions](https://espnet.github.io/espnet/installation.html)
if you haven't done that already.

```bash
cd espnet
git checkout 6752c23c61c95c9c8ba8547eab14cbd9b38d18e7
pip install -e .
cd egs2/librilight_limited/asr1
./run.sh --skip_data_prep false --skip_train true --download_model simpleoier/simpleoier_librilight_limited_asr_train_asr_hubert_base_10h_finetuning_raw_en_char
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Tue Jan 10 17:33:54 EST 2023`
- python version: `3.9.15 (main, Nov  4 2022, 16:13:54)  [GCC 11.2.0]`
- espnet version: `espnet 202209`
- pytorch version: `pytorch 1.12.1`
- Git hash: ``
  - Commit date: ``

## asr_train_asr_hubert_base_10h_finetuning_raw_en_char
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_model_valid.loss.ave/dev_clean|2694|53635|90.3|9.3|0.5|0.7|10.4|74.8|
|decode_asr_model_valid.loss.ave/dev_other|2864|50948|83.8|15.1|1.1|1.2|17.4|83.9|
|decode_asr_model_valid.loss.ave/test_clean|2620|52576|90.2|9.4|0.4|0.7|10.5|75.2|
|decode_asr_model_valid.loss.ave/test_other|2939|52343|83.6|15.2|1.1|1.3|17.6|85.3|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_model_valid.loss.ave/dev_clean|2694|284127|97.8|1.2|1.0|0.8|3.0|74.8|
|decode_asr_model_valid.loss.ave/dev_other|2864|265951|95.4|2.5|2.0|1.5|6.1|83.9|
|decode_asr_model_valid.loss.ave/test_clean|2620|281530|97.8|1.2|1.0|0.8|3.0|75.2|
|decode_asr_model_valid.loss.ave/test_other|2939|272758|95.5|2.5|2.0|1.6|6.1|85.3|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|

## ASR config

<details><summary>expand</summary>

```
config: conf/tuning/train_asr_hubert_base_10h_finetuning.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_hubert_base_10h_finetuning_raw_en_char
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
unused_parameters: true
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
init_param:
- ../../librispeech/ssl1/exp/hubert_iter1_train_ssl_torchaudiohubert_base_960h_pretrain_it1_raw/valid.loss.ave.pth:encoder:encoder
ignore_init_mismatch: false
freeze_param: []
num_iters_per_epoch: null
batch_size: 20
valid_batch_size: null
batch_bins: 3200000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_en_char/train/speech_shape
- exp/asr_stats_raw_en_char/train/text_shape.char
valid_shape_file:
- exp/asr_stats_raw_en_char/valid/speech_shape
- exp/asr_stats_raw_en_char/valid/text_shape.char
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
-   - dump/raw/train_10h/wav.scp
    - speech
    - sound
-   - dump/raw/train_10h/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/dev_clean/wav.scp
    - speech
    - sound
-   - dump/raw/dev_clean/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 5.0e-05
scheduler: warmuplr
scheduler_conf:
    warmup_steps: 8000
token_list:
- <blank>
- <unk>
- <space>
- E
- T
- A
- O
- N
- I
- H
- S
- R
- D
- L
- U
- M
- W
- C
- F
- G
- Y
- P
- B
- V
- K
- ''''
- X
- J
- Q
- Z
- <sos/eos>
init: xavier_uniform
input_size: 1
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
normalize: null
normalize_conf: {}
model: espnet
model_conf:
    ctc_weight: 1.0
    lsm_weight: 0.1
    length_normalized_loss: false
preencoder: null
preencoder_conf: {}
encoder: torchaudiohubert
encoder_conf:
    encoder_projection_dropout: 0.0
    encoder_attention_dropout: 0.0
    encoder_ff_interm_dropout: 0.1
    encoder_dropout: 0.0
    encoder_layer_drop: 0.05
    mask_prob: 0.65
    mask_channel_prob: 0.5
    mask_channel_length: 64
    num_classes: 500
    finetuning: true
    freeze_encoder_updates: 10000
postencoder: null
postencoder_conf: {}
decoder: rnn
decoder_conf: {}
preprocessor: default
preprocessor_conf: {}
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