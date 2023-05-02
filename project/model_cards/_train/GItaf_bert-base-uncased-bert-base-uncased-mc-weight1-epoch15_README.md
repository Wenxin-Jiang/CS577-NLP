---
tags:
- generated_from_trainer
model-index:
- name: bert-base-uncased-bert-base-uncased-mc-weight1-epoch15
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-uncased-bert-base-uncased-mc-weight1-epoch15

This model is a fine-tuned version of [](https://huggingface.co/) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 7.8027
- Cls loss: 3.4449
- Lm loss: 4.3556
- Cls Accuracy: 0.5706
- Cls F1: 0.5697
- Cls Precision: 0.5753
- Cls Recall: 0.5706
- Perplexity: 77.91

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
- train_batch_size: 2
- eval_batch_size: 2
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Cls loss | Lm loss | Cls Accuracy | Cls F1 | Cls Precision | Cls Recall | Perplexity |
|:-------------:|:-----:|:-----:|:---------------:|:--------:|:-------:|:------------:|:------:|:-------------:|:----------:|:----------:|
| 6.9526        | 1.0   | 3470  | 6.3154          | 1.7748   | 4.5399  | 0.4991       | 0.4577 | 0.4421        | 0.4991     | 93.68      |
| 6.0876        | 2.0   | 6940  | 6.1427          | 1.6773   | 4.4643  | 0.5545       | 0.5342 | 0.5717        | 0.5545     | 86.86      |
| 5.7231        | 3.0   | 10410 | 6.0206          | 1.5955   | 4.4240  | 0.5902       | 0.5759 | 0.6020        | 0.5902     | 83.43      |
| 5.3877        | 4.0   | 13880 | 5.9857          | 1.5772   | 4.4073  | 0.6092       | 0.6031 | 0.6052        | 0.6092     | 82.05      |
| 5.1092        | 5.0   | 17350 | 6.3742          | 1.9981   | 4.3748  | 0.5942       | 0.5901 | 0.5964        | 0.5942     | 79.42      |
| 4.8504        | 6.0   | 20820 | 6.4511          | 2.0776   | 4.3737  | 0.5890       | 0.5875 | 0.6041        | 0.5890     | 79.34      |
| 4.6369        | 7.0   | 24290 | 6.9857          | 2.6268   | 4.3571  | 0.5827       | 0.5796 | 0.5979        | 0.5827     | 78.03      |
| 4.4667        | 8.0   | 27760 | 6.9550          | 2.6075   | 4.3458  | 0.5833       | 0.5831 | 0.5904        | 0.5833     | 77.16      |
| 4.3127        | 9.0   | 31230 | 7.2041          | 2.8518   | 4.3504  | 0.5902       | 0.5856 | 0.5935        | 0.5902     | 77.51      |
| 4.1777        | 10.0  | 34700 | 7.4233          | 3.0746   | 4.3467  | 0.5793       | 0.5770 | 0.5829        | 0.5793     | 77.22      |
| 4.0871        | 11.0  | 38170 | 7.4997          | 3.1488   | 4.3489  | 0.5746       | 0.5749 | 0.5853        | 0.5746     | 77.39      |
| 3.9991        | 12.0  | 41640 | 7.6636          | 3.3113   | 4.3502  | 0.5602       | 0.5605 | 0.5676        | 0.5602     | 77.49      |
| 3.9461        | 13.0  | 45110 | 7.6065          | 3.2514   | 4.3530  | 0.5695       | 0.5690 | 0.5738        | 0.5695     | 77.71      |
| 3.9013        | 14.0  | 48580 | 7.7562          | 3.4017   | 4.3523  | 0.5787       | 0.5785 | 0.5823        | 0.5787     | 77.65      |
| 3.8731        | 15.0  | 52050 | 7.8027          | 3.4449   | 4.3556  | 0.5706       | 0.5697 | 0.5753        | 0.5706     | 77.91      |


### Framework versions

- Transformers 4.21.2
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1