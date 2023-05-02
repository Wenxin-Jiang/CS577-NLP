---
license: cc-by-nc-sa-4.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
metrics:
- bleu
model-index:
- name: mt5-small-parsinlu-opus-translation_fa_en-finetuned-fa-to-en
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
      value: 15.1329
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-parsinlu-opus-translation_fa_en-finetuned-fa-to-en

This model is a fine-tuned version of [persiannlp/mt5-small-parsinlu-opus-translation_fa_en](https://huggingface.co/persiannlp/mt5-small-parsinlu-opus-translation_fa_en) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9193
- Bleu: 15.1329
- Gen Len: 13.4603

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 3.1182        | 1.0   | 1807  | 2.5985          | 10.6445 | 13.7938 |
| 2.8377        | 2.0   | 3614  | 2.3799          | 11.852  | 13.6168 |
| 2.6644        | 3.0   | 5421  | 2.2426          | 12.877  | 13.5768 |
| 2.5286        | 4.0   | 7228  | 2.1521          | 13.5342 | 13.5567 |
| 2.4523        | 5.0   | 9035  | 2.0801          | 14.0355 | 13.5387 |
| 2.4026        | 6.0   | 10842 | 2.0197          | 14.4284 | 13.4956 |
| 2.317         | 7.0   | 12649 | 1.9691          | 14.7776 | 13.4325 |
| 2.3174        | 8.0   | 14456 | 1.9373          | 15.189  | 13.4261 |
| 2.3374        | 9.0   | 16263 | 1.9393          | 15.1149 | 13.4087 |
| 2.3131        | 10.0  | 18070 | 1.9304          | 15.0654 | 13.4234 |
| 2.295         | 11.0  | 19877 | 1.9239          | 15.102  | 13.4443 |
| 2.3017        | 12.0  | 21684 | 1.9203          | 15.1676 | 13.4575 |
| 2.3153        | 13.0  | 23491 | 1.9193          | 15.1329 | 13.4603 |
| 2.2939        | 14.0  | 25298 | 1.9193          | 15.1329 | 13.4603 |
| 2.3241        | 15.0  | 27105 | 1.9193          | 15.1329 | 13.4603 |
| 2.3376        | 16.0  | 28912 | 1.9193          | 15.1329 | 13.4603 |
| 2.2859        | 17.0  | 30719 | 1.9193          | 15.1329 | 13.4603 |
| 2.3016        | 18.0  | 32526 | 1.9193          | 15.1329 | 13.4603 |
| 2.3101        | 19.0  | 34333 | 1.9193          | 15.1329 | 13.4603 |
| 2.3088        | 20.0  | 36140 | 1.9193          | 15.1329 | 13.4603 |
| 2.2833        | 21.0  | 37947 | 1.9193          | 15.1329 | 13.4603 |
| 2.2986        | 22.0  | 39754 | 1.9193          | 15.1329 | 13.4603 |
| 2.3254        | 23.0  | 41561 | 1.9193          | 15.1329 | 13.4603 |
| 2.3165        | 24.0  | 43368 | 1.9193          | 15.1329 | 13.4603 |
| 2.289         | 25.0  | 45175 | 1.9193          | 15.1329 | 13.4603 |
| 2.3212        | 26.0  | 46982 | 1.9193          | 15.1329 | 13.4603 |
| 2.2902        | 27.0  | 48789 | 1.9193          | 15.1329 | 13.4603 |
| 2.3026        | 28.0  | 50596 | 1.9193          | 15.1329 | 13.4603 |
| 2.2949        | 29.0  | 52403 | 1.9193          | 15.1329 | 13.4603 |
| 2.3152        | 30.0  | 54210 | 1.9193          | 15.1329 | 13.4603 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.7.1+cu110
- Datasets 2.2.2
- Tokenizers 0.12.1
