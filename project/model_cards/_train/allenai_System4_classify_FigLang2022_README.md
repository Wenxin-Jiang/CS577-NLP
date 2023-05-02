---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts
---
# Model description
This is the T5-3B model for the "classify" component of System 4's "Classify then explain" pipeline, as described in our paper Just-DREAM-about-it: Figurative Language Understanding with DREAM-FLUTE, FigLang workshop @ EMNLP 2022 (Arxiv link: https://arxiv.org/abs/2210.16407) 

System 4: Two-step System - Classify then explain

In contrast to Systems 1 to 3 where the entailment/contradiction label and associated explanation are predicted jointly, System 4 uses a two-step “classify then explain” pipeline. This current model is for the "classify" component of the pipeline. The input-output format is:
```
Input <Premise> <Hypothesis> 
Output <Label>
```

# How to use this model?
We provide a quick example of how you can try out the "classify" component of System 4 in our paper with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/System4_classify_FigLang2022")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-3b")
>>> input_string = "Premise: After releasing his rage he was like a ferocious wolf. Hypothesis: After letting off his rage he sat down like a lamb. Is there a contradiction or entailment between the premise and hypothesis? Answer : "
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
['Contradiction']
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
- Loss: 0.0604
- Rouge1: 95.0232
- Rouge2: 0.0
- Rougel: 95.0232
- Rougelsum: 95.0232
- Gen Len: 3.4074


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

| Training Loss | Epoch | Step | Validation Loss | Rouge1  | Rouge2 | Rougel  | Rougelsum | Gen Len |
|:-------------:|:-----:|:----:|:---------------:|:-------:|:------:|:-------:|:---------:|:-------:|
| 0.1221        | 0.33  | 1000 | 0.1460          | 91.7717 | 0.0    | 91.9044 | 91.8381   | 3.4751  |
| 0.0957        | 0.66  | 2000 | 0.0904          | 93.6297 | 0.0    | 93.6961 | 93.6961   | 3.3955  |
| 0.0721        | 1.0   | 3000 | 0.0720          | 94.8905 | 0.0    | 94.9569 | 94.8905   | 3.4061  |
| 0.0413        | 1.33  | 4000 | 0.0786          | 94.5587 | 0.0    | 94.5587 | 94.5587   | 3.4346  |
| 0.042         | 1.66  | 5000 | 0.0604          | 95.0232 | 0.0    | 95.0232 | 95.0232   | 3.4074  |
| 0.0413        | 1.99  | 6000 | 0.0737          | 95.2223 | 0.0    | 95.2223 | 95.2223   | 3.4413  |
| 0.0198        | 2.32  | 7000 | 0.1045          | 95.0896 | 0.0    | 95.1559 | 95.1559   | 3.4101  |
| 0.0253        | 2.65  | 8000 | 0.0836          | 95.2887 | 0.0    | 95.2887 | 95.2887   | 3.4393  |
| 0.0198        | 2.99  | 9000 | 0.0922          | 94.7578 | 0.0    | 94.7578 | 94.7578   | 3.4180  |


### Framework versions

- Transformers 4.22.0.dev0
- Pytorch 1.12.1+cu113
- Datasets 2.4.0
- Tokenizers 0.12.1
