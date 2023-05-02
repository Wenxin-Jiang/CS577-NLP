---
tags:
- generated_from_trainer
metrics:
- accuracy
- f1
model-index:
- name: electra-large-discriminator-nli-efl-tweeteval
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# electra-large-discriminator-nli-efl-tweeteval

This model is a fine-tuned version of [ynie/electra-large-discriminator-snli_mnli_fever_anli_R1_R2_R3-nli](https://huggingface.co/ynie/electra-large-discriminator-snli_mnli_fever_anli_R1_R2_R3-nli) on the None dataset.
It achieves the following results on the evaluation set:
- Accuracy: 0.7943
- F1: 0.7872
- Loss: 0.3004

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Accuracy | F1     | Validation Loss |
|:-------------:|:-----:|:----:|:--------:|:------:|:---------------:|
| 0.4384        | 1.0   | 163  | 0.7444   | 0.7308 | 0.3962          |
| 0.3447        | 2.0   | 326  | 0.7659   | 0.7552 | 0.3410          |
| 0.3057        | 3.0   | 489  | 0.7750   | 0.7688 | 0.3234          |
| 0.287         | 4.0   | 652  | 0.7857   | 0.7779 | 0.3069          |
| 0.2742        | 5.0   | 815  | 0.7887   | 0.7822 | 0.3030          |
| 0.2676        | 6.0   | 978  | 0.7939   | 0.7851 | 0.2982          |
| 0.2585        | 7.0   | 1141 | 0.7909   | 0.7822 | 0.3002          |
| 0.2526        | 8.0   | 1304 | 0.7943   | 0.7876 | 0.3052          |
| 0.2479        | 9.0   | 1467 | 0.7939   | 0.7847 | 0.2997          |
| 0.2451        | 10.0  | 1630 | 0.7956   | 0.7873 | 0.3014          |
| 0.2397        | 11.0  | 1793 | 0.7943   | 0.7872 | 0.3004          |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.12.0.dev20220417
- Datasets 2.1.0
- Tokenizers 0.10.3
