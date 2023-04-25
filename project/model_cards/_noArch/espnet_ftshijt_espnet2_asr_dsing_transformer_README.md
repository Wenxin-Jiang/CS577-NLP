---
tags:
- espnet
- audio
- automatic-speech-recognition
language: noinfo
datasets:
- dsing
license: cc-by-4.0
---

## ESPnet2 ASR model 

### `espnet/ftshijt_espnet2_asr_dsing_transformer`

This model was trained by jiatong using dsing recipe in [espnet](https://github.com/espnet/espnet/).

### Demo: How to use in ESPnet2

```bash
cd espnet

pip install -e .
cd egs2/dsing/asr1
./run.sh --skip_data_prep false --skip_train true --download_model espnet/ftshijt_espnet2_asr_dsing_transformer
```

<!-- Generated by scripts/utils/show_asr_result.sh -->
# RESULTS
## Environments
- date: `Sun Mar 20 00:28:37 EDT 2022`
- python version: `3.9.7 (default, Sep 16 2021, 13:09:58)  [GCC 7.5.0]`
- espnet version: `espnet 0.10.7a1`
- pytorch version: `pytorch 1.10.1`
- Git hash: `c1ed71c6899e54c0b3dad82687886b1183cd0885`
  - Commit date: `Wed Mar 16 23:34:49 2022 -0400`

## asr_train_asr_raw_bpe500_sp
### WER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_bpe500_valid.loss.ave_asr_model_valid.acc.ave/dev|482|4018|77.0|16.2|6.8|4.0|27.0|65.1|
|decode_asr_lm_lm_train_lm_bpe500_valid.loss.ave_asr_model_valid.acc.ave/test|480|4632|76.1|17.3|6.6|3.7|27.6|57.7|

### CER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_bpe500_valid.loss.ave_asr_model_valid.acc.ave/dev|482|18692|85.0|5.8|9.2|4.2|19.2|65.1|
|decode_asr_lm_lm_train_lm_bpe500_valid.loss.ave_asr_model_valid.acc.ave/test|480|21787|84.9|6.3|8.8|4.2|19.3|57.7|

### TER

|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
|decode_asr_lm_lm_train_lm_bpe500_valid.loss.ave_asr_model_valid.acc.ave/dev|482|6097|75.2|12.8|12.0|4.1|28.9|65.1|
|decode_asr_lm_lm_train_lm_bpe500_valid.loss.ave_asr_model_valid.acc.ave/test|480|7736|75.3|14.3|10.4|4.1|28.8|57.7|

## ASR config

<details><summary>expand</summary>

```
config: conf/train_asr.yaml
print_config: false
log_level: INFO
dry_run: false
iterator_type: sequence
output_dir: exp/asr_train_asr_raw_bpe500_sp
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
num_iters_per_epoch: null
batch_size: 32
valid_batch_size: null
batch_bins: 1000000
valid_batch_bins: null
train_shape_file:
- exp/asr_stats_raw_bpe500_sp/train/speech_shape
- exp/asr_stats_raw_bpe500_sp/train/text_shape.bpe
valid_shape_file:
- exp/asr_stats_raw_bpe500_sp/valid/speech_shape
- exp/asr_stats_raw_bpe500_sp/valid/text_shape.bpe
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
-   - dump/raw/train30_sp/wav.scp
    - speech
    - kaldi_ark
-   - dump/raw/train30_sp/text
    - text
    - text
valid_data_path_and_name_and_type:
-   - dump/raw/dev/wav.scp
    - speech
    - kaldi_ark
-   - dump/raw/dev/text
    - text
    - text
allow_variable_data_keys: false
max_cache_size: 0.0
max_cache_fd: 32
valid_max_cache_size: null
optim: adam
optim_conf:
    lr: 1.0
scheduler: noamlr
scheduler_conf:
    warmup_steps: 25000
token_list:
- <blank>
- <unk>
- ▁I
- ''''
- ▁YOU
- S
- T
- ▁THE
- M
- ▁ME
- ▁A
- ▁AND
- ▁TO
- E
- A
- ING
- D
- ▁MY
- ▁
- O
- ▁IT
- I
- N
- RE
- Y
- ▁BE
- ▁IN
- ▁ON
- ▁LOVE
- U
- ▁WE
- LL
- H
- ▁YOUR
- ▁S
- IN
- ▁OF
- ▁DO
- ▁THAT
- ▁ALL
- L
- ▁DON
- ▁OH
- ▁LIKE
- ▁KNOW
- ▁FOR
- ▁CAN
- ▁JUST
- P
- ▁BUT
- ED
- K
- ▁WHEN
- ▁SO
- R
- ▁GO
- ▁WHAT
- ▁C
- ▁WITH
- W
- ▁F
- C
- ▁NO
- ER
- ▁ONE
- ▁LET
- VE
- ES
- ▁NOW
- ▁BABY
- G
- ▁GOT
- ▁COME
- CAUSE
- LE
- B
- ▁B
- AR
- ▁UP
- ▁'
- ▁W
- ▁SEE
- ▁TIME
- ▁ARE
- ▁G
- ▁LOOK
- ▁THIS
- F
- ▁IS
- ▁NEVER
- ▁M
- ▁P
- AN
- ▁WAS
- ▁WAY
- ▁IF
- OR
- ▁SAY
- V
- ▁R
- ▁T
- ▁DOWN
- RA
- ▁THERE
- ▁HEART
- ▁NOT
- RO
- ▁WILL
- ▁OUT
- CE
- ▁WANT
- ▁YEAH
- ▁HAVE
- ▁GIVE
- ▁TOO
- ▁GONNA
- ▁HOW
- ▁NEED
- ▁GET
- ▁TAKE
- ▁EVERY
- ▁FEEL
- ▁HE
- EN
- ▁FROM
- ▁HA
- ▁K
- ▁SHE
- 'ON'
- ▁DI
- RI
- ▁ONLY
- NE
- ▁WHO
- ▁AWAY
- ▁E
- ▁D
- ▁LIFE
- ▁MAKE
- IC
- ▁BACK
- ▁WHERE
- ▁MADE
- ▁DAY
- ▁HERE
- ▁LO
- ▁HER
- ▁AS
- ▁GOOD
- ▁WANNA
- ▁OOH
- ▁TELL
- LY
- TH
- ▁WON
- ▁LIGHT
- ▁KEEP
- ▁MA
- ▁LA
- ▁SH
- ▁WORLD
- ▁MORE
- ▁LI
- AL
- ▁COULD
- ▁GIRL
- ▁NOTHING
- ▁EVER
- ▁THINK
- IE
- ▁BY
- ▁AT
- ▁TONIGHT
- ▁THEY
- ▁CALL
- ▁HO
- ▁WOULD
- IL
- ▁OUR
- ▁FALL
- ▁NIGHT
- ▁THAN
- ▁DE
- ▁SOME
- ▁WAIT
- ▁RIGHT
- ▁RE
- ▁HALLELUJAH
- ▁TH
- NG
- ▁CO
- ▁WERE
- ▁TALK
- ET
- ▁BO
- ▁HOLD
- UR
- ▁BEEN
- ▁US
- ▁PA
- VER
- ▁EYES
- ▁DREAM
- ▁SONG
- ▁SHOULD
- ▁STILL
- ▁OVER
- TA
- ▁ANYMORE
- IGHT
- ▁STAY
- ▁BETTER
- LESS
- ▁THROUGH
- ▁LITTLE
- X
- ▁GONE
- ▁AIN
- ▁DA
- ▁HOLDING
- ▁HURT
- ▁TRY
- ▁FIND
- Z
- DE
- ▁LAST
- ▁SAID
- ▁ALWAYS
- ▁BODY
- ▁MIND
- ▁CRY
- ▁EVEN
- ▁RUN
- ▁HOPE
- ▁WITHOUT
- ▁MISS
- ▁ABOUT
- ▁HAND
- ▁J
- ▁AGAIN
- ▁THOUGH
- ▁NAH
- ▁LIVE
- ▁BA
- ▁OLD
- ▁HEAD
- ▁FIRE
- ▁MAN
- ▁SOMETHING
- ▁WHY
- THER
- ▁HOME
- ▁OR
- ▁INSIDE
- ▁NEW
- ▁HEY
- TION
- ▁EVERYTHING
- ▁HAD
- ▁SOMETIMES
- ▁HARD
- ▁TOUCH
- ▁HEAR
- ▁AM
- ▁MUCH
- ▁LONG
- ▁STAR
- GETTING
- ▁WALK
- ▁PEOPLE
- ▁BEFORE
- ▁CLOSE
- ▁TWO
- ▁FAR
- ▁SHOW
- ▁STAND
- ▁LOSE
- ▁HELP
- ▁NAME
- ▁BOY
- ▁TRUE
- ▁PLAY
- ▁DARK
- ▁THINGS
- ▁NA
- ▁TEAR
- ▁END
- ▁NOBODY
- ▁SEA
- ▁ROCKABYE
- ▁BELIEVE
- ▁BROKE
- ▁AROUND
- ▁START
- ▁KISS
- ▁FEELING
- ▁BREAK
- ▁SOMEONE
- ▁FRIEND
- ▁ALONE
- ▁BEAUTIFUL
- ▁CRAZY
- ▁OWN
- OSE
- ▁STOP
- ▁LOST
- ▁HIM
- ▁BAD
- ▁CHANCE
- ▁REALLY
- ▁WISH
- ▁MOVE
- ▁SKY
- ▁PLACE
- AKE
- ▁LEAVE
- ▁YA
- ▁STRONG
- ▁PUT
- ▁OPEN
- ▁WRONG
- ▁COLD
- OCK
- ▁USED
- ▁FOUND
- ▁LONELY
- ▁DANCE
- EACH
- ▁ANOTHER
- ▁SIDE
- ▁UNDER
- ▁MATTER
- ▁THESE
- ▁CARE
- ▁MINE
- ▁SHINE
- ▁AFRAID
- ▁TURN
- ▁PLEASE
- ▁SUN
- ▁DIAMOND
- ▁UNTIL
- ▁FACE
- ▁LEARN
- ▁TRUST
- ▁WONDER
- ▁BREATH
- ATE
- ▁SORRY
- ▁HU
- ▁WATCH
- ▁LATE
- ROUND
- ▁ARMS
- ▁PERFECT
- ▁MAYBE
- ▁PULL
- ▁REMEMBER
- ▁FIGHT
- ▁MYSELF
- ▁INTO
- ▁DARLING
- ▁THUNDER
- ▁FOLLOW
- ▁REASON
- ▁BURN
- ▁HIS
- ▁MUST
- ▁FREE
- ▁FLASHLIGHT
- ▁1
- ▁ENOUGH
- ▁DRINK
- ▁WORDS
- ▁HIDE
- ▁UN
- ▁FORGET
- ▁SURE
- ▁CHANGE
- ▁SMILE
- ▁PROMISE
- ▁FOREVER
- '2'
- ▁SWEET
- ▁SAME
- ▁OOOH
- ▁PART
- ▁SOMEBODY
- NESS
- ▁BRIGHT
- ▁HEAVEN
- ▁DEEP
- ▁HIGH
- ▁INSTEAD
- ▁MOMENT
- ▁ALONG
- ▁ALRIGHT
- ▁SLOW
- ▁TOMORROW
- ▁SOUL
- ▁QU
- ▁PUSH
- ▁CHANDELIER
- ▁LEFT
- SIDE
- ▁TOLD
- ▁KNEW
- READY
- ▁LOVING
- ▁SAW
- '3'
- ▁WORK
- ▁DANCING
- ▁THREE
- ▁SAVE
- ▁SHOOT
- ▁LEAD
- ▁SKI
- ▁WILD
- ▁WIND
- ▁WHILE
- ▁EDGE
- ▁HAPPY
- ▁FEAR
- STUCK
- ▁MOST
- ▁LISTEN
- ▁WOAH
- ▁FIRST
- ▁JOLENE
- ▁VOICE
- ▁COMP
- ▁MILLION
- FUL
- ▁OOOOOH
- ▁CAME
- ▁RISE
- ▁NEXT
- ▁COUNT
- ▁MOUNTAIN
- ▁ROOM
- ▁BLUE
- ▁HIT
- ▁RAISE
- J
- ▁THOUSAND
- ▁SHAP
- ▁TREAT
- ▁DRY
- ▁FINALLY
- ▁TITANIUM
- ▁CARRY
- ▁TRUTH
- ▁WATER
- ▁MORNING
- TIME
- ▁BELONG
- ▁UMA
- ▁ALIVE
- ▁ELSE
- ▁ANGEL
- ▁BRAND
- ▁APART
- ▁EVERYBODY
- ▁SOUND
- ▁GUESS
- ▁PRAY
- ▁FAITH
- ▁AFTER
- ▁THROW
- ▁TRIED
- ▁SLEEP
- ▁FOOL
- ▁DISCOVERING
- ▁FUCK
- ▁TASTE
- ▁UNDERSTAND
- ▁SHAME
- ▁POWER
- ▁WELCOME
- ▁FELT
- ▁SAFE
- ▁DESERVE
- ▁GAME
- ▁SUPERMA
- ▁SWEAR
- ▁BETWEEN
- ▁GLASS
- ▁CATCH
- ▁TOGETHER
- '0'
- '4'
- '6'
- '5'
- '1'
- '8'
- '7'
- '9'
- Q
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
bpemodel: data/token_list/bpe_unigram500/bpe.model
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
specaug: null
specaug_conf: {}
normalize: global_mvn
normalize_conf:
    stats_file: exp/asr_stats_raw_bpe500_sp/train/feats_stats.npz
preencoder: null
preencoder_conf: {}
encoder: transformer
encoder_conf:
    input_layer: conv2d
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
version: 0.10.7a1
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