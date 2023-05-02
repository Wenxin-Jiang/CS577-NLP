---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
metrics:
- bleu
model-index:
- name: opus-mt-ar-en-finetuned-ar-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: opus_infopankki
      type: opus_infopankki
      args: ar-en
    metrics:
    - name: Bleu
      type: bleu
      value: 53.5086
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-ar-en-finetuned-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7636
- Bleu: 53.5086
- Gen Len: 13.5728

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 278  | 1.5114          | 35.2767 | 14.2084 |
| 1.6677        | 2.0   | 556  | 1.4025          | 37.5243 | 14.0245 |
| 1.6677        | 3.0   | 834  | 1.3223          | 39.4262 | 13.8101 |
| 1.4743        | 4.0   | 1112 | 1.2567          | 40.7045 | 13.8533 |
| 1.4743        | 5.0   | 1390 | 1.2001          | 41.8356 | 13.8083 |
| 1.3428        | 6.0   | 1668 | 1.1504          | 43.2448 | 13.6958 |
| 1.3428        | 7.0   | 1946 | 1.1072          | 44.177  | 13.6783 |
| 1.2595        | 8.0   | 2224 | 1.0701          | 45.17   | 13.6587 |
| 1.1829        | 9.0   | 2502 | 1.0345          | 45.9612 | 13.6706 |
| 1.1829        | 10.0  | 2780 | 1.0042          | 46.9009 | 13.6236 |
| 1.1188        | 11.0  | 3058 | 0.9760          | 47.7478 | 13.6205 |
| 1.1188        | 12.0  | 3336 | 0.9505          | 48.3082 | 13.6283 |
| 1.0735        | 13.0  | 3614 | 0.9270          | 48.9782 | 13.6203 |
| 1.0735        | 14.0  | 3892 | 0.9060          | 49.5541 | 13.6311 |
| 1.0269        | 15.0  | 4170 | 0.8869          | 49.9905 | 13.6222 |
| 1.0269        | 16.0  | 4448 | 0.8700          | 50.4806 | 13.6047 |
| 0.9983        | 17.0  | 4726 | 0.8538          | 50.9186 | 13.6159 |
| 0.9647        | 18.0  | 5004 | 0.8398          | 51.3492 | 13.6146 |
| 0.9647        | 19.0  | 5282 | 0.8271          | 51.7219 | 13.5275 |
| 0.9398        | 20.0  | 5560 | 0.8156          | 52.0177 | 13.5756 |
| 0.9398        | 21.0  | 5838 | 0.8053          | 52.3619 | 13.5807 |
| 0.9206        | 22.0  | 6116 | 0.7963          | 52.6051 | 13.5652 |
| 0.9206        | 23.0  | 6394 | 0.7885          | 52.8322 | 13.5669 |
| 0.9012        | 24.0  | 6672 | 0.7818          | 52.9402 | 13.5701 |
| 0.9012        | 25.0  | 6950 | 0.7762          | 53.1182 | 13.5695 |
| 0.8965        | 26.0  | 7228 | 0.7717          | 53.1596 | 13.5612 |
| 0.8836        | 27.0  | 7506 | 0.7681          | 53.3116 | 13.5719 |
| 0.8836        | 28.0  | 7784 | 0.7656          | 53.4399 | 13.5758 |
| 0.8777        | 29.0  | 8062 | 0.7642          | 53.4805 | 13.5737 |
| 0.8777        | 30.0  | 8340 | 0.7636          | 53.5086 | 13.5728 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.3.2
- Tokenizers 0.12.1
