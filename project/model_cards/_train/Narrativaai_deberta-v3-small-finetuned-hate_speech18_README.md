---
license: mit
tags:
- generated_from_trainer
datasets:
- hate_speech18
widget:
- text: "ok, so do we need to kill them too or are the slavs okay ? for some reason whenever i hear the word slav , the word slobber comes to mind and i picture a slobbering half breed creature like the humpback of notre dame or Igor haha"
metrics:
- accuracy
model-index:
- name: deberta-v3-small-hate-speech
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: hate_speech18
      type: hate_speech18
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.916058394160584
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# DeBERTa v3 small fine-tuned on hate_speech18 dataset for Hate Speech Detection

This model is a fine-tuned version of [microsoft/deberta-v3-small](https://huggingface.co/microsoft/deberta-v3-small) on the hate_speech18 dataset.
It achieves the following results on the evaluation set:
- Loss: 0.2922
- Accuracy: 0.9161

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
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.4147        | 1.0   | 650  | 0.3910          | 0.8832   |
| 0.2975        | 2.0   | 1300 | 0.2922          | 0.9161   |
| 0.2575        | 3.0   | 1950 | 0.3555          | 0.9051   |
| 0.1553        | 4.0   | 2600 | 0.4263          | 0.9124   |
| 0.1267        | 5.0   | 3250 | 0.4238          | 0.9161   |


### Framework versions

- Transformers 4.12.5
- Pytorch 1.10.0+cu111
- Datasets 1.16.1
- Tokenizers 0.10.3
