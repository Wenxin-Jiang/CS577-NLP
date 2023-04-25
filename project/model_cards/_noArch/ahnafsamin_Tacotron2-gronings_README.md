---
tags:
- text-to-speech
- gronings
- Tacotron 2
language: gos
datasets:
- gronings
---
## GroTTS Model 

This model is trained with the [Tacotron 2](https://arxiv.org/abs/1712.05884) architecture using approx. 2 hours of Gronings TTS dataset. For the best results, you need to download the vocoder separately from [here](https://huggingface.co/ahnafsamin/parallelwavegan-gronings) and then use the following code:
```
from espnet2.bin.tts_inference import Text2Speech
from scipy.io.wavfile import write

model = Text2Speech.from_pretrained(
    model_file="path_to_the_model_file_in_pth_format",
    vocoder_file="path_to_the_vocoder_file_in_pkl_format"
)
output = model("This is a simple test.")
write("x.wav", 22050, output['wav'].numpy())
```


## TTS config

<details><summary>expand</summary>

```
config: conf/train.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_raw_char_tacotron
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
    - loss
    - min
-   - train
    - loss
    - min
keep_nbest_models: 5
nbest_averaging_interval: 0
grad_clip: 1.0
grad_clip_type: 2.0
grad_noise: false
accum_grad: 2
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
num_iters_per_epoch: 1000
batch_size: 20
valid_batch_size: null
batch_bins: 2000000
valid_batch_bins: null
train_shape_file:
- exp/tts_stats_raw_char_tacotron/train/text_shape.char
- exp/tts_stats_raw_char_tacotron/train/speech_shape
valid_shape_file:
- exp/tts_stats_raw_char_tacotron/valid/text_shape.char
- exp/tts_stats_raw_char_tacotron/valid/speech_shape
batch_type: numel
valid_batch_type: null
fold_length:
- 150
- 204800
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 500
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/tr_no_dev/text
    - text
    - text
-   - dump/raw/tr_no_dev/wav.scp
    - speech
    - sound
valid_data_path_and_name_and_type:
-   - dump/raw/dev/text
    - text
    - text
-   - dump/raw/dev/wav.scp
    - speech
    - sound
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 0.001
    eps: 1.0e-06
    weight_decay: 0.0
scheduler: null
scheduler_conf: {}
token_list:
- <blank>
- <unk>
- <space>
- E
- N
- A
- O
- T
- I
- R
- D
- L
- S
- K
- M
- G
- U
- H
- .
- W
- V
- Z
- P
- B
- ','
- J
- C
- F
- '?'
- ''''
- '!'
- Y
- X
- '`'
- <sos/eos>
odim: null
model_conf: {}
use_preprocessor: true
token_type: char
bpemodel: null
non_linguistic_symbols: null
cleaner: tacotron
g2p: g2p_en
feats_extract: fbank
feats_extract_conf:
    n_fft: 1024
    hop_length: 256
    win_length: null
    fs: 22050
    fmin: 80
    fmax: 7600
    n_mels: 80
normalize: global_mvn
normalize_conf:
    stats_file: exp/tts_stats_raw_char_tacotron/train/feats_stats.npz
tts: tacotron2
tts_conf:
    embed_dim: 512
    elayers: 1
    eunits: 512
    econv_layers: 3
    econv_chans: 512
    econv_filts: 5
    atype: location
    adim: 512
    aconv_chans: 32
    aconv_filts: 15
    cumulate_att_w: true
    dlayers: 2
    dunits: 1024
    prenet_layers: 2
    prenet_units: 256
    postnet_layers: 5
    postnet_chans: 512
    postnet_filts: 5
    output_activation: null
    use_batch_norm: true
    use_concate: true
    use_residual: false
    dropout_rate: 0.5
    zoneout_rate: 0.1
    reduction_factor: 1
    spk_embed_dim: null
    use_masking: true
    bce_pos_weight: 5.0
    use_guided_attn_loss: true
    guided_attn_loss_sigma: 0.4
    guided_attn_loss_lambda: 1.0
pitch_extract: null
pitch_extract_conf: {}
pitch_normalize: null
pitch_normalize_conf: {}
energy_extract: null
energy_extract_conf: {}
energy_normalize: null
energy_normalize_conf: {}
required:
- output_dir
- token_list
version: 0.10.7a1
distributed: false


```
</details>