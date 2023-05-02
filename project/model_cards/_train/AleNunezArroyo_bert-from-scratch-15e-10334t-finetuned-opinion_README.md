---
tags:
- generated_from_trainer
model-index:
- name: bert-from-scratch-15e-10334t-finetuned-opinion
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-from-scratch-15e-10334t-finetuned-opinion

This model is a fine-tuned version of [](https://huggingface.co/) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 5.5936

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss |
|:-------------:|:-----:|:-----:|:---------------:|
| 6.5669        | 1.0   | 902   | 6.2062          |
| 6.1906        | 2.0   | 1804  | 6.0842          |
| 6.0858        | 3.0   | 2706  | 6.0119          |
| 6.0325        | 4.0   | 3608  | 5.9765          |
| 5.9894        | 5.0   | 4510  | 5.9406          |
| 5.958         | 6.0   | 5412  | 5.9109          |
| 5.9195        | 7.0   | 6314  | 5.8513          |
| 5.8653        | 8.0   | 7216  | 5.8068          |
| 5.8215        | 9.0   | 8118  | 5.7579          |
| 5.772         | 10.0  | 9020  | 5.7021          |
| 5.7374        | 11.0  | 9922  | 5.6582          |
| 5.7041        | 12.0  | 10824 | 5.6425          |
| 5.6762        | 13.0  | 11726 | 5.6251          |
| 5.6606        | 14.0  | 12628 | 5.6135          |
| 5.655         | 15.0  | 13530 | 5.6090          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
