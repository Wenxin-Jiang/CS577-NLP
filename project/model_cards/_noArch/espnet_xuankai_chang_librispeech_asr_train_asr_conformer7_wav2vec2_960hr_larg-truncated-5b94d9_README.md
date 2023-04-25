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

## `Xuankai Chang/xuankai_chang_librispeech_asr_train_asr_conformer7_wav2vec2_960hr_large_raw_en_bpe5000_sp_25epoch, fs=16k, lang=en`

This model was trained by Takashi Maekaku using librispeech recipe in [espnet](https://github.com/espnet/espnet/).

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
- date: `Sat Jul  3 23:10:19 JST 2021`
- python version: `3.7.9 (default, Apr 23 2021, 13:48:31)  [GCC 5.5.0 20171010]`
- espnet version: `espnet 0.9.9`
- pytorch version: `pytorch 1.7.0`
- Git hash: `0f7558a716ab830d0c29da8785840124f358d47b`
  - Commit date: `Tue Jun 8 15:33:49 2021 -0400`

## asr_train_asr_conformer7_wav2vec2_960hr_large_raw_en_bpe5000_sp
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/dev_clean|2703|54402|98.3|1.6|0.2|0.2|1.9|24.9|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/dev_other|2864|50948|95.1|4.3|0.6|0.4|5.4|42.8|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/test_clean|2620|52576|98.1|1.7|0.2|0.2|2.2|26.8|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/test_other|2939|52343|95.3|4.1|0.6|0.5|5.2|45.8|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/dev_clean|2703|288456|99.5|0.2|0.2|0.2|0.6|24.9|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/dev_other|2864|265951|98.1|1.0|0.9|0.5|2.4|42.8|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/test_clean|2620|281530|99.5|0.2|0.3|0.2|0.7|26.8|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/test_other|2939|272758|98.3|0.8|0.9|0.5|2.3|45.8|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/dev_clean|2703|68010|97.8|1.6|0.6|0.4|2.6|24.9|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/dev_other|2864|63110|94.1|4.3|1.6|1.1|7.0|42.8|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/test_clean|2620|65818|97.6|1.6|0.8|0.4|2.8|26.8|
|decode_asr_lm_lm_train_lm_transformer2_en_bpe5000_17epoch_asr_model_valid.acc.best/test_other|2939|65101|94.3|4.0|1.8|1.0|6.7|45.8|
```

### Training config

See full config in [`config.yaml`](./exp/asr_train_asr_conformer7_hubert_960hr_large_raw_en_bpe5000_sp/config.yaml)

```yaml
config: conf/tuning/train_asr_conformer7_hubert_960hr_large.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_conformer7_hubert_960hr_large_raw_en_bpe5000_sp
ngpu: 3
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

