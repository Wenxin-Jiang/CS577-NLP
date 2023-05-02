---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: indic-bert-finetuned-combined-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-bert-finetuned-combined-DS

This model is a fine-tuned version of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9783
- Accuracy: 0.5871
- Precision: 0.5527
- Recall: 0.5574
- F1: 0.5537

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-06
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0904        | 1.0   | 711   | 1.0759          | 0.4452   | 0.4368    | 0.4155 | 0.3333 |
| 1.0537        | 2.0   | 1422  | 1.0363          | 0.5063   | 0.5079    | 0.4902 | 0.4889 |
| 1.0233        | 3.0   | 2133  | 1.0207          | 0.5302   | 0.5195    | 0.5266 | 0.4956 |
| 1.0091        | 3.99  | 2844  | 1.0168          | 0.5379   | 0.5248    | 0.5313 | 0.5124 |
| 0.9983        | 4.99  | 3555  | 1.0009          | 0.5681   | 0.5344    | 0.5424 | 0.5335 |
| 0.9854        | 5.99  | 4266  | 0.9950          | 0.5829   | 0.5490    | 0.5548 | 0.5492 |
| 0.9728        | 6.99  | 4977  | 0.9917          | 0.5751   | 0.5436    | 0.5515 | 0.5434 |
| 0.9616        | 7.99  | 5688  | 0.9888          | 0.5492   | 0.5183    | 0.5308 | 0.5107 |
| 0.9476        | 8.99  | 6399  | 0.9815          | 0.5836   | 0.5488    | 0.5526 | 0.5499 |
| 0.9355        | 9.99  | 7110  | 0.9962          | 0.5520   | 0.5316    | 0.5419 | 0.5223 |
| 0.924         | 10.98 | 7821  | 0.9823          | 0.5674   | 0.5363    | 0.5453 | 0.5315 |
| 0.9112        | 11.98 | 8532  | 0.9773          | 0.5829   | 0.5479    | 0.5504 | 0.5488 |
| 0.9002        | 12.98 | 9243  | 0.9761          | 0.5815   | 0.5452    | 0.5479 | 0.5459 |
| 0.8904        | 13.98 | 9954  | 0.9726          | 0.5913   | 0.5558    | 0.5495 | 0.5512 |
| 0.8823        | 14.98 | 10665 | 0.9785          | 0.5843   | 0.5526    | 0.5583 | 0.5533 |
| 0.8742        | 15.98 | 11376 | 0.9765          | 0.5843   | 0.5493    | 0.5543 | 0.5500 |
| 0.8653        | 16.98 | 12087 | 0.9746          | 0.5864   | 0.5501    | 0.5532 | 0.5508 |
| 0.8612        | 17.97 | 12798 | 0.9770          | 0.5885   | 0.5539    | 0.5566 | 0.5548 |
| 0.8558        | 18.97 | 13509 | 0.9796          | 0.5836   | 0.5510    | 0.5565 | 0.5520 |
| 0.8561        | 19.97 | 14220 | 0.9783          | 0.5871   | 0.5527    | 0.5574 | 0.5537 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
