---
language: en
tags:
- qa
- classification
- question
- answering
- SQuAD
- metric
- nlg
- t5-small
license: mit
datasets:
- squad
- cnndm
model-index:
- name: t5-weighter_cnndm-en
  results:
  - task:
      name: Classification
      type: Question Weighter
widget:
   - text: "a Buckingham Palace guard </s> Who felt on a manhole? </s> This is the embarrassing moment a Buckingham Palace guard slipped and fell on a manhole cover in front of hundreds of shocked tourists as he took up position in his sentry box. [...] The Guard comprises two detachments, one each for Buckingham Palace and St James’s Palace, under the command of the Captain of The Queen’s Guard."
---
# t5-weighter_cnndm-en

## Model description
This model is a *Classifier* model based on T5-small, that predicts if a answer / question couple is considered as important fact or not (Is this answer enough relevant to appear in a plausible summary?).
It is actually a component of [QuestEval](https://github.com/ThomasScialom/QuestEval) metric but can be used independently as it is.


## How to use
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("ThomasNLG/t5-weighter_cnndm-en")

model = T5ForConditionalGeneration.from_pretrained("ThomasNLG/t5-weighter_cnndm-en")
```

You can play with the model using the inference API, the text input format should follow this template (accordingly to the training stage of the model):

`text_input = "{ANSWER} </s> {QUESTION} </s> {CONTEXT}"`

## Training data
The model was trained on synthetic data as described in [Questeval: Summarization asks for fact-based evaluation](https://arxiv.org/abs/2103.12693).

### Citation info

```bibtex
@article{scialom2021questeval,
  title={Questeval: Summarization asks for fact-based evaluation},
  author={Scialom, Thomas and Dray, Paul-Alexis and Gallinari, Patrick and Lamprier, Sylvain and Piwowarski, Benjamin and Staiano, Jacopo and Wang, Alex},
  journal={arXiv preprint arXiv:2103.12693},
  year={2021}
}
```