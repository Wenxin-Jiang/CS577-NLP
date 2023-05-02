---
license: apache-2.0
tags:
- generated_from_trainer
model-index:
- name: wav2vec2-ksponspeech
  results: []
  
---


# wav2vec2-ksponspeech

This model is a fine-tuned version of [Wav2vec2-large-xlsr-53](https://huggingface.co/facebook/wav2vec2-large-xlsr-53) on the None dataset.  
It achieves the following results on the evaluation set:

- **WER(Word Error Rate)** for Third party test data : 0.373

**For improving WER:**
- Numeric / Character Unification
- Decoding the word with the correct notation (from word based on pronounciation)
- Uniform use of special characters (. / ?)
- Converting non-existent words to existing words

## Model description

Korean Wav2vec with Ksponspeech dataset.  

This model was trained by two dataset :

- Train1 : https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-train (1 ~ 20000th data in Ksponspeech)
- Train2 : https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-train2 (20100 ~ 40100th data in Ksponspeech)
- Validation : https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-test (20000 ~ 20100th data in Ksponspeech)
- Third party test : https://huggingface.co/datasets/Taeham/wav2vec2-ksponspeech-test (60000 ~ 20100th data in Ksponspeech)

### Hardward Specification
- GPU : GEFORCE RTX 3080ti 12GB
- CPU : Intel i9-12900k
- RAM : 32GB

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 4
- eval_batch_size: 4
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.19.4
- Pytorch 1.11.0
- Datasets 2.2.2
- Tokenizers 0.12.1
