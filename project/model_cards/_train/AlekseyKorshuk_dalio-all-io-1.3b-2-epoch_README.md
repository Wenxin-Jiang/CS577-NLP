---
license: other
tags:
- generated_from_trainer
datasets:
- AlekseyKorshuk/dalio-all-io
metrics:
- accuracy
model-index:
- name: dalio-all-io-1.3b-2-epoch
  results:
  - task:
      name: Causal Language Modeling
      type: text-generation
    dataset:
      name: AlekseyKorshuk/dalio-all-io
      type: AlekseyKorshuk/dalio-all-io
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.057553854065481976
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# dalio-all-io-1.3b-2-epoch

This model is a fine-tuned version of [facebook/opt-1.3b](https://huggingface.co/facebook/opt-1.3b) on the AlekseyKorshuk/dalio-all-io dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2949
- Accuracy: 0.0576

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
- num_epochs: 2.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 2.6543        | 0.03  | 1    | 2.6113          | 0.0513   |
| 2.6077        | 0.07  | 2    | 2.6113          | 0.0513   |
| 2.5964        | 0.1   | 3    | 2.5605          | 0.0519   |
| 2.7302        | 0.14  | 4    | 2.5234          | 0.0527   |
| 2.7002        | 0.17  | 5    | 2.5078          | 0.0529   |
| 2.5674        | 0.21  | 6    | 2.4941          | 0.0533   |
| 2.6399        | 0.24  | 7    | 2.4883          | 0.0534   |
| 2.533         | 0.28  | 8    | 2.4805          | 0.0536   |
| 2.7202        | 0.31  | 9    | 2.4746          | 0.0536   |
| 2.5137        | 0.34  | 10   | 2.4648          | 0.0534   |
| 2.499         | 0.38  | 11   | 2.4512          | 0.0536   |
| 2.7026        | 0.41  | 12   | 2.4414          | 0.0539   |
| 2.5254        | 0.45  | 13   | 2.4336          | 0.0543   |
| 2.5667        | 0.48  | 14   | 2.4238          | 0.0545   |
| 2.5715        | 0.52  | 15   | 2.4160          | 0.0548   |
| 2.3739        | 0.55  | 16   | 2.4102          | 0.0550   |
| 2.4756        | 0.59  | 17   | 2.4043          | 0.0549   |
| 2.4783        | 0.62  | 18   | 2.3984          | 0.0550   |
| 2.5665        | 0.66  | 19   | 2.3906          | 0.0549   |
| 2.4888        | 0.69  | 20   | 2.3906          | 0.0549   |
| 2.4476        | 0.72  | 21   | 2.3828          | 0.0550   |
| 2.604         | 0.76  | 22   | 2.375           | 0.0552   |
| 2.3416        | 0.79  | 23   | 2.3652          | 0.0554   |
| 2.6028        | 0.83  | 24   | 2.3555          | 0.0555   |
| 2.3425        | 0.86  | 25   | 2.3477          | 0.0558   |
| 2.4142        | 0.9   | 26   | 2.3398          | 0.0558   |
| 2.5317        | 0.93  | 27   | 2.3340          | 0.0559   |
| 2.4119        | 0.97  | 28   | 2.3301          | 0.0561   |
| 2.4048        | 1.0   | 29   | 2.3262          | 0.0563   |
| 1.9646        | 1.03  | 30   | 2.3242          | 0.0564   |
| 1.9233        | 1.07  | 31   | 2.3203          | 0.0563   |
| 1.9276        | 1.1   | 32   | 2.3203          | 0.0564   |
| 1.8702        | 1.14  | 33   | 2.3281          | 0.0565   |
| 2.0997        | 1.17  | 34   | 2.3340          | 0.0565   |
| 1.7943        | 1.21  | 35   | 2.3320          | 0.0568   |
| 1.8579        | 1.24  | 36   | 2.3242          | 0.0567   |
| 1.8844        | 1.28  | 37   | 2.3145          | 0.0568   |
| 1.9288        | 1.31  | 38   | 2.3086          | 0.0569   |
| 1.6616        | 1.34  | 39   | 2.3047          | 0.0570   |
| 1.6443        | 1.38  | 40   | 2.3047          | 0.0571   |
| 1.7616        | 1.41  | 41   | 2.3027          | 0.0572   |
| 1.7904        | 1.45  | 42   | 2.3027          | 0.0571   |
| 1.8762        | 1.48  | 43   | 2.3027          | 0.0573   |
| 1.6569        | 1.52  | 44   | 2.3027          | 0.0573   |
| 1.647         | 1.55  | 45   | 2.3027          | 0.0573   |
| 1.8168        | 1.59  | 46   | 2.3027          | 0.0574   |
| 1.7194        | 1.62  | 47   | 2.3027          | 0.0573   |
| 1.7667        | 1.66  | 48   | 2.3027          | 0.0572   |
| 1.7621        | 1.69  | 49   | 2.3027          | 0.0573   |
| 1.7269        | 1.72  | 50   | 2.3008          | 0.0573   |
| 1.7815        | 1.76  | 51   | 2.3008          | 0.0574   |
| 1.8318        | 1.79  | 52   | 2.2988          | 0.0574   |
| 1.9366        | 1.83  | 53   | 2.2988          | 0.0575   |
| 1.736         | 1.86  | 54   | 2.2969          | 0.0576   |
| 1.9984        | 1.9   | 55   | 2.2969          | 0.0575   |
| 1.7203        | 1.93  | 56   | 2.2949          | 0.0575   |
| 1.7391        | 1.97  | 57   | 2.2949          | 0.0576   |
| 1.6611        | 2.0   | 58   | 2.2949          | 0.0576   |


### Framework versions

- Transformers 4.25.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.3.2
- Tokenizers 0.12.1
