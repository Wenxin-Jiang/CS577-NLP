---
license: mit
tags:
- generated_from_trainer
model-index:
- name: deberta-classifier-feedback-1024
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-classifier-feedback-1024

This model is a fine-tuned version of [TTian/deberta-mlm-feedback-1024](https://huggingface.co/TTian/deberta-mlm-feedback-1024) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6246

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 1.038         | 0.04  | 10   | 0.8470          |
| 0.8858        | 0.08  | 20   | 0.7317          |
| 0.8166        | 0.13  | 30   | 0.8127          |
| 0.7791        | 0.17  | 40   | 0.8111          |
| 0.7977        | 0.21  | 50   | 0.7540          |
| 0.7815        | 0.25  | 60   | 0.7204          |
| 0.7467        | 0.3   | 70   | 0.7446          |
| 0.7525        | 0.34  | 80   | 0.7522          |
| 0.716         | 0.38  | 90   | 0.7542          |
| 0.7617        | 0.42  | 100  | 0.7095          |
| 0.7618        | 0.47  | 110  | 0.7147          |
| 0.7297        | 0.51  | 120  | 0.8648          |
| 0.7797        | 0.55  | 130  | 0.7150          |
| 0.7466        | 0.59  | 140  | 0.7360          |
| 0.745         | 0.64  | 150  | 0.6842          |
| 0.718         | 0.68  | 160  | 0.7408          |
| 0.7455        | 0.72  | 170  | 0.7029          |
| 0.7476        | 0.76  | 180  | 0.7106          |
| 0.695         | 0.81  | 190  | 0.6781          |
| 0.6603        | 0.85  | 200  | 0.7713          |
| 0.7763        | 0.89  | 210  | 0.7619          |
| 0.6858        | 0.93  | 220  | 0.7252          |
| 0.6567        | 0.97  | 230  | 0.7017          |
| 0.6529        | 1.02  | 240  | 0.7030          |
| 0.6752        | 1.06  | 250  | 0.6717          |
| 0.7078        | 1.1   | 260  | 0.6868          |
| 0.6428        | 1.14  | 270  | 0.6694          |
| 0.6173        | 1.19  | 280  | 0.7137          |
| 0.6753        | 1.23  | 290  | 0.7363          |
| 0.6326        | 1.27  | 300  | 0.6808          |
| 0.6241        | 1.31  | 310  | 0.6855          |
| 0.6717        | 1.36  | 320  | 0.6627          |
| 0.633         | 1.4   | 330  | 0.7079          |
| 0.6541        | 1.44  | 340  | 0.6475          |
| 0.5998        | 1.48  | 350  | 0.7008          |
| 0.7088        | 1.53  | 360  | 0.6558          |
| 0.6209        | 1.57  | 370  | 0.6536          |
| 0.6159        | 1.61  | 380  | 0.6805          |
| 0.6297        | 1.65  | 390  | 0.6617          |
| 0.6506        | 1.69  | 400  | 0.6459          |
| 0.6397        | 1.74  | 410  | 0.6450          |
| 0.6181        | 1.78  | 420  | 0.7158          |
| 0.6609        | 1.82  | 430  | 0.6336          |
| 0.6066        | 1.86  | 440  | 0.6232          |
| 0.6418        | 1.91  | 450  | 0.6272          |
| 0.6499        | 1.95  | 460  | 0.6268          |
| 0.6021        | 1.99  | 470  | 0.6431          |
| 0.5899        | 2.03  | 480  | 0.6395          |
| 0.5524        | 2.08  | 490  | 0.6278          |
| 0.5182        | 2.12  | 500  | 0.6690          |
| 0.5768        | 2.16  | 510  | 0.6400          |
| 0.5326        | 2.2   | 520  | 0.6386          |
| 0.5641        | 2.25  | 530  | 0.6759          |
| 0.5794        | 2.29  | 540  | 0.6483          |
| 0.5341        | 2.33  | 550  | 0.6273          |
| 0.5604        | 2.37  | 560  | 0.6393          |
| 0.529         | 2.42  | 570  | 0.6389          |
| 0.5433        | 2.46  | 580  | 0.6272          |
| 0.5574        | 2.5   | 590  | 0.6387          |
| 0.5279        | 2.54  | 600  | 0.6613          |
| 0.5066        | 2.58  | 610  | 0.6376          |
| 0.5235        | 2.63  | 620  | 0.6449          |
| 0.516         | 2.67  | 630  | 0.6285          |
| 0.5888        | 2.71  | 640  | 0.6391          |
| 0.5326        | 2.75  | 650  | 0.6226          |
| 0.5486        | 2.8   | 660  | 0.6373          |
| 0.5176        | 2.84  | 670  | 0.6272          |
| 0.5038        | 2.88  | 680  | 0.6235          |
| 0.5335        | 2.92  | 690  | 0.6266          |
| 0.557         | 2.97  | 700  | 0.6246          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.0
- Tokenizers 0.13.2
