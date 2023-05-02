---
license: mit
tags:
- generated_from_trainer
model-index:
- name: deberta-classifier-feedback-1024-pseudo
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# deberta-classifier-feedback-1024-pseudo

This model is a fine-tuned version of [TTian/deberta-classifier-feedback-1024](https://huggingface.co/TTian/deberta-classifier-feedback-1024) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.1018

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
| 0.5566        | 0.01  | 10   | 0.8514          |
| 0.3244        | 0.03  | 20   | 0.8647          |
| 0.2631        | 0.04  | 30   | 0.6700          |
| 0.2237        | 0.06  | 40   | 0.8904          |
| 0.2103        | 0.07  | 50   | 0.7951          |
| 0.2576        | 0.08  | 60   | 0.8669          |
| 0.2519        | 0.1   | 70   | 0.9586          |
| 0.2419        | 0.11  | 80   | 0.7507          |
| 0.2088        | 0.13  | 90   | 1.1316          |
| 0.218         | 0.14  | 100  | 0.7750          |
| 0.1886        | 0.15  | 110  | 0.9505          |
| 0.1979        | 0.17  | 120  | 0.9668          |
| 0.2069        | 0.18  | 130  | 0.9559          |
| 0.2633        | 0.2   | 140  | 1.1578          |
| 0.2176        | 0.21  | 150  | 0.9224          |
| 0.2026        | 0.22  | 160  | 0.9700          |
| 0.2231        | 0.24  | 170  | 1.0094          |
| 0.2396        | 0.25  | 180  | 1.1268          |
| 0.2172        | 0.27  | 190  | 0.9728          |
| 0.2105        | 0.28  | 200  | 0.9813          |
| 0.2816        | 0.29  | 210  | 0.8179          |
| 0.1927        | 0.31  | 220  | 1.0210          |
| 0.1686        | 0.32  | 230  | 1.0608          |
| 0.1662        | 0.34  | 240  | 0.9698          |
| 0.1969        | 0.35  | 250  | 0.9445          |
| 0.2037        | 0.36  | 260  | 1.0223          |
| 0.1684        | 0.38  | 270  | 0.9921          |
| 0.1934        | 0.39  | 280  | 0.9738          |
| 0.1927        | 0.41  | 290  | 0.9370          |
| 0.1978        | 0.42  | 300  | 1.0144          |
| 0.1591        | 0.43  | 310  | 0.9222          |
| 0.1748        | 0.45  | 320  | 0.9433          |
| 0.2245        | 0.46  | 330  | 0.9773          |
| 0.2297        | 0.48  | 340  | 0.9884          |
| 0.1746        | 0.49  | 350  | 1.0024          |
| 0.152         | 0.5   | 360  | 0.9463          |
| 0.1514        | 0.52  | 370  | 1.0633          |
| 0.1898        | 0.53  | 380  | 1.1181          |
| 0.1438        | 0.55  | 390  | 1.0994          |
| 0.1426        | 0.56  | 400  | 1.0228          |
| 0.1545        | 0.58  | 410  | 1.1413          |
| 0.146         | 0.59  | 420  | 1.0416          |
| 0.1295        | 0.6   | 430  | 1.0037          |
| 0.1538        | 0.62  | 440  | 1.0532          |
| 0.1584        | 0.63  | 450  | 1.1754          |
| 0.1607        | 0.65  | 460  | 1.0540          |
| 0.1518        | 0.66  | 470  | 1.0318          |
| 0.1447        | 0.67  | 480  | 1.0777          |
| 0.1432        | 0.69  | 490  | 1.0318          |
| 0.1491        | 0.7   | 500  | 1.0717          |
| 0.1134        | 0.72  | 510  | 1.0512          |
| 0.1106        | 0.73  | 520  | 1.1904          |
| 0.1521        | 0.74  | 530  | 1.0705          |
| 0.1485        | 0.76  | 540  | 1.0390          |
| 0.1431        | 0.77  | 550  | 1.1089          |
| 0.1537        | 0.79  | 560  | 1.0316          |
| 0.1472        | 0.8   | 570  | 1.1694          |
| 0.129         | 0.81  | 580  | 1.1325          |
| 0.1286        | 0.83  | 590  | 1.0471          |
| 0.1338        | 0.84  | 600  | 1.1001          |
| 0.1285        | 0.86  | 610  | 1.0770          |
| 0.1379        | 0.87  | 620  | 1.1107          |
| 0.1299        | 0.88  | 630  | 1.0579          |
| 0.1151        | 0.9   | 640  | 1.0898          |
| 0.1119        | 0.91  | 650  | 1.1335          |
| 0.1297        | 0.93  | 660  | 1.1061          |
| 0.1218        | 0.94  | 670  | 1.1080          |
| 0.1038        | 0.95  | 680  | 1.0922          |
| 0.1286        | 0.97  | 690  | 1.1035          |
| 0.1263        | 0.98  | 700  | 1.1118          |
| 0.1182        | 1.0   | 710  | 1.1018          |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
