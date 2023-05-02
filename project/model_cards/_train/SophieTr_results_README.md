---
tags:
- generated_from_trainer
model-index:
- name: results
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# results

This model is a fine-tuned version of [sshleifer/distill-pegasus-xsum-16-4](https://huggingface.co/sshleifer/distill-pegasus-xsum-16-4) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4473

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
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 7.2378        | 0.51  | 100  | 7.1853          |
| 7.2309        | 1.01  | 200  | 6.6342          |
| 6.4796        | 1.52  | 300  | 6.3206          |
| 6.2691        | 2.02  | 400  | 6.0184          |
| 5.7382        | 2.53  | 500  | 5.5754          |
| 4.9922        | 3.03  | 600  | 4.5178          |
| 3.6031        | 3.54  | 700  | 2.8579          |
| 2.5203        | 4.04  | 800  | 2.4718          |
| 2.2563        | 4.55  | 900  | 2.4128          |
| 2.1425        | 5.05  | 1000 | 2.3767          |
| 2.004         | 5.56  | 1100 | 2.3982          |
| 2.0437        | 6.06  | 1200 | 2.3787          |
| 1.9407        | 6.57  | 1300 | 2.3952          |
| 1.9194        | 7.07  | 1400 | 2.3964          |
| 1.758         | 7.58  | 1500 | 2.4056          |
| 1.918         | 8.08  | 1600 | 2.4101          |
| 1.9162        | 8.59  | 1700 | 2.4085          |
| 1.8983        | 9.09  | 1800 | 2.4058          |
| 1.6939        | 9.6   | 1900 | 2.4050          |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.15.1
- Tokenizers 0.10.3
