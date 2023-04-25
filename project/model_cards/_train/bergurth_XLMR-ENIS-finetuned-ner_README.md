---
license: agpl-3.0
tags:
- generated_from_trainer
datasets:
- mim_gold_ner
metrics:
- precision
- recall
- f1
- accuracy
widget:
- text: Bónus feðgarnir Jóhannes Jónsson og Jón Ásgeir Jóhannesson opnuðu fyrstu Bónusbúðina í 400 fermetra húsnæði við Skútuvog laugardaginn 8. apríl 1989
model-index:
- name: XLMR-ENIS-finetuned-ner
  results:
  - task:
      name: Token Classification
      type: token-classification
    dataset:
      name: mim_gold_ner
      type: mim_gold_ner
      args: mim-gold-ner
    metrics:
    - name: Precision
      type: precision
      value: 0.861851332398317
    - name: Recall
      type: recall
      value: 0.8384309266628767
    - name: F1
      type: f1
      value: 0.849979828251974
    - name: Accuracy
      type: accuracy
      value: 0.9830620929487668
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# XLMR-ENIS-finetuned-ner

This model is a fine-tuned version of [vesteinn/XLMR-ENIS](https://huggingface.co/vesteinn/XLMR-ENIS) on the mim_gold_ner dataset.
It achieves the following results on the evaluation set:
- Loss: 0.0938
- Precision: 0.8619
- Recall: 0.8384
- F1: 0.8500
- Accuracy: 0.9831

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
- train_batch_size: 16
- eval_batch_size: 16
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3

### Training results

| Training Loss | Epoch | Step | Validation Loss | Precision | Recall | F1     | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:---------:|:------:|:------:|:--------:|
| 0.0574        | 1.0   | 2904 | 0.0983          | 0.8374    | 0.8061 | 0.8215 | 0.9795   |
| 0.0321        | 2.0   | 5808 | 0.0991          | 0.8525    | 0.8235 | 0.8378 | 0.9811   |
| 0.0179        | 3.0   | 8712 | 0.0938          | 0.8619    | 0.8384 | 0.8500 | 0.9831   |


### Framework versions

- Transformers 4.11.2
- Pytorch 1.9.0+cu102
- Datasets 1.12.1
- Tokenizers 0.10.3
