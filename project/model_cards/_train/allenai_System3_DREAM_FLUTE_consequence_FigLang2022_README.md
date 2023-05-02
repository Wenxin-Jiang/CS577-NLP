---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for System 3 DREAM-FLUTE (consequence), as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

Systems 3: DREAM-FLUTE - Providing DREAM’s different dimensions as input context 

We adapt DREAM’s scene elaborations (Gu et al., 2022) for the figurative language understanding NLI task by using the DREAM model to generate elaborations for the premise and hypothesis separately. This allows us to investigate if similarities or differences in the scene elaborations for the premise and hypothesis will provide useful signals for entailment/contradiction label prediction and improving explanation quality. The input-output format is:
```
Input <Premise> <Premise-elaboration-from-DREAM> <Hypothesis> <Hypothesis-elaboration-from-DREAM>
Output <Label> <Explanation>
```
where the scene elaboration dimensions from DREAM are: consequence, emotion, motivation, and social norm. We also consider a system incorporating all these dimensions as additional context.

In this model, DREAM-FLUTE (consequence), we use elaborations along the "likely consequence" dimension. For more details on DREAM, please refer to DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/).

# How to use this model?
We provide a quick example of how you can try out DREAM-FLUTE (consequence) in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_consequence_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: My decision-making skills are not purely based on emotions and gut. [Premise - likely consequence] I make more balanced and informed decisions. Hypothesis: My personal feelings color my judgment in this case. [Hypothesis - likely consequence] I make a decision that is not in the best interests of the company. Is there a contradiction or entailment between the premise and hypothesis?"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
["Answer : Contradiction. Explanation : To have personal feelings color one's judgment means to make decisions based on them, but this context describes making decisions based on facts and not emotions"]
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
- Loss: 0.7505
- Rouge1: 58.425
- Rouge2: 38.2333
- Rougel: 52.1326
- Rougelsum: 52.1316
- Gen Len: 41.0909


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
| 0.9958        | 0.33  | 1000 | 0.8928          | 39.7038 | 27.4256 | 38.1226 | 38.1237   | 19.0    |
| 0.8973        | 0.66  | 2000 | 0.8252          | 41.4862 | 29.5302 | 39.6228 | 39.5913   | 18.9987 |
| 0.8837        | 1.0   | 3000 | 0.7854          | 41.2109 | 29.7022 | 39.6115 | 39.5989   | 19.0    |
| 0.5656        | 1.33  | 4000 | 0.8016          | 41.0368 | 29.76   | 39.4324 | 39.4341   | 19.0    |
| 0.5598        | 1.66  | 5000 | 0.7802          | 41.6073 | 30.3183 | 39.9937 | 39.9743   | 19.0    |
| 0.5495        | 1.99  | 6000 | 0.7505          | 41.7965 | 30.6031 | 40.1514 | 40.1509   | 19.0    |
| 0.3341        | 2.32  | 7000 | 0.8518          | 41.6758 | 30.9028 | 40.134  | 40.1415   | 18.9954 |
| 0.3493        | 2.65  | 8000 | 0.8544          | 41.5856 | 31.1526 | 40.154  | 40.1726   | 18.9940 |
| 0.3535        | 2.99  | 9000 | 0.8291          | 41.9552 | 31.4885 | 40.5239 | 40.5235   | 19.0    |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
