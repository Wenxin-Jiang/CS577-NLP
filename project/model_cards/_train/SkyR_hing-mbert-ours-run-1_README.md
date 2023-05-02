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
- name: hing-mbert-ours-run-1
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-ours-run-1

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.9965
- Accuracy: 0.665
- Precision: 0.6151
- Recall: 0.6082
- F1: 0.6090

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9757        | 1.0   | 100  | 0.7526          | 0.665    | 0.6358    | 0.6149 | 0.5854 |
| 0.7227        | 2.0   | 200  | 1.1062          | 0.69     | 0.6679    | 0.6031 | 0.6025 |
| 0.4345        | 3.0   | 300  | 1.2601          | 0.67     | 0.6512    | 0.6031 | 0.6001 |
| 0.2738        | 4.0   | 400  | 1.4485          | 0.67     | 0.6333    | 0.5968 | 0.6050 |
| 0.1171        | 5.0   | 500  | 1.9132          | 0.65     | 0.6216    | 0.6170 | 0.5944 |
| 0.0941        | 6.0   | 600  | 1.8293          | 0.685    | 0.6420    | 0.6439 | 0.6409 |
| 0.0348        | 7.0   | 700  | 2.3249          | 0.675    | 0.6424    | 0.6386 | 0.6384 |
| 0.0317        | 8.0   | 800  | 2.4134          | 0.67     | 0.6171    | 0.6120 | 0.6128 |
| 0.0056        | 9.0   | 900  | 2.6733          | 0.68     | 0.6343    | 0.6313 | 0.6300 |
| 0.0095        | 10.0  | 1000 | 2.5950          | 0.685    | 0.6318    | 0.6289 | 0.6295 |
| 0.0081        | 11.0  | 1100 | 2.3885          | 0.69     | 0.6407    | 0.6434 | 0.6410 |
| 0.023         | 12.0  | 1200 | 2.4087          | 0.67     | 0.6206    | 0.6231 | 0.6212 |
| 0.0054        | 13.0  | 1300 | 2.4516          | 0.675    | 0.6229    | 0.6227 | 0.6128 |
| 0.0047        | 14.0  | 1400 | 2.6152          | 0.68     | 0.6285    | 0.6256 | 0.6263 |
| 0.0063        | 15.0  | 1500 | 2.8077          | 0.69     | 0.6498    | 0.6281 | 0.6309 |
| 0.0028        | 16.0  | 1600 | 2.7084          | 0.675    | 0.6254    | 0.6214 | 0.6207 |
| 0.0025        | 17.0  | 1700 | 2.8360          | 0.67     | 0.6175    | 0.6128 | 0.6145 |
| 0.0011        | 18.0  | 1800 | 2.8591          | 0.655    | 0.6001    | 0.5958 | 0.5971 |
| 0.0005        | 19.0  | 1900 | 2.9419          | 0.665    | 0.6151    | 0.6082 | 0.6090 |
| 0.0002        | 20.0  | 2000 | 2.9965          | 0.665    | 0.6151    | 0.6082 | 0.6090 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
