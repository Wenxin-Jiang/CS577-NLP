---
model-index:
- name: eurocorpV4
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: sroie
      type: sroie
      config: discharge
      split: test
      args: discharge
    metrics:
    - name: Precision
      type: precision
      value: 0.9548022598870056
    - name: Recall
      type: recall
      value: 0.9602272727272727
    - name: F1
      type: f1
      value: 0.9575070821529744
    - name: Accuracy
      type: accuracy
      value: 0.9819121447028424
pipeline_tag: document-question-answering
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# eurocorpV4

This model is a fine-tuned version of [microsoft/layoutlmv3-large](https://huggingface.co/microsoft/layoutlmv3-large) on the sroie dataset.
It achieves the following results on the evaluation set:
- Loss: 0.1239
- Precision: 0.9548
- Recall: 0.9602
- F1: 0.9575
- Accuracy: 0.9819

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 1000

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| No log        | 0.33  | 100  | 0.3452          | 0.7399    | 0.7273 | 0.7335 | 0.9276   |
| No log        | 0.66  | 200  | 0.1688          | 0.9070    | 0.8864 | 0.8966 | 0.9677   |
| No log        | 0.99  | 300  | 0.1135          | 0.9157    | 0.9261 | 0.9209 | 0.9742   |
| No log        | 1.32  | 400  | 0.1319          | 0.9261    | 0.9261 | 0.9261 | 0.9742   |
| 0.2834        | 1.65  | 500  | 0.1300          | 0.9375    | 0.9375 | 0.9375 | 0.9755   |
| 0.2834        | 1.98  | 600  | 0.1384          | 0.9598    | 0.9489 | 0.9543 | 0.9780   |
| 0.2834        | 2.31  | 700  | 0.1298          | 0.9266    | 0.9318 | 0.9292 | 0.9767   |
| 0.2834        | 2.64  | 800  | 0.1232          | 0.9438    | 0.9545 | 0.9492 | 0.9806   |
| 0.2834        | 2.97  | 900  | 0.1261          | 0.9548    | 0.9602 | 0.9575 | 0.9819   |
| 0.0247        | 3.3   | 1000 | 0.1239          | 0.9548    | 0.9602 | 0.9575 | 0.9819   |


### Framework versions

- Transformers 4.26.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.2.2
- Tokenizers 0.13.2