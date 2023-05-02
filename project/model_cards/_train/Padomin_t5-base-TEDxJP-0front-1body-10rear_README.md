---
license: cc-by-sa-4.0
tags:
- generated_from_trainer
datasets:
- te_dx_jp
model-index:
- name: t5-base-TEDxJP-0front-1body-10rear
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# t5-base-TEDxJP-0front-1body-10rear

This model is a fine-tuned version of [sonoisa/t5-base-japanese](https://huggingface.co/sonoisa/t5-base-japanese) on the te_dx_jp dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4646
- Wer: 0.1756
- Mer: 0.1698
- Wil: 0.2581
- Wip: 0.7419
- Hits: 55450
- Substitutions: 6518
- Deletions: 2619
- Insertions: 2202
- Cer: 0.1383

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0001
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 10

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Wer    | Mer    | Wil    | Wip    | Hits  | Substitutions | Deletions | Insertions | Cer    |
|:-------------:|:-----:|:-----:|:---------------:|:------:|:------:|:------:|:------:|:-----:|:-------------:|:---------:|:----------:|:------:|
| 0.6456        | 1.0   | 1457  | 0.4955          | 0.2298 | 0.2127 | 0.3032 | 0.6968 | 54935 | 6936          | 2716      | 5190       | 0.2008 |
| 0.5333        | 2.0   | 2914  | 0.4472          | 0.1817 | 0.1755 | 0.2646 | 0.7354 | 55142 | 6584          | 2861      | 2291       | 0.1431 |
| 0.4864        | 3.0   | 4371  | 0.4420          | 0.1774 | 0.1714 | 0.2600 | 0.7400 | 55396 | 6542          | 2649      | 2266       | 0.1397 |
| 0.429         | 4.0   | 5828  | 0.4374          | 0.1764 | 0.1704 | 0.2587 | 0.7413 | 55446 | 6512          | 2629      | 2249       | 0.1389 |
| 0.3741        | 5.0   | 7285  | 0.4413          | 0.1744 | 0.1687 | 0.2559 | 0.7441 | 55518 | 6416          | 2653      | 2198       | 0.1383 |
| 0.3467        | 6.0   | 8742  | 0.4467          | 0.1742 | 0.1686 | 0.2564 | 0.7436 | 55493 | 6466          | 2628      | 2159       | 0.1390 |
| 0.3761        | 7.0   | 10199 | 0.4524          | 0.1754 | 0.1696 | 0.2577 | 0.7423 | 55471 | 6498          | 2618      | 2210       | 0.1380 |
| 0.3102        | 8.0   | 11656 | 0.4557          | 0.1751 | 0.1695 | 0.2574 | 0.7426 | 55412 | 6478          | 2697      | 2133       | 0.1395 |
| 0.3008        | 9.0   | 13113 | 0.4632          | 0.1758 | 0.1700 | 0.2584 | 0.7416 | 55421 | 6516          | 2650      | 2189       | 0.1387 |
| 0.3051        | 10.0  | 14570 | 0.4646          | 0.1756 | 0.1698 | 0.2581 | 0.7419 | 55450 | 6518          | 2619      | 2202       | 0.1383 |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1+cu116
- Datasets 2.4.0
- Tokenizers 0.12.1
