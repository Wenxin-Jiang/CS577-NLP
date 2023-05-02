---
language:
- ckb
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- ckb
- robust-speech-event
- model_for_talk
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: Akashpb13/Central_kurdish_xlsr
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: ckb
    metrics:
    - name: Test WER
      type: wer
      value: 0.36754389884276845
    - name: Test CER
      type: cer
      value: 0.07827896768334217
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: ckb
    metrics:
    - name: Test WER
      type: wer
      value: 0.36754389884276845
    - name: Test CER
      type: cer
      value: 0.07827896768334217
---

# Akashpb13/Central_kurdish_xlsr

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_7_0 - hu dataset.
It achieves the following results on evaluation set (which is 10 percent of train data set merged with invalidated data, reported, other and dev datasets):
- Loss: 0.348580	
- Wer: 0.401147

## Model description
"facebook/wav2vec2-xls-r-300m" was finetuned.

## Intended uses & limitations
More information needed
## Training and evaluation data
Training data - 
Common voice Central Kurdish train.tsv, dev.tsv, invalidated.tsv, reported.tsv, and other.tsv 
Only those points were considered where upvotes were greater than downvotes and duplicates were removed after concatenation of all the datasets given in common voice 7.0

## Training procedure
For creating the train dataset, all possible datasets were appended and 90-10 split was used. 

### Training hyperparameters

The following hyperparameters were used during training:

- learning_rate: 0.000095637994662983496
- train_batch_size: 16
- eval_batch_size: 16
- seed: 13
- gradient_accumulation_steps: 2
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 200
- num_epochs: 100
- mixed_precision_training: Native AMP


### Training results

| Step  | Training Loss | Validation Loss | Wer      |
|-------|---------------|-----------------|----------|
| 500   | 5.097800      | 2.190326        | 1.001207 |
| 1000  | 0.797500      | 0.331392        | 0.576819 |
| 1500  | 0.405100      | 0.262009        | 0.549049 |
| 2000  | 0.322100      | 0.248178        | 0.479626 |
| 2500  | 0.264600      | 0.258866        | 0.488983 |
| 3000  | 0.228300      | 0.261523        | 0.469665 |
| 3500  | 0.201000      | 0.270135        | 0.451856 |
| 4000  | 0.180900      | 0.279302        | 0.448536 |
| 4500  | 0.163800      | 0.280921        | 0.459704 |
| 5000  | 0.147300      | 0.319249        | 0.471778 |
| 5500  | 0.137600      | 0.289546        | 0.449140 |
| 6000  | 0.132000      | 0.311350        | 0.458195 |
| 6500  | 0.117100      | 0.316726        | 0.432840 |
| 7000  | 0.109200      | 0.302210        | 0.439481 |
| 7500  | 0.104900      | 0.325913        | 0.439481 |
| 8000  | 0.097500      | 0.329446        | 0.431935 |
| 8500  | 0.088600      | 0.345259        | 0.425898 |
| 9000  | 0.084900      | 0.342891        | 0.428313 |
| 9500  | 0.080900      | 0.353081        | 0.424389 |
| 10000 | 0.075600      | 0.347063        | 0.424992 |
| 10500 | 0.072800      | 0.330086        | 0.424691 |
| 11000 | 0.068100      | 0.350658        | 0.421974 |
| 11500 | 0.064700      | 0.342949        | 0.413522 |
| 12000 | 0.061500      | 0.341704        | 0.415334 |
| 12500 | 0.059500      | 0.346279        | 0.411410 |
| 13000 | 0.057400      | 0.349901        | 0.407184 |
| 13500 | 0.056400      | 0.347733        | 0.402656 |
| 14000 | 0.053300      | 0.344899        | 0.405976 |
| 14500 | 0.052900      | 0.346708        | 0.402656 |
| 15000 | 0.050600      | 0.344118        | 0.400845 |
| 15500 | 0.050200      | 0.348396        | 0.402958 |
| 16000 | 0.049800      | 0.348312        | 0.401751 |
| 16500 | 0.051900      | 0.348372        | 0.401147 |
| 17000 | 0.049800      | 0.348580        | 0.401147 |

     

### Framework versions
- Transformers 4.16.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.18.1
- Tokenizers 0.10.3

#### Evaluation Commands

1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python eval.py --model_id Akashpb13/Central_kurdish_xlsr --dataset mozilla-foundation/common_voice_8_0 --config ckb --split test
```

