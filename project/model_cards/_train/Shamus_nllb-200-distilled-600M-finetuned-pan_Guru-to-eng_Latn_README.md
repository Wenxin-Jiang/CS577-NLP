---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: nllb-200-distilled-600M-finetuned-pan_Guru-to-eng_Latn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# nllb-200-distilled-600M-finetuned-pan_Guru-to-eng_Latn

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.8728
- Bleu: 42.5453
- Gen Len: 32.376

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
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- gradient_accumulation_steps: 4
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 6

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| 1.5153        | 0.72  | 500  | 1.0531          | 34.9696 | 32.548  |
| 1.1282        | 1.45  | 1000 | 0.9580          | 38.3648 | 31.832  |
| 1.0299        | 2.18  | 1500 | 0.9235          | 40.1212 | 31.964  |
| 0.942         | 2.9   | 2000 | 0.8963          | 41.2737 | 31.884  |
| 0.8869        | 3.63  | 2500 | 0.8847          | 41.4381 | 31.82   |
| 0.8553        | 4.35  | 3000 | 0.8780          | 42.1548 | 32.136  |
| 0.8306        | 5.08  | 3500 | 0.8733          | 42.3333 | 32.64   |
| 0.8063        | 5.8   | 4000 | 0.8728          | 42.5453 | 32.376  |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
