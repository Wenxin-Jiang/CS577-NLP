---
tags:
- fastai
- text-generation

language: ml

widget:
- text: "ഓഹരി വിപണി തകരുമ്പോള്‍ നിക്ഷേപം എങ്ങനെ സുരക്ഷിതമാക്കാം"
  example_title: "Malayalam Casual Language Model"

datasets:
- rajeshradhakrishnan/malayalam_wiki

---

# Blurr x Casual Machine Learning Model trained on Malayalam (മലയാളം) text. (Working in Progress)


[![മലയാളം: notebook](https://img.shields.io/badge/മലയാളം%20-notebook-green.svg)](https://nbviewer.org/github/rajeshradhakrishnanmvk/kitchen2.0/blob/main/ml/malayalam_blurr_xlm_roberta_base.ipynb)


---

# malayalam-blurr-xlm-roberta-base (base-sized model)

malayalam-blurr-xlm-roberta-base model is pre-trained on [xlm-roberta-base](https://huggingface.co/xlm-roberta-base) using the library [blurr](https://ohmeow.github.io/blurr/) Language Model using fastai x huggingface frameworks.

Ref: [Causal Language Modeling](https://ohmeow.github.io/blurr/text-modeling-language-modeling.html#Causal-language-modeling). 

## Usage

```
!pip install -Uqq huggingface_hub["fastai"] ohmeow-blurr

from huggingface_hub import from_pretrained_fastai
learner = from_pretrained_fastai(repo_id)

learner.blurr_generate("ബ്‌ളൂർ പഠിക്കാൻ വളെരെ എളുപ്പമാണ് എന്തുകൊണ്ട് എന്നാൽ", max_length=50, do_sample=True, top_k=25)

```

## Intended uses & limitations

It's not fine tuned to the state of the art accuracy

## Training and evaluation data

[Wiki 2020 Malayalam Dataset ](https://huggingface.co/datasets/rajeshradhakrishnan/malayalam_wiki)
