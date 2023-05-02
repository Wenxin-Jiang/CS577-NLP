---
language: 
  - en
tags:
- QA
- Question Answering
- SQuAD
license: "mit"
datasets:
- squad
metrics:
- squad

model-index:
- name: distilroberta-base
  results:
  - task:
      type: question-answering             # Required. Example: automatic-speech-recognition
      name: Question Answering             # Optional. Example: Speech Recognition
    dataset:
      type: squad          # Required. Example: common_voice. Use dataset id from https://hf.co/datasets
      name: SQuAD          # Required. A pretty name for the dataset. Example: Common Voice (French)
      split: validation        # Optional. Example: test
     
    metrics:
      - type: squad         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 76.37653736991486       # Required. Example: 20.90
        name: SQuAD EM         # Optional. Example: Test WER
        config: exact_match     # Optional. The name of the metric configuration used in `load_metric()`. Example: bleurt-large-512 in `load_metric("bleurt", "bleurt-large-512")`. See the `datasets` docs for more info: https://huggingface.co/docs/datasets/v2.1.0/en/loading#load-configurations
      - type: squad         # Required. Example: wer. Use metric id from https://hf.co/metrics
        value: 84.5528918750732       # Required. Example: 20.90
        name: SQuAD F1         # Optional. Example: Test WER
        config: F1
       
---

distilroberta-base fined-tuned on SQuAD (https://huggingface.co/datasets/squad)

Hyperparameters:
- epochs: 1
- lr: 1e-5
- train batch sie: 16
- optimizer: adamW
- lr_scheduler: linear
- num warming steps: 0
- max_length: 512

Results on the dev set:
- 'exact_match': 76.37653736991486
- 'f1': 84.5528918750732


It took 1h 20 min to train on Colab.