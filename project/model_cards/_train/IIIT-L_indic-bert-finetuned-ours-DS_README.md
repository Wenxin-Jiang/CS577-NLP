---
license: mit
tags:
- generated_from_trainer
metrics:
- accuracy
- precision
- recall
- f1
model-index:
- name: indic-bert-finetuned-ours-DS
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# indic-bert-finetuned-ours-DS

This model is a fine-tuned version of [ai4bharat/indic-bert](https://huggingface.co/ai4bharat/indic-bert) on an unknown dataset.
It achieves the following results on the evaluation set:
- Loss: 2.1832
- Accuracy: 0.655
- Precision: 0.6023
- Recall: 0.6027
- F1: 0.6025

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 1e-05
- train_batch_size: 16
- eval_batch_size: 32
- seed: 43
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 25

### Training results

| Training Loss | Epoch | Step | Validation Loss | Accuracy | Precision | Recall | F1     |
|:-------------:|:-----:|:----:|:---------------:|:--------:|:---------:|:------:|:------:|
| 1.0681        | 0.99  | 99   | 1.0180          | 0.365    | 0.3435    | 0.4038 | 0.2773 |
| 0.9384        | 1.98  | 198  | 0.8475          | 0.62     | 0.6235    | 0.5610 | 0.4821 |
| 0.8201        | 2.97  | 297  | 0.8187          | 0.68     | 0.6839    | 0.6086 | 0.5812 |
| 0.7178        | 3.96  | 396  | 0.7717          | 0.7      | 0.7117    | 0.6670 | 0.6470 |
| 0.62          | 4.95  | 495  | 0.7839          | 0.66     | 0.6165    | 0.6244 | 0.6174 |
| 0.5135        | 5.94  | 594  | 0.8392          | 0.675    | 0.6270    | 0.6234 | 0.6246 |
| 0.4073        | 6.93  | 693  | 0.8930          | 0.665    | 0.6251    | 0.6254 | 0.6240 |
| 0.3365        | 7.92  | 792  | 0.9362          | 0.675    | 0.6298    | 0.6276 | 0.6242 |
| 0.2719        | 8.91  | 891  | 1.0108          | 0.685    | 0.6388    | 0.6293 | 0.6326 |
| 0.2007        | 9.9   | 990  | 1.1214          | 0.675    | 0.6300    | 0.6299 | 0.6290 |
| 0.1567        | 10.89 | 1089 | 1.1367          | 0.67     | 0.6193    | 0.6212 | 0.6178 |
| 0.1074        | 11.88 | 1188 | 1.3157          | 0.65     | 0.6292    | 0.6317 | 0.6227 |
| 0.0821        | 12.87 | 1287 | 1.5412          | 0.665    | 0.6415    | 0.6330 | 0.6259 |
| 0.0588        | 13.86 | 1386 | 1.7215          | 0.64     | 0.5862    | 0.5869 | 0.5865 |
| 0.0337        | 14.85 | 1485 | 1.7556          | 0.64     | 0.6078    | 0.6082 | 0.6032 |
| 0.0244        | 15.84 | 1584 | 1.8713          | 0.66     | 0.6173    | 0.6186 | 0.6158 |
| 0.0166        | 16.83 | 1683 | 1.9666          | 0.66     | 0.5995    | 0.5973 | 0.5973 |
| 0.0124        | 17.82 | 1782 | 1.9245          | 0.66     | 0.6165    | 0.6194 | 0.6163 |
| 0.0079        | 18.81 | 1881 | 2.0814          | 0.65     | 0.6026    | 0.6023 | 0.6012 |
| 0.0051        | 19.8  | 1980 | 2.1029          | 0.645    | 0.6014    | 0.5986 | 0.5975 |
| 0.0031        | 20.79 | 2079 | 2.1155          | 0.655    | 0.6029    | 0.6027 | 0.6023 |
| 0.0029        | 21.78 | 2178 | 2.1221          | 0.655    | 0.6       | 0.6000 | 0.5999 |
| 0.0021        | 22.77 | 2277 | 2.2065          | 0.65     | 0.5917    | 0.5898 | 0.5905 |
| 0.0017        | 23.76 | 2376 | 2.1903          | 0.65     | 0.5910    | 0.5898 | 0.5902 |
| 0.0016        | 24.75 | 2475 | 2.1832          | 0.655    | 0.6023    | 0.6027 | 0.6025 |


### Framework versions

- Transformers 4.20.1
- Pytorch 1.10.1+cu111
- Datasets 2.3.2
- Tokenizers 0.12.1
