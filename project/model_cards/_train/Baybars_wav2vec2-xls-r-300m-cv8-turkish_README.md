---
language:
- tr
license: apache-2.0
tags:
- automatic-speech-recognition
- common_voice
- generated_from_trainer
- hf-asr-leaderboard
- robust-speech-event
- tr
datasets:
- common_voice
model-index:
- name: ''
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the COMMON_VOICE - TR dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4164
- Wer: 0.3098
- Cer: 0.0764

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Language Model
N-gram language model is trained by [mpoyraz](https://huggingface.co/mpoyraz/wav2vec2-xls-r-300m-cv7-turkish) on a Turkish Wikipedia articles using KenLM and [ngram-lm-wiki](https://github.com/mpoyraz/ngram-lm-wiki) repo was used to generate arpa LM and convert it into binary format.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 64
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 100.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 0.6356        | 9.09  | 500  | 0.5055          | 0.5536 | 0.1381 |
| 0.3847        | 18.18 | 1000 | 0.4002          | 0.4247 | 0.1065 |
| 0.3377        | 27.27 | 1500 | 0.4193          | 0.4167 | 0.1078 |
| 0.2175        | 36.36 | 2000 | 0.4351          | 0.3861 | 0.0974 |
| 0.2074        | 45.45 | 2500 | 0.3962          | 0.3622 | 0.0916 |
| 0.159         | 54.55 | 3000 | 0.4062          | 0.3526 | 0.0888 |
| 0.1882        | 63.64 | 3500 | 0.3991          | 0.3445 | 0.0850 |
| 0.1766        | 72.73 | 4000 | 0.4214          | 0.3396 | 0.0847 |
| 0.116         | 81.82 | 4500 | 0.4182          | 0.3265 | 0.0812 |
| 0.0718        | 90.91 | 5000 | 0.4259          | 0.3191 | 0.0781 |
| 0.019         | 100.0 | 5500 | 0.4164          | 0.3098 | 0.0764 |


## Evaluation Commands
Please install [unicode_tr](https://pypi.org/project/unicode_tr/) package before running evaluation. It is used for Turkish text processing.
1. To evaluate on `mozilla-foundation/common_voice_7_0` with split `test`
```bash
python eval.py --model_id Baybars/wav2vec2-xls-r-300m-cv8-turkish --dataset mozilla-foundation/common_voice_8_0 --config tr --split test
```

2. To evaluate on `speech-recognition-community-v2/dev_data`

```bash
python eval.py --model_id Baybars/wav2vec2-xls-r-300m-cv8-turkish --dataset speech-recognition-community-v2/dev_data --config tr --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0
