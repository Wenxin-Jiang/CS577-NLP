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
- name: hing-mbert-ours-run-5
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# hing-mbert-ours-run-5

This model is a fine-tuned version of [l3cube-pune/hing-mbert](https://huggingface.co/l3cube-pune/hing-mbert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 3.2437
- Accuracy: 0.665
- Precision: 0.6223
- Recall: 0.5991
- F1: 0.6039

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
| 0.9643        | 1.0   | 100  | 0.7996          | 0.69     | 0.6596    | 0.6593 | 0.6521 |
| 0.6951        | 2.0   | 200  | 1.0464          | 0.66     | 0.6597    | 0.5831 | 0.5734 |
| 0.4245        | 3.0   | 300  | 0.9640          | 0.64     | 0.6025    | 0.6033 | 0.6010 |
| 0.238         | 4.0   | 400  | 1.6744          | 0.68     | 0.7095    | 0.6445 | 0.6359 |
| 0.1477        | 5.0   | 500  | 1.7115          | 0.665    | 0.6362    | 0.6422 | 0.6360 |
| 0.1206        | 6.0   | 600  | 2.0459          | 0.635    | 0.5749    | 0.5752 | 0.5726 |
| 0.0528        | 7.0   | 700  | 2.5698          | 0.66     | 0.6230    | 0.5904 | 0.5985 |
| 0.0525        | 8.0   | 800  | 2.2729          | 0.625    | 0.5741    | 0.5860 | 0.5733 |
| 0.0174        | 9.0   | 900  | 2.6227          | 0.635    | 0.6099    | 0.6044 | 0.6019 |
| 0.0088        | 10.0  | 1000 | 2.8854          | 0.63     | 0.5699    | 0.5676 | 0.5680 |
| 0.0085        | 11.0  | 1100 | 3.2173          | 0.655    | 0.6043    | 0.5771 | 0.5821 |
| 0.0121        | 12.0  | 1200 | 3.1270          | 0.665    | 0.6214    | 0.5903 | 0.5971 |
| 0.0141        | 13.0  | 1300 | 2.6648          | 0.655    | 0.5981    | 0.5978 | 0.5961 |
| 0.0116        | 14.0  | 1400 | 3.1711          | 0.665    | 0.6192    | 0.5915 | 0.5971 |
| 0.007         | 15.0  | 1500 | 3.0954          | 0.66     | 0.6156    | 0.5961 | 0.6009 |
| 0.0037        | 16.0  | 1600 | 3.3065          | 0.65     | 0.6027    | 0.5791 | 0.5824 |
| 0.0031        | 17.0  | 1700 | 3.1715          | 0.665    | 0.6177    | 0.5999 | 0.6048 |
| 0.0021        | 18.0  | 1800 | 3.1602          | 0.665    | 0.6220    | 0.6029 | 0.6082 |
| 0.0021        | 19.0  | 1900 | 3.2027          | 0.655    | 0.6096    | 0.5893 | 0.5937 |
| 0.0018        | 20.0  | 2000 | 3.2437          | 0.665    | 0.6223    | 0.5991 | 0.6039 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
