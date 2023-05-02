---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- scitldr
model-index:
- name: distilbart-cnn-12-6-finetuned-scitldr
  results: []
widget:
- text: "Reinforcement learning provides a powerful and general framework for decision making and control, but its application in practice is often hindered by the need for extensive feature and reward engineering. Deep reinforcement learning methods can remove the need for explicit engineering of policy or value features but still require a manually specified reward function. Inverse reinforcement learning holds the promise of automatic reward acquisition, but has proven exceptionally difficult to apply to large, high-dimensional problems with unknown dynamics. In this work, we propose AIRL, a practical and scalable inverse reinforcement learning algorithm based on an adversarial reward learning formulation that is competitive with direct imitation learning algorithms. Additionally, we show that AIRL is able to recover portable reward functions that are robust to changes in dynamics, enabling us to learn policies even under significant variation in the environment seen during training. "
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbart-cnn-12-6-finetuned-scitldr

This model is a fine-tuned version of [sshleifer/distilbart-cnn-12-6](https://huggingface.co/sshleifer/distilbart-cnn-12-6) on the scitldr dataset.
It achieves the following results on the evaluation set:
- eval_loss: 3.7113
- eval_rouge1: 31.4431
- eval_rouge2: 13.1766
- eval_rougeL: 24.2038
- eval_rougeLsum: 26.3167
- eval_runtime: 151.7265
- eval_samples_per_second: 4.08
- eval_steps_per_second: 0.514
- epoch: 4.0
- step: 996

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
