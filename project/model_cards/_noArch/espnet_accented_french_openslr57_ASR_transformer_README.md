---
tags:
- espnet
- audio
- automatic-speech-recognition
language: fr
datasets:
- accented french (openslr56)

license: cc-by-4.0
---


## ESPnet2  model

This model was trained by Dan Berrebbi using  recipe in [espnet](https://github.com/espnet/espnet/).

# RESULTS
## Environments
- date: `Sat Apr 16 14:14:45 EDT 2022`
- python version: `3.9.12 (main, Apr  5 2022, 06:56:58)  [GCC 7.5.0]`
- espnet version: `espnet 0.10.6a1`
- pytorch version: `pytorch 1.11.0+cu102`
- Git hash: `f6cbc61353e0a1cefe81ae596278f7db1f0b7dd9`
  - Commit date: `Fri Apr 15 18:31:26 2022 -0400`
- Model on HuggingFace repository : https://huggingface.co/espnet/accented_french_openslr57_ASR_transformer

## asr_transformer_baseline
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_asr_model_valid.acc.ave_10best/devtest|481|3172|97.4|1.6|1.0|0.2|2.8|15.0|
|decode_asr_asr_model_valid.acc.ave_10best/test|515|2941|85.2|13.4|1.3|9.1|23.9|58.4|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_asr_model_valid.acc.ave_10best/devtest|481|16205|98.7|0.2|1.1|0.2|1.5|15.0|
|decode_asr_asr_model_valid.acc.ave_10best/test|515|16233|95.8|2.0|2.2|2.1|6.3|58.4|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_asr_model_valid.acc.ave_10best/devtest|481|7555|98.1|0.6|1.4|0.3|2.2|15.0|
|decode_asr_asr_model_valid.acc.ave_10best/test|515|7998|88.9|6.7|4.5|1.3|12.4|58.4|



##  ASR config

<details><summary>expand</summary>

``` 
config: conf/tuning/train_asr_transformer.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_transformer_baseline
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
max_epoch: 100
patience: 15
val_scheduler_criterion:
- valid
- loss
early_stopping_criterion:
- valid
- loss
- min
best_model_criterion:
-   - valid
    - acc
    - max
keep_nbest_models: 10
nbest_averaging_interval: 0
grad_clip: 5
grad_clip_type: 2.0
grad_noise: false
accum_grad: 4
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
num_iters_per_epoch: null
batch_size: 16
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_bpe250/train/speech_shape
- exp/asr_stats_raw_bpe250/train/text_shape.bpe
valid_shape_file:
- exp/asr_stats_raw_bpe250/valid/speech_shape
- exp/asr_stats_raw_bpe250/valid/text_shape.bpe
batch_type: folded
valid_batch_type: null
fold_length:
- 80000
- 150
sort_in_batch: descending
sort_batch: descending
multiple_iterator: false
chunk_length: 500
chunk_shift_ratio: 0.5
num_cache_chunks: 1024
train_data_path_and_name_and_type:
-   - dump/raw/train/wav.scp
    - speech
    - sound
-   - dump/raw/train/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/dev/wav.scp
    - speech
    - sound
-   - dump/raw/dev/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 1
scheduler: noamlr
scheduler_conf:
    warmup_steps: 4000
token_list:
- <blank>
- <unk>
- ▁
- s
- u
- t
- ''''
- i
- r
- e
- a
- ▁est
- o
- ▁de
- l
- ▁a
- c
- é
- '-'
- n
- ▁d
- re
- ▁l
- ▁la
- m
- ▁que
- ▁n
- ce
- ▁le
- d
- ▁c
- ▁il
- 'on'
- p
- à
- ▁qui
- it
- ▁f
- is
- te
- ▁qu
- ▁un
- in
- ▁pas
- ▁ne
- ▁vous
- er
- ▁les
- ▁et
- en
- ▁ma
- ▁se
- ▁en
- ▁on
- f
- ent
- b
- ▁p
- ▁t
- ra
- ▁b
- ▁vo
- che
- ez
- ro
- le
- eur
- ne
- ▁m
- il
- or
- ▁vi
- vous
- ▁sa
- tre
- es
- ▁bien
- ie
- ▁ou
- ▁au
- ▁par
- ▁pa
- ▁h
- ir
- ▁bon
- ille
- me
- ▁ce
- ▁y
- ▁fait
- ▁des
- eau
- ▁avez
- and
- ur
- ant
- ▁du
- ▁mo
- h
- ▁co
- ▁plus
- ▁pour
- ▁une
- ▁je
- ▁faut
- ier
- sse
- ▁é
- eux
- nt
- ▁re
- ▁cha
- ▁sont
- que
- age
- ▁tout
- de
- y
- ▁son
- ▁tou
- â
- elle
- ée
- ▁dans
- ▁personne
- ▁va
- ▁pr
- ▁dé
- ▁con
- ▁ave
- ▁si
- aux
- ▁mais
- ▁me
- ▁peut
- ▁po
- nge
- ▁ba
- ▁comme
- ter
- ▁jamais
- ine
- ▁ch
- ▁quelle
- ▁j
- ▁mieux
- ment
- ion
- ette
- ▁cett
- ▁faire
- ▁vaut
- aire
- z
- ▁sur
- ▁homme
- ▁soi
- ▁mon
- ▁rien
- ▁nous
- ▁autre
- ▁perd
- ▁bou
- ▁combien
- ▁parle
- ▁donne
- omp
- ▁deux
- oir
- ▁ici
- ▁peu
- ▁grand
- ▁sou
- jours
- ▁pro
- sans
- ▁petit
- ▁femme
- ard
- ▁bonne
- ix
- use
- q
- ▁ami
- ▁êtes
- ▁point
- ▁être
- ▁prend
- ▁enfant
- ▁cour
- ▁mauvais
- ▁médecin
- ement
- ô
- û
- ▁veut
- ▁trop
- ation
- able
- ▁euh
- ▁fou
- jou
- ▁temps
- ▁allez
- ▁app
- x
- ▁chien
- ▁ça
- ▁doit
- ▁aller
- avoir
- puis
- ▁plai
- j
- ▁dire
- ▁maître
- ance
- éri
- ▁cheval
- ▁mort
- ▁monsieur
- ▁sui
- ▁fois
- ▁porte
- ▁alors
- ▁quelqu
- ▁couleur
- ▁arrive
- ▁besoin
- ▁chose
- ▁souvent
- ▁rend
- ▁plaît
- ▁bonjour
- ç
- ï
- /
- w
- œ
- k
- ù
- î
- ê
- è
- g
- F
- P
- A
- v
- <sos/eos>
init: xavier_uniform
input_size: null
ctc_conf:
    dropout_rate: 0.0
    ctc_type: builtin
    reduce: true
    ignore_nan_grad: true
joint_net_conf: null
model_conf:
    ctc_weight: 0.3
    lsm_weight: 0.1
    length_normalized_loss: false
use_preprocessor: true
token_type: bpe
bpemodel: data/token_list/bpe_unigram250/bpe.model
non_linguistic_symbols: null
cleaner: null
g2p: null
speech_volume_normalize: null
rir_scp: null
rir_apply_prob: 1.0
noise_scp: null
noise_apply_prob: 1.0
noise_db_range: '13_15'
frontend: default
frontend_conf:
    fs: 16k
specaug: specaug
specaug_conf:
    apply_time_warp: true
    time_warp_window: 5
    time_warp_mode: bicubic
    apply_freq_mask: true
    freq_mask_width_range:
    - 0
    - 30
    num_freq_mask: 2
    apply_time_mask: true
    time_mask_width_range:
    - 0
    - 40
    num_time_mask: 2
normalize: utterance_mvn
normalize_conf: {}
preencoder: null
preencoder_conf: {}
encoder: transformer
encoder_conf:
    input_layer: conv2d2
    num_blocks: 12
    linear_units: 2048
    dropout_rate: 0.1
    output_size: 256
    attention_heads: 4
    attention_dropout_rate: 0.0
postencoder: null
postencoder_conf: {}
decoder: transformer
decoder_conf:
    input_layer: embed
    num_blocks: 6
    linear_units: 2048
    dropout_rate: 0.1
required:
- output_dir
- token_list
version: 0.10.6a1
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
