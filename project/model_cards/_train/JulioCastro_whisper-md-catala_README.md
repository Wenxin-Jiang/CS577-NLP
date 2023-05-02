---
language:
- ca
license: apache-2.0
tags:
- whisper-event
- generated_from_trainer
datasets:
- mozilla-foundation/common_voice_11_0
metrics:
- wer
model-index:
- name: Whisper Medium Catala 1k steps
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 11.0, Fleurs, SLR69, tb3_parla, parlament_parla
      type: mozilla-foundation/common_voice_11_0, google/fleurs, openslr, collectivat/tv3_parla, projecte-aina/parlament_parla
      config: ca
      split: test
      args: ca
    metrics:
    - name: Wer
      type: wer
      value: 10.9688
---

Whisper Md Ca - 1k
This model is a fine-tuned version of openai/whisper-medium on the Common Voice 11.0 dataset. It achieves the following results on the evaluation set:

Loss: 0.2554
Wer: 10.9688
Model description
More information needed

Intended uses & limitations
More information needed

Training and evaluation data
More information needed

Training procedure
Training hyperparameters
The following hyperparameters were used during training:

learning_rate: 1e-05
train_batch_size: 32
eval_batch_size: 8
seed: 42
gradient_accumulation_steps: 2
total_train_batch_size: 64
optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
lr_scheduler_type: linear
lr_scheduler_warmup_steps: 100
training_steps: 1000
mixed_precision_training: Native AMP

Training results
Training Loss	Epoch	Step	Validation Loss	Wer
0.2554	1.0	1000	0.2554	10.9688
Framework versions
Transformers 4.26.0.dev0
Pytorch 1.13.1+cu117
Datasets 2.7.1.dev0
Tokenizers 0.13.2