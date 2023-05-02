---
language: en
tags:
- qa
- question
- generation
- SQuAD
- data2text
- metric
- nlg
- t5-small
license: mit
datasets:
- squad_v2
model-index:
- name: t5-qg_webnlg_synth-en
  results:
  - task:
      name: Data Question Generation
      type: Text To Text Generation
widget:
   - text: "The Eagle </s> name [ The Eagle ] , eatType [ coffee shop ] , food [ French ] , priceRange [ Â£ 2 0 - 2 5 ]"
---
# t5-qg_webnlg_synth-en

## Model description
This model is a *Data Question Generation* model based on T5-small, that generates questions, given a structured table as input and the conditioned answer. 
It is actually a component of [QuestEval](https://github.com/ThomasScialom/QuestEval) metric but can be used independently as it is, for QG only.


## How to use
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

tokenizer = T5Tokenizer.from_pretrained("ThomasNLG/t5-qg_webnlg_synth-en")

model = T5ForConditionalGeneration.from_pretrained("ThomasNLG/t5-qg_webnlg_synth-en")
```

You can play with the model using the inference API, the text input format should follow this template (accordingly to the training stage of the model):

`text_input = "{ANSWER} </s> {CONTEXT}"`

where `CONTEXT is a structured table that is linearised this way:

`CONTEXT = "name [ The Eagle ] , eatType [ coffee shop ] , food [ French ] , priceRange [ Â£ 2 0 - 2 5 ]"`


## Training data
The model was trained on synthetic data as described in [Data-QuestEval: A Referenceless Metric for Data to Text Semantic Evaluation](https://arxiv.org/abs/2104.07555).

### Citation info

```bibtex
@article{rebuffel2021data,
  title={Data-QuestEval: A Referenceless Metric for Data to Text Semantic Evaluation},
  author={Rebuffel, Cl{\'e}ment and Scialom, Thomas and Soulier, Laure and Piwowarski, Benjamin and Lamprier, Sylvain and Staiano, Jacopo and Scoutheeten, Geoffrey and Gallinari, Patrick},
  journal={arXiv preprint arXiv:2104.07555},
  year={2021}
}
```