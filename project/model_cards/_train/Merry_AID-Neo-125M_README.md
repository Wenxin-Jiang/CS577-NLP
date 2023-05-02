---
language: en
license: mit
pipeline_tag: text-generation
---
# AID-Neo-125M

## Model description
This model was inspired by -- and finetuned on the same dataset of -- [KoboldAI's GPT-Neo-125M-AID (Mia) model](https://huggingface.co/KoboldAI/GPT-Neo-125M-AID): the AI Dungeon dataset (`text_adventures.txt`). This was to fix a possible oversight in the original model, which was trained with [an unfortunate bug](https://github.com/EricFillion/happy-transformer/issues/283). You could technically consider it a "retraining" of the same model using different software.

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0