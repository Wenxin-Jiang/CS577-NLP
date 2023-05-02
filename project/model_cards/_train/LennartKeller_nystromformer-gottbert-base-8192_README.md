---
tags:
- generated_from_trainer
model-index:
- name: first
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# first

This model is a fine-tuned version of [nystromformer-gottbert-base-8192](https://huggingface.co/nystromformer-gottbert-base-8192) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5135

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
- train_batch_size: 2
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 3.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 6.7133        | 0.1   | 500   | 6.6155          |
| 2.7876        | 0.2   | 1000  | 2.5542          |
| 2.1831        | 0.3   | 1500  | 2.0356          |
| 2.0316        | 0.4   | 2000  | 1.8793          |
| 2.0678        | 0.49  | 2500  | 1.7954          |
| 1.8182        | 0.59  | 3000  | 1.7473          |
| 1.7393        | 0.69  | 3500  | 1.7081          |
| 1.7586        | 0.79  | 4000  | 1.6787          |
| 1.7417        | 0.89  | 4500  | 1.6563          |
| 1.8256        | 0.99  | 5000  | 1.6370          |
| 1.7957        | 1.09  | 5500  | 1.6219          |
| 1.6876        | 1.19  | 6000  | 1.6084          |
| 1.7172        | 1.28  | 6500  | 1.5941          |
| 1.6564        | 1.38  | 7000  | 1.5881          |
| 1.732         | 1.48  | 7500  | 1.5757          |
| 1.8272        | 1.58  | 8000  | 1.5692          |
| 1.7951        | 1.68  | 8500  | 1.5617          |
| 1.6669        | 1.78  | 9000  | 1.5546          |
| 1.6489        | 1.88  | 9500  | 1.5458          |
| 1.772         | 1.98  | 10000 | 1.5439          |
| 1.7424        | 2.08  | 10500 | 1.5379          |
| 1.7077        | 2.17  | 11000 | 1.5322          |
| 1.6926        | 2.27  | 11500 | 1.5294          |
| 1.656         | 2.37  | 12000 | 1.5274          |
| 1.7002        | 2.47  | 12500 | 1.5201          |
| 1.7102        | 2.57  | 13000 | 1.5197          |
| 1.7158        | 2.67  | 13500 | 1.5162          |
| 1.6081        | 2.77  | 14000 | 1.5169          |
| 1.754         | 2.87  | 14500 | 1.5140          |
| 1.3588        | 2.96  | 15000 | 1.5135          |


### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.1+cu113
- Datasets 1.18.3
- Tokenizers 0.11.0
