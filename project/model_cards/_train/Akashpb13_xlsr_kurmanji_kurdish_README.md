---
language:
- kmr
- ku
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- kmr
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/xlsr_kurmanji_kurdish
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: kmr
    metrics:
    - name: Test WER
      type: wer
      value: 0.33073206986250464
    - name: Test CER
      type: cer
      value: 0.08035244447163924
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: kmr
    metrics:
    - name: Test WER
      type: wer
      value: 0.33073206986250464
    - name: Test CER
      type: cer
      value: 0.08035244447163924
---

# Akashpb13/xlsr_kurmanji_kurdish

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - hu dataset.
It achieves the following results on the evaluation set (which is 10 percent of train data set merged with invalidated data, reported, other, and dev datasets):
- Loss: 0.292389
- Wer: 0.388585
## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice Kurmanji Kurdish train.tsv, dev.tsv, invalidated.tsv, reported.tsv, and other.tsv 
Only those points were considered where upvotes were greater than downvotes and duplicates were removed after concatenation of all the datasets given in common voice 7.0

## Training procedure
For creating the training dataset, all possible datasets were appended and 90-10 split was used. 

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 0.000096
- train_batch_size: 16
- eval_batch_size: 16
- seed: 13
- gradient_accumulation_steps: 16
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 200
- num_epochs: 100
- mixed_precision_training: Native AMP


### Training results

| Step | Training Loss | Validation Loss | Wer      |
|------|---------------|-----------------|----------|
| 200  | 4.382500      | 3.183725        | 1.000000 |
| 400  | 2.870200      | 0.996664        | 0.781117 |
| 600  | 0.609900      | 0.333755        | 0.445052 |
| 800  | 0.326800      | 0.305729        | 0.403157 |
| 1000 | 0.255000      | 0.290734        | 0.391621 |
| 1200 | 0.226300      | 0.292389        | 0.388585 |

### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.1
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/xlsr_kurmanji_kurdish --dataset mozilla-foundation/common_voice_8_0 --config kmr --split test
```

