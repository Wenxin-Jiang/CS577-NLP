---
license: bsd-3-clause
---
# CodeGen (CodeGen-Mono 6B)

## Model description

CodeGen is a family of autoregressive language models for **program synthesis** from the paper: [A Conversational Paradigm for Program Synthesis](https://arxiv.org/abs/2203.13474) by Erik Nijkamp, Bo Pang, Hiroaki Hayashi, Lifu Tu, Huan Wang, Yingbo Zhou, Silvio Savarese, Caiming Xiong. The models are originally released in [this repository](https://github.com/salesforce/CodeGen), under 3 pre-training data variants (`NL`, `Multi`, `Mono`) and 4 model size variants (`350M`, `2B`, `6B`, `16B`).

The checkpoint included in this repository is denoted as **CodeGen-Mono 6B** in the paper, where "Mono" means the model is initialized with *CodeGen-Multi 6B* and further pre-trained on a Python programming language dataset, and "6B" refers to the number of trainable parameters.

## Training data

This checkpoint (CodeGen-Mono 6B) was firstly initialized with *CodeGen-Multi 6B*, and then pre-trained on BigPython dataset. The data consists of 71.7B tokens of Python programming language. See Section 2.1 of the [paper](https://arxiv.org/abs/2203.13474) for more details.

## Training procedure

CodeGen was trained using cross-entropy loss to maximize the likelihood of sequential inputs.
The family of models are trained using multiple TPU-v4-512 by Google, leveraging data and model parallelism.
See Section 2.3 of the [paper](https://arxiv.org/abs/2203.13474) for more details.

## Evaluation results

We evaluate our models on two code generation benchmark: HumanEval and MTPB. Please refer to the [paper](https://arxiv.org/abs/2203.13474) for more details.


## Intended Use and Limitations

As an autoregressive language model, CodeGen is capable of extracting features from given natural language and programming language texts, and calculating the likelihood of them.
However, the model is intended for and best at **program synthesis**, that is, generating executable code given English prompts, where the prompts should be in the form of a comment string. The model can complete partially-generated code as well.

## How to use

This model can be easily loaded using the `AutoModelForCausalLM` functionality:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codegen-6B-mono")
model = AutoModelForCausalLM.from_pretrained("Salesforce/codegen-6B-mono")

text = "def hello_world():"
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
