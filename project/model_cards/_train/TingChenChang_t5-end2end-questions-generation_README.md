---
tags:
- generated_from_trainer
model-index:
- name: t5-end2end-questions-generation
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-end2end-questions-generation

This model is a fine-tuned version of [TingChenChang/t5-end2end-questions-generation](https://huggingface.co/TingChenChang/t5-end2end-questions-generation) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.5291

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- gradient_accumulation_steps: 16
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.5711        | 0.4   | 100  | 1.6119          |
| 1.5353        | 0.8   | 200  | 1.6052          |
| 1.502         | 1.2   | 300  | 1.6082          |
| 1.4525        | 1.6   | 400  | 1.5918          |
| 1.4463        | 2.0   | 500  | 1.5847          |
| 1.3885        | 2.4   | 600  | 1.6236          |
| 1.4029        | 2.8   | 700  | 1.5962          |
| 1.3947        | 3.2   | 800  | 1.5932          |
| 1.3685        | 3.6   | 900  | 1.5898          |
| 1.3926        | 4.0   | 1000 | 1.5624          |
| 1.4666        | 4.4   | 1100 | 1.5535          |
| 1.4573        | 4.8   | 1200 | 1.5483          |
| 1.4342        | 5.2   | 1300 | 1.5449          |
| 1.4281        | 5.6   | 1400 | 1.5347          |
| 1.4031        | 6.0   | 1500 | 1.5456          |
| 1.375         | 6.4   | 1600 | 1.5375          |
| 1.3867        | 6.8   | 1700 | 1.5393          |
| 1.3763        | 7.2   | 1800 | 1.5401          |
| 1.357         | 7.6   | 1900 | 1.5361          |
| 1.3568        | 8.0   | 2000 | 1.5295          |
| 1.3503        | 8.4   | 2100 | 1.5377          |
| 1.3335        | 8.8   | 2200 | 1.5353          |
| 1.3416        | 9.2   | 2300 | 1.5288          |
| 1.3179        | 9.6   | 2400 | 1.5324          |
| 1.3276        | 10.0  | 2500 | 1.5291          |


### Framework versions

- Transformers 4.22.2
- Pytorch 1.12.1+cu102
- Datasets 2.6.1
- Tokenizers 0.12.1
