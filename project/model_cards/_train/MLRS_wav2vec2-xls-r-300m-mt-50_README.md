---
language:
- mt
tags:
- generated_from_trainer
- low-resource
- automatic-speech-recognition
- mt
datasets:
- mozilla-foundation/common_voice_7_0
- MASRI-HEADSET-V2
model-index:
- name: wav2vec2-xls-r-300m-mt-50
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 7
      type: mozilla-foundation/common_voice_7_0
      args: mt
    metrics:
    - name: Test WER
      type: wer
      value: 9.37
    - name: Test CER
      type: cer
      value: 2.12
license: cc-by-nc-sa-4.0
---

# wav2vec2-xls-r-300m-mt-50

This model was fine-tuned on a combined dataset.

Sample usage is included with Run_ASR_Pipeline.py

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 32
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Framework versions

- Transformers 4.16.2
- Pytorch 1.10.2
- Datasets 1.18.4
- Tokenizers 0.10.3

## License

This work is licensed under a
[Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License][cc-by-nc-sa].
Permissions beyond the scope of this license may be available at [https://mlrs.research.um.edu.mt/](https://mlrs.research.um.edu.mt/).

[![CC BY-NC-SA 4.0][cc-by-nc-sa-image]][cc-by-nc-sa]

[cc-by-nc-sa]: http://creativecommons.org/licenses/by-nc-sa/4.0/
[cc-by-nc-sa-image]: https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png