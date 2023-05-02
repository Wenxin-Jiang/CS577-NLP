---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for System 2 as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

System 2: Jointly predicting the type of figurative language 

Using type of figurative language provided as part of the training set (Chakrabarty et al., 2022), one of our models jointly predicts the type of figurative language, together with the target label and explanation:
```
Input <Premise> <Hypothesis> 
Output <Figurative-Language-Type> <Label> <Explanation>
```

# How to use this model?
We provide a quick example of how you can try out System 2 in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System2_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: Yesterday two gangs were fighting just in front of my home. Hypothesis: Yesterday I saw two gangs fighting right in front of my house and it totally didn't make me scared at all. What is the type of figurative language involved? Is there a contradiction or entailment between the premise and hypothesis?"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['Answer : [Type] Sarcasm [Label] Contradiction. Explanation : Seeing two gangs of people fighting in public can be really dangerous and scary, so someone who claims that they were not scared at all is being sarcastic.']
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
- Loss: 0.6078
- Rouge1: 62.8674
- Rouge2: 45.0585
- Rougel: 57.5618
- Rougelsum: 57.5172
- Gen Len: 50.7558

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
| 0.8068        | 0.33  | 1000 | 0.7251          | 30.6353 | 25.0792 | 30.619  | 30.6274   | 19.0    |
| 0.7276        | 0.66  | 2000 | 0.6715          | 30.8651 | 26.1492 | 30.8543 | 30.8519   | 19.0    |
| 0.7063        | 1.0   | 3000 | 0.6338          | 31.0263 | 26.6749 | 31.0094 | 31.0098   | 19.0    |
| 0.4516        | 1.33  | 4000 | 0.6447          | 30.9942 | 26.5984 | 30.9834 | 30.9778   | 19.0    |
| 0.4538        | 1.66  | 5000 | 0.6183          | 31.0179 | 26.7012 | 31.005  | 31.0018   | 19.0    |
| 0.4373        | 1.99  | 6000 | 0.6078          | 31.0085 | 26.7116 | 30.9952 | 30.9894   | 19.0    |
| 0.2743        | 2.32  | 7000 | 0.6910          | 31.0051 | 26.7349 | 30.9975 | 30.9851   | 19.0    |
| 0.2819        | 2.65  | 8000 | 0.6831          | 31.0876 | 26.848  | 31.0766 | 31.0753   | 19.0    |
| 0.2849        | 2.99  | 9000 | 0.6673          | 30.9223 | 26.5899 | 30.9165 | 30.9073   | 19.0    |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
