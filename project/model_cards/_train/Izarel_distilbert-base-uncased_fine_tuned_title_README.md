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
- name: distilbert-base-uncased_fine_tuned_title
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_fine_tuned_title

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2615
- Accuracy: {'accuracy': 0.877634820695319}
- Recall: {'recall': 0.8474786132372805}
- Precision: {'precision': 0.8953502200023784}
- F1: {'f1': 0.8707569536806801}

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
| 0.3093        | 1.0   | 2284  | 0.3021          | {'accuracy': 0.8779085683000274} | {'recall': 0.8560333183250788} | {'precision': 0.8888499298737728} | {'f1': 0.8721330275229358} |
| 0.2459        | 2.0   | 4568  | 0.2909          | {'accuracy': 0.8894059676977827} | {'recall': 0.8513057181449797} | {'precision': 0.9153957879448076} | {'f1': 0.8821882654846612} |
| 0.1696        | 3.0   | 6852  | 0.3259          | {'accuracy': 0.8808102929099371} | {'recall': 0.8595227375056281} | {'precision': 0.8915353181552831} | {'f1': 0.875236403232277}  |
| 0.1179        | 4.0   | 9136  | 0.4946          | {'accuracy': 0.8729811114152751} | {'recall': 0.8610986042323278} | {'precision': 0.8756868131868132} | {'f1': 0.8683314415437005} |
| 0.0775        | 5.0   | 11420 | 0.6547          | {'accuracy': 0.8708458800985491} | {'recall': 0.8041422782530392} | {'precision': 0.9202627850057967} | {'f1': 0.8582927854868745} |
| 0.0522        | 6.0   | 13704 | 0.6699          | {'accuracy': 0.8768683274021353} | {'recall': 0.8325078793336335} | {'precision': 0.9067058967757754} | {'f1': 0.8680241769849187} |
| 0.0406        | 7.0   | 15988 | 0.8149          | {'accuracy': 0.8739118532712838} | {'recall': 0.8330706888788834} | {'precision': 0.9002554433767181} | {'f1': 0.8653610055539316} |
| 0.0298        | 8.0   | 18272 | 0.8906          | {'accuracy': 0.8753353408157679} | {'recall': 0.8421882035119316} | {'precision': 0.8952973555103506} | {'f1': 0.8679310944840787} |
| 0.0217        | 9.0   | 20556 | 1.0192          | {'accuracy': 0.8754448398576512} | {'recall': 0.8624493471409275} | {'precision': 0.8791738382099827} | {'f1': 0.8707312915506562} |
| 0.017         | 10.0  | 22840 | 1.0550          | {'accuracy': 0.8758828360251848} | {'recall': 0.8556956325979289} | {'precision': 0.8852917200419238} | {'f1': 0.8702421155056951} |
| 0.0139        | 11.0  | 25124 | 1.0873          | {'accuracy': 0.8728716123733917} | {'recall': 0.8582845565060784} | {'precision': 0.8776473296500921} | {'f1': 0.8678579558388345} |
| 0.0114        | 12.0  | 27408 | 1.1506          | {'accuracy': 0.8716123733917328} | {'recall': 0.8628995947771274} | {'precision': 0.8718298646650745} | {'f1': 0.8673417435085139} |
| 0.0061        | 13.0  | 29692 | 1.2574          | {'accuracy': 0.8696961401587736} | {'recall': 0.874943719045475}  | {'precision': 0.8596549435965495} | {'f1': 0.8672319535869686} |
| 0.0035        | 14.0  | 31976 | 1.2490          | {'accuracy': 0.8784560635094443} | {'recall': 0.85006753714543}   | {'precision': 0.8947867298578199} | {'f1': 0.8718540752713001} |
| 0.0028        | 15.0  | 34260 | 1.2615          | {'accuracy': 0.877634820695319}  | {'recall': 0.8474786132372805} | {'precision': 0.8953502200023784} | {'f1': 0.8707569536806801} |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
