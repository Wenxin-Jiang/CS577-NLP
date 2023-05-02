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
- name: hing-mbert-ours-run-2
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-ours-run-2

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.3919
- Accuracy: 0.62
- Precision: 0.5759
- Recall: 0.5631
- F1: 0.5669

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
| 1.0284        | 1.0   | 100  | 1.2914          | 0.595    | 0.5712    | 0.4800 | 0.4642 |
| 0.8127        | 2.0   | 200  | 0.8552          | 0.59     | 0.5744    | 0.5675 | 0.4891 |
| 0.5499        | 3.0   | 300  | 1.1212          | 0.645    | 0.6544    | 0.5600 | 0.5475 |
| 0.3433        | 4.0   | 400  | 1.2017          | 0.605    | 0.5872    | 0.5866 | 0.5791 |
| 0.2218        | 5.0   | 500  | 1.8329          | 0.655    | 0.6458    | 0.6064 | 0.6055 |
| 0.1763        | 6.0   | 600  | 2.4194          | 0.655    | 0.6140    | 0.5802 | 0.5871 |
| 0.1022        | 7.0   | 700  | 2.3894          | 0.66     | 0.6171    | 0.6045 | 0.6048 |
| 0.0631        | 8.0   | 800  | 2.8259          | 0.605    | 0.5704    | 0.5255 | 0.5259 |
| 0.0254        | 9.0   | 900  | 2.9135          | 0.65     | 0.6013    | 0.5734 | 0.5784 |
| 0.0316        | 10.0  | 1000 | 3.0548          | 0.62     | 0.5862    | 0.5650 | 0.5670 |
| 0.026         | 11.0  | 1100 | 3.1020          | 0.62     | 0.5722    | 0.5593 | 0.5619 |
| 0.0152        | 12.0  | 1200 | 3.0692          | 0.62     | 0.5685    | 0.5597 | 0.5621 |
| 0.0156        | 13.0  | 1300 | 3.1068          | 0.615    | 0.5771    | 0.5589 | 0.5624 |
| 0.0237        | 14.0  | 1400 | 3.3487          | 0.62     | 0.5924    | 0.5589 | 0.5642 |
| 0.0094        | 15.0  | 1500 | 3.2007          | 0.615    | 0.5665    | 0.5639 | 0.5650 |
| 0.0054        | 16.0  | 1600 | 3.2838          | 0.62     | 0.5807    | 0.5657 | 0.5690 |
| 0.005         | 17.0  | 1700 | 3.2258          | 0.615    | 0.5846    | 0.5723 | 0.5747 |
| 0.005         | 18.0  | 1800 | 3.3572          | 0.63     | 0.5827    | 0.5698 | 0.5736 |
| 0.0022        | 19.0  | 1900 | 3.3642          | 0.62     | 0.5759    | 0.5631 | 0.5669 |
| 0.0019        | 20.0  | 2000 | 3.3919          | 0.62     | 0.5759    | 0.5631 | 0.5669 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
