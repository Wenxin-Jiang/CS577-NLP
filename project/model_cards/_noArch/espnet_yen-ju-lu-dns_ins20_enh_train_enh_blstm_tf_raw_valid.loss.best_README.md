---
tags:
- espnet
- audio
- audio-source-separation
- audio-to-audio
language: en
datasets:
- dns_ins20
license: cc-by-4.0
inference: false
---

# ESPnet2 ENH pretrained model

## `neillu23/dns_ins20_enh_train_enh_blstm_tf_raw_valid.loss.best, fs=16k, lang=en`

♻️ Imported from <https://zenodo.org/record/4923697#.YOAOIpozZH4>.

This model was trained by neillu23 using dns_ins20 recipe in [espnet](https://github.com/espnet/espnet/).

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
- date: `Wed Jun  9 09:49:34 CST 2021`
- python version: `3.8.10 (default, May 19 2021, 18:05:58)  [GCC 7.3.0]`
- espnet version: `espnet 0.9.9`
- pytorch version: `pytorch 1.4.0`
- Git hash: `c1dfefb98bf59f654e0907b9681668eaca8ddfcc`
  - Commit date: `Tue Jun 8 17:23:26 2021 +0800`


## enh_train_enh_blstm_tf_raw

config: ./conf/tuning/train_enh_blstm_tf.yaml

|dataset|STOI|SAR|SDR|SIR|
|---|---|---|---|---|
|enhanced_cv_synthetic|0.98|23.87|23.87|0.00|
|enhanced_tt_synthetic_no_reverb|0.96|15.94|15.94|0.00|
|enhanced_tt_synthetic_with_reverb|0.84|11.86|11.86|0.00|
```

### Training config

See full config in [`config.yaml`](./exp/enh_train_enh_blstm_tf_raw/config.yaml)

```yaml
config: ./conf/tuning/train_enh_blstm_tf.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/enh_train_enh_blstm_tf_raw
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
dist_master_port: 45398
dist_launcher: null
multiprocessing_distributed: true
unused_parameters: false
sharded_ddp: false
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: true
```
