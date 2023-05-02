---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for the "explain" component of System 4's "Classify then explain" pipeline, as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

System 4: Two-step System - Classify then explain

In contrast to Systems 1 to 3 where the entailment/contradiction label and associated explanation are predicted jointly, System 4 uses a two-step “classify then explain” pipeline. This current model is for the "explain" component of the pipeline. The input-output format is:
```
Input <Premise> <Hypothesis> <Label> 
Output <Explanation>
```

# How to use this model?
We provide a quick example of how you can try out the "explain" component of System 4 in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System4_explain_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: It is wrong to lie to children. Hypothesis: Telling lies to the young is like clippin the wings of a butterfly. Is there a contradiction or entailment between the premise and hypothesis? Answer : Entailment. Explanation : "
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['Clipping the wings of a butterfly means that the butterfly will never be able to fly, so lying to children is like doing the same.']
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
- Loss: 1.0331
- Rouge1: 53.8485
- Rouge2: 32.8855
- Rougel: 46.6534
- Rougelsum: 46.6435
- Gen Len: 29.7724


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
| 1.3633        | 0.33  | 1000 | 1.2468          | 44.8469 | 24.3002 | 37.9797 | 37.9943   | 18.8341 |
| 1.2531        | 0.66  | 2000 | 1.1445          | 45.7234 | 25.6755 | 39.5817 | 39.5653   | 18.8786 |
| 1.2148        | 1.0   | 3000 | 1.0806          | 47.4244 | 27.6605 | 41.0803 | 41.0628   | 18.7339 |
| 0.7554        | 1.33  | 4000 | 1.1006          | 47.5505 | 28.2781 | 41.385  | 41.3774   | 18.6556 |
| 0.7761        | 1.66  | 5000 | 1.0671          | 48.583  | 29.6223 | 42.5451 | 42.5247   | 18.6821 |
| 0.7777        | 1.99  | 6000 | 1.0331          | 48.8329 | 30.5086 | 43.0964 | 43.0586   | 18.6881 |
| 0.4378        | 2.32  | 7000 | 1.1978          | 48.6239 | 30.2101 | 42.8863 | 42.8851   | 18.7259 |
| 0.4715        | 2.66  | 8000 | 1.1545          | 49.1311 | 31.0582 | 43.523  | 43.5043   | 18.7598 |
| 0.462         | 2.99  | 9000 | 1.1471          | 49.4022 | 31.7946 | 44.0345 | 44.0128   | 18.7200 |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
