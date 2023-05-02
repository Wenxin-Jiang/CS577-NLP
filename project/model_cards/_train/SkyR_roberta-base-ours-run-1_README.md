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
- name: run-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# run-1

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.3480
- Accuracy: 0.73
- Precision: 0.6930
- Recall: 0.6829
- F1: 0.6871

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
| 1.0042        | 1.0   | 50   | 0.8281          | 0.665    | 0.6105    | 0.6240 | 0.6016 |
| 0.8062        | 2.0   | 100  | 0.9313          | 0.665    | 0.6513    | 0.6069 | 0.5505 |
| 0.627         | 3.0   | 150  | 0.8275          | 0.72     | 0.6713    | 0.6598 | 0.6638 |
| 0.4692        | 4.0   | 200  | 0.8289          | 0.68     | 0.6368    | 0.6447 | 0.6398 |
| 0.2766        | 5.0   | 250  | 1.1263          | 0.72     | 0.6893    | 0.6431 | 0.6417 |
| 0.1868        | 6.0   | 300  | 1.2901          | 0.725    | 0.6823    | 0.6727 | 0.6764 |
| 0.1054        | 7.0   | 350  | 1.6742          | 0.68     | 0.6696    | 0.6427 | 0.6384 |
| 0.0837        | 8.0   | 400  | 1.6199          | 0.72     | 0.6826    | 0.6735 | 0.6772 |
| 0.0451        | 9.0   | 450  | 1.8324          | 0.735    | 0.7029    | 0.6726 | 0.6727 |
| 0.0532        | 10.0  | 500  | 2.1136          | 0.705    | 0.6949    | 0.6725 | 0.6671 |
| 0.0178        | 11.0  | 550  | 2.1136          | 0.73     | 0.6931    | 0.6810 | 0.6832 |
| 0.0111        | 12.0  | 600  | 2.2740          | 0.69     | 0.6505    | 0.6430 | 0.6461 |
| 0.0205        | 13.0  | 650  | 2.3026          | 0.725    | 0.6965    | 0.6685 | 0.6716 |
| 0.0181        | 14.0  | 700  | 2.2901          | 0.735    | 0.7045    | 0.6806 | 0.6876 |
| 0.0074        | 15.0  | 750  | 2.2277          | 0.74     | 0.7075    | 0.6923 | 0.6978 |
| 0.0063        | 16.0  | 800  | 2.2720          | 0.75     | 0.7229    | 0.7051 | 0.7105 |
| 0.0156        | 17.0  | 850  | 2.1237          | 0.73     | 0.6908    | 0.6841 | 0.6854 |
| 0.0027        | 18.0  | 900  | 2.2376          | 0.73     | 0.6936    | 0.6837 | 0.6874 |
| 0.003         | 19.0  | 950  | 2.3359          | 0.735    | 0.6992    | 0.6897 | 0.6937 |
| 0.0012        | 20.0  | 1000 | 2.3480          | 0.73     | 0.6930    | 0.6829 | 0.6871 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
