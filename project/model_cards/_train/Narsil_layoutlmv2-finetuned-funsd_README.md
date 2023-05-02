---
tags:
- generated_from_trainer
datasets:
- funsd
pipeline_tag: object-detection
widget:
- src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/invoice.png"
  example_title: invoice
- src: "https://huggingface.co/spaces/impira/docquery/resolve/2359223c1837a7587402bda0f2643382a6eefeab/contract.jpeg"
  example_title: contract
model_index:
- name: layoutlmv2-finetuned-funsd
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: funsd
      type: funsd
      args: funsd
duplicated_from: nielsr/layoutlmv2-finetuned-funsd
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# layoutlmv2-finetuned-funsd

This model is a fine-tuned version of [microsoft/layoutlmv2-base-uncased](https://huggingface.co/microsoft/layoutlmv2-base-uncased) on the funsd dataset.

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000
- mixed_precision_training: Native AMP

### Training results



### Framework versions

- Transformers 4.9.0.dev0
- Pytorch 1.8.0+cu101
- Datasets 1.9.0
- Tokenizers 0.10.3
