---
language: 
- pt
license: mit
tags:
- generated_from_trainer
model-index:
- name: bert-base-portuguese-cased-finetuned-peticoes
  results: []
widget:
- text: "Com efeito, se tal fosse possível, o Poder [MASK] – que não dispõe de função legislativa – passaria a desempenhar atribuição que lhe é institucionalmente estranha (a de legislador positivo), usurpando, desse modo, no contexto de um sistema de poderes essencialmente limitados, competência que não lhe pertence, com evidente transgressão ao princípio constitucional da separação de poderes."
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# bert-base-portuguese-cased-finetuned-peticoes

This model is a fine-tuned version of [neuralmind/bert-base-portuguese-cased](https://huggingface.co/neuralmind/bert-base-portuguese-cased) on the None dataset.
It achieves the following results on the evaluation set:
- Loss: 1.0878

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
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| No log        | 1.0   | 215  | 1.1349          |
| No log        | 2.0   | 430  | 1.0925          |
| 1.3219        | 3.0   | 645  | 1.0946          |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.9.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
