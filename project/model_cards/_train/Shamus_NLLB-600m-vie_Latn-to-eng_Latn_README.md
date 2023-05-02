---
license: cc-by-nc-4.0
tags:
- generated_from_trainer
metrics:
- bleu
model-index:
- name: NLLB-600m-vie_Latn-to-eng_Latn
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# NLLB-600m-vie_Latn-to-eng_Latn

This model is a fine-tuned version of [facebook/nllb-200-distilled-600M](https://huggingface.co/facebook/nllb-200-distilled-600M) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1189
- Bleu: 36.6767
- Gen Len: 47.504

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
- train_batch_size: 3
- eval_batch_size: 3
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 24
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 10000
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 1.9294        | 2.24  | 1000  | 1.5970          | 23.6201 | 48.1    |
| 1.4           | 4.47  | 2000  | 1.3216          | 28.9526 | 45.156  |
| 1.2071        | 6.71  | 3000  | 1.2245          | 32.5538 | 46.576  |
| 1.0893        | 8.95  | 4000  | 1.1720          | 34.265  | 46.052  |
| 1.0064        | 11.19 | 5000  | 1.1497          | 34.9249 | 46.508  |
| 0.9562        | 13.42 | 6000  | 1.1331          | 36.4619 | 47.244  |
| 0.9183        | 15.66 | 7000  | 1.1247          | 36.4723 | 47.26   |
| 0.8858        | 17.9  | 8000  | 1.1198          | 36.7058 | 47.376  |
| 0.8651        | 20.13 | 9000  | 1.1201          | 36.7897 | 47.496  |
| 0.8546        | 22.37 | 10000 | 1.1189          | 36.6767 | 47.504  |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
