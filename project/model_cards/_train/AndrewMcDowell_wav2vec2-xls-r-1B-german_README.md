---
language:
- de
license: apache-2.0
tags:
- automatic-speech-recognition
- mozilla-foundation/common_voice_8_0
- generated_from_trainer
- robust-speech-event
- de
- hf-asr-leaderboard
datasets:
- mozilla-foundation/common_voice_8_0
model-index:
- name: XLS-R-300M - German
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 15.25
    - name: Test CER
      type: cer
      value: 3.78
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 35.29
    - name: Test CER
      type: cer
      value: 13.83
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Test Data
      type: speech-recognition-community-v2/eval_data
      args: de
    metrics:
    - name: Test WER
      type: wer
      value: 36.2
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-1b](https://huggingface.co/facebook/wav2vec2-xls-r-1b) on the MOZILLA-FOUNDATION/COMMON_VOICE_8_0 - DE dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1355
- Wer: 0.1532

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 7.5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 2000
- num_epochs: 2.5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|
| 1.0826        | 0.07  | 1000  | 0.4637          | 0.4654 |
| 1.118         | 0.15  | 2000  | 0.2595          | 0.2687 |
| 1.1268        | 0.22  | 3000  | 0.2635          | 0.2661 |
| 1.0919        | 0.29  | 4000  | 0.2417          | 0.2566 |
| 1.1013        | 0.37  | 5000  | 0.2414          | 0.2567 |
| 1.0898        | 0.44  | 6000  | 0.2546          | 0.2731 |
| 1.0808        | 0.51  | 7000  | 0.2399          | 0.2535 |
| 1.0719        | 0.59  | 8000  | 0.2353          | 0.2528 |
| 1.0446        | 0.66  | 9000  | 0.2427          | 0.2545 |
| 1.0347        | 0.73  | 10000 | 0.2266          | 0.2402 |
| 1.0457        | 0.81  | 11000 | 0.2290          | 0.2448 |
| 1.0124        | 0.88  | 12000 | 0.2295          | 0.2448 |
| 1.025         | 0.95  | 13000 | 0.2138          | 0.2345 |
| 1.0107        | 1.03  | 14000 | 0.2108          | 0.2294 |
| 0.9758        | 1.1   | 15000 | 0.2019          | 0.2204 |
| 0.9547        | 1.17  | 16000 | 0.2000          | 0.2178 |
| 0.986         | 1.25  | 17000 | 0.2018          | 0.2200 |
| 0.9588        | 1.32  | 18000 | 0.1992          | 0.2138 |
| 0.9413        | 1.39  | 19000 | 0.1898          | 0.2049 |
| 0.9339        | 1.47  | 20000 | 0.1874          | 0.2056 |
| 0.9268        | 1.54  | 21000 | 0.1797          | 0.1976 |
| 0.9194        | 1.61  | 22000 | 0.1743          | 0.1905 |
| 0.8987        | 1.69  | 23000 | 0.1738          | 0.1932 |
| 0.8884        | 1.76  | 24000 | 0.1703          | 0.1873 |
| 0.8939        | 1.83  | 25000 | 0.1633          | 0.1831 |
| 0.8629        | 1.91  | 26000 | 0.1549          | 0.1750 |
| 0.8607        | 1.98  | 27000 | 0.1550          | 0.1738 |
| 0.8316        | 2.05  | 28000 | 0.1512          | 0.1709 |
| 0.8321        | 2.13  | 29000 | 0.1481          | 0.1657 |
| 0.825         | 2.2   | 30000 | 0.1446          | 0.1627 |
| 0.8115        | 2.27  | 31000 | 0.1396          | 0.1583 |
| 0.7959        | 2.35  | 32000 | 0.1389          | 0.1569 |
| 0.7835        | 2.42  | 33000 | 0.1362          | 0.1545 |
| 0.7959        | 2.49  | 34000 | 0.1355          | 0.1531 |


### Framework versions

- Transformers 4.17.0.dev0
- Pytorch 1.10.2+cu102
- Datasets 1.18.2.dev0
- Tokenizers 0.11.0

#### Evaluation Commands
1. To evaluate on `mozilla-foundation/common_voice_8_0` with split `test`

```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-1B-german --dataset mozilla-foundation/common_voice_8_0 --config de --split test --log_outputs
```

2. To evaluate on test dev data
```bash
python ./eval.py --model_id AndrewMcDowell/wav2vec2-xls-r-1B-german --dataset speech-recognition-community-v2/dev_data --config de --split validation --chunk_length_s 5.0 --stride_length_s 1.0
```