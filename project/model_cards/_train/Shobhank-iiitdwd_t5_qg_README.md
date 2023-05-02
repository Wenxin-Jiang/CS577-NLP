---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- squad_modified_for_t5_qg
model-index:
- name: t5-end2end-questions-answers-generation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-end2end-questions-answers-generation

This model is a fine-tuned version of [t5-base](https://huggingface.co/t5-base) on the squad_modified_for_t5_qg dataset.
It achieves the following results on the evaluation set:
- Loss: 1.3810

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 7

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 2.5388        | 0.34  | 100  | 1.7772          |
| 1.8647        | 0.68  | 200  | 1.6304          |
| 1.7367        | 1.02  | 300  | 1.5443          |
| 1.6048        | 1.36  | 400  | 1.4884          |
| 1.5559        | 1.69  | 500  | 1.4590          |
| 1.5309        | 2.03  | 600  | 1.4440          |
| 1.465         | 2.37  | 700  | 1.4215          |
| 1.4601        | 2.71  | 800  | 1.4078          |
| 1.4439        | 3.05  | 900  | 1.4123          |
| 1.3988        | 3.39  | 1000 | 1.4108          |
| 1.3896        | 3.73  | 1100 | 1.3915          |
| 1.3781        | 4.07  | 1200 | 1.3927          |
| 1.3557        | 4.41  | 1300 | 1.3849          |
| 1.3476        | 4.75  | 1400 | 1.3877          |
| 1.3419        | 5.08  | 1500 | 1.3836          |
| 1.3203        | 5.42  | 1600 | 1.3765          |
| 1.3135        | 5.76  | 1700 | 1.3754          |
| 1.3251        | 6.1   | 1800 | 1.3794          |
| 1.3004        | 6.44  | 1900 | 1.3786          |
| 1.299         | 6.78  | 2000 | 1.3810          |


### Framework versions

- Transformers 4.23.1
- Pytorch 1.12.1+cu113
- Datasets 2.6.1
- Tokenizers 0.13.1
