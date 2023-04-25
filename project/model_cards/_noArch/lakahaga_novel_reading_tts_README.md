---
tags:
- espnet
- audio
- text-to-speech
language: ko
datasets:
- novelspeech
license: cc-by-4.0
---

## ESPnet2 TTS model 

### `lakahaga/novel_reading_tts`

This model was trained by lakahaga using novelspeech recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout 9827dfe37f69e8e55f902dc4e340de5108596311
pip install -e .
cd egs2/novelspeech/tts1
./run.sh --skip_data_prep false --skip_train true --download_model lakahaga/novel_reading_tts
```



## TTS config

<details><summary>expand</summary>

```
config: conf/tuning/train_conformer_fastspeech2.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_conformer_fastspeech2_raw_phn_tacotron_none
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
dist_master_port: 34177
dist_launcher: null
multiprocessing_distributed: true
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
accum_grad: 10
no_forward_run: false
resume: true
train_dtype: float32
use_amp: false
log_interval: null
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
batch_bins: 25600000
valid_batch_bins: null
train_shape_file:
- exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/text_shape.phn
- exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/speech_shape
valid_shape_file:
- exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//valid/text_shape.phn
- exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//valid/speech_shape
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
-   - exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/tr_no_dev/durations
    - durations
    - text_int
-   - dump/raw/tr_no_dev/wav.scp
    - speech
    - sound
-   - exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/collect_feats/pitch.scp
    - pitch
    - npy
-   - exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/collect_feats/energy.scp
    - energy
    - npy
-   - dump/raw/tr_no_dev/utt2sid
    - sids
    - text_int
valid_data_path_and_name_and_type:
-   - dump/raw/dev/text
    - text
    - text
-   - exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/dev/durations
    - durations
    - text_int
-   - dump/raw/dev/wav.scp
    - speech
    - sound
-   - exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//valid/collect_feats/pitch.scp
    - pitch
    - npy
-   - exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//valid/collect_feats/energy.scp
    - energy
    - npy
-   - dump/raw/dev/utt2sid
    - sids
    - text_int
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
- '='
- _
- A
- Y
- N
- O
- E
- U
- L
- G
- S
- D
- M
- J
- H
- B
- ZERO
- TWO
- C
- .
- Q
- ','
- P
- T
- SEVEN
- X
- W
- THREE
- ONE
- NINE
- K
- EIGHT
- '@'
- '!'
- Z
- '?'
- F
- SIX
- FOUR
- '#'
- $
- +
- '%'
- FIVE
- '~'
- AND
- '*'
- '...'
- ''
- ^
- <sos/eos>
odim: null
model_conf: {}
use_preprocessor: true
token_type: phn
bpemodel: null
non_linguistic_symbols: null
cleaner: tacotron
g2p: null
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
    stats_file: exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/feats_stats.npz
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
    encoder_normalize_before: true
    decoder_normalize_before: true
    reduction_factor: 1
    encoder_type: conformer
    decoder_type: conformer
    conformer_pos_enc_layer_type: rel_pos
    conformer_self_attn_layer_type: rel_selfattn
    conformer_activation_type: swish
    use_macaron_style_in_conformer: true
    use_cnn_in_conformer: true
    conformer_enc_kernel_size: 7
    conformer_dec_kernel_size: 31
    init_type: xavier_uniform
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
    stats_file: exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/pitch_stats.npz
energy_extract: energy
energy_extract_conf:
    fs: 22050
    n_fft: 1024
    hop_length: 256
    win_length: null
    reduction_factor: 1
energy_normalize: global_mvn
energy_normalize_conf:
    stats_file: exp/tts_train_raw_phn_tacotron_none/decode_use_teacher_forcingtrue_train.loss.best/stats//train/energy_stats.npz
required:
- output_dir
- token_list
version: 0.10.5a1
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




@inproceedings{hayashi2020espnet,
  title={{Espnet-TTS}: Unified, reproducible, and integratable open source end-to-end text-to-speech toolkit},
  author={Hayashi, Tomoki and Yamamoto, Ryuichi and Inoue, Katsuki and Yoshimura, Takenori and Watanabe, Shinji and Toda, Tomoki and Takeda, Kazuya and Zhang, Yu and Tan, Xu},
  booktitle={Proceedings of IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP)},
  pages={7654--7658},
  year={2020},
  organization={IEEE}
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
