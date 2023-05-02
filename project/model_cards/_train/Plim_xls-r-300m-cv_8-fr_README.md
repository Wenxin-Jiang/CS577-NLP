---
language:
- fr
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
model-index:
- name: XLS-R-300m - French
  results:
  - task:
      name: Automatic Speech Recognition 
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: fr
    metrics:
       - name: Test WER
         type: wer
         value: to recompute with STEP 24000
       - name: Test CER
         type: cer
         value: to recompute with STEP 24000
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: fr
    metrics:
       - name: Test WER
         type: wer
         value: 35.29
       - name: Test CER
         type: cer
         value: 13.94

---

## Model description

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - FR dataset.

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 5.0 (extended to 7.0 with training with checkpoint)
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 2.9114        | 0.29  | 1000  | inf             | 0.9997 |
| 1.2436        | 0.57  | 2000  | inf             | 0.4310 |
| 1.0552        | 0.86  | 3000  | inf             | 0.3144 |
| 1.0044        | 1.15  | 4000  | inf             | 0.2814 |
| 0.9718        | 1.43  | 5000  | inf             | 0.2658 |
| 0.9502        | 1.72  | 6000  | inf             | 0.2566 |
| 0.9418        | 2.01  | 7000  | inf             | 0.2476 |
| 0.9215        | 2.29  | 8000  | inf             | 0.2420 |
| 0.9236        | 2.58  | 9000  | inf             | 0.2388 |
| 0.9014        | 2.87  | 10000 | inf             | 0.2354 |
| 0.8814        | 3.15  | 11000 | inf             | 0.2312 |
| 0.8809        | 3.44  | 12000 | inf             | 0.2285 |
| 0.8717        | 3.73  | 13000 | inf             | 0.2263 |
| 0.8787        | 4.01  | 14000 | inf             | 0.2218 |
| 0.8567        | 4.3   | 15000 | inf             | 0.2193 |
| 0.8488        | 4.59  | 16000 | inf             | 0.2187 |
| 0.8359        | 4.87  | 17000 | inf             | 0.2172 |

Training continued with checkpoint from STEP 17000:

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| /             | 5.16  | 18000 | inf             | 0.2176 |
| /             | 5.45  | 19000 | inf             | 0.2181 |
| /             | 5.73  | 20000 | inf             | 0.2155 |
| /             | 6.02  | 21000 | inf             | 0.2140 |
| /             | 6.31  | 22000 | inf             | 0.2124 |
| /             | 6.59  | 23000 | inf             | 0.2117 |
| /             | 6.88  | 24000 | inf             | 0.2116 |


It achieves the best result on the validation set on Step 24000:
- Wer: 0.2116

Got some issue with validation loss calculation.

### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.3.dev0
- Tokenizers 0.11.0

### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8` with split `test`

```bash
python eval.py --model_id Plim/xls-r-300m-cv_8-fr --dataset mozilla-foundation/common_voice_8_0 --config fr --split test
```

2. To evaluate on `speech-recognition-community-v2/dev_data`

```bash
python eval.py --model_id Plim/xls-r-300m-cv_8-fr --dataset speech-recognition-community-v2/dev_data --config fr --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```
