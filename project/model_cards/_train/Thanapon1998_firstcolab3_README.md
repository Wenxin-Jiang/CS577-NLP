---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice_11_0
metrics:
- wer
model-index:
- name: firstcolab3
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: common_voice_11_0
      type: common_voice_11_0
      config: th
      split: train+validation
      args: th
    metrics:
    - name: Wer
      type: wer
      value: 0.6226224783861671
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# firstcolab3

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice_11_0 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2756
- Wer: 0.6226
- Cer: 0.0535

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 20
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|
| 7.187         | 0.75  | 1000  | 3.7705          | 1.0    | 1.0    |
| 2.0277        | 1.5   | 2000  | 0.6139          | 0.9202 | 0.1545 |
| 0.8368        | 2.24  | 3000  | 0.4351          | 0.8589 | 0.1147 |
| 0.6772        | 2.99  | 4000  | 0.3762          | 0.8200 | 0.0990 |
| 0.5702        | 3.74  | 5000  | 0.3434          | 0.7889 | 0.0891 |
| 0.5205        | 4.49  | 6000  | 0.3427          | 0.7726 | 0.0855 |
| 0.4773        | 5.24  | 7000  | 0.3073          | 0.7408 | 0.0767 |
| 0.4389        | 5.98  | 8000  | 0.2969          | 0.7421 | 0.0759 |
| 0.4069        | 6.73  | 9000  | 0.2884          | 0.7134 | 0.0711 |
| 0.3858        | 7.48  | 10000 | 0.2952          | 0.7066 | 0.0699 |
| 0.36          | 8.23  | 11000 | 0.2846          | 0.6902 | 0.0662 |
| 0.3517        | 8.98  | 12000 | 0.2729          | 0.6756 | 0.0638 |
| 0.3265        | 9.72  | 13000 | 0.2844          | 0.6756 | 0.0645 |
| 0.3127        | 10.47 | 14000 | 0.2769          | 0.6803 | 0.0640 |
| 0.3016        | 11.22 | 15000 | 0.2772          | 0.6566 | 0.0618 |
| 0.2855        | 11.97 | 16000 | 0.2791          | 0.6540 | 0.0598 |
| 0.2699        | 12.72 | 17000 | 0.2714          | 0.6455 | 0.0589 |
| 0.264         | 13.46 | 18000 | 0.2782          | 0.6472 | 0.0588 |
| 0.2518        | 14.21 | 19000 | 0.2693          | 0.6398 | 0.0578 |
| 0.2498        | 14.96 | 20000 | 0.2761          | 0.6300 | 0.0561 |
| 0.2426        | 15.71 | 21000 | 0.2796          | 0.6366 | 0.0561 |
| 0.2271        | 16.45 | 22000 | 0.2804          | 0.6336 | 0.0554 |
| 0.2271        | 17.2  | 23000 | 0.2758          | 0.6347 | 0.0552 |
| 0.22          | 17.95 | 24000 | 0.2785          | 0.6279 | 0.0544 |
| 0.2143        | 18.7  | 25000 | 0.2783          | 0.6246 | 0.0538 |
| 0.2134        | 19.45 | 26000 | 0.2756          | 0.6226 | 0.0535 |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
