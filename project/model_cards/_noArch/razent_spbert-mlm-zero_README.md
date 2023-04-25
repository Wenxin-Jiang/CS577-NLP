---
language: 
  - code

tags:
- question-answering
- knowledge-graph
---


# SPBERT MLM (Scratch)

## Introduction
Paper: [SPBERT: An Efficient Pre-training BERT on SPARQL Queries for Question Answering over Knowledge Graphs](https://arxiv.org/abs/2106.09997)

Authors: _Hieu Tran, Long Phan, James Anibal, Binh T. Nguyen, Truong-Son Nguyen_

## How to use
For more details, do check out [our Github repo](https://github.com/heraclex12/NLP2SPARQL). 

Here is an example in Pytorch:
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained('razent/spbert-mlm-zero')
model = AutoModel.from_pretrained("razent/spbert-mlm-zero")
text = "select * where brack_open var_a var_b var_c sep_dot brack_close"
encoded_input = tokenizer(text, return_tensors='pt')
output = model(**encoded_input)
```
or Tensorflow
```python
from transformers import AutoTokenizer, TFAutoModel
tokenizer = AutoTokenizer.from_pretrained('razent/spbert-mlm-zero')
model = TFAutoModel.from_pretrained("razent/spbert-mlm-zero")
text = "select * where brack_open var_a var_b var_c sep_dot brack_close"
encoded_input = tokenizer(text, return_tensors='tf')
output = model(encoded_input)
```

## Citation
```
@misc{tran2021spbert,
      title={SPBERT: An Efficient Pre-training BERT on SPARQL Queries for Question Answering over Knowledge Graphs}, 
      author={Hieu Tran and Long Phan and James Anibal and Binh T. Nguyen and Truong-Son Nguyen},
      year={2021},
      eprint={2106.09997},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```