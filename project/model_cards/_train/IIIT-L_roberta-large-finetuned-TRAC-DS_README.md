---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: roberta-large-finetuned-TRAC-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# roberta-large-finetuned-TRAC-DS

This model is a fine-tuned version of [roberta-large](https://huggingface.co/roberta-large) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.8198
- Accuracy: 0.7190
- Precision: 0.6955
- Recall: 0.6979
- F1: 0.6963

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
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 20

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 0.9538        | 1.0   | 612   | 0.8083          | 0.6111   | 0.6192    | 0.6164 | 0.5994 |
| 0.7924        | 2.0   | 1224  | 0.7594          | 0.6601   | 0.6688    | 0.6751 | 0.6424 |
| 0.6844        | 3.0   | 1836  | 0.6986          | 0.7042   | 0.6860    | 0.6969 | 0.6858 |
| 0.5715        | 3.99  | 2448  | 0.7216          | 0.7075   | 0.6957    | 0.6978 | 0.6925 |
| 0.45          | 4.99  | 3060  | 0.7963          | 0.7288   | 0.7126    | 0.7074 | 0.7073 |
| 0.352         | 5.99  | 3672  | 1.0824          | 0.7141   | 0.6999    | 0.6774 | 0.6818 |
| 0.2546        | 6.99  | 4284  | 1.0884          | 0.7230   | 0.7006    | 0.7083 | 0.7028 |
| 0.1975        | 7.99  | 4896  | 1.5338          | 0.7337   | 0.7090    | 0.7063 | 0.7074 |
| 0.1656        | 8.99  | 5508  | 1.8182          | 0.7100   | 0.6882    | 0.6989 | 0.6896 |
| 0.1358        | 9.98  | 6120  | 2.1623          | 0.7173   | 0.6917    | 0.6959 | 0.6934 |
| 0.1235        | 10.98 | 6732  | 2.3249          | 0.7141   | 0.6881    | 0.6914 | 0.6888 |
| 0.1003        | 11.98 | 7344  | 2.3474          | 0.7124   | 0.6866    | 0.6920 | 0.6887 |
| 0.0826        | 12.98 | 7956  | 2.3574          | 0.7083   | 0.6853    | 0.6959 | 0.6874 |
| 0.0727        | 13.98 | 8568  | 2.4989          | 0.7116   | 0.6858    | 0.6934 | 0.6883 |
| 0.0553        | 14.98 | 9180  | 2.8090          | 0.7026   | 0.6747    | 0.6710 | 0.6725 |
| 0.0433        | 15.97 | 9792  | 2.6647          | 0.7255   | 0.7010    | 0.7028 | 0.7018 |
| 0.0449        | 16.97 | 10404 | 2.6568          | 0.7247   | 0.7053    | 0.6997 | 0.7010 |
| 0.0373        | 17.97 | 11016 | 2.7632          | 0.7149   | 0.6888    | 0.6938 | 0.6909 |
| 0.0278        | 18.97 | 11628 | 2.8245          | 0.7124   | 0.6866    | 0.6930 | 0.6889 |
| 0.0288        | 19.97 | 12240 | 2.8198          | 0.7190   | 0.6955    | 0.6979 | 0.6963 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
