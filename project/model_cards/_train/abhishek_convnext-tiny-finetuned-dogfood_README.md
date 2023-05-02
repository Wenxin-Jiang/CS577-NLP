---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- imagefolder
- lewtun/dog_food
metrics:
- accuracy
model-index:
- name: convnext-tiny-finetuned-dogfood
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: lewtun/dog_food
      type: lewtun/dog_food
      args: lewtun--dog_food
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7253333333333334
  - task:
      type: image-classification
      name: Image Classification
    dataset:
      name: lewtun/dog_food
      type: lewtun/dog_food
      config: lewtun--dog_food
      split: test
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.6866666666666666
      verified: true
    - name: Precision Macro
      type: precision
      value: 0.7181484576740136
      verified: true
    - name: Precision Micro
      type: precision
      value: 0.6866666666666666
      verified: true
    - name: Precision Weighted
      type: precision
      value: 0.7235392474854474
      verified: true
    - name: Recall Macro
      type: recall
      value: 0.7006250320552644
      verified: true
    - name: Recall Micro
      type: recall
      value: 0.6866666666666666
      verified: true
    - name: Recall Weighted
      type: recall
      value: 0.6866666666666666
      verified: true
    - name: F1 Macro
      type: f1
      value: 0.6690027379410202
      verified: true
    - name: F1 Micro
      type: f1
      value: 0.6866666666666666
      verified: true
    - name: F1 Weighted
      type: f1
      value: 0.6647526870157503
      verified: true
    - name: loss
      type: loss
      value: 0.9549381732940674
      verified: true
    - name: matthews_correlation
      type: matthews_correlation
      value: 0.5737269361889515
      verified: true
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# convnext-tiny-finetuned-dogfood

This model is a fine-tuned version of [facebook/convnext-tiny-224](https://huggingface.co/facebook/convnext-tiny-224) on the lewtun/dog_food dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9277
- Accuracy: 0.7253

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 128
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 1

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 1.0681        | 1.0   | 16   | 0.9125          | 0.7422   |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.11.0+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
