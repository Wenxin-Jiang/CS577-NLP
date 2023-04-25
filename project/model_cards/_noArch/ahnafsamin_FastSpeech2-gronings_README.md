---
tags:
- text-to-speech
- gronings
- FastSpeech 2
language: gos
datasets:
- gronings
license: afl-3.0
---
## GroTTS Model 

This model was trained with the [FastSpeech 2](https://arxiv.org/abs/2006.04558) architecture using approx. 2 hours of Gronings TTS dataset. For the best results, you need to download the vocoder separately from [here](https://huggingface.co/ahnafsamin/parallelwavegan-gronings) and then use the following code:
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

The GroTTS model is deployed [here](https://huggingface.co/spaces/ahnafsamin/GroTTS-FastSpeech2).

## TTS config

<details><summary>expand</summary>

```
config: conf/tuning/train_fastspeech2.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_fastspeech2_raw_char_tacotron
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
max_epoch: 1000
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
accum_grad: 8
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
num_iters_per_epoch: 800
batch_size: 20
valid_batch_size: null
batch_bins: 3000000
valid_batch_bins: null
train_shape_file:
- exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/text_shape.char
- exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/speech_shape
valid_shape_file:
- exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/valid/text_shape.char
- exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/valid/speech_shape
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
-   - exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/tr_no_dev/durations
    - durations
    - text_int
-   - dump/raw/tr_no_dev/wav.scp
    - speech
    - sound
-   - exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/collect_feats/pitch.scp
    - pitch
    - npy
-   - exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/collect_feats/energy.scp
    - energy
    - npy
valid_data_path_and_name_and_type:
-   - dump/raw/dev/text
    - text
    - text
-   - exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/dev/durations
    - durations
    - text_int
-   - dump/raw/dev/wav.scp
    - speech
    - sound
-   - exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/valid/collect_feats/pitch.scp
    - pitch
    - npy
-   - exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/valid/collect_feats/energy.scp
    - energy
    - npy
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 1.0
scheduler: noamlr
scheduler_conf:
    model_size: 384
    warmup_steps: 4000
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
    stats_file: exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/feats_stats.npz
tts: fastspeech2
tts_conf:
    adim: 384
    aheads: 2
    elayers: 4
    eunits: 1536
    dlayers: 4
    dunits: 1536
    positionwise_layer_type: conv1d
    positionwise_conv_kernel_size: 3
    duration_predictor_layers: 2
    duration_predictor_chans: 256
    duration_predictor_kernel_size: 3
    postnet_layers: 5
    postnet_filts: 5
    postnet_chans: 256
    use_masking: true
    use_scaled_pos_enc: true
    encoder_normalize_before: true
    decoder_normalize_before: true
    reduction_factor: 1
    init_type: xavier_uniform
    init_enc_alpha: 1.0
    init_dec_alpha: 1.0
    transformer_enc_dropout_rate: 0.2
    transformer_enc_positional_dropout_rate: 0.2
    transformer_enc_attn_dropout_rate: 0.2
    transformer_dec_dropout_rate: 0.2
    transformer_dec_positional_dropout_rate: 0.2
    transformer_dec_attn_dropout_rate: 0.2
    pitch_predictor_layers: 5
    pitch_predictor_chans: 256
    pitch_predictor_kernel_size: 5
    pitch_predictor_dropout: 0.5
    pitch_embed_kernel_size: 1
    pitch_embed_dropout: 0.0
    stop_gradient_from_pitch_predictor: true
    energy_predictor_layers: 2
    energy_predictor_chans: 256
    energy_predictor_kernel_size: 3
    energy_predictor_dropout: 0.5
    energy_embed_kernel_size: 1
    energy_embed_dropout: 0.0
    stop_gradient_from_energy_predictor: false
pitch_extract: dio
pitch_extract_conf:
    fs: 22050
    n_fft: 1024
    hop_length: 256
    f0max: 400
    f0min: 80
    reduction_factor: 1
pitch_normalize: global_mvn
pitch_normalize_conf:
    stats_file: exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/pitch_stats.npz
energy_extract: energy
energy_extract_conf:
    fs: 22050
    n_fft: 1024
    hop_length: 256
    win_length: null
    reduction_factor: 1
energy_normalize: global_mvn
energy_normalize_conf:
    stats_file: exp/tts_train_raw_char_tacotron/decode_use_teacher_forcingtrue_train.loss.ave/stats/train/energy_stats.npz
required:
- output_dir
- token_list
version: 0.10.7a1
distributed: false

```
</details>