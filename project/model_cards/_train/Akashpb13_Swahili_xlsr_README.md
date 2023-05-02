---
language:
- sw
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
- sw
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/Swahili_xlsr
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: sw
    metrics:
    - name: Test WER
      type: wer
      value: 0.11763625454589981
    - name: Test CER
      type: cer
      value: 0.02884228669922436
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
      value: 0.11763625454589981
    - name: Test CER
      type: cer
      value: 0.02884228669922436
---

# Akashpb13/Swahili_xlsr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - hu dataset.
It achieves the following results on the evaluation set (which is 10 percent of train data set merged with dev datasets):
- Loss: 0.159032
- Wer: 0.187934
## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice Hausa train.tsv and dev.tsv
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
- num_epochs: 80
- mixed_precision_training: Native AMP


### Training results

| Step | Training Loss | Validation Loss | Wer      |
|------|---------------|-----------------|----------|
| 500  | 4.810000      | 2.168847        | 0.995747 |
| 1000 | 0.564200      | 0.209411        | 0.303485 |
| 1500 | 0.217700      | 0.153959        | 0.239534 |
| 2000 | 0.150700      | 0.139901        | 0.216327 |
| 2500 | 0.119400      | 0.137543        | 0.208828 |
| 3000 | 0.099500      | 0.140921        | 0.203045 |
| 3500 | 0.087100      | 0.138835        | 0.199649 |
| 4000 | 0.074600      | 0.141297        | 0.195844 |
| 4500 | 0.066600      | 0.148560        | 0.194127 |
| 5000 | 0.060400      | 0.151214        | 0.194388 |
| 5500 | 0.054400      | 0.156072        | 0.192187 |
| 6000 | 0.051100      | 0.154726        | 0.190322 |
| 6500 | 0.048200      | 0.159847        | 0.189538 |
| 7000 | 0.046400      | 0.158727        | 0.188307 |
| 7500 | 0.046500      | 0.159032        | 0.187934 |


### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.3
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/Swahili_xlsr --dataset mozilla-foundation/common_voice_8_0 --config sw --split test
```

