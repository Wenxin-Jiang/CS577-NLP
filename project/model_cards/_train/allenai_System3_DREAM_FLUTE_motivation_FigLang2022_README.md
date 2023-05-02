---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for System 3 DREAM-FLUTE (motivation), as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

Systems 3: DREAM-FLUTE - Providing DREAM’s different dimensions as input context 

We adapt DREAM’s scene elaborations (Gu et al., 2022) for the figurative language understanding NLI task by using the DREAM model to generate elaborations for the premise and hypothesis separately. This allows us to investigate if similarities or differences in the scene elaborations for the premise and hypothesis will provide useful signals for entailment/contradiction label prediction and improving explanation quality. The input-output format is:
```
Input <Premise> <Premise-elaboration-from-DREAM> <Hypothesis> <Hypothesis-elaboration-from-DREAM>
Output <Label> <Explanation>
```
where the scene elaboration dimensions from DREAM are: consequence, emotion, motivation, and social norm. We also consider a system incorporating all these dimensions as additional context.

In this model, DREAM-FLUTE (motivation), we use elaborations along the "motivation" dimension. For more details on DREAM, please refer to DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/).

# How to use this model?
We provide a quick example of how you can try out DREAM-FLUTE (motivation) in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_motivation_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string =  "Premise: After years of service and contribution to the company, he was finally promoted. [Premise - motivation] Company's motivation is to recognize his hard work. Hypothesis: The company released him after many years of service. [Hypothesis - motivation] Company's motivation is to get someone else to work. Is there a contradiction or entailment between the premise and hypothesis?"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['Answer : Contradiction. Explanation : To release someone means to let them go from a position, while to promote someone means to give them a higher position.']
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
- Loss: 0.7515
- Rouge1: 58.2308
- Rouge2: 38.281
- Rougel: 52.0293
- Rougelsum: 52.0425
- Gen Len: 40.5912

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
| 0.9996        | 0.33  | 1000 | 0.8940          | 39.4794 | 27.1937 | 37.848  | 37.8416   | 18.9980 |
| 0.9033        | 0.66  | 2000 | 0.8276          | 41.3816 | 29.2481 | 39.5342 | 39.514    | 18.9987 |
| 0.8713        | 1.0   | 3000 | 0.7840          | 41.392  | 29.7142 | 39.642  | 39.6292   | 19.0    |
| 0.5631        | 1.33  | 4000 | 0.8079          | 41.1312 | 29.9449 | 39.5757 | 39.5775   | 19.0    |
| 0.5577        | 1.66  | 5000 | 0.7781          | 41.4609 | 30.3437 | 39.9114 | 39.8902   | 19.0    |
| 0.5426        | 1.99  | 6000 | 0.7515          | 41.9285 | 30.9247 | 40.3207 | 40.3087   | 19.0    |
| 0.33          | 2.32  | 7000 | 0.8601          | 41.6921 | 30.9567 | 40.1845 | 40.1805   | 18.9954 |
| 0.3442        | 2.65  | 8000 | 0.8910          | 41.5437 | 31.0748 | 40.1653 | 40.1579   | 18.9861 |
| 0.3474        | 2.99  | 9000 | 0.8354          | 41.8455 | 31.4446 | 40.5079 | 40.5116   | 18.9907 |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
