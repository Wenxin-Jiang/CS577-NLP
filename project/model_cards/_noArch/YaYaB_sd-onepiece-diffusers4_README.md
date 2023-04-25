---
language: en
license: apache-2.0
library_name: diffusers
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
datasets: YaYaB/onepiece-blip-captions
metrics: []
---

<!-- This model card has been generated automatically according to the information the training script had access to. You
should probably proofread and complete it, then remove this comment. -->

# sd-onepiece-diffusers4

## Model description

This diffusion model is trained with the [🤗 Diffusers](https://github.com/huggingface/diffusers) library 
on the `YaYaB/onepiece-blip-captions` dataset.

## Intended uses & limitations

#### How to use

```python
# TODO: add an example code snippet for running this diffusion pipeline
```

#### Limitations and bias

[TODO: provide examples of latent issues and potential remediations]

## Training data

[TODO: describe the data used to train the model]

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 1
- eval_batch_size: 1
- gradient_accumulation_steps: 4
- optimizer: AdamW with betas=(0.9, 0.999), weight_decay=0.01 and epsilon=1e-08
- lr_scheduler: constant
- lr_warmup_steps: 500
- ema_inv_gamma: None
- ema_inv_gamma: None
- ema_inv_gamma: None
- mixed_precision: fp16

### Training results

📈 [TensorBoard logs](https://huggingface.co/YaYaB/sd-onepiece-diffusers4/tensorboard?#scalars)

