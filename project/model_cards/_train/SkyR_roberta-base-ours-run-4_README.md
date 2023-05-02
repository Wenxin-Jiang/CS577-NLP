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
- name: run-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# run-4

This model is a fine-tuned version of [roberta-base](https://huggingface.co/roberta-base) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.6296
- Accuracy: 0.685
- Precision: 0.6248
- Recall: 0.6164
- F1: 0.6188

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
| 1.0195        | 1.0   | 50   | 0.8393          | 0.615    | 0.4126    | 0.5619 | 0.4606 |
| 0.7594        | 2.0   | 100  | 0.7077          | 0.7      | 0.6896    | 0.6663 | 0.6178 |
| 0.5515        | 3.0   | 150  | 0.9342          | 0.68     | 0.6334    | 0.5989 | 0.6016 |
| 0.3739        | 4.0   | 200  | 0.7755          | 0.735    | 0.7032    | 0.7164 | 0.7063 |
| 0.2648        | 5.0   | 250  | 0.9200          | 0.7      | 0.6584    | 0.6677 | 0.6611 |
| 0.1726        | 6.0   | 300  | 1.1898          | 0.71     | 0.6653    | 0.6550 | 0.6570 |
| 0.1452        | 7.0   | 350  | 1.5086          | 0.73     | 0.6884    | 0.6768 | 0.6812 |
| 0.0856        | 8.0   | 400  | 2.6159          | 0.68     | 0.6754    | 0.5863 | 0.5951 |
| 0.1329        | 9.0   | 450  | 1.9491          | 0.71     | 0.6692    | 0.6442 | 0.6463 |
| 0.0322        | 10.0  | 500  | 1.7897          | 0.74     | 0.6977    | 0.6939 | 0.6946 |
| 0.0345        | 11.0  | 550  | 1.9100          | 0.725    | 0.6827    | 0.6853 | 0.6781 |
| 0.026         | 12.0  | 600  | 2.5041          | 0.68     | 0.6246    | 0.6115 | 0.6137 |
| 0.0084        | 13.0  | 650  | 2.5343          | 0.715    | 0.6708    | 0.6617 | 0.6637 |
| 0.0145        | 14.0  | 700  | 2.4112          | 0.715    | 0.6643    | 0.6595 | 0.6614 |
| 0.0119        | 15.0  | 750  | 2.5303          | 0.705    | 0.6479    | 0.6359 | 0.6390 |
| 0.0026        | 16.0  | 800  | 2.6299          | 0.705    | 0.6552    | 0.6447 | 0.6455 |
| 0.0077        | 17.0  | 850  | 2.4044          | 0.715    | 0.6667    | 0.6576 | 0.6596 |
| 0.0055        | 18.0  | 900  | 2.8077          | 0.68     | 0.6208    | 0.6065 | 0.6098 |
| 0.0078        | 19.0  | 950  | 2.5608          | 0.68     | 0.6200    | 0.6104 | 0.6129 |
| 0.0018        | 20.0  | 1000 | 2.6296          | 0.685    | 0.6248    | 0.6164 | 0.6188 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.1+cu116
- Tokenizers 0.13.2
