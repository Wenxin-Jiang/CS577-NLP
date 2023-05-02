---
language:
- ha
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- ha
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- robust-speech-event
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/Hausa_xlsr
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ha
    metrics:
    - name: Test WER
      type: wer
      value: 0.20614541257934219
    - name: Test CER
      type: cer
      value: 0.04358048053214061
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ha
    metrics:
    - name: Test WER
      type: wer
      value: 0.20614541257934219
    - name: Test CER
      type: cer
      value: 0.04358048053214061
---

# Akashpb13/Hausa_xlsr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) 
It achieves the following results on the evaluation set (which is 10 percent of train data set merged with invalidated data, reported, other, and dev datasets):
- Loss: 0.275118
- Wer: 0.329955
## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice Hausa train.tsv, dev.tsv, invalidated.tsv, reported.tsv and other.tsv 
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
- num_epochs: 50
- mixed_precision_training: Native AMP


### Training results

| Step | Training Loss | Validation Loss | Wer      |
|------|---------------|-----------------|----------|
| 500  | 5.175900      | 2.750914        | 1.000000 |
| 1000 | 1.028700      | 0.338649        | 0.497999 |
| 1500 | 0.332200      | 0.246896        | 0.402241 |
| 2000 | 0.227300      | 0.239640        | 0.395839 |
| 2500 | 0.175000      | 0.239577        | 0.373966 |
| 3000 | 0.140400      | 0.243272        | 0.356095 |
| 3500 | 0.119200      | 0.263761        | 0.365164 |
| 4000 | 0.099300      | 0.265954        | 0.353428 |
| 4500 | 0.084400      | 0.276367        | 0.349693 |
| 5000 | 0.073700      | 0.282631        | 0.343825 |
| 5500 | 0.068000      | 0.282344        | 0.341158 |
| 6000 | 0.064500      | 0.281591        | 0.342491 |

	


### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.3
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/Hausa_xlsr --dataset mozilla-foundation/common_voice_8_0 --config ha --split test
```

