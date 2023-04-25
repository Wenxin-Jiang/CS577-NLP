---
tags:
- espnet
- audio
- automatic-speech-recognition
language: ru
datasets:
- commonvoice
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `espnet/russian_commonvoice_blstm`

This model was trained by dzeinali using commonvoice recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout fa1b865352475b744c37f70440de1cc6b257ba70
pip install -e .
cd egs2/commonvoice/asr1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/russian_commonvoice_blstm
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Wed Mar 23 19:56:59 EDT 2022`
- python version: `3.9.5 (default, Jun  4 2021, 12:28:51)  [GCC 7.5.0]`
- espnet version: `espnet 0.10.6a1`
- pytorch version: `pytorch 1.8.1+cu102`
- Git hash: `fa1b865352475b744c37f70440de1cc6b257ba70`
  - Commit date: `Wed Feb 16 16:42:36 2022 -0500`

## asr_blstm_specaug_num_time_mask_2_lr_0.1
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_rnn_asr_model_valid.acc.ave/test_ru|7307|71189|79.3|18.4|2.4|2.1|22.8|71.1|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_rnn_asr_model_valid.acc.ave/test_ru|7307|537025|95.0|3.0|2.0|1.1|6.1|71.1|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_rnn_asr_model_valid.acc.ave/test_ru|7307|399162|93.2|4.5|2.3|1.4|8.2|71.1|

## ASR config

<details><summary>expand</summary>

```
config: conf/tuning/train_asr_rnn.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_blstm_specaug_num_time_mask_2_lr_0.1
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
max_epoch: 15
patience: 3
val_scheduler_criterion:
- valid
- loss
early_stopping_criterion:
- valid
- loss
- min
best_model_criterion:
-   - train
    - loss
    - min
-   - valid
    - loss
    - min
-   - train
    - acc
    - max
-   - valid
    - acc
    - max
keep_nbest_models:
- 10
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
batch_size: 30
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_ru_bpe150_sp/train/speech_shape
- exp/asr_stats_raw_ru_bpe150_sp/train/text_shape.bpe
valid_shape_file:
- exp/asr_stats_raw_ru_bpe150_sp/valid/speech_shape
- exp/asr_stats_raw_ru_bpe150_sp/valid/text_shape.bpe
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
-   - dump/raw/train_ru_sp/wav.scp
    - speech
    - sound
-   - dump/raw/train_ru_sp/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/dev_ru/wav.scp
    - speech
    - sound
-   - dump/raw/dev_ru/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adadelta
optim_conf:
    lr: 0.1
scheduler: null
scheduler_conf: {}
token_list:
- <blank>
- <unk>
- ▁
- е
- о
- и
- с
- м
- а
- в
- н
- д
- т
- у
- .
- я
- ы
- л
- й
- з
- п
- к
- но
- ','
- ▁в
- ра
- б
- ж
- ю
- г
- го
- ▁по
- ▁с
- ни
- ч
- х
- р
- ко
- ре
- ш
- ли
- ть
- ▁на
- ль
- ва
- ер
- ▁и
- ет
- ст
- ро
- на
- ла
- ле
- ь
- ен
- то
- ло
- да
- ка
- ▁не
- ств
- ти
- ци
- ся
- ▁за
- ▁про
- че
- ем
- ру
- же
- та
- ▁при
- ▁со
- ▁это
- ри
- ф
- ки
- бо
- ц
- ▁С
- ста
- ения
- щ
- сти
- э
- К
- О
- А
- И
- '-'
- Т
- Я
- Б
- Д
- М
- '?'
- –
- Г
- —
- '!'
- У
- ъ
- '"'
- »
- ё
- Ф
- ':'
- Х
- Ю
- F
- ;
- O
- I
- E
- R
- −
- В
- С
- ''''
- П
- C
- L
- A
- ‐
- H
- T
- G
- S
- (
- )
- B
- K
- P
- Z
- M
- Й
- X
- Ц
- Ж
- Ч
- Ш
- «
- З
- Л
- Е
- Р
- Э
- N
- Н
- <sos/eos>
init: null
input_size: null
ctc_conf:
    dropout_rate: 0.0
    ctc_type: builtin
    reduce: true
    ignore_nan_grad: true
joint_net_conf: null
model_conf:
    ctc_weight: 0.5
use_preprocessor: true
token_type: bpe
bpemodel: data/ru_token_list/bpe_unigram150/bpe.model
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
    stats_file: exp/asr_stats_raw_ru_bpe150_sp/train/feats_stats.npz
preencoder: null
preencoder_conf: {}
encoder: vgg_rnn
encoder_conf:
    rnn_type: lstm
    bidirectional: true
    use_projection: true
    num_layers: 4
    hidden_size: 1024
    output_size: 1024
postencoder: null
postencoder_conf: {}
decoder: rnn
decoder_conf:
    num_layers: 2
    hidden_size: 1024
    sampling_probability: 0
    att_conf:
        atype: location
        adim: 1024
        aconv_chans: 10
        aconv_filts: 100
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