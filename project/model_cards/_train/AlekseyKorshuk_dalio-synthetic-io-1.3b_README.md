---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-synthetic-io
metrics:
- accuracy
model-index:
- name: dalio-synthetic-io-1.3b
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-synthetic-io
      type: AlekseyKorshuk/dalio-synthetic-io
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.06357949136406908
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dalio-synthetic-io-1.3b

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the AlekseyKorshuk/dalio-synthetic-io dataset.
It achieves the following results on the evaluation set:
- Loss: 2.4961
- Accuracy: 0.0636

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 3e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- distributed_type: multi-GPU
- num_devices: 8
- total_train_batch_size: 16
- total_eval_batch_size: 16
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- num_epochs: 1.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6941        | 0.05  | 1    | 2.6543          | 0.0622   |
| 2.6914        | 0.11  | 2    | 2.6543          | 0.0622   |
| 2.6003        | 0.16  | 3    | 2.6016          | 0.0627   |
| 2.5603        | 0.21  | 4    | 2.5703          | 0.0626   |
| 2.606         | 0.26  | 5    | 2.5508          | 0.0629   |
| 2.5439        | 0.32  | 6    | 2.5449          | 0.0629   |
| 2.4449        | 0.37  | 7    | 2.5469          | 0.0629   |
| 2.5422        | 0.42  | 8    | 2.5469          | 0.0630   |
| 2.6101        | 0.47  | 9    | 2.5410          | 0.0632   |
| 2.4482        | 0.53  | 10   | 2.5352          | 0.0630   |
| 2.501         | 0.58  | 11   | 2.5293          | 0.0631   |
| 2.5967        | 0.63  | 12   | 2.5215          | 0.0634   |
| 2.4998        | 0.68  | 13   | 2.5137          | 0.0635   |
| 2.5957        | 0.74  | 14   | 2.5098          | 0.0636   |
| 2.5967        | 0.79  | 15   | 2.5039          | 0.0639   |
| 2.5022        | 0.84  | 16   | 2.5             | 0.0637   |
| 2.4314        | 0.89  | 17   | 2.4980          | 0.0637   |
| 2.6279        | 0.95  | 18   | 2.4961          | 0.0636   |
| 2.571         | 1.0   | 19   | 2.4961          | 0.0636   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
