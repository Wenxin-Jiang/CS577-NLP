---
language:
- hu
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- hu
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/xlsr_hungarian_new
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: hu
    metrics:
    - name: Test WER
      type: wer
      value: 0.2851621517163838
    - name: Test CER
      type: cer
      value: 0.06112982522287432
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: hu
    metrics:
    - name: Test WER
      type: wer
      value: 0.2851621517163838
    - name: Test CER
      type: cer
      value: 0.06112982522287432
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: hu
    metrics:
    - name: Test WER
      type: wer
      value: 47.15
---

# Akashpb13/xlsr_hungarian_new

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - hu dataset.
It achieves the following results on evaluation set (which is 10 percent of train data set merged with invalidated data, reported, other and dev datasets):
- Loss: 0.197464
- Wer: 0.330094
## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice hungarian train.tsv, dev.tsv, invalidated.tsv, reported.tsv, and other.tsv 
Only those points were considered where upvotes were greater than downvotes and duplicates were removed after concatenation of all the datasets given in common voice 7.0

## Training procedure
For creating the train dataset, all possible datasets were appended and 90-10 split was used. 

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 0.000095637994662983496
- train_batch_size: 16
- eval_batch_size: 16
- seed: 13
- gradient_accumulation_steps: 16
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 500
- num_epochs: 100
- mixed_precision_training: Native AMP


### Training results

| Step | Training Loss | Validation Loss | Wer      |
|------|---------------|-----------------|----------|
| 500  | 4.785300      | 0.952295        | 0.796236 |
| 1000 | 0.535800      | 0.217474        | 0.381613 |
| 1500 | 0.258400      | 0.205524        | 0.345056 |
| 2000 | 0.202800      | 0.198680        | 0.336264 |
| 2500 | 0.182700      | 0.197464        | 0.330094 |
     

### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.3
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/xlsr_hungarian_new --dataset mozilla-foundation/common_voice_8_0 --config hu --split test
```

