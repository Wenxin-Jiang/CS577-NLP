---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model_index:
- name: opus-mt-ja-en-finetuned-ja-to-en_xml
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    metric:
      name: Bleu
      type: bleu
      value: 73.8646
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-ja-en-finetuned-ja-to-en_xml

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-ja-en](https://huggingface.co/Helsinki-NLP/opus-mt-ja-en) on an unkown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7520
- Bleu: 73.8646
- Gen Len: 27.0884

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 1.0512        | 1.0   | 748  | 0.8333          | 59.8234 | 27.905  |
| 0.6076        | 2.0   | 1496 | 0.7817          | 62.5606 | 26.1834 |
| 0.4174        | 3.0   | 2244 | 0.7817          | 64.8346 | 28.2918 |
| 0.2971        | 4.0   | 2992 | 0.7653          | 67.6013 | 27.2222 |
| 0.2172        | 5.0   | 3740 | 0.7295          | 69.4017 | 27.0174 |
| 0.1447        | 6.0   | 4488 | 0.7522          | 68.8355 | 28.2865 |
| 0.0953        | 7.0   | 5236 | 0.7596          | 71.4743 | 27.1861 |
| 0.0577        | 8.0   | 5984 | 0.7469          | 72.0684 | 26.921  |
| 0.04          | 9.0   | 6732 | 0.7526          | 73.2821 | 27.1365 |
| 0.0213        | 10.0  | 7480 | 0.7520          | 73.8646 | 27.0884 |


### Framework versions

- Transformers 4.9.1
- Pytorch 1.10.0+cu111
- Datasets 1.10.2
- Tokenizers 0.10.3
