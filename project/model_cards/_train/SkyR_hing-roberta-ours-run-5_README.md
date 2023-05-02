---
license: cc-by-4.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: hing-roberta-ours-run-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-roberta-ours-run-5

This model is a fine-tuned version of [l3cube-pune/hing-roberta](https://huggingface.co/l3cube-pune/hing-roberta) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.0980
- Accuracy: 0.725
- Precision: 0.6881
- Recall: 0.6575
- F1: 0.6651

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9336        | 1.0   | 200  | 0.7394          | 0.675    | 0.6450    | 0.6509 | 0.6398 |
| 0.6924        | 2.0   | 400  | 0.9530          | 0.66     | 0.6285    | 0.5845 | 0.5551 |
| 0.4406        | 3.0   | 600  | 0.8914          | 0.68     | 0.6462    | 0.6527 | 0.6479 |
| 0.2493        | 4.0   | 800  | 1.7083          | 0.68     | 0.6441    | 0.6446 | 0.6426 |
| 0.1231        | 5.0   | 1000 | 1.9496          | 0.695    | 0.6570    | 0.6624 | 0.6591 |
| 0.0788        | 6.0   | 1200 | 2.5025          | 0.67     | 0.6209    | 0.6039 | 0.6011 |
| 0.0408        | 7.0   | 1400 | 2.2651          | 0.695    | 0.6594    | 0.6617 | 0.6517 |
| 0.0434        | 8.0   | 1600 | 2.4072          | 0.725    | 0.6941    | 0.6754 | 0.6710 |
| 0.0074        | 9.0   | 1800 | 2.7817          | 0.7      | 0.6535    | 0.6467 | 0.6488 |
| 0.023         | 10.0  | 2000 | 2.8578          | 0.7      | 0.6470    | 0.6353 | 0.6337 |
| 0.0151        | 11.0  | 2200 | 2.7783          | 0.695    | 0.6457    | 0.6373 | 0.6390 |
| 0.0108        | 12.0  | 2400 | 2.5953          | 0.695    | 0.6563    | 0.6586 | 0.6564 |
| 0.0192        | 13.0  | 2600 | 3.0715          | 0.705    | 0.6631    | 0.6326 | 0.6320 |
| 0.0149        | 14.0  | 2800 | 3.1048          | 0.715    | 0.6769    | 0.6450 | 0.6503 |
| 0.0205        | 15.0  | 3000 | 2.7812          | 0.71     | 0.6657    | 0.6538 | 0.6565 |
| 0.0024        | 16.0  | 3200 | 2.9304          | 0.72     | 0.6796    | 0.6537 | 0.6610 |
| 0.0033        | 17.0  | 3400 | 2.7170          | 0.73     | 0.6899    | 0.6760 | 0.6811 |
| 0.0056        | 18.0  | 3600 | 2.9693          | 0.72     | 0.6783    | 0.6560 | 0.6628 |
| 0.0015        | 19.0  | 3800 | 3.0943          | 0.72     | 0.6825    | 0.6541 | 0.6611 |
| 0.0017        | 20.0  | 4000 | 3.0980          | 0.725    | 0.6881    | 0.6575 | 0.6651 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
