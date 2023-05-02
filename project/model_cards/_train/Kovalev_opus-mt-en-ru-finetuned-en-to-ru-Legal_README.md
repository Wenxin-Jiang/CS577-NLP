---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: opus-mt-en-ru-finetuned-en-to-ru-Legal
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-en-ru-finetuned-en-to-ru-Legal

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-en-ru](https://huggingface.co/Helsinki-NLP/opus-mt-en-ru) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8561
- Bleu: 46.7284
- Gen Len: 23.1317

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-05
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 387  | 1.1719          | 34.0562 | 22.991  |
| 1.524         | 2.0   | 774  | 1.0342          | 37.7233 | 23.0052 |
| 1.0226        | 3.0   | 1161 | 0.9595          | 40.0983 | 22.9755 |
| 0.8066        | 4.0   | 1548 | 0.9188          | 41.9634 | 23.1162 |
| 0.8066        | 5.0   | 1935 | 0.8907          | 43.6537 | 23.0923 |
| 0.6637        | 6.0   | 2322 | 0.8771          | 44.5208 | 23.1097 |
| 0.5697        | 7.0   | 2709 | 0.8669          | 45.5589 | 23.1388 |
| 0.5175        | 8.0   | 3096 | 0.8603          | 46.2211 | 23.2356 |
| 0.5175        | 9.0   | 3483 | 0.8566          | 46.7201 | 23.1375 |
| 0.4768        | 10.0  | 3870 | 0.8561          | 46.7284 | 23.1317 |


### Framework versions

- Transformers 4.13.0
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.10.3
