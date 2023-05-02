---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
model-index:
- name: wav2vec2-base-960h-finetuned
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-base-960h-finetuned

This model is a fine-tuned version of [facebook/wav2vec2-base-960h](https://huggingface.co/facebook/wav2vec2-base-960h) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1430
- Accuracy: 0.6516

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.5958        | 1.0   | 203  | 2.4754          | 0.2714   |
| 2.0809        | 2.0   | 406  | 1.9972          | 0.3930   |
| 1.8486        | 3.0   | 609  | 1.6918          | 0.4658   |
| 1.5857        | 4.0   | 812  | 1.5089          | 0.5186   |
| 1.4819        | 5.0   | 1015 | 1.4027          | 0.5508   |
| 1.3859        | 6.0   | 1218 | 1.3146          | 0.5867   |
| 1.3448        | 7.0   | 1421 | 1.2078          | 0.6281   |
| 1.2551        | 8.0   | 1624 | 1.1600          | 0.6447   |
| 1.1506        | 9.0   | 1827 | 1.1595          | 0.6512   |
| 1.2435        | 10.0  | 2030 | 1.1430          | 0.6516   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
