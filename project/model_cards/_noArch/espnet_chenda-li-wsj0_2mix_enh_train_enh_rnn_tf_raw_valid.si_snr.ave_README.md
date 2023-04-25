---
tags:
- espnet
- audio
- audio-source-separation
- audio-to-audio
language: en
datasets:
- wsj0_2mix
license: cc-by-4.0
inference: false
---

# ESPnet2 ENH pretrained model

## `Chenda Li/wsj0_2mix_enh_train_enh_rnn_tf_raw_valid.si_snr.ave, fs=8k, lang=en`

♻️ Imported from <https://zenodo.org/record/4498554#.YOAOEpozZH4>.

This model was trained by Chenda Li using wsj0_2mix recipe in [espnet](https://github.com/espnet/espnet/).

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
- date: `Thu Feb  4 01:08:19 CST 2021`
- python version: `3.7.6 (default, Jan  8 2020, 19:59:22)  [GCC 7.3.0]`
- espnet version: `espnet 0.9.7`
- pytorch version: `pytorch 1.5.0`
- Git hash: `a3334220b0352931677946d178fade3313cf82bb`
  - Commit date: `Fri Jan 29 23:35:47 2021 +0800`


## enh_train_enh_rnn_tf_raw

config: conf/tuning/train_enh_rnn_tf.yaml

|dataset|STOI|SAR|SDR|SIR|
|---|---|---|---|---|
|enhanced_cv_min_8k|0.891065|11.556|10.3982|18.0655|
|enhanced_tt_min_8k|0.896373|11.4086|10.2433|18.0496|
```

### Training config

See full config in [`config.yaml`](./exp/enh_train_enh_rnn_tf_raw/config.yaml)

```yaml
config: conf/tuning/train_enh_rnn_tf.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/enh_train_enh_rnn_tf_raw
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
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
```
