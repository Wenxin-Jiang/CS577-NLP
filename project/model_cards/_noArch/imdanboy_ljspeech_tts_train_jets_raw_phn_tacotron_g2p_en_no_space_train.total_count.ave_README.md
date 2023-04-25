---
tags:
- espnet
- audio
- text-to-speech
language: en
datasets:
- ljspeech
license: cc-by-4.0
---

## ESPnet2 TTS model 

### `imdanboy/ljspeech_tts_train_jets_raw_phn_tacotron_g2p_en_no_space_train.total_count.ave`

This model was trained by imdanboy using ljspeech recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet
git checkout c173c30930631731e6836c274a591ad571749741
pip install -e .
cd egs2/ljspeech/tts1
./run.sh --skip_data_prep false --skip_train true --download_model imdanboy/ljspeech_tts_train_jets_raw_phn_tacotron_g2p_en_no_space_train.total_count.ave
```



## TTS config

<details><summary>expand</summary>

```
config: conf/tuning/train_jets.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_jets_raw_phn_tacotron_g2p_en_no_space
ngpu: 1
seed: 777
num_workers: 4
num_att_plot: 3
dist_backend: nccl
dist_init_method: env://
dist_world_size: 4
dist_rank: 0
local_rank: 0
dist_master_addr: localhost
dist_master_port: 39471
dist_launcher: null
multiprocessing_distributed: true
unused_parameters: true
sharded_ddp: false
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: false
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
    - text2mel_loss
    - min
-   - train
    - text2mel_loss
    - min
-   - train
    - total_count
    - max
keep_nbest_models: 5
nbest_averaging_interval: 0
grad_clip: -1
grad_clip_type: 2.0
grad_noise: false
accum_grad: 1
no_forward_run: false
resume: true
train_dtype: float32
use_amp: false
log_interval: 50
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
batch_bins: 3000000
valid_batch_bins: null
train_shape_file:
- exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/text_shape.phn
- exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/speech_shape
valid_shape_file:
- exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/valid/text_shape.phn
- exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/valid/speech_shape
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
-   - exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/collect_feats/pitch.scp
    - pitch
    - npy
-   - exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/collect_feats/energy.scp
    - energy
    - npy
valid_data_path_and_name_and_type:
-   - dump/raw/dev/text
    - text
    - text
-   - dump/raw/dev/wav.scp
    - speech
    - sound
-   - exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/valid/collect_feats/pitch.scp
    - pitch
    - npy
-   - exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/valid/collect_feats/energy.scp
    - energy
    - npy
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adamw
optim_conf:
    lr: 0.0002
    betas:
    - 0.8
    - 0.99
    eps: 1.0e-09
    weight_decay: 0.0
scheduler: exponentiallr
scheduler_conf:
    gamma: 0.999875
optim2: adamw
optim2_conf:
    lr: 0.0002
    betas:
    - 0.8
    - 0.99
    eps: 1.0e-09
    weight_decay: 0.0
scheduler2: exponentiallr
scheduler2_conf:
    gamma: 0.999875
