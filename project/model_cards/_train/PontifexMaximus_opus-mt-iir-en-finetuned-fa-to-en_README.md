---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
metrics:
- bleu
model-index:
- name: opus-mt-iir-en-finetuned-fa-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: opus_infopankki
      type: opus_infopankki
      args: en-fa
    metrics:
    - name: Bleu
      type: bleu
      value: 36.687
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-iir-en-finetuned-fa-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-iir-en](https://huggingface.co/Helsinki-NLP/opus-mt-iir-en) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0968
- Bleu: 36.687
- Gen Len: 16.039

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 3.1614        | 1.0   | 1509  | 2.8058          | 12.326  | 16.5467 |
| 2.7235        | 2.0   | 3018  | 2.4178          | 15.6912 | 16.6396 |
| 2.4839        | 3.0   | 4527  | 2.1905          | 18.1971 | 16.4884 |
| 2.3044        | 4.0   | 6036  | 2.0272          | 20.197  | 16.4735 |
| 2.1943        | 5.0   | 7545  | 1.9012          | 22.2265 | 16.4266 |
| 2.0669        | 6.0   | 9054  | 1.7984          | 23.7711 | 16.353  |
| 1.985         | 7.0   | 10563 | 1.7100          | 24.986  | 16.284  |
| 1.9024        | 8.0   | 12072 | 1.6346          | 26.1758 | 16.217  |
| 1.8484        | 9.0   | 13581 | 1.5692          | 27.2782 | 16.1924 |
| 1.7761        | 10.0  | 15090 | 1.5111          | 28.2761 | 16.144  |
| 1.733         | 11.0  | 16599 | 1.4599          | 29.2184 | 16.2438 |
| 1.6772        | 12.0  | 18108 | 1.4150          | 30.0026 | 16.1949 |
| 1.6297        | 13.0  | 19617 | 1.3743          | 30.7839 | 16.1565 |
| 1.5918        | 14.0  | 21126 | 1.3370          | 31.4921 | 16.1323 |
| 1.5548        | 15.0  | 22635 | 1.3038          | 32.0621 | 16.076  |
| 1.5333        | 16.0  | 24144 | 1.2743          | 32.6881 | 16.0078 |
| 1.5145        | 17.0  | 25653 | 1.2478          | 33.3794 | 16.1228 |
| 1.4826        | 18.0  | 27162 | 1.2240          | 33.8335 | 16.0809 |
| 1.4488        | 19.0  | 28671 | 1.2021          | 34.2819 | 16.0479 |
| 1.4386        | 20.0  | 30180 | 1.1829          | 34.7206 | 16.0578 |
| 1.4127        | 21.0  | 31689 | 1.1660          | 35.031  | 16.0717 |
| 1.4089        | 22.0  | 33198 | 1.1510          | 35.4142 | 16.0391 |
| 1.3922        | 23.0  | 34707 | 1.1380          | 35.6777 | 16.0461 |
| 1.377         | 24.0  | 36216 | 1.1273          | 35.95   | 16.0569 |
| 1.3598        | 25.0  | 37725 | 1.1175          | 36.2435 | 16.0426 |
| 1.3515        | 26.0  | 39234 | 1.1097          | 36.4009 | 16.0247 |
| 1.3441        | 27.0  | 40743 | 1.1042          | 36.4815 | 16.0447 |
| 1.3412        | 28.0  | 42252 | 1.1001          | 36.6092 | 16.0489 |
| 1.3527        | 29.0  | 43761 | 1.0976          | 36.6703 | 16.0383 |
| 1.3397        | 30.0  | 45270 | 1.0968          | 36.687  | 16.039  |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.7.1+cu110
- Datasets 2.2.2
- Tokenizers 0.12.1
