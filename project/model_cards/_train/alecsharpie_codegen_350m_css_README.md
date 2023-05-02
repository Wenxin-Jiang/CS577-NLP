---
language:
- code
license: bsd-3-clause
tags:
- code
- generative
datasets:
- bigcode/the-stack
---

# CodeGen (CodeGen-CSS 350M)

## Model description

CodeGen is a family of autoregressive language models for **program synthesis** from the paper: [A Conversational Paradigm for Program Synthesis](https://arxiv.org/abs/2203.13474) by Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, Caiming Xiong. The models are originally released in [this repository](https://github.com/salesforce/CodeGen), under 3 pre-training data variants (`NL`, `Multi`, `Mono`) and 4 model size variants (`350M`, `2B`, `6B`, `16B`).

The checkpoint included in this repository is finetuned on top of the **CodeGen-Multi 350M**, where "Multi" means the model is initialized with *CodeGen-NL 350M* and further pre-trained on a dataset of multiple programming languages, and "350M" refers to the number of trainable parameters.

It has been finetuned on CSS code contained in bigcode/the-stack dataset on huggingface

## Training data

This checkpoint (CodeGen-Multi 350M) was firstly initialized with *CodeGen-NL 350M*, and then pre-trained on [BigQuery](https://console.cloud.google.com/marketplace/details/github/github-repos), a large-scale dataset of multiple programming languages from GitHub repositories. The data consists of 119.2B tokens and includes C, C++, Go, Java, JavaScript, and Python.

Lastly it has been finetuned on CSS code contained in [bigcode/the-stack](https://huggingface.co/datasets/bigcode/the-stack) dataset on huggingface

## Training procedure

Initially:
CodeGen was trained using cross-entropy loss to maximize the likelihood of sequential inputs.
The family of models are trained using multiple TPU-v4-512 by Google, leveraging data and model parallelism.
See Section 2.3 of the [paper](https://arxiv.org/abs/2203.13474) for more details.

Finetune:
I fine tuned the 350M model on a single A100 with 40Gb of RAM, with batch size 10 and an input length of 512 tokens
Used 80-90% of the RAM

## Intended Use and Limitations

As an autoregressive language model, CodeGen is capable of extracting features from given natural language and programming language texts, and calculating the likelihood of them.
However, the model is intended for and best at **program synthesis**, that is, generating executable code given English prompts, where the prompts should be in the form of a comment string. The model can complete partially-generated code as well.

## How to use

This model can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-350M-multi")
model = AutoModelForCausalLM.from_pretrained("alecsharpie/codegen_350m_css")

text = ".header-container {"

input_ids = tokenizer(text, return_tensors="pt").input_ids
generated_ids = model.generate(input_ids, max_length=128)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```

## BibTeX entry and citation info

```bibtex
@article{Nijkamp2022ACP,
  title={A Conversational Paradigm for Program Synthesis},
  author={Nijkamp, Erik and Pang, Bo and Hayashi, Hiroaki and Tu, Lifu and Wang, Huan and Zhou, Yingbo and Savarese, Silvio and Xiong, Caiming},
  journal={arXiv preprint},
  year={2022}
}
```