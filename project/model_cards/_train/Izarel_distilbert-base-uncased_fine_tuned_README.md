---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: distilbert-base-uncased_fine_tuned_title_and_text
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_fine_tuned

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an reddit dataset -for NSFW classification.
It was trained on titles + body_text of submissions.
It achieves the following results on the evaluation set:
- Loss: 1.0159
- Accuracy: {'accuracy': 0.9095537914043252}
- Recall: {'recall': 0.8936873290793071}
- Precision: {'precision': 0.916024293389395}
- F1: {'f1': 0.9047179605490829}

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy                         | Recall                         | Precision                         | F1                         |
|:-------------:|:-----:|:-----:|:---------------:|:--------------------------------:|:------------------------------:|:---------------------------------:|:--------------------------:|
| 0.256         | 1.0   | 2284  | 0.2569          | {'accuracy': 0.9085683000273748} | {'recall': 0.8976754785779398} | {'precision': 0.9107514450867052} | {'f1': 0.9041661884540342} |
| 0.1948        | 2.0   | 4568  | 0.2471          | {'accuracy': 0.9138242540377771} | {'recall': 0.8644029170464904} | {'precision': 0.9518193224592221} | {'f1': 0.9060074047533739} |
| 0.1318        | 3.0   | 6852  | 0.3057          | {'accuracy': 0.914207500684369}  | {'recall': 0.8977894257064722} | {'precision': 0.9216282606152767} | {'f1': 0.9095526695526697} |
| 0.0865        | 4.0   | 9136  | 0.4174          | {'accuracy': 0.9047358335614564} | {'recall': 0.8697584320875114} | {'precision': 0.9274605103280681} | {'f1': 0.8976831706456546} |
| 0.0545        | 5.0   | 11420 | 0.4635          | {'accuracy': 0.9095537914043252} | {'recall': 0.8849134001823155} | {'precision': 0.9236441484300666} | {'f1': 0.9038640595903165} |
| 0.0359        | 6.0   | 13704 | 0.5654          | {'accuracy': 0.9071448124828908} | {'recall': 0.8919781221513218} | {'precision': 0.9127798507462687} | {'f1': 0.9022591055786076} |
| 0.0262        | 7.0   | 15988 | 0.5568          | {'accuracy': 0.8994251300301123} | {'recall': 0.900865998176846}  | {'precision': 0.8910176941282543} | {'f1': 0.8959147827072356} |
| 0.0181        | 8.0   | 18272 | 0.6846          | {'accuracy': 0.9042430878729811} | {'recall': 0.9026891522333638} | {'precision': 0.898491550413973}  | {'f1': 0.9005854601261866} |
| 0.0121        | 9.0   | 20556 | 0.7516          | {'accuracy': 0.9071448124828908} | {'recall': 0.8990428441203282} | {'precision': 0.906896551724138}  | {'f1': 0.9029526207370108} |
| 0.0119        | 10.0  | 22840 | 0.8614          | {'accuracy': 0.9050095811661648} | {'recall': 0.9002962625341842} | {'precision': 0.9018376897614427} | {'f1': 0.9010663169299197} |
| 0.0105        | 11.0  | 25124 | 0.7298          | {'accuracy': 0.9105940323022174} | {'recall': 0.8907247037374658} | {'precision': 0.9206218348839948} | {'f1': 0.9054265361672554} |
| 0.0049        | 12.0  | 27408 | 0.9237          | {'accuracy': 0.9101560361346839} | {'recall': 0.8828623518687329} | {'precision': 0.9266834110752302} | {'f1': 0.9042422827799498} |
| 0.0026        | 13.0  | 29692 | 0.9489          | {'accuracy': 0.9066520667944156} | {'recall': 0.8988149498632635} | {'precision': 0.9061458931648478} | {'f1': 0.9024655340083519} |
| 0.0016        | 14.0  | 31976 | 1.0045          | {'accuracy': 0.9099917875718587} | {'recall': 0.8963081130355515} | {'precision': 0.9146511627906977} | {'f1': 0.9053867403314917} |
| 0.0022        | 15.0  | 34260 | 1.0159          | {'accuracy': 0.9095537914043252} | {'recall': 0.8936873290793071} | {'precision': 0.916024293389395}  | {'f1': 0.9047179605490829} |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
