---
license: apache-2.0
tags:
- generated_from_trainer
metrics:
- accuracy
- recall
- precision
- f1
model-index:
- name: distilbert-base-uncased_fine_tuned_body_text
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilbert-base-uncased_fine_tuned_body_text

This model is a fine-tuned version of [distilbert-base-uncased](https://huggingface.co/distilbert-base-uncased) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 1.2153
- Accuracy: {'accuracy': 0.8827265261428963}
- Recall: {'recall': 0.8641975308641975}
- Precision: {'precision': 0.8900034993584509}
- F1: {'f1': 0.8769106999195494}

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
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 15

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Accuracy                         | Recall                         | Precision                         | F1                         |
|:-------------:|:-----:|:-----:|:---------------:|:--------------------------------:|:------------------------------:|:---------------------------------:|:--------------------------:|
| 0.3056        | 1.0   | 2284  | 0.3040          | {'accuracy': 0.8874897344648235} | {'recall': 0.8466417487824216} | {'precision': 0.914261252446184}  | {'f1': 0.8791531902381653} |
| 0.2279        | 2.0   | 4568  | 0.2891          | {'accuracy': 0.8908294552422666} | {'recall': 0.8606863744478424} | {'precision': 0.9086452230060983} | {'f1': 0.8840158213122382} |
| 0.1467        | 3.0   | 6852  | 0.3580          | {'accuracy': 0.8882562277580072} | {'recall': 0.8452825914599615} | {'precision': 0.9170557876628164} | {'f1': 0.8797076678257796} |
| 0.0921        | 4.0   | 9136  | 0.4560          | {'accuracy': 0.8754448398576512} | {'recall': 0.8948918337297542} | {'precision': 0.8543468858131488} | {'f1': 0.8741494717043756} |
| 0.0587        | 5.0   | 11420 | 0.5701          | {'accuracy': 0.8768135778811935} | {'recall': 0.8139087099331748} | {'precision': 0.9221095855254716} | {'f1': 0.8646372277704246} |
| 0.0448        | 6.0   | 13704 | 0.6738          | {'accuracy': 0.8767040788393101} | {'recall': 0.8794880507418734} | {'precision': 0.8673070479168994} | {'f1': 0.873355078168935}  |
| 0.0289        | 7.0   | 15988 | 0.7965          | {'accuracy': 0.8798248015329866} | {'recall': 0.8491335372069317} | {'precision': 0.8967703349282297} | {'f1': 0.8723020536389552} |
| 0.0214        | 8.0   | 18272 | 0.8244          | {'accuracy': 0.8811387900355871} | {'recall': 0.8576282704723072} | {'precision': 0.8922931887815225} | {'f1': 0.8746173837712965} |
| 0.0147        | 9.0   | 20556 | 0.8740          | {'accuracy': 0.8806460443471119} | {'recall': 0.8669158455091177} | {'precision': 0.8839357893521191} | {'f1': 0.8753430924062213} |
| 0.0099        | 10.0  | 22840 | 0.9716          | {'accuracy': 0.8788940596769779} | {'recall': 0.8694076339336279} | {'precision': 0.8787635947338294} | {'f1': 0.8740605784559327} |
| 0.0092        | 11.0  | 25124 | 1.0296          | {'accuracy': 0.8822885299753627} | {'recall': 0.8669158455091177} | {'precision': 0.8870089233978444} | {'f1': 0.876847290640394}  |
| 0.0039        | 12.0  | 27408 | 1.0974          | {'accuracy': 0.8787845606350945} | {'recall': 0.8628383735417374} | {'precision': 0.8836561883772184} | {'f1': 0.8731232091690544} |
| 0.0053        | 13.0  | 29692 | 1.0833          | {'accuracy': 0.8799890500958116} | {'recall': 0.8503794314191868} | {'precision': 0.8960496479293472} | {'f1': 0.8726173872617387} |
| 0.0032        | 14.0  | 31976 | 1.1731          | {'accuracy': 0.8813030385984123} | {'recall': 0.8705402650356778} | {'precision': 0.8823326828148318} | {'f1': 0.8763968072976055} |
| 0.0017        | 15.0  | 34260 | 1.2153          | {'accuracy': 0.8827265261428963} | {'recall': 0.8641975308641975} | {'precision': 0.8900034993584509} | {'f1': 0.8769106999195494} |


### Framework versions

- Transformers 4.21.0
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
