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
- name: run-3
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# run-3

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4223
- Accuracy: 0.75
- Precision: 0.7128
- Recall: 0.6998
- F1: 0.7043

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
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0025        | 1.0   | 50   | 0.8925          | 0.63     | 0.6703    | 0.5704 | 0.5060 |
| 0.8187        | 2.0   | 100  | 0.7915          | 0.595    | 0.6007    | 0.5926 | 0.5344 |
| 0.5671        | 3.0   | 150  | 0.9573          | 0.695    | 0.6520    | 0.6350 | 0.6380 |
| 0.3218        | 4.0   | 200  | 0.9195          | 0.68     | 0.6447    | 0.6539 | 0.6461 |
| 0.2208        | 5.0   | 250  | 1.2429          | 0.715    | 0.6801    | 0.6617 | 0.6663 |
| 0.1614        | 6.0   | 300  | 1.5295          | 0.71     | 0.6736    | 0.6543 | 0.6423 |
| 0.1129        | 7.0   | 350  | 2.1055          | 0.71     | 0.6779    | 0.6413 | 0.6511 |
| 0.098         | 8.0   | 400  | 1.9579          | 0.705    | 0.6697    | 0.6558 | 0.6601 |
| 0.0479        | 9.0   | 450  | 2.0535          | 0.72     | 0.6794    | 0.6663 | 0.6711 |
| 0.0173        | 10.0  | 500  | 2.5381          | 0.7      | 0.6838    | 0.6604 | 0.6608 |
| 0.0308        | 11.0  | 550  | 2.4592          | 0.735    | 0.7014    | 0.6851 | 0.6901 |
| 0.0265        | 12.0  | 600  | 2.3131          | 0.725    | 0.6910    | 0.6845 | 0.6849 |
| 0.016         | 13.0  | 650  | 2.4025          | 0.74     | 0.7035    | 0.6915 | 0.6949 |
| 0.013         | 14.0  | 700  | 2.3933          | 0.745    | 0.7070    | 0.6831 | 0.6909 |
| 0.016         | 15.0  | 750  | 2.6819          | 0.725    | 0.7006    | 0.6738 | 0.6759 |
| 0.0126        | 16.0  | 800  | 2.3679          | 0.74     | 0.7050    | 0.6839 | 0.6898 |
| 0.0023        | 17.0  | 850  | 2.5252          | 0.745    | 0.7119    | 0.6880 | 0.6933 |
| 0.01          | 18.0  | 900  | 2.5598          | 0.74     | 0.7056    | 0.6828 | 0.6906 |
| 0.0093        | 19.0  | 950  | 2.4353          | 0.745    | 0.7057    | 0.6922 | 0.6974 |
| 0.0039        | 20.0  | 1000 | 2.4223          | 0.75     | 0.7128    | 0.6998 | 0.7043 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
