---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- precision
- recall
- f1
- accuracy
model-index:
- name: bert-finetuned-mutation-recognition-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-finetuned-mutation-recognition-2

This model is a fine-tuned version of [bert-base-cased](https://huggingface.co/bert-base-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0818
- Dnamutation F1: 0.6371
- Snp F1: 0.0952
- Proteinmutation F1: 0.8412
- Precision: 0.7646
- Recall: 0.6596
- F1: 0.7082
- Accuracy: 0.9877

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step | Validation Loss | Dnamutation F1 | Snp F1 | Proteinmutation F1 | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------------:|:------:|:------------------:|:---------:|:------:|:------:|:--------:|
| No log        | 1.0   | 403  | 0.0383          | 0.5871         | 0.0    | 0.7573             | 0.6195    | 0.6770 | 0.6470 | 0.9872   |
| 0.0863        | 2.0   | 806  | 0.0349          | 0.6202         | 0.0    | 0.8646             | 0.6815    | 0.7408 | 0.7099 | 0.9889   |
| 0.0295        | 3.0   | 1209 | 0.0415          | 0.5670         | 0.0    | 0.7689             | 0.6887    | 0.6035 | 0.6433 | 0.9866   |
| 0.019         | 4.0   | 1612 | 0.0430          | 0.5909         | 0.4742 | 0.7840             | 0.6667    | 0.6615 | 0.6641 | 0.9881   |
| 0.0127        | 5.0   | 2015 | 0.0507          | 0.6345         | 0.0    | 0.8455             | 0.7290    | 0.6867 | 0.7072 | 0.9885   |
| 0.0127        | 6.0   | 2418 | 0.0678          | 0.5946         | 0.05   | 0.8087             | 0.7471    | 0.6170 | 0.6758 | 0.9868   |
| 0.0067        | 7.0   | 2821 | 0.0544          | 0.6693         | 0.2727 | 0.8475             | 0.7208    | 0.7292 | 0.725  | 0.9884   |
| 0.0042        | 8.0   | 3224 | 0.0642          | 0.6694         | 0.2000 | 0.8401             | 0.7390    | 0.7118 | 0.7251 | 0.9885   |
| 0.0019        | 9.0   | 3627 | 0.0847          | 0.6271         | 0.0976 | 0.8416             | 0.7671    | 0.6499 | 0.7037 | 0.9877   |
| 0.0014        | 10.0  | 4030 | 0.0818          | 0.6371         | 0.0952 | 0.8412             | 0.7646    | 0.6596 | 0.7082 | 0.9877   |


### Framework versions

- Transformers 4.17.0
- Pytorch 1.10.2
- Datasets 2.0.0
- Tokenizers 0.12.1
