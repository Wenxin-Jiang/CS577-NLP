---
license: apache-2.0
tags:
- generated_from_trainer
- stereotype
- gender
- gender_bias
widget:
- text: "Cauterize is not just for fans of the guitarist or his other projects, but those that love music that is both aggressive and infectious and gave the album 4 out of 5 stars ."
metrics:
- accuracy
model-index:
- name: distilRoberta-stereotype
  results:
  - task:
      name: Text Classification
      type: text-classification
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.989151002901476
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilRoberta-stereotype

This model is a fine-tuned version of [distilroberta-base](https://huggingface.co/distilroberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0651
- Accuracy: 0.9892

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|
| 0.0783        | 1.0   | 5615  | 0.0703          | 0.9847   |
| 0.0468        | 2.0   | 11230 | 0.0573          | 0.9863   |
| 0.0316        | 3.0   | 16845 | 0.0580          | 0.9882   |
| 0.0172        | 4.0   | 22460 | 0.0591          | 0.9885   |
| 0.0098        | 5.0   | 28075 | 0.0651          | 0.9892   |


### Framework versions

- Transformers 4.10.2
- Pytorch 1.9.0+cu102
- Datasets 1.11.0
- Tokenizers 0.10.3


Created by: [Narrativa](https://www.narrativa.com/)

About Narrativa: Natural Language Generation (NLG) | Gabriele, our machine learning-based platform, builds and deploys natural language solutions. #NLG #AI