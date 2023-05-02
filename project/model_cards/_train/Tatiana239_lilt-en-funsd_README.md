---
license: mit
tags:
- generated_from_trainer
datasets:
- funsd-layoutlmv3
model-index:
- name: lilt-en-funsd
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# lilt-en-funsd

This model is a fine-tuned version of [SCUT-DLVCLab/lilt-roberta-en-base](https://huggingface.co/SCUT-DLVCLab/lilt-roberta-en-base) on the funsd-layoutlmv3 dataset.
It achieves the following results on the evaluation set:
- Loss: 1.7928
- Answer: {'precision': 0.8716763005780347, 'recall': 0.9228886168910648, 'f1': 0.8965517241379309, 'number': 817}
- Header: {'precision': 0.5648148148148148, 'recall': 0.5126050420168067, 'f1': 0.5374449339207047, 'number': 119}
- Question: {'precision': 0.8945454545454545, 'recall': 0.9136490250696379, 'f1': 0.9039963252181902, 'number': 1077}
- Overall Precision: 0.8678
- Overall Recall: 0.8937
- Overall F1: 0.8806
- Overall Accuracy: 0.7985

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
- training_steps: 2500
- mixed_precision_training: Native AMP

### Training results

| Training Loss | Epoch  | Step | Validation Loss | Answer                                                                                                   | Header                                                                                                    | Question                                                                                                  | Overall Precision | Overall Recall | Overall F1 | Overall Accuracy |
|:-------------:|:------:|:----:|:---------------:|:--------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:---------------------------------------------------------------------------------------------------------:|:-----------------:|:--------------:|:----------:|:----------------:|
| 0.4236        | 10.53  | 200  | 0.9583          | {'precision': 0.8623962040332147, 'recall': 0.8898408812729498, 'f1': 0.8759036144578314, 'number': 817} | {'precision': 0.5131578947368421, 'recall': 0.3277310924369748, 'f1': 0.39999999999999997, 'number': 119} | {'precision': 0.8450704225352113, 'recall': 0.947075208913649, 'f1': 0.893169877408056, 'number': 1077}   | 0.8401            | 0.8872         | 0.8630     | 0.8016           |
| 0.0421        | 21.05  | 400  | 1.4064          | {'precision': 0.8573113207547169, 'recall': 0.8898408812729498, 'f1': 0.8732732732732732, 'number': 817} | {'precision': 0.4301675977653631, 'recall': 0.6470588235294118, 'f1': 0.5167785234899329, 'number': 119}  | {'precision': 0.8667883211678832, 'recall': 0.8820798514391829, 'f1': 0.87436723423838, 'number': 1077}   | 0.8262            | 0.8713         | 0.8482     | 0.7733           |
| 0.0121        | 31.58  | 600  | 1.5114          | {'precision': 0.8534090909090909, 'recall': 0.9192166462668299, 'f1': 0.8850913376546846, 'number': 817} | {'precision': 0.5930232558139535, 'recall': 0.42857142857142855, 'f1': 0.4975609756097561, 'number': 119} | {'precision': 0.8824577025823687, 'recall': 0.9201485608170845, 'f1': 0.9009090909090909, 'number': 1077} | 0.8583            | 0.8907         | 0.8742     | 0.8044           |
| 0.0058        | 42.11  | 800  | 1.4988          | {'precision': 0.8361391694725028, 'recall': 0.9118727050183598, 'f1': 0.8723653395784543, 'number': 817} | {'precision': 0.5203252032520326, 'recall': 0.5378151260504201, 'f1': 0.5289256198347108, 'number': 119}  | {'precision': 0.8798206278026905, 'recall': 0.9108635097493036, 'f1': 0.8950729927007299, 'number': 1077} | 0.8408            | 0.8892         | 0.8643     | 0.7982           |
| 0.004         | 52.63  | 1000 | 1.5823          | {'precision': 0.8455467869222097, 'recall': 0.9179926560587516, 'f1': 0.880281690140845, 'number': 817}  | {'precision': 0.5263157894736842, 'recall': 0.5042016806722689, 'f1': 0.5150214592274679, 'number': 119}  | {'precision': 0.867595818815331, 'recall': 0.924791086350975, 'f1': 0.8952808988764045, 'number': 1077}   | 0.8404            | 0.8972         | 0.8679     | 0.7996           |
| 0.0028        | 63.16  | 1200 | 1.6518          | {'precision': 0.8492822966507177, 'recall': 0.8690330477356181, 'f1': 0.8590441621294616, 'number': 817} | {'precision': 0.5855855855855856, 'recall': 0.5462184873949579, 'f1': 0.5652173913043478, 'number': 119}  | {'precision': 0.88, 'recall': 0.9192200557103064, 'f1': 0.899182561307902, 'number': 1077}                | 0.8518            | 0.8768         | 0.8641     | 0.7939           |
| 0.0013        | 73.68  | 1400 | 1.8819          | {'precision': 0.8378672470076169, 'recall': 0.9424724602203183, 'f1': 0.8870967741935485, 'number': 817} | {'precision': 0.6794871794871795, 'recall': 0.44537815126050423, 'f1': 0.5380710659898478, 'number': 119} | {'precision': 0.9006622516556292, 'recall': 0.8839368616527391, 'f1': 0.8922211808809747, 'number': 1077} | 0.8642            | 0.8818         | 0.8729     | 0.7931           |
| 0.0013        | 84.21  | 1600 | 1.8234          | {'precision': 0.8519362186788155, 'recall': 0.9155446756425949, 'f1': 0.8825958702064898, 'number': 817} | {'precision': 0.5585585585585585, 'recall': 0.5210084033613446, 'f1': 0.5391304347826087, 'number': 119}  | {'precision': 0.9120982986767486, 'recall': 0.8960074280408542, 'f1': 0.9039812646370023, 'number': 1077} | 0.8671            | 0.8818         | 0.8744     | 0.7996           |
| 0.0008        | 94.74  | 1800 | 1.7898          | {'precision': 0.844170403587444, 'recall': 0.9216646266829865, 'f1': 0.8812170860152135, 'number': 817}  | {'precision': 0.5294117647058824, 'recall': 0.5294117647058824, 'f1': 0.5294117647058824, 'number': 119}  | {'precision': 0.8756613756613757, 'recall': 0.9220055710306406, 'f1': 0.898236092265943, 'number': 1077}  | 0.8434            | 0.8987         | 0.8701     | 0.7901           |
| 0.0004        | 105.26 | 2000 | 1.8115          | {'precision': 0.8396436525612472, 'recall': 0.9228886168910648, 'f1': 0.8793002915451895, 'number': 817} | {'precision': 0.6063829787234043, 'recall': 0.4789915966386555, 'f1': 0.5352112676056338, 'number': 119}  | {'precision': 0.8909090909090909, 'recall': 0.9099350046425255, 'f1': 0.90032154340836, 'number': 1077}   | 0.8561            | 0.8897         | 0.8726     | 0.7939           |
| 0.0004        | 115.79 | 2200 | 1.7928          | {'precision': 0.8716763005780347, 'recall': 0.9228886168910648, 'f1': 0.8965517241379309, 'number': 817} | {'precision': 0.5648148148148148, 'recall': 0.5126050420168067, 'f1': 0.5374449339207047, 'number': 119}  | {'precision': 0.8945454545454545, 'recall': 0.9136490250696379, 'f1': 0.9039963252181902, 'number': 1077} | 0.8678            | 0.8937         | 0.8806     | 0.7985           |
| 0.0003        | 126.32 | 2400 | 1.8271          | {'precision': 0.863013698630137, 'recall': 0.9253365973072215, 'f1': 0.8930891907855877, 'number': 817}  | {'precision': 0.6105263157894737, 'recall': 0.48739495798319327, 'f1': 0.5420560747663552, 'number': 119} | {'precision': 0.8935395814376706, 'recall': 0.9117920148560817, 'f1': 0.9025735294117648, 'number': 1077} | 0.8676            | 0.8922         | 0.8797     | 0.7983           |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.12.1+cu102
- Datasets 2.8.0
- Tokenizers 0.13.1
