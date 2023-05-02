---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for System 3 DREAM-FLUTE (social norm), as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

Systems 3: DREAM-FLUTE - Providing DREAM’s different dimensions as input context 

We adapt DREAM’s scene elaborations (Gu et al., 2022) for the figurative language understanding NLI task by using the DREAM model to generate elaborations for the premise and hypothesis separately. This allows us to investigate if similarities or differences in the scene elaborations for the premise and hypothesis will provide useful signals for entailment/contradiction label prediction and improving explanation quality. The input-output format is:
```
Input <Premise> <Premise-elaboration-from-DREAM> <Hypothesis> <Hypothesis-elaboration-from-DREAM>
Output <Label> <Explanation>
```
where the scene elaboration dimensions from DREAM are: consequence, emotion, motivation, and social norm. We also consider a system incorporating all these dimensions as additional context.

In this model, DREAM-FLUTE (social norm), we use elaborations along the "social norm" dimension. For more details on DREAM, please refer to DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/).

# How to use this model?
We provide a quick example of how you can try out DREAM-FLUTE (social norm) in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System3_DREAM_FLUTE_social_norm_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: Sure ,he snorted just to make me feel even better about the already great situation. [Premise - social norm] It's good to make people feel better about a situation. Hypothesis: Sure, he snorted, just rub it in. [Hypothesis - social norm] It's rude to rub something in someone's face when they don't want to. Is there a contradiction or entailment between the premise and hypothesis?"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['Answer : Contradiction. Explanation : To rub it in means to make someone feel bad about themselves, but in this sentence he is making the speaker feel better about the already great situation.']
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
- Loss: 0.7615
- Rouge1: 57.6814
- Rouge2: 37.489
- Rougel: 51.4698
- Rougelsum: 51.4842
- Gen Len: 40.8553


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
| 0.9974        | 0.33  | 1000 | 0.8955          | 39.7614 | 27.3853 | 38.1015 | 38.0975   | 19.0    |
| 0.8983        | 0.66  | 2000 | 0.8300          | 41.4031 | 29.3769 | 39.5984 | 39.5886   | 19.0    |
| 0.8764        | 1.0   | 3000 | 0.7855          | 41.2619 | 29.5054 | 39.5859 | 39.5748   | 18.9980 |
| 0.5603        | 1.33  | 4000 | 0.8033          | 41.0015 | 29.8488 | 39.5492 | 39.522    | 18.9980 |
| 0.5619        | 1.66  | 5000 | 0.7869          | 41.3655 | 30.0581 | 39.7462 | 39.7231   | 19.0    |
| 0.5389        | 1.99  | 6000 | 0.7615          | 41.3902 | 30.2049 | 39.8797 | 39.8779   | 19.0    |
| 0.3325        | 2.32  | 7000 | 0.8776          | 41.1737 | 30.3441 | 39.6744 | 39.652    | 18.9954 |
| 0.3509        | 2.65  | 8000 | 0.8501          | 41.2653 | 30.5342 | 39.7315 | 39.7252   | 18.9907 |
| 0.3499        | 2.99  | 9000 | 0.8546          | 41.6401 | 31.0585 | 40.2659 | 40.2487   | 18.9907 |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
