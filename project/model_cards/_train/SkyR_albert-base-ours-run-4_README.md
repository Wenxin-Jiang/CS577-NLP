---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: albert-base-ours-run-4
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# albert-base-ours-run-4

This model is a fine-tuned version of [albert-base-v2](https://huggingface.co/albert-base-v2) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.9565
- Accuracy: 0.72
- Precision: 0.6790
- Recall: 0.6770
- F1: 0.6766

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0253        | 1.0   | 200  | 0.8974          | 0.605    | 0.7186    | 0.5341 | 0.4555 |
| 0.8121        | 2.0   | 400  | 0.8260          | 0.675    | 0.6792    | 0.6308 | 0.6112 |
| 0.6153        | 3.0   | 600  | 0.8504          | 0.66     | 0.6180    | 0.6026 | 0.6073 |
| 0.441         | 4.0   | 800  | 0.8917          | 0.685    | 0.6463    | 0.6385 | 0.6403 |
| 0.3273        | 5.0   | 1000 | 0.9384          | 0.69     | 0.6534    | 0.6602 | 0.6561 |
| 0.2138        | 6.0   | 1200 | 1.3501          | 0.705    | 0.6573    | 0.6374 | 0.6388 |
| 0.1435        | 7.0   | 1400 | 1.4614          | 0.71     | 0.6693    | 0.6553 | 0.6601 |
| 0.1202        | 8.0   | 1600 | 1.5825          | 0.7      | 0.6648    | 0.6592 | 0.6530 |
| 0.0587        | 9.0   | 1800 | 1.7755          | 0.72     | 0.6839    | 0.6849 | 0.6840 |
| 0.0237        | 10.0  | 2000 | 1.7240          | 0.735    | 0.6960    | 0.6924 | 0.6940 |
| 0.018         | 11.0  | 2200 | 1.7230          | 0.745    | 0.7105    | 0.7003 | 0.7026 |
| 0.0096        | 12.0  | 2400 | 1.7812          | 0.75     | 0.7225    | 0.7142 | 0.7158 |
| 0.006         | 13.0  | 2600 | 1.8223          | 0.75     | 0.7265    | 0.7082 | 0.7147 |
| 0.0033        | 14.0  | 2800 | 1.9872          | 0.76     | 0.7434    | 0.7107 | 0.7188 |
| 0.003         | 15.0  | 3000 | 1.8818          | 0.72     | 0.6778    | 0.6766 | 0.6765 |
| 0.0027        | 16.0  | 3200 | 1.9816          | 0.75     | 0.7125    | 0.6990 | 0.7043 |
| 0.002         | 17.0  | 3400 | 1.9268          | 0.725    | 0.6832    | 0.6834 | 0.6825 |
| 0.0023        | 18.0  | 3600 | 1.9456          | 0.73     | 0.6913    | 0.6898 | 0.6898 |
| 0.0025        | 19.0  | 3800 | 1.9543          | 0.72     | 0.6790    | 0.6770 | 0.6766 |
| 0.0016        | 20.0  | 4000 | 1.9565          | 0.72     | 0.6790    | 0.6770 | 0.6766 |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Tokenizers 0.13.2
