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
- name: indic-bert-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-bert-finetuned-TRAC-DS

This model is a fine-tuned version of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9922
- Accuracy: 0.5825
- Precision: 0.5493
- Recall: 0.5412
- F1: 0.5428

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0755        | 1.99  | 612  | 1.0346          | 0.5057   | 0.4072    | 0.4554 | 0.3806 |
| 1.0175        | 3.99  | 1224 | 1.0096          | 0.5678   | 0.6135    | 0.5011 | 0.4422 |
| 0.9974        | 5.98  | 1836 | 1.0010          | 0.5776   | 0.5637    | 0.5140 | 0.4799 |
| 0.9812        | 7.97  | 2448 | 0.9960          | 0.5694   | 0.5426    | 0.5283 | 0.5298 |
| 0.9675        | 9.97  | 3060 | 0.9956          | 0.5776   | 0.5565    | 0.5422 | 0.5442 |
| 0.9542        | 11.96 | 3672 | 0.9925          | 0.5882   | 0.5601    | 0.5420 | 0.5419 |
| 0.944         | 13.95 | 4284 | 0.9907          | 0.5866   | 0.5525    | 0.5441 | 0.5454 |
| 0.9347        | 15.95 | 4896 | 0.9921          | 0.5858   | 0.5527    | 0.5441 | 0.5456 |
| 0.9271        | 17.94 | 5508 | 0.9906          | 0.5931   | 0.5596    | 0.5482 | 0.5490 |
| 0.9236        | 19.93 | 6120 | 0.9922          | 0.5825   | 0.5493    | 0.5412 | 0.5428 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
