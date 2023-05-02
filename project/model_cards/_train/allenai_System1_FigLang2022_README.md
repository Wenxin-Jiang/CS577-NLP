---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---

# Model description

This is the T5-3B model for System 1 as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

System 1: Using original data

Given the <Premise, Hypothesis, Label, Explanation> in the original data, we first trained a sequence-to-sequence model for the figurative language NLI task
using the following input-output format: 
```
Input <Premise> <Hypothesis>
Output <Label> <Explanation>
```

# How to use this model?
We provide a quick example of how you can try out System 1 in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System1_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: My neighbor actually purchased a dream car of mine and I see it parked in his driveway everyday just taunting me. Hypothesis: My neighbor's new car is exactly my dream car, and I feel so happy every time I see it parked in his driveway. Is there a contradiction or entailment between the premise and hypothesis?"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
["Answer : Contradiction. Explanation : Most people would not be happy to see someone else's new car that they cannot afford because it is way out of their budget"]
```

# More details about DREAM-FLUTE ...
For more details about DREAM-FLUTE, please refer to our:
* 📄Paper: https://arxiv.org/abs/2210.16407
* 💻GitHub Repo: https://github.com/allenai/dream/ 

This model is part of our DREAM-series of works. This is a line of research where we make use of scene elaboration for building a "mental model" of situation given in text. Check out our GitHub Repo for more!

# More details about this model ...
## Training and evaluation data

We use the FLUTE dataset for the FigLang2022SharedTask (https://huggingface.co/datasets/ColumbiaNLP/FLUTE) for training this model. ∼7500 samples are provided as the training set. We used a 80-20 split to create our own training (6027 samples) and validation (1507 samples) partitions on which we build our models. For details on how we make use of the training data provided in the FigLang2022 shared task, please refer to https://github.com/allenai/dream/blob/main/FigLang2022SharedTask/Process_Data_Train_Dev_split.ipynb.

## Model details

This model is a fine-tuned version of [t5-3b](https://huggingface.co/t5-3b). 

It achieves the following results on the evaluation set:
- Loss: 0.7602
- Rouge1: 58.1212
- Rouge2: 38.1109
- Rougel: 52.1198
- Rougelsum: 52.092
- Gen Len: 40.4851

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- distributed_type: multi-GPU
- num_devices: 2
- total_train_batch_size: 2
- total_eval_batch_size: 2
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 3.0

### Training results

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2  | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:-------:|:-------:|:---------:|:-------:|
| 1.0017        | 0.33  | 1000 | 0.8958          | 40.072  | 27.6729 | 38.429  | 38.4023   | 19.0    |
| 0.9054        | 0.66  | 2000 | 0.8336          | 41.4505 | 29.2616 | 39.5164 | 39.4976   | 19.0    |
| 0.8777        | 1.0   | 3000 | 0.7863          | 41.4221 | 29.6675 | 39.6719 | 39.6627   | 19.0    |
| 0.5608        | 1.33  | 4000 | 0.8007          | 41.1495 | 29.9008 | 39.5706 | 39.5554   | 19.0    |
| 0.5594        | 1.66  | 5000 | 0.7785          | 41.3834 | 30.2818 | 39.8259 | 39.8324   | 19.0    |
| 0.5498        | 1.99  | 6000 | 0.7602          | 41.6364 | 30.6513 | 40.1522 | 40.1332   | 19.0    |
| 0.3398        | 2.32  | 7000 | 0.8580          | 41.4948 | 30.7467 | 40.0274 | 40.0116   | 18.9954 |
| 0.3518        | 2.65  | 8000 | 0.8430          | 41.7283 | 31.178  | 40.3487 | 40.3328   | 18.9861 |
| 0.3465        | 2.99  | 9000 | 0.8405          | 41.956  | 31.527  | 40.5671 | 40.5517   | 18.9907 |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1


