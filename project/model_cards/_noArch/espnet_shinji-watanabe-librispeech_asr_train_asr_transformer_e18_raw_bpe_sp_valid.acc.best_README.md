---
tags:
- espnet
- audio
- automatic-speech-recognition
language: en
datasets:
- librispeech
license: cc-by-4.0
inference: false
---

# ESPnet2 ASR pretrained model

## `Shinji Watanabe/librispeech_asr_train_asr_transformer_e18_raw_bpe_sp_valid.acc.best, fs=16k, lang=en`

♻️ Imported from <https://zenodo.org/record/3966501#.YOAOUZozZH5>

This model was trained by Shinji Watanabe using librispeech recipe in [espnet](https://github.com/espnet/espnet/).

### Python API

```text
See https://github.com/espnet/espnet_model_zoo
```

### Evaluate in the recipe

```python
# coming soon
```

### Results

```bash
# RESULTS
## Environments
- date: `Tue Jul 21 07:58:39 EDT 2020`
- python version: `3.7.3 (default, Mar 27 2019, 22:11:17)  [GCC 7.3.0]`
- espnet version: `espnet 0.8.0`
- pytorch version: `pytorch 1.4.0`
- Git hash: `75db853dd26a40d3d4dd979b2ff2457fbbb0cd69`
  - Commit date: `Mon Jul 20 10:49:12 2020 -0400`

## asr_train_asr_transformer_e18_raw_bpe_sp
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_dev_clean_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2703|54402|97.9|1.8|0.2|0.2|2.3|28.2|
|decode_dev_clean_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2703|54402|97.9|1.9|0.2|0.3|2.4|29.5|
|decode_dev_other_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2864|50948|94.6|4.7|0.7|0.7|6.0|46.6|
|decode_dev_other_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2864|50948|94.4|5.0|0.5|0.8|6.3|47.5|
|decode_test_clean_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2620|52576|97.7|2.0|0.3|0.3|2.6|30.4|
|decode_test_clean_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2620|52576|97.7|2.0|0.2|0.3|2.6|30.1|
|decode_test_other_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2939|52343|94.5|4.8|0.7|0.7|6.2|49.7|
|decode_test_other_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2939|52343|94.3|5.1|0.6|0.8|6.5|50.3|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_dev_clean_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2703|288456|99.3|0.3|0.3|0.2|0.9|28.2|
|decode_dev_clean_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2703|288456|99.3|0.4|0.3|0.2|0.9|29.5|
|decode_dev_other_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2864|265951|97.7|1.2|1.1|0.6|2.9|46.6|
|decode_dev_other_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2864|265951|97.7|1.3|1.0|0.8|3.0|47.5|
|decode_test_clean_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2620|281530|99.3|0.3|0.4|0.3|1.0|30.4|
|decode_test_clean_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2620|281530|99.4|0.3|0.3|0.3|0.9|30.1|
|decode_test_other_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2939|272758|97.8|1.1|1.1|0.7|2.9|49.7|
|decode_test_other_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2939|272758|97.9|1.2|0.9|0.8|2.9|50.3|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_dev_clean_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2703|69307|97.2|1.8|1.0|0.4|3.2|28.2|
|decode_dev_clean_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2703|69307|97.2|1.9|1.0|0.5|3.3|29.5|
|decode_dev_other_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2864|64239|93.3|4.4|2.2|1.2|7.9|46.6|
|decode_dev_other_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2864|64239|93.2|4.9|1.9|1.5|8.3|47.5|
|decode_test_clean_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2620|66712|97.0|1.9|1.1|0.4|3.3|30.4|
|decode_test_clean_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2620|66712|97.1|1.9|1.0|0.5|3.3|30.1|
|decode_test_other_decode_asr_beam_size20_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2939|66329|93.1|4.5|2.4|1.0|7.9|49.7|
|decode_test_other_decode_asr_beam_size5_lm_train_lm_adam_bpe_valid.loss.best_asr_model_valid.acc.best|2939|66329|93.1|4.8|2.1|1.4|8.3|50.3|
```

### Training config

See full config in [`config.yaml`](./exp/asr_train_asr_transformer_e18_raw_bpe_sp/config.yaml)

```yaml
config: conf/tuning/train_asr_transformer_e18.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_transformer_e18_raw_bpe_sp
ngpu: 1
seed: 0
num_workers: 1
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: 4
dist_rank: 3
local_rank: 3
dist_master_addr: localhost
dist_master_port: 33643
dist_launcher: null
multiprocessing_distributed: true
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
```