generator_first: true
token_list:
- <blank>
- <unk>
- AH0
- N
- T
- D
- S
- R
- L
- DH
- K
- Z
- IH1
- IH0
- M
- EH1
- W
- P
- AE1
- AH1
- V
- ER0
- F
- ','
- AA1
- B
- HH
- IY1
- UW1
- IY0
- AO1
- EY1
- AY1
- .
- OW1
- SH
- NG
- G
- ER1
- CH
- JH
- Y
- AW1
- TH
- UH1
- EH2
- OW0
- EY2
- AO0
- IH2
- AE2
- AY2
- AA2
- UW0
- EH0
- OY1
- EY0
- AO2
- ZH
- OW2
- AE0
- UW2
- AH2
- AY0
- IY2
- AW2
- AA0
- ''''
- ER2
- UH2
- '?'
- OY2
- '!'
- AW0
- UH0
- OY0
- ..
- <sos/eos>
odim: null
model_conf: {}
use_preprocessor: true
token_type: phn
bpemodel: null
non_linguistic_symbols: null
cleaner: tacotron
g2p: g2p_en_no_space
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
    stats_file: exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/feats_stats.npz
tts: jets
tts_conf:
    generator_type: jets_generator
    generator_params:
        adim: 256
        aheads: 2
        elayers: 4
        eunits: 1024
        dlayers: 4
        dunits: 1024
        positionwise_layer_type: conv1d
        positionwise_conv_kernel_size: 3
        duration_predictor_layers: 2
        duration_predictor_chans: 256
        duration_predictor_kernel_size: 3
        use_masking: true
        encoder_normalize_before: true
        decoder_normalize_before: true
        encoder_type: transformer
        decoder_type: transformer
        conformer_rel_pos_type: latest
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
        generator_out_channels: 1
        generator_channels: 512
        generator_global_channels: -1
        generator_kernel_size: 7
        generator_upsample_scales:
        - 8
        - 8
        - 2
        - 2
        generator_upsample_kernel_sizes:
        - 16
        - 16
        - 4
        - 4
        generator_resblock_kernel_sizes:
        - 3
        - 7
        - 11
        generator_resblock_dilations:
        -   - 1
            - 3
            - 5
        -   - 1
            - 3
            - 5
        -   - 1
            - 3
            - 5
        generator_use_additional_convs: true
        generator_bias: true
        generator_nonlinear_activation: LeakyReLU
        generator_nonlinear_activation_params:
            negative_slope: 0.1
        generator_use_weight_norm: true
        segment_size: 64
        idim: 78
        odim: 80
    discriminator_type: hifigan_multi_scale_multi_period_discriminator
    discriminator_params:
        scales: 1
        scale_downsample_pooling: AvgPool1d
        scale_downsample_pooling_params:
            kernel_size: 4
            stride: 2
            padding: 2
        scale_discriminator_params:
            in_channels: 1
            out_channels: 1
            kernel_sizes:
            - 15
            - 41
            - 5
            - 3
            channels: 128
            max_downsample_channels: 1024
            max_groups: 16
            bias: true
            downsample_scales:
            - 2
            - 2
            - 4
            - 4
            - 1
            nonlinear_activation: LeakyReLU
            nonlinear_activation_params:
                negative_slope: 0.1
            use_weight_norm: true
            use_spectral_norm: false
        follow_official_norm: false
        periods:
        - 2
        - 3
        - 5
        - 7
        - 11
        period_discriminator_params:
            in_channels: 1
            out_channels: 1
            kernel_sizes:
            - 5
            - 3
            channels: 32
            downsample_scales:
            - 3
            - 3
            - 3
            - 3
            - 1
            max_downsample_channels: 1024
            bias: true
            nonlinear_activation: LeakyReLU
            nonlinear_activation_params:
                negative_slope: 0.1
            use_weight_norm: true
            use_spectral_norm: false
    generator_adv_loss_params:
        average_by_discriminators: false
        loss_type: mse
    discriminator_adv_loss_params:
        average_by_discriminators: false
        loss_type: mse
    feat_match_loss_params:
        average_by_discriminators: false
        average_by_layers: false
        include_final_outputs: true
    mel_loss_params:
        fs: 22050
        n_fft: 1024
        hop_length: 256
        win_length: null
        window: hann
        n_mels: 80
        fmin: 0
        fmax: null
        log_base: null
    lambda_adv: 1.0
    lambda_mel: 45.0
    lambda_feat_match: 2.0
    lambda_var: 1.0
    lambda_align: 2.0
    sampling_rate: 22050
    cache_generator_outputs: true
pitch_extract: dio
pitch_extract_conf:
    reduction_factor: 1
    use_token_averaged_f0: false
    fs: 22050
    n_fft: 1024
    hop_length: 256
    f0max: 400
    f0min: 80
pitch_normalize: global_mvn
pitch_normalize_conf:
    stats_file: exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/pitch_stats.npz
energy_extract: energy
energy_extract_conf:
    reduction_factor: 1
    use_token_averaged_energy: false
    fs: 22050
    n_fft: 1024
    hop_length: 256
    win_length: null
energy_normalize: global_mvn
energy_normalize_conf:
    stats_file: exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/energy_stats.npz
required:
- output_dir
- token_list
version: '202204'
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
