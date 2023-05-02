---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- id_panl_bppt
metrics:
- bleu
model-index:
- name: opus-mt-id-en-finetuned-id-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: id_panl_bppt
      type: id_panl_bppt
      config: id_panl_bppt
      split: train
      args: id_panl_bppt
    metrics:
    - name: Bleu
      type: bleu
      value: 30.557
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-id-en-finetuned-id-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-id-en](https://huggingface.co/Helsinki-NLP/opus-mt-id-en) on the id_panl_bppt dataset.
It achieves the following results on the evaluation set:
- Loss: 1.6469
- Bleu: 30.557
- Gen Len: 29.8247

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 2e-06
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step  | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:-----:|:---------------:|:-------:|:-------:|
| 2.5737        | 1.0   | 751   | 2.2222          | 24.4223 | 30.3344 |
| 2.3756        | 2.0   | 1502  | 2.1264          | 25.419  | 30.3147 |
| 2.3146        | 3.0   | 2253  | 2.0588          | 26.0995 | 30.1959 |
| 2.2411        | 4.0   | 3004  | 2.0072          | 26.5944 | 30.0763 |
| 2.1927        | 5.0   | 3755  | 1.9657          | 27.0422 | 30.0773 |
| 2.1554        | 6.0   | 4506  | 1.9284          | 27.4151 | 30.0715 |
| 2.1105        | 7.0   | 5257  | 1.8980          | 27.6645 | 29.9426 |
| 2.0841        | 8.0   | 6008  | 1.8680          | 28.023  | 29.9797 |
| 2.0491        | 9.0   | 6759  | 1.8438          | 28.2456 | 29.9342 |
| 2.0265        | 10.0  | 7510  | 1.8218          | 28.5378 | 29.8968 |
| 2.0065        | 11.0  | 8261  | 1.8012          | 28.7599 | 29.8907 |
| 1.9764        | 12.0  | 9012  | 1.7835          | 28.9369 | 29.8796 |
| 1.969         | 13.0  | 9763  | 1.7663          | 29.1565 | 29.8671 |
| 1.9474        | 14.0  | 10514 | 1.7506          | 29.3313 | 29.893  |
| 1.9397        | 15.0  | 11265 | 1.7378          | 29.4567 | 29.8512 |
| 1.9217        | 16.0  | 12016 | 1.7239          | 29.6245 | 29.8361 |
| 1.9174        | 17.0  | 12767 | 1.7127          | 29.7464 | 29.8398 |
| 1.9021        | 18.0  | 13518 | 1.7030          | 29.9035 | 29.8621 |
| 1.89          | 19.0  | 14269 | 1.6934          | 29.9669 | 29.8225 |
| 1.878         | 20.0  | 15020 | 1.6847          | 30.0961 | 29.8398 |
| 1.8671        | 21.0  | 15771 | 1.6774          | 30.1878 | 29.839  |
| 1.8634        | 22.0  | 16522 | 1.6717          | 30.2341 | 29.8134 |
| 1.8536        | 23.0  | 17273 | 1.6653          | 30.3356 | 29.816  |
| 1.8533        | 24.0  | 18024 | 1.6602          | 30.3548 | 29.8251 |
| 1.8476        | 25.0  | 18775 | 1.6560          | 30.4323 | 29.8315 |
| 1.8362        | 26.0  | 19526 | 1.6528          | 30.4682 | 29.8277 |
| 1.8463        | 27.0  | 20277 | 1.6501          | 30.5002 | 29.8236 |
| 1.8369        | 28.0  | 21028 | 1.6484          | 30.5236 | 29.8257 |
| 1.8313        | 29.0  | 21779 | 1.6472          | 30.55   | 29.8259 |
| 1.8332        | 30.0  | 22530 | 1.6469          | 30.557  | 29.8247 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0
- Datasets 2.4.0
- Tokenizers 0.12.1
