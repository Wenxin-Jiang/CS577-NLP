---
language: pt
license: mit
tags:
- question-answering
- bert
- bert-base
- pytorch
datasets:
- brWaC
- squad
- squad_v1_pt
metrics:
- squad
---

# Portuguese BERT base cased QA (Question Answering), finetuned on SQUAD v1.1

## Introduction

The model was trained on the dataset SQUAD v1.1 in portuguese from the [Deep Learning Brasil group](http://www.deeplearningbrasil.com.br/) on Google Colab. 

The language model used is the [BERTimbau Base](https://huggingface.co/neuralmind/bert-base-portuguese-cased) (aka "bert-base-portuguese-cased") from [Neuralmind.ai](https://neuralmind.ai/): BERTimbau Base is a pretrained BERT model for Brazilian Portuguese that achieves state-of-the-art performances on three downstream NLP tasks: Named Entity Recognition, Sentence Textual Similarity and Recognizing Textual Entailment. It is available in two sizes: Base and Large.

## Informations on the method used

All the informations are in the blog post : [NLP | Modelo de Question Answering em qualquer idioma baseado no BERT base (estudo de caso em português)](https://medium.com/@pierre_guillou/nlp-modelo-de-question-answering-em-qualquer-idioma-baseado-no-bert-base-estudo-de-caso-em-12093d385e78)

## Notebooks in Google Colab & GitHub

- Google Colab: [colab_question_answering_BERT_base_cased_squad_v11_pt.ipynb](https://drive.google.com/file/d/1YkfxAjNkPzOr6hsHc7t7LTv3HYgUCWlX/view?usp=share_link)
- GitHub: [colab_question_answering_BERT_base_cased_squad_v11_pt.ipynb](https://github.com/GuiSales404/QA_system_pt-br)

## Performance

The results obtained are the following:

```
f1 = 79.38
exact match = 67.51
```

## How to use the model... with Pipeline

```python
import transformers
from transformers import pipeline

# source: https://pt.wikipedia.org/wiki/Pandemia_de_COVID-19
context = r"""
A pandemia de COVID-19, também conhecida como pandemia de coronavírus, é uma pandemia em curso de COVID-19, 
uma doença respiratória aguda causada pelo coronavírus da síndrome respiratória aguda grave 2 (SARS-CoV-2). 
A doença foi identificada pela primeira vez em Wuhan, na província de Hubei, República Popular da China, 
em 1 de dezembro de 2019, mas o primeiro caso foi reportado em 31 de dezembro do mesmo ano. 
Acredita-se que o vírus tenha uma origem zoonótica, porque os primeiros casos confirmados 
tinham principalmente ligações ao Mercado Atacadista de Frutos do Mar de Huanan, que também vendia animais vivos. 
Em 11 de março de 2020, a Organização Mundial da Saúde declarou o surto uma pandemia. Até 8 de fevereiro de 2021, 
pelo menos 105 743 102 casos da doença foram confirmados em pelo menos 191 países e territórios, 
com cerca de 2 308 943 mortes e 58 851 440 pessoas curadas.
"""

model_name = 'pierreguillou/bert-base-cased-squad-v1.1-portuguese'
nlp = pipeline("question-answering", model=model_name)

question = "Quando começou a pandemia de Covid-19 no mundo?"

result = nlp(question=question, context=context)

print(f"Answer: '{result['answer']}', score: {round(result['score'], 4)}, start: {result['start']}, end: {result['end']}")

# Answer: '1 de dezembro de 2019', score: 0.713, start: 328, end: 349
```

## How to use the model... with the Auto classes

```python
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
  
tokenizer = AutoTokenizer.from_pretrained("pierreguillou/bert-base-cased-squad-v1.1-portuguese")
model = AutoModelForQuestionAnswering.from_pretrained("pierreguillou/bert-base-cased-squad-v1.1-portuguese")
```             

Or just clone the model repo:

```python
git lfs install
git clone https://huggingface.co/pierreguillou/bert-base-cased-squad-v1.1-portuguese
  
# if you want to clone without large files – just their pointers
# prepend your git clone with the following env var:
  
GIT_LFS_SKIP_SMUDGE=1
```               

## Limitations and bias

The training data used for this model come from Portuguese SQUAD. It could contain a lot of unfiltered content, which is far from neutral, and biases. We're working on ways to improve this by using computational grammars for text data augmentation. 

## Author

Portuguese BERT base cased QA (Question Answering), finetuned on SQUAD v1.1 was trained and evaluated by [Pierre GUILLOU](https://www.linkedin.com/in/pierreguillou/) thanks to the Open Source code, platforms and advices of many organizations ([link to the list](https://medium.com/@pierre_guillou/nlp-modelo-de-question-answering-em-qualquer-idioma-baseado-no-bert-base-estudo-de-caso-em-12093d385e78#c572)). In particular: [Hugging Face](https://huggingface.co/), [Neuralmind.ai](https://neuralmind.ai/), [Deep Learning Brasil group](http://www.deeplearningbrasil.com.br/), [Google Colab](https://colab.research.google.com/) and [AI Lab](https://ailab.unb.br/).

## Citation
This research is running using Pierre Guillou notebooks, all this job is available in [this](https://medium.com/@pierre_guillou/nlp-nas-empresas-como-eu-treinei-um-modelo-t5-em-portugu%C3%AAs-na-tarefa-qa-no-google-colab-e8eb0dc38894) medium article. Thank you !

If you use our work, please cite:

```bibtex
@inproceedings{pierreguillou2021bertbasecasedsquadv11portuguese,
  title={Portuguese BERT base cased QA (Question Answering), finetuned on SQUAD v1.1},
  author={Pierre Guillou},
  year={2021}
}
```