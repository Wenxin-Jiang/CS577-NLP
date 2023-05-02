---
language: en
tags:
- qg
- question
- generation
- SQuAD
- metric
- nlg
- t5-small
license: mit
datasets:
- squad
model-index:
- name: t5-qg_squad1-en
  results:
  - task: 
      name: Question Generation
      type: Text2Text-Generation
widget:
   - text: "sv1 </s> Louis 14 </s> Louis 14 was a French King."
---
# t5-qg_squad1-en

## Model description
This model is a *Question Generation* model based on T5-small.
It is actually a component of [QuestEval](https://github.com/ThomasScialom/QuestEval) metric but can be used independently as it is, for QG only.


## How to use
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("ThomasNLG/t5-qg_squad1-en")

model = T5ForConditionalGeneration.from_pretrained("ThomasNLG/t5-qg_squad1-en")
```

You can play with the model using the inference API, the text input format should follow this template (accordingly to the training stage of the model):

`text_input = "sv1 </s> {ANSWER} </s> {CONTEXT}"`

## Training data
The model was trained on SQuAD.


### Citation info

```bibtex
@article{scialom2020QuestEval,
  title={QuestEval: Summarization Asks for Fact-based Evaluation},
  author={Scialom, Thomas and Dray, Paul-Alexis and Gallinari, Patrick and Lamprier, Sylvain and Piwowarski, Benjamin and Staiano, Jacopo and Wang, Alex},
  journal={arXiv preprint arXiv:2103.12693},
  year={2021}
}
```