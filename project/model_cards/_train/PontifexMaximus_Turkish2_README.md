---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- opus_infopankki
metrics:
- bleu
model-index:
- name: opus-mt-tr-en-finetuned-tr-to-en
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: opus_infopankki
      type: opus_infopankki
      args: en-tr
    metrics:
    - name: Bleu
      type: bleu
      value: 56.617
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# opus-mt-tr-en-finetuned-tr-to-en

This model is a fine-tuned version of [Helsinki-NLP/opus-mt-tr-en](https://huggingface.co/Helsinki-NLP/opus-mt-tr-en) on the opus_infopankki dataset.
It achieves the following results on the evaluation set:
- Loss: 0.6321
- Bleu: 56.617
- Gen Len: 13.5983

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
- train_batch_size: 64
- eval_batch_size: 64
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Bleu    | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|
| No log        | 1.0   | 241  | 1.2487          | 41.0053 | 13.0461 |
| No log        | 2.0   | 482  | 1.1630          | 43.1077 | 13.0386 |
| 1.4091        | 3.0   | 723  | 1.0992          | 44.6583 | 13.0445 |
| 1.4091        | 4.0   | 964  | 1.0463          | 45.5931 | 13.0289 |
| 1.2325        | 5.0   | 1205 | 1.0012          | 46.7039 | 12.9998 |
| 1.2325        | 6.0   | 1446 | 0.9610          | 47.6783 | 13.0274 |
| 1.1284        | 7.0   | 1687 | 0.9262          | 48.622  | 12.9866 |
| 1.1284        | 8.0   | 1928 | 0.8939          | 48.4984 | 13.5762 |
| 1.0486        | 9.0   | 2169 | 0.8642          | 49.1496 | 13.5918 |
| 1.0486        | 10.0  | 2410 | 0.8391          | 49.8875 | 13.5905 |
| 0.9866        | 11.0  | 2651 | 0.8150          | 50.6447 | 13.5803 |
| 0.9866        | 12.0  | 2892 | 0.7941          | 51.2059 | 13.5731 |
| 0.9362        | 13.0  | 3133 | 0.7741          | 51.7071 | 13.5754 |
| 0.9362        | 14.0  | 3374 | 0.7564          | 52.4185 | 13.5781 |
| 0.8928        | 15.0  | 3615 | 0.7398          | 53.0814 | 13.5744 |
| 0.8928        | 16.0  | 3856 | 0.7247          | 53.5711 | 13.5783 |
| 0.8598        | 17.0  | 4097 | 0.7111          | 54.0559 | 13.568  |
| 0.8598        | 18.0  | 4338 | 0.6988          | 54.5188 | 13.5598 |
| 0.8274        | 19.0  | 4579 | 0.6876          | 54.78   | 13.5765 |
| 0.8274        | 20.0  | 4820 | 0.6780          | 55.1494 | 13.5762 |
| 0.8086        | 21.0  | 5061 | 0.6688          | 55.5813 | 13.5788 |
| 0.8086        | 22.0  | 5302 | 0.6610          | 55.6403 | 13.5796 |
| 0.7878        | 23.0  | 5543 | 0.6539          | 55.7731 | 13.5989 |
| 0.7878        | 24.0  | 5784 | 0.6483          | 55.9956 | 13.593  |
| 0.7718        | 25.0  | 6025 | 0.6432          | 56.2303 | 13.5904 |
| 0.7718        | 26.0  | 6266 | 0.6390          | 56.4825 | 13.5975 |
| 0.7633        | 27.0  | 6507 | 0.6360          | 56.5334 | 13.5958 |
| 0.7633        | 28.0  | 6748 | 0.6338          | 56.5357 | 13.5965 |
| 0.7633        | 29.0  | 6989 | 0.6325          | 56.5862 | 13.5974 |
| 0.7584        | 30.0  | 7230 | 0.6321          | 56.617  | 13.5983 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.12.0
- Datasets 2.3.2
- Tokenizers 0.12.1
