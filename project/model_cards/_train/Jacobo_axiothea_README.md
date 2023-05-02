---
tags:
- generated_from_trainer
language:
- grc
model-index:
- name: dioBERTo
  results: []
widget:
- text: "Πλάτων ὁ Περικτιόνης <mask> γένος ἀνέφερεν εἰς Σόλωνα."
- text: "ὁ Κριτίας ἀπέβλεψε <mask> τὴν θύραν."
- text: "Ὦ φίλε Κλεινία, καλῶς μὲν <mask>."

---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# axiothea

This is an experimental roberta model trained with an ancient Greek corpus of about 900 MB, which was scrapped from the web and post-processed. Duplicate texts and editorial punctuation were removed. The training dataset will be soon available in the Huggingface datasets hub. Training a model of ancient Greek is challenging given that it is a low resource language from which 50% of the register has only survived in fragmentary texts. The model is provided by the Diogenet project at the University of California, San Diego. 
 
It achieves the following results on the evaluation set:

- Loss: 3.3351

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
- num_epochs: 10.0

### Training results

| Training Loss | Epoch | Step    | Validation Loss |
|:-------------:|:-----:|:-------:|:---------------:|
| 4.7013        | 1.0   | 341422  | 4.8813          |
| 4.2866        | 2.0   | 682844  | 4.4422          |
| 4.0496        | 3.0   | 1024266 | 4.2132          |
| 3.8503        | 4.0   | 1365688 | 4.0246          |
| 3.6917        | 5.0   | 1707110 | 3.8756          |
| 3.4917        | 6.0   | 2048532 | 3.7381          |
| 3.3907        | 7.0   | 2389954 | 3.6107          |
| 3.2876        | 8.0   | 2731376 | 3.5044          |
| 3.1994        | 9.0   | 3072798 | 3.3980          |
| 3.0806        | 10.0  | 3414220 | 3.3095          |


### Framework versions

- Transformers 4.13.0.dev0
- Pytorch 1.10.0+cu102
- Datasets 1.14.0
- Tokenizers 0.10.3
