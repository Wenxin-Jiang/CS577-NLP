---
tags:
- espnet
- audio
- text-to-speech
language: en
datasets:
- ryanspeech
license: cc-by-nc-4.0
widget:
- text: "This seems a very pleasant place, and I think I shall enjoy myself very much."
---
## RyanSpeech model (based on ESPnet2)

### `espnet/english_male_ryanspeech_tacotron`
This model was trained by [Rohola Zandie](https://scholar.google.com/citations?user=xv0jIe0AAAAJ&hl=en) using ryanspeech recipe in [espnet](https://github.com/espnet/espnet/). For the best results you need to download the vocoder separately from [here](https://drive.google.com/file/d/10GYvB_mIKzXzSjD67tSnBhknZRoBjsNb/view?usp=sharing) and then use the following code:

```

from espnet2.bin.tts_inference import Text2Speech
from scipy.io.wavfile import write

model = Text2Speech.from_pretrained(
    model_file="espnet/english_male_ryanspeech_tacotron",
    vocoder_file="path_to_vocoder/train_nodev_parallel_wavegan.v1.long/checkpoint-1000000steps.pkl"
)

output = model("This is a simple test.")

write("x.wav", 22050, output['wav'].numpy())
```


## Download the dataset
You can download RyanSpeech dataset from [here](https://www.kaggle.com/datasets/roholazandie/ryanspeech) or here.

## TTS config

<details><summary>expand</summary>

```
config: conf/train.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/tts_train_raw_phn_tacotron_g2p_en_no_space
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
grad_clip: 1.0
grad_clip_type: 2.0
grad_noise: false
accum_grad: 1
no_forward_run: false
resume: true
train_dtype: float32
use_amp: false
log_interval: null
pretrain_path: []
pretrain_key: []
num_iters_per_epoch: 500
batch_size: 20
valid_batch_size: null
batch_bins: 5120000
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
- AH0
- T
- N
- S
- R
- D
- L
- K
- IH1
- M
- EH1
- Z
- DH
- UW1
- AE1
- IH0
- AY1
- AH1
- W
- .
- P
- F
- IY1
- V
- ER0
- AA1
- B
- AO1
- HH
- EY1
- IY0
- ','
- Y
- NG
- OW1
- G
- AW1
- TH
- SH
- UH1
- '?'
- ER1
- JH
- CH
- OW0
- OW2
- EH2
- IH2
- EY2
- AA2
- AE2
- AY2
- ''''
- OY1
- UW0
- '!'
- AO2
- EH0
- ZH
- AH2
- AE0
- UW2
- AA0
- AY0
- IY2
- AW2
- AO0
- EY0
- ER2
- UH2
- '...'
- AW0
- UH0
- OY2
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
    fs: 22050
    fmin: 80
    fmax: 7600
    n_mels: 80
    hop_length: 256
    n_fft: 1024
    win_length: null
normalize: global_mvn
normalize_conf:
    stats_file: exp/tts_stats_raw_phn_tacotron_g2p_en_no_space/train/feats_stats.npz
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
distributed: false

```

</details>


### Citing RyanSpeech

```BibTex
@inproceedings{Zandie2021RyanSpeechAC,
  title={RyanSpeech: A Corpus for Conversational Text-to-Speech Synthesis},
  author={Rohola Zandie and Mohammad H. Mahoor and Julia Madsen and Eshrat S. Emamian},
  booktitle={Interspeech},
  year={2021}
}
```