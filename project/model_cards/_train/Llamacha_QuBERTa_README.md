---
language: 
- qu
tags:
- Llamacha
---


# QuBERTa 

QuBERTa es un modelo de lenguaje basado en RoBERTa para el quechua. Nuestro modelo de lenguaje fue pre-entrenado con 5M de tokens del quechua sureño (Collao y Chanka).

El modelo utiliza un tokenizador Byte-level BPE con un vocabulario de 52000 tokens de subpalabras.

## Usabilidad
Una vez descargado los pesos y el tokenizador es necesario adjuntarlo en un sola carpeta, en este caso fue `QuBERTa `.

```python
from transformers import pipeline

fill_mask = pipeline(
    "fill-mask",
    model="./QuBERTa",
    tokenizer="./QuBERTa"
)
```
Se hace la prueba, la cual esta en fases de mejoras.

```python
fill_mask("allinllachu <mask> allinlla huk wasipita.")
```
    [{'score': 0.23992203176021576,
     'sequence': 'allinllachu nisqaqa allinlla huk wasipita.',
     'token': 334,
     'token_str': ' nisqaqa'},
    {'score': 0.061005301773548126,
     'sequence': 'allinllachu, allinlla huk wasipita.',
     'token': 16,
     'token_str': ','},
     {'score': 0.028720015659928322,
     'sequence': "allinllachu' allinlla huk wasipita.",
     'token': 11,
     'token_str': "'"},
    {'score': 0.012927944771945477,
    'sequence': 'allinllachu kay allinlla huk wasipita.',
    'token': 377,
    'token_str': ' kay'},
    {'score': 0.01230092253535986,
    'sequence': 'allinllachu. allinlla huk wasipita.',
     'token': 18,
    'token_str': '.'}]
