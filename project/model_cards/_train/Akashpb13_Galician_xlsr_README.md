---
language:
- gl
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- gl
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/Galician_xlsr
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
      value: 0.11308483789555426
    - name: Test CER
      type: cer
      value: 0.023982371794871796
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: gl
    metrics:
    - name: Test WER
      type: wer
      value: 0.11308483789555426
    - name: Test CER
      type: cer
      value: 0.023982371794871796
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8.0
      type: mozilla-foundation/common_voice_8_0
      args: gl
    metrics:
    - name: Test WER
      type: wer
      value: 11.31
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: gl
    metrics:
    - name: Test WER
      type: wer
      value: 39.05
---

# Akashpb13/Galician_xlsr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - hu dataset.
It achieves the following results on the evaluation set (which is 10 percent of train data set merged with invalidated data, reported, other, and dev datasets):
- Loss: 0.137096
- Wer: 0.196230
## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice Galician train.tsv, dev.tsv, invalidated.tsv, reported.tsv, and other.tsv 
Only those points were considered where upvotes were greater than downvotes and duplicates were removed after concatenation of all the datasets given in common voice 7.0

## Training procedure
For creating the training dataset, all possible datasets were appended and 90-10 split was used. 

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 0.000096
- train_batch_size: 16
- eval_batch_size: 16
- seed: 13
- gradient_accumulation_steps: 2
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 500
- num_epochs: 100
- mixed_precision_training: Native AMP


### Training results

| Step | Training Loss | Validation Loss | Wer      |
|------|---------------|-----------------|----------|
| 500  | 5.038100      | 3.035432        | 1.000000 |
| 1000 | 2.180000      | 0.406300        | 0.557964 |
| 1500 | 0.331700      | 0.153797        | 0.262394 |
| 2000 | 0.171600      | 0.145268        | 0.235627 |
| 2500 | 0.125900      | 0.136622        | 0.228087 |
| 3000 | 0.105400      | 0.131650        | 0.224128 |
| 3500 | 0.087600      | 0.141032        | 0.217531 |
| 4000 | 0.078300      | 0.143675        | 0.214515 |
| 4500 | 0.070000      | 0.144607        | 0.208106 |
| 5000 | 0.061500      | 0.135259        | 0.202828 |
| 5500 | 0.055600      | 0.130638        | 0.203959 |
| 6000 | 0.050500      | 0.137416        | 0.202451 |
| 6500 | 0.046600      | 0.140379        | 0.200000 |
| 7000 | 0.040800      | 0.140179        | 0.200377 |
| 7500 | 0.041000      | 0.138089        | 0.196795 |
| 8000 | 0.038400      | 0.136927        | 0.197172 |

### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.3
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/Galician_xlsr --dataset mozilla-foundation/common_voice_8_0 --config gl --split test
```

