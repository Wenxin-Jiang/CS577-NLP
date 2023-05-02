---
language: en
tags:
- qa
- question 
- answering
- SQuAD
- metric
- nlg
- t5-small
license: mit
datasets:
- squad_v2
model-index:
- name: t5-qa_squad2neg-en
  results:
  - task: 
      name: Question Answering
      type: extractive-qa
widget:
   - text: "Who was Louis 14? </s> Louis 14 was a French King."
---
# t5-qa_squad2neg-en

## Model description
This model is a *Question Answering* model based on T5-small. 
It is actually a component of [QuestEval](https://github.com/ThomasScialom/QuestEval) metric but can be used independently as it is, for QA only.


## How to use
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("ThomasNLG/t5-qa_squad2neg-en")

model = T5ForConditionalGeneration.from_pretrained("ThomasNLG/t5-qa_squad2neg-en")
```

You can play with the model using the inference API, the text input format should follow this template (accordingly to the training stage of the model):

`text_input = "{QUESTION} </s> {CONTEXT}"`

## Training data
The model was trained on: 
- SQuAD-v2
- SQuAD-v2 neg: in addition to the training data of SQuAD-v2, for each answerable example, a negative sampled example has been added with the label *unanswerable*  to help the model learning when the question is not answerable given the context. For more details, see the [paper](https://arxiv.org/abs/2103.12693).


### Citation info

```bibtex
@article{scialom2020QuestEval,
  title={QuestEval: Summarization Asks for Fact-based Evaluation},
  author={Scialom, Thomas and Dray, Paul-Alexis and Gallinari, Patrick and Lamprier, Sylvain and Piwowarski, Benjamin and Staiano, Jacopo and Wang, Alex},
  journal={arXiv preprint arXiv:2103.12693},
  year={2021}
}
```
