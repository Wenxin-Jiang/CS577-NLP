---
license: apache-2.0
tags:
- summarization
- generated_from_trainer
datasets:
- big_patent
metrics:
- rouge
model-index:
- name: mt5-small-finetuned-Big-Patent-h
  results:
  - task:
      name: Sequence-to-sequence Language Modeling
      type: text2text-generation
    dataset:
      name: big_patent
      type: big_patent
      config: h
      split: train
      args: h
    metrics:
    - name: Rouge1
      type: rouge
      value: 33.9091
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# mt5-small-finetuned-Big-Patent-h

This model is a fine-tuned version of [google/mt5-small](https://huggingface.co/google/mt5-small) on the big_patent dataset.
It achieves the following results on the evaluation set:
- Loss: 2.2622
- Rouge1: 33.9091
- Rouge2: 14.1731
- Rougel: 30.105
- Rougelsum: 30.3666

## Model description

In this project, we fine-tuned mT5small, a multilingual variant of T5 that was pre-trained on a new Common Crawl-based dataset covering 101 languages.
The model was fine-tuned on the electric patent corpus using a variety of techniques, including transfer learning, data augmentation, and hyperparameter tuning.

## Intended uses & limitations

The fine-tuned model showed significant improvements in performance on the electric patent-specific tasks compared to the original pre-trained model.

Note: This project is suitable for researchers who are working on electric patent, as it's fine-tuned on electric patents and it can be used for related NLP problems for electric patent and electric patent research.

## Training and evaluation data
A subset of electric patents were used to fine-tune the model.

The fine-tuned model was evaluated using the ROUGE metric on a variety of natural language processing tasks specific to the patent domain, including, named entity recognition, and summarization.

## Training procedure

The model was fine-tuned on the electric patent corpus using a variety of techniques, including transfer learning, data augmentation, and hyperparameter tuning.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5.6e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 8

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|
| 2.5817        | 1.0   | 1071 | 2.3830          | 32.8521 | 13.2087 | 29.5594 | 29.7744   |
| 2.5657        | 2.0   | 2142 | 2.3345          | 33.9434 | 14.0573 | 30.0135 | 30.2533   |
| 2.4915        | 3.0   | 3213 | 2.2761          | 33.2033 | 13.2053 | 29.5126 | 29.8023   |
| 2.4365        | 4.0   | 4284 | 2.3041          | 33.8649 | 13.6629 | 30.0377 | 30.257    |
| 2.3952        | 5.0   | 5355 | 2.2722          | 33.9208 | 13.8018 | 30.1035 | 30.3432   |
| 2.3628        | 6.0   | 6426 | 2.2850          | 33.883  | 13.9537 | 30.0579 | 30.2417   |
| 2.3474        | 7.0   | 7497 | 2.2858          | 33.7201 | 14.0808 | 30.0762 | 30.255    |
| 2.331         | 8.0   | 8568 | 2.2622          | 33.9091 | 14.1731 | 30.105  | 30.3666   |


### Framework versions

- Transformers 4.24.0
- Pytorch 1.12.1+cu113
- Datasets 2.7.1
- Tokenizers 0.13.2
