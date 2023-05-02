---
language:
- or
license: apache-2.0
tags:
- automatic-speech-recognition
- generated_from_trainer
- hf-asr-leaderboard
- model_for_talk
- mozilla-foundation/common_voice_8_0
- or
- robust-speech-event
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-or-dx12
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 8
      type: mozilla-foundation/common_voice_8_0
      args: or
    metrics:
    - name: Test WER
      type: wer
      value: 0.5947242206235012
    - name: Test CER
      type: cer
      value: 0.18272388876724327
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Robust Speech Event - Dev Data
      type: speech-recognition-community-v2/dev_data
      args: or
    metrics:
    - name: Test WER
      type: wer
      value: NA
    - name: Test CER
      type: cer
      value: NA
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-or-dx12

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4638
- Wer: 0.5602

### Evaluation Commands

1. To evaluate on mozilla-foundation/common_voice_8_0 with test split

python eval.py --model_id DrishtiSharma/wav2vec2-large-xls-r-300m-or-dx12 --dataset mozilla-foundation/common_voice_8_0 --config or --split test --log_outputs

2. To evaluate on speech-recognition-community-v2/dev_data

Oriya language isn't available in speech-recognition-community-v2/dev_data

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0004
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 200
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Wer    |
|:-------------:|:------:|:----:|:---------------:|:------:|
| 13.5059       | 4.17   | 100  | 10.3789         | 1.0    |
| 4.5964        | 8.33   | 200  | 4.3294          | 1.0    |
| 3.4448        | 12.5   | 300  | 3.7903          | 1.0    |
| 3.3683        | 16.67  | 400  | 3.5289          | 1.0    |
| 2.042         | 20.83  | 500  | 1.1531          | 0.7857 |
| 0.5721        | 25.0   | 600  | 1.0267          | 0.7646 |
| 0.3274        | 29.17  | 700  | 1.0773          | 0.6938 |
| 0.2466        | 33.33  | 800  | 1.0323          | 0.6647 |
| 0.2047        | 37.5   | 900  | 1.1255          | 0.6733 |
| 0.1847        | 41.67  | 1000 | 1.1194          | 0.6515 |
| 0.1453        | 45.83  | 1100 | 1.1215          | 0.6601 |
| 0.1367        | 50.0   | 1200 | 1.1898          | 0.6627 |
| 0.1334        | 54.17  | 1300 | 1.3082          | 0.6687 |
| 0.1041        | 58.33  | 1400 | 1.2514          | 0.6177 |
| 0.1024        | 62.5   | 1500 | 1.2055          | 0.6528 |
| 0.0919        | 66.67  | 1600 | 1.4125          | 0.6369 |
| 0.074         | 70.83  | 1700 | 1.4006          | 0.6634 |
| 0.0681        | 75.0   | 1800 | 1.3943          | 0.6131 |
| 0.0709        | 79.17  | 1900 | 1.3545          | 0.6296 |
| 0.064         | 83.33  | 2000 | 1.2437          | 0.6237 |
| 0.0552        | 87.5   | 2100 | 1.3762          | 0.6190 |
| 0.056         | 91.67  | 2200 | 1.3763          | 0.6323 |
| 0.0514        | 95.83  | 2300 | 1.2897          | 0.6164 |
| 0.0409        | 100.0  | 2400 | 1.4257          | 0.6104 |
| 0.0379        | 104.17 | 2500 | 1.4219          | 0.5853 |
| 0.0367        | 108.33 | 2600 | 1.4361          | 0.6032 |
| 0.0412        | 112.5  | 2700 | 1.4713          | 0.6098 |
| 0.0353        | 116.67 | 2800 | 1.4132          | 0.6369 |
| 0.0336        | 120.83 | 2900 | 1.5210          | 0.6098 |
| 0.0302        | 125.0  | 3000 | 1.4686          | 0.5939 |
| 0.0398        | 129.17 | 3100 | 1.5456          | 0.6204 |
| 0.0291        | 133.33 | 3200 | 1.4111          | 0.5827 |
| 0.0247        | 137.5  | 3300 | 1.3866          | 0.6151 |
| 0.0196        | 141.67 | 3400 | 1.4513          | 0.5880 |
| 0.0218        | 145.83 | 3500 | 1.5100          | 0.5899 |
| 0.0196        | 150.0  | 3600 | 1.4936          | 0.5999 |
| 0.0164        | 154.17 | 3700 | 1.5012          | 0.5701 |
| 0.0168        | 158.33 | 3800 | 1.5601          | 0.5919 |
| 0.0151        | 162.5  | 3900 | 1.4891          | 0.5761 |
| 0.0137        | 166.67 | 4000 | 1.4839          | 0.5800 |
| 0.0143        | 170.83 | 4100 | 1.4826          | 0.5754 |
| 0.0114        | 175.0  | 4200 | 1.4950          | 0.5708 |
| 0.0092        | 179.17 | 4300 | 1.5008          | 0.5694 |
| 0.0104        | 183.33 | 4400 | 1.4774          | 0.5728 |
| 0.0096        | 187.5  | 4500 | 1.4948          | 0.5767 |
| 0.0105        | 191.67 | 4600 | 1.4557          | 0.5694 |
| 0.009         | 195.83 | 4700 | 1.4615          | 0.5628 |
| 0.0081        | 200.0  | 4800 | 1.4638          | 0.5602 |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.0+cu111
- Datasets 1.18.3
- Tokenizers 0.11.0
