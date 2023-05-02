---
license: apache-2.0
tags:
- summarization
- mT5_multilingual_XLSum
- mt5
- abstractive summarization
- ar
- xlsum
- generated_from_trainer
datasets:
- xlsum
model-index:
- name: mt5-base-finetune-ar-xlsum
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-base-finetune-ar-xlsum

This model is a fine-tuned version of [google/mt5-base](https://huggingface.co/google/mt5-base) on the xlsum dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2546
- Rouge-1: 22.2
- Rouge-2: 9.57
- Rouge-l: 20.26
- Gen Len: 19.0
- Bertscore: 71.43

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 250
- num_epochs: 10
- label_smoothing_factor: 0.1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge-1 | Rouge-2 | Rouge-l | Gen Len | Bertscore |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:-------:|:---------:|
| 4.9261        | 1.0   | 585  | 3.6314          | 18.19   | 6.49    | 16.37   | 19.0    | 70.17     |
| 3.8429        | 2.0   | 1170 | 3.4253          | 19.45   | 7.58    | 17.73   | 19.0    | 70.35     |
| 3.6311        | 3.0   | 1755 | 3.3569          | 20.83   | 8.54    | 18.9    | 19.0    | 70.89     |
| 3.4917        | 4.0   | 2340 | 3.3101          | 20.77   | 8.53    | 18.89   | 19.0    | 70.98     |
| 3.3873        | 5.0   | 2925 | 3.2867          | 21.47   | 9.0     | 19.54   | 19.0    | 71.23     |
| 3.3037        | 6.0   | 3510 | 3.2693          | 21.41   | 9.0     | 19.5    | 19.0    | 71.21     |
| 3.2357        | 7.0   | 4095 | 3.2581          | 22.05   | 9.36    | 20.04   | 19.0    | 71.43     |
| 3.1798        | 8.0   | 4680 | 3.2522          | 22.21   | 9.56    | 20.23   | 19.0    | 71.41     |
| 3.1359        | 9.0   | 5265 | 3.2546          | 22.27   | 9.58    | 20.23   | 19.0    | 71.46     |
| 3.0997        | 10.0  | 5850 | 3.2546          | 22.2    | 9.57    | 20.26   | 19.0    | 71.43     |


### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0+cu113
- Datasets 2.2.2
- Tokenizers 0.12.1
