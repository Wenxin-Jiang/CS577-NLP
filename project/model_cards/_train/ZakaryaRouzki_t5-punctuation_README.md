---
language: 
  - "fr"
tags:
- t5
- french
- punctuation
license: apache-2.0
datasets:
- orange_sum
- mlsum
---

# 🚀 Text Punctuator Based on Transformers model T5.
T5 model fine-tuned for punctuation restoration.
Model currently supports only French Language. More language supports will be added later using mT5.

Train Datasets : 
Model trained using 2 french datasets (around 500k records): 
- [orange_sum](https://huggingface.co/datasets/orange_sum) 
- [mlsum](https://huggingface.co/datasets/mlsum) (only french text)


More info will be added later.

## 🚀 Usage
**TextPunctuator as a wrapper of the model.**
1. Install the package.
```bash
pip install TextPunctuator
```
2. Simple example
```python
from Punctuator import TextPunctuator
punctuator = TextPunctuator(use_gpu=False)
# text input
text = "Sur la base de ces échanges Blake Lemoine a donc jugé que le système avait atteint \
        un niveau de conscience lui permettant d'être sensible Ce dernier a ensuite envoyé \
        par email un rapport sur la sensibilité supposée de LaMDA à deux cents employés de \
        Google Très vite les dirigeants de l’entreprise ont rejeté les allégations"
text_punctuated = punctuator.punctuate(text, lang='fr')
text_punctuated
# output : 
""" Sur la base de ces échanges, Blake Lemoine a donc jugé que le système avait atteint un niveau de 
conscience lui permettant d’être sensible. Ce dernier a ensuite envoyé par email un rapport sur  
la sensibilité supposée de LaMDA à deux cents employés de Google. Très vite, les dirigeants de 
l’entreprise ont rejeté les allégations. """
```

## ☕ Contact 
Contact [Zakarya ROUZKI ](mailto:zakaryarouzki@gmail.com) or at [Linkedin](https://linkedin.com/in/rouzki).
