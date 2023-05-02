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
- Loss: 1.5653
- Answer: {'precision': 0.8498293515358362, 'recall': 0.9143206854345165, 'f1': 0.8808962264150944, 'number': 817}
- Header: {'precision': 0.6521739130434783, 'recall': 0.5042016806722689, 'f1': 0.5687203791469194, 'number': 119}
- Question: {'precision': 0.8874887488748875, 'recall': 0.9155060352831941, 'f1': 0.9012797074954296, 'number': 1077}
- Overall Precision: 0.8612
- Overall Recall: 0.8907
- Overall F1: 0.8757
- Overall Accuracy: 0.8129

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
| 0.4298        | 10.53  | 200  | 0.9916          | {'precision': 0.7861771058315334, 'recall': 0.8910648714810282, 'f1': 0.8353413654618475, 'number': 817} | {'precision': 0.6617647058823529, 'recall': 0.37815126050420167, 'f1': 0.4812834224598931, 'number': 119} | {'precision': 0.8677390527256479, 'recall': 0.9015784586815228, 'f1': 0.8843351548269581, 'number': 1077} | 0.8254            | 0.8664         | 0.8454     | 0.7855           |
| 0.0444        | 21.05  | 400  | 1.2861          | {'precision': 0.8777239709443099, 'recall': 0.8873929008567931, 'f1': 0.8825319537431527, 'number': 817} | {'precision': 0.50920245398773, 'recall': 0.6974789915966386, 'f1': 0.5886524822695035, 'number': 119}    | {'precision': 0.8607929515418502, 'recall': 0.9071494893221913, 'f1': 0.8833634719710669, 'number': 1077} | 0.8404            | 0.8867         | 0.8629     | 0.7885           |
| 0.0119        | 31.58  | 600  | 1.6730          | {'precision': 0.8451025056947609, 'recall': 0.9082007343941249, 'f1': 0.8755162241887906, 'number': 817} | {'precision': 0.6575342465753424, 'recall': 0.40336134453781514, 'f1': 0.5, 'number': 119}                | {'precision': 0.8945420906567992, 'recall': 0.8978644382544104, 'f1': 0.8962001853568119, 'number': 1077} | 0.8647            | 0.8728         | 0.8687     | 0.7919           |
| 0.0066        | 42.11  | 800  | 1.5189          | {'precision': 0.7907949790794979, 'recall': 0.9253365973072215, 'f1': 0.8527918781725887, 'number': 817} | {'precision': 0.5327102803738317, 'recall': 0.4789915966386555, 'f1': 0.504424778761062, 'number': 119}   | {'precision': 0.8740942028985508, 'recall': 0.8960074280408542, 'f1': 0.88491517652453, 'number': 1077}   | 0.8205            | 0.8833         | 0.8507     | 0.7868           |
| 0.004         | 52.63  | 1000 | 1.4418          | {'precision': 0.8623103850641773, 'recall': 0.9045287637698899, 'f1': 0.8829151732377538, 'number': 817} | {'precision': 0.5163934426229508, 'recall': 0.5294117647058824, 'f1': 0.5228215767634855, 'number': 119}  | {'precision': 0.881651376146789, 'recall': 0.8922934076137419, 'f1': 0.8869404706968159, 'number': 1077}  | 0.8521            | 0.8758         | 0.8638     | 0.8041           |
| 0.0024        | 63.16  | 1200 | 1.5428          | {'precision': 0.8417508417508418, 'recall': 0.9179926560587516, 'f1': 0.8782201405152226, 'number': 817} | {'precision': 0.6304347826086957, 'recall': 0.48739495798319327, 'f1': 0.5497630331753555, 'number': 119} | {'precision': 0.8842676311030742, 'recall': 0.9080779944289693, 'f1': 0.8960146587265231, 'number': 1077} | 0.8550            | 0.8872         | 0.8708     | 0.8042           |
| 0.0015        | 73.68  | 1400 | 1.5302          | {'precision': 0.8338983050847457, 'recall': 0.9033047735618115, 'f1': 0.8672150411280846, 'number': 817} | {'precision': 0.5081967213114754, 'recall': 0.5210084033613446, 'f1': 0.5145228215767635, 'number': 119}  | {'precision': 0.8859813084112149, 'recall': 0.8802228412256268, 'f1': 0.8830926874708895, 'number': 1077} | 0.8416            | 0.8684         | 0.8548     | 0.8060           |
| 0.0013        | 84.21  | 1600 | 1.5327          | {'precision': 0.8610129564193169, 'recall': 0.8947368421052632, 'f1': 0.8775510204081634, 'number': 817} | {'precision': 0.5922330097087378, 'recall': 0.5126050420168067, 'f1': 0.5495495495495496, 'number': 119}  | {'precision': 0.8766637089618456, 'recall': 0.9173630454967502, 'f1': 0.896551724137931, 'number': 1077}  | 0.8562            | 0.8843         | 0.8700     | 0.8111           |
| 0.0005        | 94.74  | 1800 | 1.5100          | {'precision': 0.8355704697986577, 'recall': 0.9143206854345165, 'f1': 0.8731735827001753, 'number': 817} | {'precision': 0.691358024691358, 'recall': 0.47058823529411764, 'f1': 0.5599999999999999, 'number': 119}  | {'precision': 0.8776785714285714, 'recall': 0.9127205199628597, 'f1': 0.8948566226672735, 'number': 1077} | 0.8525            | 0.8872         | 0.8695     | 0.8067           |
| 0.0004        | 105.26 | 2000 | 1.5419          | {'precision': 0.8548387096774194, 'recall': 0.9082007343941249, 'f1': 0.8807121661721069, 'number': 817} | {'precision': 0.5922330097087378, 'recall': 0.5126050420168067, 'f1': 0.5495495495495496, 'number': 119}  | {'precision': 0.8763345195729537, 'recall': 0.914577530176416, 'f1': 0.8950477055883689, 'number': 1077}  | 0.8535            | 0.8882         | 0.8705     | 0.8078           |
| 0.0002        | 115.79 | 2200 | 1.5490          | {'precision': 0.846674182638106, 'recall': 0.9192166462668299, 'f1': 0.8814553990610329, 'number': 817}  | {'precision': 0.6060606060606061, 'recall': 0.5042016806722689, 'f1': 0.5504587155963303, 'number': 119}  | {'precision': 0.8831521739130435, 'recall': 0.9052924791086351, 'f1': 0.8940852819807427, 'number': 1077} | 0.8545            | 0.8872         | 0.8706     | 0.8130           |
| 0.0002        | 126.32 | 2400 | 1.5653          | {'precision': 0.8498293515358362, 'recall': 0.9143206854345165, 'f1': 0.8808962264150944, 'number': 817} | {'precision': 0.6521739130434783, 'recall': 0.5042016806722689, 'f1': 0.5687203791469194, 'number': 119}  | {'precision': 0.8874887488748875, 'recall': 0.9155060352831941, 'f1': 0.9012797074954296, 'number': 1077} | 0.8612            | 0.8907         | 0.8757     | 0.8129           |


### Framework versions

- Transformers 4.25.1
- Pytorch 1.13.0+cu117
- Datasets 2.8.0
- Tokenizers 0.13.2
