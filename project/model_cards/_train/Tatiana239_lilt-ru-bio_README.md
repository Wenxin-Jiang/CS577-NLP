---
tags:
- generated_from_trainer
datasets:
- funsd-layoutlmv3
model-index:
- name: lilt-ru-bio
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lilt-ru-bio

This model was trained from scratch on the funsd-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.4705
- Answer: {'precision': 0.8711583924349882, 'recall': 0.9020807833537332, 'f1': 0.8863499699338545, 'number': 817}
- Header: {'precision': 0.6336633663366337, 'recall': 0.5378151260504201, 'f1': 0.5818181818181819, 'number': 119}
- Question: {'precision': 0.8966455122393472, 'recall': 0.9182915506035283, 'f1': 0.9073394495412844, 'number': 1077}
- Overall Precision: 0.8732
- Overall Recall: 0.8892
- Overall F1: 0.8811
- Overall Accuracy: 0.8223

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 8
- eval_batch_size: 8
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- training_steps: 500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch | Step | Validation Loss | Answer                                                                                                   | Header                                                                                                   | Question                                                                                                  | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy |
|:-------------:|:-----:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------:|:--------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:-----------------:|:--------------:|:----------:|:----------------:|
| 0.0199        | 5.26  | 100  | 1.3310          | {'precision': 0.8788627935723115, 'recall': 0.8702570379436965, 'f1': 0.8745387453874538, 'number': 817} | {'precision': 0.6288659793814433, 'recall': 0.5126050420168067, 'f1': 0.5648148148148148, 'number': 119} | {'precision': 0.8519148936170213, 'recall': 0.9294336118848654, 'f1': 0.8889875666074601, 'number': 1077} | 0.8520            | 0.8808         | 0.8661     | 0.8038           |
| 0.0085        | 10.53 | 200  | 1.5426          | {'precision': 0.8631578947368421, 'recall': 0.9033047735618115, 'f1': 0.8827751196172249, 'number': 817} | {'precision': 0.5641025641025641, 'recall': 0.5546218487394958, 'f1': 0.559322033898305, 'number': 119}  | {'precision': 0.899812734082397, 'recall': 0.8922934076137419, 'f1': 0.8960372960372962, 'number': 1077}  | 0.8652            | 0.8768         | 0.8710     | 0.8120           |
| 0.0047        | 15.79 | 300  | 1.5043          | {'precision': 0.8698710433763188, 'recall': 0.9082007343941249, 'f1': 0.8886227544910178, 'number': 817} | {'precision': 0.5508474576271186, 'recall': 0.5462184873949579, 'f1': 0.5485232067510548, 'number': 119} | {'precision': 0.8980716253443526, 'recall': 0.9080779944289693, 'f1': 0.9030470914127423, 'number': 1077} | 0.8665            | 0.8867         | 0.8765     | 0.8086           |
| 0.0017        | 21.05 | 400  | 1.4705          | {'precision': 0.8711583924349882, 'recall': 0.9020807833537332, 'f1': 0.8863499699338545, 'number': 817} | {'precision': 0.6336633663366337, 'recall': 0.5378151260504201, 'f1': 0.5818181818181819, 'number': 119} | {'precision': 0.8966455122393472, 'recall': 0.9182915506035283, 'f1': 0.9073394495412844, 'number': 1077} | 0.8732            | 0.8892         | 0.8811     | 0.8223           |
| 0.0012        | 26.32 | 500  | 1.5088          | {'precision': 0.8744075829383886, 'recall': 0.9033047735618115, 'f1': 0.8886213124623721, 'number': 817} | {'precision': 0.5904761904761905, 'recall': 0.5210084033613446, 'f1': 0.5535714285714286, 'number': 119} | {'precision': 0.8935395814376706, 'recall': 0.9117920148560817, 'f1': 0.9025735294117648, 'number': 1077} | 0.8701            | 0.8852         | 0.8776     | 0.8174           |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1
- Datasets 2.8.0
- Tokenizers 0.13.2
