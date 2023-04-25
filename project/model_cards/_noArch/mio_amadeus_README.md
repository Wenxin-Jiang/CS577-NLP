---
tags:
- espnet
- audio
- text-to-speech
language: jp
datasets:
- amadeus
license: cc-by-4.0
---

## ESPnet2 TTS model 

### `mio/amadeus`

This model was trained by mio using [amadeus recipe](https://github.com/mio2333/espnet/tree/master/egs2/amadeus/tts1) in [espnet](https://github.com/espnet/espnet/).


### Demo: How to use in ESPnet2

Follow the [ESPnet installation instructions](https://espnet.github.io/espnet/installation.html)
if you haven't done that already.

```bash
cd espnet
git checkout d5b5ec7b2e77bd3e10707141818b7e6c57ac6b3f
pip install -e .
cd egs2/amadeus/tts1
./run.sh --skip_data_prep false --skip_train true --download_model mio/amadeus
```



## TTS config

<details><summary>expand</summary>

```
config: conf/tuning/finetune_vits.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_amadeus_vits_finetune_from_jsut_32_sentence
ngpu: 1
seed: 777
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
unused_parameters: true
sharded_ddp: false
cudnn_enabled: true
cudnn_benchmark: false
cudnn_deterministic: false
collect_stats: false
write_collected_feats: false
max_epoch: 2000
patience: null
val_scheduler_criterion:
- valid
- loss
early_stopping_criterion:
- valid
- loss
- min
best_model_criterion:
-   - train
    - total_count
    - max
keep_nbest_models: 3
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
create_graph_in_tensorboard: false
use_wandb: true
wandb_project: amadeus
wandb_id: null
wandb_entity: null
wandb_name: null
wandb_model_log_interval: -1
detect_anomaly: false
pretrain_path: null
init_param:
- downloads/f3698edf589206588f58f5ec837fa516/exp/tts_train_vits_raw_phn_jaconv_pyopenjtalk_accent_with_pause/train.total_count.ave_10best.pth:tts:tts
ignore_init_mismatch: false
freeze_param: []
num_iters_per_epoch: null
batch_size: 20
valid_batch_size: null
batch_bins: 5000000
valid_batch_bins: null
train_shape_file:
- exp/tts_stats_raw_linear_spectrogram_phn_jaconv_pyopenjtalk_accent_with_pause/train/text_shape.phn
- exp/tts_stats_raw_linear_spectrogram_phn_jaconv_pyopenjtalk_accent_with_pause/train/speech_shape
valid_shape_file:
- exp/tts_stats_raw_linear_spectrogram_phn_jaconv_pyopenjtalk_accent_with_pause/valid/text_shape.phn
- exp/tts_stats_raw_linear_spectrogram_phn_jaconv_pyopenjtalk_accent_with_pause/valid/speech_shape
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
-   - dump/22k/raw/train/text
    - text
    - text
-   - dump/22k/raw/train/wav.scp
    - speech
    - sound
valid_data_path_and_name_and_type:
-   - dump/22k/raw/dev/text
    - text
    - text
-   - dump/22k/raw/dev/wav.scp
    - speech
    - sound
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adamw
optim_conf:
    lr: 0.0001
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
    lr: 0.0001
    betas:
    - 0.8
    - 0.99
    eps: 1.0e-09
    weight_decay: 0.0
scheduler2: exponentiallr
scheduler2_conf:
    gamma: 0.999875
generator_first: false
token_list:
- <blank>
- <unk>
- '1'
- '2'
- '0'
- '3'
- '4'
- '-1'
- '5'
- a
- o
- '-2'
- i
- '-3'
- u
- e
- k
- n
- t
- '6'
- r
- '-4'
- s
- N
- m
- pau
- '7'
- sh
- d
- g
- w
- '8'
- U
- '-5'
- I
- cl
- h
- y
- b
- '9'
- j
- ts
- ch
- '-6'
- z
- p
- '-7'
- f
- ky
- ry
- '-8'
- gy
- '-9'
- hy
- ny
- '-10'
- by
- my
- '-11'
- '-12'
- '-13'
- py
- '-14'
- '-15'
- v
- '10'
- '-16'
- '-17'
- '11'
- '-21'
- '-20'
- '12'
- '-19'
- '13'
- '-18'
- '14'
- dy
- '15'
- ty
- '-22'
- '16'
- '18'
- '19'
- '17'
- <sos/eos>
odim: null
model_conf: {}
use_preprocessor: true
token_type: phn
bpemodel: null
non_linguistic_symbols: null
cleaner: jaconv
g2p: pyopenjtalk_accent_with_pause
feats_extract: linear_spectrogram
feats_extract_conf:
    n_fft: 1024
    hop_length: 256
    win_length: null
normalize: null
normalize_conf: {}
tts: vits
tts_conf:
    generator_type: vits_generator
    generator_params:
        hidden_channels: 192
        spks: -1
        global_channels: -1
        segment_size: 32
        text_encoder_attention_heads: 2
        text_encoder_ffn_expand: 4
        text_encoder_blocks: 6
        text_encoder_positionwise_layer_type: conv1d
        text_encoder_positionwise_conv_kernel_size: 3
        text_encoder_positional_encoding_layer_type: rel_pos
        text_encoder_self_attention_layer_type: rel_selfattn
        text_encoder_activation_type: swish
        text_encoder_normalize_before: true
        text_encoder_dropout_rate: 0.1
        text_encoder_positional_dropout_rate: 0.0
        text_encoder_attention_dropout_rate: 0.1
        use_macaron_style_in_text_encoder: true
        use_conformer_conv_in_text_encoder: false
        text_encoder_conformer_kernel_size: -1
        decoder_kernel_size: 7
        decoder_channels: 512
        decoder_upsample_scales:
        - 8
        - 8
        - 2
        - 2
        decoder_upsample_kernel_sizes:
        - 16
        - 16
        - 4
        - 4
        decoder_resblock_kernel_sizes:
        - 3
        - 7
        - 11
        decoder_resblock_dilations:
        -   - 1
            - 3
            - 5
        -   - 1
            - 3
            - 5
        -   - 1
            - 3
            - 5
        use_weight_norm_in_decoder: true
        posterior_encoder_kernel_size: 5
        posterior_encoder_layers: 16
        posterior_encoder_stacks: 1
        posterior_encoder_base_dilation: 1
        posterior_encoder_dropout_rate: 0.0
        use_weight_norm_in_posterior_encoder: true
        flow_flows: 4
        flow_kernel_size: 5
        flow_base_dilation: 1
        flow_layers: 4
        flow_dropout_rate: 0.0
        use_weight_norm_in_flow: true
        use_only_mean_in_flow: true
        stochastic_duration_predictor_kernel_size: 3
        stochastic_duration_predictor_dropout_rate: 0.5
        stochastic_duration_predictor_flows: 4
        stochastic_duration_predictor_dds_conv_layers: 3
        vocabs: 85
        aux_channels: 513
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
    lambda_dur: 1.0
    lambda_kl: 1.0
    sampling_rate: 22050
    cache_generator_outputs: true
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
version: '202207'
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
