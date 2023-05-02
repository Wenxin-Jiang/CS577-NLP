---
license: apache-2.0
tags:
- image-classification
- generated_from_trainer
datasets:
- imagefolder
widget:
  - src: https://huggingface.co/alkzar90/croupier-creature-classifier/resolve/main/examples/crusader_peco_peco.png
    example_title: Crusader-Rangarok-Online
  - src: https://huggingface.co/alkzar90/croupier-creature-classifier/resolve/main/examples/goblin_wow.png
    example_title: Goblin-WoW
  - src: https://huggingface.co/alkzar90/croupier-creature-classifier/resolve/main/examples/dobby_harry_potter.jpg
    example_title: Dobby-Harry-Potter
  - src: https://huggingface.co/alkzar90/croupier-creature-classifier/resolve/main/examples/resident_evil_nemesis.jpeg
    example_title: Nemesis-Resident-Evil
metrics:
- accuracy
model-index:
- name: croupier-creature-classifier
  results:
  - task:
      name: Image Classification
      type: image-classification
    dataset:
      name: croupier-mtg-dataset
      type: imagefolder
      config: alkzar90--croupier-mtg-dataset
      split: train
      args: alkzar90--croupier-mtg-dataset
    metrics:
    - name: Accuracy
      type: accuracy
      value: 0.7471264367816092
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# croupier-creature-classifier

This model is a fine-tuned version of [google/vit-base-patch16-224-in21k](https://huggingface.co/google/vit-base-patch16-224-in21k) on the croupier-mtg-dataset dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7583
- Accuracy: 0.7471

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0002
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------:|
| 0.6663        | 1.1   | 100  | 1.0179          | 0.5941   |
| 0.4924        | 2.2   | 200  | 0.7036          | 0.7529   |
| 0.4552        | 3.3   | 300  | 0.6123          | 0.7824   |
| 0.2355        | 4.4   | 400  | 0.5748          | 0.7647   |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.0+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
