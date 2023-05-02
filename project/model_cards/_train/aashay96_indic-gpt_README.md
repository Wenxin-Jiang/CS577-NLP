---
license: mit
tags:
- generated_from_trainer
model-index:
- name: indic-gpt
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-gpt

This model is a fine-tuned version of [gpt2](https://huggingface.co/gpt2) on an Indian Language(https://ai4bharat.iitm.ac.in/corpora) dataset. Sample Dataset is present on https://huggingface.co/datasets/aashay96/indic-gpt.
It achieves the following results on the evaluation set:
- Loss: 1.9482

## Model description

Model is trained on multiple Indian Languages - Assamese, bengali, gujarati, Kannada, Malayalam,telugu, tamil, odhiya and punjabi.



## Intended uses & limitations

More information needed

## Training and evaluation data

TBD - Evaluation on indic_glue 

## Training procedure

Check the notebook!

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0005
- train_batch_size: 128
- eval_batch_size: 128
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 1024
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_steps: 100
- num_epochs: 1
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss |
|:-------------:|:-----:|:----:|:---------------:|
| 3.3653        | 0.3   | 500  | 2.2985          |
| 2.2079        | 0.61  | 1000 | 2.0401          |
| 2.0396        | 0.91  | 1500 | 1.9482          |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu116
- Datasets 2.8.0
- Tokenizers 0.13.2
