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
      value: 51.6508
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-ar-en-finetuned-ar-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ar-en](https://huggingface.co/Helsinki-NLP/opus-mt-ar-en) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7269
- Bleu: 51.6508
- Gen Len: 15.0812

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
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 1.4974        | 1.0   | 1587  | 1.3365          | 36.9061 | 15.3385 |
| 1.3768        | 2.0   | 3174  | 1.2139          | 39.5476 | 15.2079 |
| 1.2887        | 3.0   | 4761  | 1.1265          | 41.2771 | 15.2034 |
| 1.2076        | 4.0   | 6348  | 1.0556          | 42.6907 | 15.2687 |
| 1.1512        | 5.0   | 7935  | 0.9975          | 43.9498 | 15.2072 |
| 1.0797        | 6.0   | 9522  | 0.9491          | 45.224  | 15.2034 |
| 1.0499        | 7.0   | 11109 | 0.9101          | 46.1387 | 15.1651 |
| 1.0095        | 8.0   | 12696 | 0.8778          | 47.0586 | 15.1788 |
| 0.9833        | 9.0   | 14283 | 0.8501          | 47.8083 | 15.162  |
| 0.9601        | 10.0  | 15870 | 0.8267          | 48.5236 | 15.1784 |
| 0.9457        | 11.0  | 17457 | 0.8059          | 49.1717 | 15.095  |
| 0.9233        | 12.0  | 19044 | 0.7883          | 49.7742 | 15.1126 |
| 0.8964        | 13.0  | 20631 | 0.7736          | 50.2168 | 15.0917 |
| 0.8849        | 14.0  | 22218 | 0.7606          | 50.5583 | 15.0913 |
| 0.8751        | 15.0  | 23805 | 0.7504          | 50.8481 | 15.1108 |
| 0.858         | 16.0  | 25392 | 0.7417          | 51.1841 | 15.0989 |
| 0.8673        | 17.0  | 26979 | 0.7353          | 51.4271 | 15.0939 |
| 0.8548        | 18.0  | 28566 | 0.7306          | 51.535  | 15.0911 |
| 0.8483        | 19.0  | 30153 | 0.7279          | 51.6102 | 15.078  |
| 0.8614        | 20.0  | 31740 | 0.7269          | 51.6508 | 15.0812 |


### Framework versions

- Transformers 4.19.2
- Pytorch 1.7.1+cu110
- Datasets 2.2.2
- Tokenizers 0.12.1
