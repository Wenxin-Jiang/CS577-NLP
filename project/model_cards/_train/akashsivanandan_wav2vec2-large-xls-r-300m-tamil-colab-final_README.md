---
license: apache-2.0
tags:
- generated_from_trainer
datasets:
- common_voice
model-index:
- name: wav2vec2-large-xls-r-300m-tamil-colab-final
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# wav2vec2-large-xls-r-300m-tamil-colab-final

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on the common_voice dataset.
It achieves the following results on the evaluation set:
- Loss: 0.7539
- Wer: 0.6135

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 0.0003
- train_batch_size: 16
- eval_batch_size: 8
- seed: 42
- gradient_accumulation_steps: 2
- total_train_batch_size: 32
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 500
- num_epochs: 30
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Wer    |
|:-------------:|:-----:|:----:|:---------------:|:------:|
| 11.1466       | 1.0   | 118  | 4.3444          | 1.0    |
| 3.4188        | 2.0   | 236  | 3.2496          | 1.0    |
| 2.8617        | 3.0   | 354  | 1.6165          | 1.0003 |
| 0.958         | 4.0   | 472  | 0.7984          | 0.8720 |
| 0.5929        | 5.0   | 590  | 0.6733          | 0.7831 |
| 0.4628        | 6.0   | 708  | 0.6536          | 0.7621 |
| 0.3834        | 7.0   | 826  | 0.6037          | 0.7155 |
| 0.3242        | 8.0   | 944  | 0.6376          | 0.7184 |
| 0.2736        | 9.0   | 1062 | 0.6214          | 0.7070 |
| 0.2433        | 10.0  | 1180 | 0.6158          | 0.6944 |
| 0.2217        | 11.0  | 1298 | 0.6548          | 0.6830 |
| 0.1992        | 12.0  | 1416 | 0.6331          | 0.6775 |
| 0.1804        | 13.0  | 1534 | 0.6644          | 0.6874 |
| 0.1639        | 14.0  | 1652 | 0.6629          | 0.6649 |
| 0.143         | 15.0  | 1770 | 0.6927          | 0.6836 |
| 0.1394        | 16.0  | 1888 | 0.6933          | 0.6888 |
| 0.1296        | 17.0  | 2006 | 0.7039          | 0.6860 |
| 0.1212        | 18.0  | 2124 | 0.7042          | 0.6628 |
| 0.1121        | 19.0  | 2242 | 0.7132          | 0.6475 |
| 0.1069        | 20.0  | 2360 | 0.7423          | 0.6438 |
| 0.1063        | 21.0  | 2478 | 0.7171          | 0.6484 |
| 0.1025        | 22.0  | 2596 | 0.7396          | 0.6451 |
| 0.0946        | 23.0  | 2714 | 0.7400          | 0.6432 |
| 0.0902        | 24.0  | 2832 | 0.7385          | 0.6286 |
| 0.0828        | 25.0  | 2950 | 0.7368          | 0.6286 |
| 0.079         | 26.0  | 3068 | 0.7471          | 0.6306 |
| 0.0747        | 27.0  | 3186 | 0.7524          | 0.6201 |
| 0.0661        | 28.0  | 3304 | 0.7576          | 0.6201 |
| 0.0659        | 29.0  | 3422 | 0.7579          | 0.6130 |
| 0.0661        | 30.0  | 3540 | 0.7539          | 0.6135 |


### Framework versions

- Transformers 4.11.3
- Pytorch 1.10.0+cu111
- Datasets 1.13.3
- Tokenizers 0.10.3
