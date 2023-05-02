---
language: 
- en
- es
- eu
datasets:
- squad
widget:
- text: "When was Florence Nightingale born?"
  context: "Florence Nightingale, known for being the founder of modern nursing, was born in Florence, Italy, in 1820."
  example_title: "English"
- text: "¿Por qué provincias pasa el Tajo?"
  context: "El Tajo es el río más largo de la península ibérica, a la que atraviesa en su parte central, siguiendo un rumbo este-oeste, con una leve inclinación hacia el suroeste, que se acentúa cuando llega a Portugal, donde recibe el nombre de Tejo.

Nace en los montes Universales, en la sierra de Albarracín, sobre la rama occidental del sistema Ibérico y, después de recorrer 1007 km, llega al océano Atlántico en la ciudad de Lisboa. En su desembocadura forma el estuario del mar de la Paja, en el que vierte un caudal medio de 456 m³/s. En sus primeros 816 km atraviesa España, donde discurre por cuatro comunidades autónomas (Aragón, Castilla-La Mancha, Madrid y Extremadura) y un total de seis provincias (Teruel, Guadalajara, Cuenca, Madrid, Toledo y Cáceres)."
  example_title: "Español"
- text: "Zer beste izenak ditu Tartalo?"
  context: "Tartalo euskal mitologiako izaki begibakar artzain erraldoia da. Tartalo izena zenbait euskal hizkeratan herskari-bustidurarekin ahoskatu ohi denez, horrelaxe ere idazten da batzuetan: Ttarttalo. Euskal Herriko zenbait tokitan, Torto edo Anxo ere esaten diote."
  example_title: "Euskara"
---

# ixambert-base-cased finetuned for QA

This is a basic implementation of the multilingual model ["ixambert-base-cased"](https://huggingface.co/ixa-ehu/ixambert-base-cased), fine-tuned on SQuAD v1.1 and an experimental version of SQuAD1.1 in Basque (1/3 size of original SQuAD1.1), that is able to answer basic factual questions in English, Spanish and Basque.

## Overview

* **Language model:** ixambert-base-cased
* **Languages:** English, Spanish and Basque
* **Downstream task:** Extractive QA
* **Training data:** SQuAD v1.1 + experimental SQuAD1.1 in Basque
* **Eval data:** SQuAD v1.1 + experimental SQuAD1.1 in Basque
* **Infrastructure:** 1x GeForce RTX 2080

## Outputs

The model outputs the answer to the question, the start and end positions of the answer in the original context, and a score for the probability for that span of text to be the correct answer. For example:

```python
{'score': 0.9667195081710815, 'start': 101, 'end': 105, 'answer': '1820'}
```

## How to use

```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "MarcBrun/ixambert-finetuned-squad-eu-en"

# To get predictions
context = "Florence Nightingale, known for being the founder of modern nursing, was born in Florence, Italy, in 1820"
question = "When was Florence Nightingale born?"
qa = pipeline("question-answering", model=model_name, tokenizer=model_name)
pred = qa(question=question,context=context)

# To load the model and tokenizer
model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)
```

## Hyperparameters

```
batch_size = 8
n_epochs = 3
learning_rate = 2e-5
optimizer = AdamW
lr_schedule = linear
max_seq_len = 384
doc_stride = 128
``` 