---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for System 3 DREAM-FLUTE (all 4 dimensions), as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

Systems 3: DREAM-FLUTE - Providing DREAM’s different dimensions as input context 

We adapt DREAM’s scene elaborations (Gu et al., 2022) for the figurative language understanding NLI task by using the DREAM model to generate elaborations for the premise and hypothesis separately. This allows us to investigate if similarities or differences in the scene elaborations for the premise and hypothesis will provide useful signals for entailment/contradiction label prediction and improving explanation quality. The input-output format is:
```
Input <Premise> <Premise-elaboration-from-DREAM> <Hypothesis> <Hypothesis-elaboration-from-DREAM>
Output <Label> <Explanation>
```
where the scene elaboration dimensions from DREAM are: consequence, emotion, motivation, and social norm. We also consider a system incorporating all these dimensions as additional context.

In this model, DREAM-FLUTE (all 4 dimensions), we use elaborations along all DREAM dimensions. For more details on DREAM, please refer to DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/).

# How to use this model?
We provide a quick example of how you can try out DREAM-FLUTE (all 4 dimensions) in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_all_dimensions_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: I was really looking forward to camping but now it is going to rain so I won't go. [Premise - social norm] It's okay to be disappointed when plans change. [Premise - emotion] I (myself)'s emotion is disappointed. [Premise - motivation] I (myself)'s motivation is to stay home. [Premise - likely consequence] I will miss out on a great experience and be bored and sad. Hypothesis: I am absolutely elated at the prospects of getting drenched in the rain and then sleep in a wet tent just to have the experience of camping. [Hypothesis - social norm] It's good to want to have new experiences. [Hypothesis - emotion] I (myself)'s emotion is excited. [Hypothesis - motivation] I (myself)'s motivation is to have fun. [Hypothesis - likely consequence] I am so excited that I forget to bring a raincoat and my tent gets soaked. Is there a contradiction or entailment between the premise and hypothesis?"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['Answer : Contradiction. Explanation : Camping in the rain is often associated with the prospect of getting wet and cold, so someone who is elated about it is not being rational.']
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
- Loss: 0.7499
- Rouge1: 58.5551
- Rouge2: 38.5673
- Rougel: 52.3701
- Rougelsum: 52.335
- Gen Len: 40.7452


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
| 0.992         | 0.33  | 1000 | 0.8911          | 39.9287 | 27.5817 | 38.2127 | 38.2042   | 19.0    |
| 0.9022        | 0.66  | 2000 | 0.8409          | 40.8873 | 28.7963 | 39.16   | 39.1615   | 19.0    |
| 0.8744        | 1.0   | 3000 | 0.7813          | 41.2617 | 29.5498 | 39.5857 | 39.5695   | 19.0    |
| 0.5636        | 1.33  | 4000 | 0.7961          | 41.1429 | 30.2299 | 39.6592 | 39.6648   | 19.0    |
| 0.5585        | 1.66  | 5000 | 0.7763          | 41.2581 | 30.0851 | 39.6859 | 39.68     | 19.0    |
| 0.5363        | 1.99  | 6000 | 0.7499          | 41.8302 | 30.964  | 40.3059 | 40.2964   | 19.0    |
| 0.3347        | 2.32  | 7000 | 0.8540          | 41.4633 | 30.6209 | 39.9933 | 39.9948   | 18.9954 |
| 0.341         | 2.65  | 8000 | 0.8599          | 41.6576 | 31.0316 | 40.1466 | 40.1526   | 18.9907 |
| 0.3531        | 2.99  | 9000 | 0.8368          | 42.05   | 31.6387 | 40.6239 | 40.6254   | 18.9907 |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
