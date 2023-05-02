---
license: bsd-3-clause
---
# CodeT5 (large-size model pretrained with NTP objective on Python)

## Model description

CodeT5 is a family of encoder-decoder language models for code from the paper: [CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation](https://arxiv.org/pdf/2109.00859.pdf) by Yue Wang, Weishi Wang, Shafiq Joty, and Steven C.H. Hoi.

The checkpoint included in this repository is denoted as **CodeT5-large-ntp-py** (770M), which is introduced by the paper: [CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning](https://arxiv.org/pdf/2207.01780.pdf) by Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese, Steven C.H. Hoi.

## Training data

CodeT5-large-ntp-py was pretrained on [CodeSearchNet](https://arxiv.org/abs/1909.09436) data in six programming languages (Ruby/JavaScript/Go/Python/Java/PHP) and GCPY (the Python split of [Github Code](https://huggingface.co/datasets/codeparrot/github-code)) data.  See Section 4.1 of the [paper](https://arxiv.org/pdf/2207.01780.pdf) for more details.

## Training procedure

CodeT5-large-ntp-py was first pretrained using Masked Span Prediction (MSP) objective on CodeSearchNet for 150 epochs and on GCPY for 10 epochs, followed by another 10 epochs on GCPY using Next Token Prediction (NTP) objective. See Section 4.1 of the [paper](https://arxiv.org/pdf/2207.01780.pdf) for more details.


## Evaluation results
We evaluated this checkpoint on [APPS](https://github.com/hendrycks/apps) benchmark. See Table 5 of the [paper](https://arxiv.org/pdf/2207.01780.pdf) for more details.


## How to use

This model can be easily loaded using the `T5ForConditionalGeneration` functionality:

```python
from transformers import AutoTokenizer, T5ForConditionalGeneration
tokenizer = AutoTokenizer.from_pretrained("Salesforce/codet5-large-ntp-py")
model = T5ForConditionalGeneration.from_pretrained("Salesforce/codet5-large-ntp-py")
text = "def hello_world():"
input_ids = tokenizer(text, return_tensors="pt").input_ids

# simply generate a single sequence
generated_ids = model.generate(input_ids, max_length=128)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
```

## BibTeX entry and citation info

```bibtex
@inproceedings{CodeT52021,
  author    = {Yue Wang and Weishi Wang and Shafiq R. Joty and Steven C. H. Hoi},
  title     = {CodeT5: Identifier-aware Unified Pre-trained Encoder-Decoder Models for Code Understanding and Generation},
  booktitle = {EMNLP},
  pages     = {8696--8708},
  publisher = {Association for Computational Linguistics},
  year      = {2021}
}

@article{CodeRL2022
  author    = {Hung Le, Yue Wang, Akhilesh Deepak Gotmare, Silvio Savarese, Steven C.H. Hoi},
  title     = {CodeRL: Mastering Code Generation through Pretrained Models and Deep Reinforcement Learning},
  journal   = {arXiv preprint},
  volume    = {abs/2207.01780},
  year      = {2022}
}
```