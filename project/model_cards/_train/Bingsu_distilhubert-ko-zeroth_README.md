---
license: apache-2.0
tags:
- automatic-speech-recognition
- zeroth
- generated_from_trainer
model-index:
- name: distilhubert-ko-zeroth
  results: []
language:
- ko
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# distilhubert-ko-zeroth

This model is a fine-tuned version of [ntu-spml/distilhubert](https://huggingface.co/ntu-spml/distilhubert) on the BINGSU/ZEROTH-KOREAN - NA dataset.
It achieves the following results on the evaluation set:
- Loss: 0.9934
- Cer: 0.2066

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.001
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine_with_restarts
- lr_scheduler_warmup_steps: 500
- num_epochs: 10.0
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Cer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| No log        | 0.57  | 400  | 3.2681          | 0.6761 |
| 7.285         | 1.15  | 800  | 1.5312          | 0.4170 |
| 1.259         | 1.72  | 1200 | 1.3459          | 0.3846 |
| 0.9108        | 2.3   | 1600 | 1.1357          | 0.3239 |
| 0.7227        | 2.87  | 2000 | 1.0571          | 0.3056 |
| 0.7227        | 3.45  | 2400 | 1.0002          | 0.2829 |
| 0.5689        | 4.02  | 2800 | 0.8773          | 0.2553 |
| 0.4676        | 4.6   | 3200 | 0.8634          | 0.2462 |
| 0.3805        | 5.17  | 3600 | 0.8504          | 0.2323 |
| 0.2548        | 5.75  | 4000 | 0.8480          | 0.2260 |
| 0.2548        | 6.32  | 4400 | 0.8550          | 0.2231 |
| 0.189         | 6.9   | 4800 | 0.8587          | 0.2159 |
| 0.1336        | 7.47  | 5200 | 0.9012          | 0.2101 |
| 0.0827        | 8.05  | 5600 | 0.9302          | 0.2100 |
| 0.0506        | 8.62  | 6000 | 0.9622          | 0.2063 |
| 0.0506        | 9.2   | 6400 | 0.9826          | 0.2062 |
| 0.0389        | 9.77  | 6800 | 0.9933          | 0.2067 |


### Framework versions

- Transformers 4.21.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1
