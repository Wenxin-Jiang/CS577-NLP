---
license: mit
tags:
- flair
- token-classification
- sequence-tagger-model
language: "pt"
widget:
- text: "FISIOTERAPIA TRAUMATO - MANHÃ  Henrique Dias, 38 anos. Exercícios metabólicos de extremidades inferiores. Realizo mobilização patelar e leve mobilização de flexão de joelho conforme liberado pelo Dr Marcelo Arocha. Oriento cuidados e posicionamentos."
---

## Portuguese Name Identification

The [NoHarm-Anony - De-Identification of Clinical Notes Using Contextualized Language Models and a Token Classifier](https://link.springer.com/chapter/10.1007/978-3-030-91699-2_3) paper contains Flair-based models for Portuguese Language, initialized with [Flair BBP](https://github.com/jneto04/ner-pt) & trained on clinical notes with names tagged. 

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger
# load tagger
tagger = SequenceTagger.load("noharm-ai/anony")
# make example sentence
sentence = Sentence("FISIOTERAPIA TRAUMATO - MANHÃ  Henrique Dias, 38 anos. Exercícios metabólicos de extremidades inferiores. Realizo mobilização patelar e leve mobilização de flexão de joelho conforme liberado pelo Dr Marcelo Arocha. Oriento cuidados e posicionamentos.")
# predict NER tags
tagger.predict(sentence)
# print sentence
print(sentence)
# print predicted NER spans
print('The following NER tags are found:')
# iterate over entities and print
for entity in sentence.get_spans('ner'):
    print(entity)
```

This yields the following output:
```
Span [5,6]: "Henrique Dias"   [− Labels: NOME (0.9735)]
Span [31,32]: "Marcelo Arocha"   [− Labels: NOME (0.9803)]
```

So, the entities "*Henrique Dias*" (labeled as a **nome**) and "*Marcelo Arocha*" (labeled as a **nome**) are found in the sentence. 



## More Information

Refer to the original paper, [De-Identification of Clinical Notes Using Contextualized Language Models and a Token Classifier](https://link.springer.com/chapter/10.1007/978-3-030-91699-2_3) for additional details and performance.

## Acknowledgements

We thank Dr. Ana Helena D. P. S. Ulbrich, who provided the clinical notes dataset from the hospital, for her valuable cooperation. We also thank the volunteers of the Institute of Artificial Intelligence in Healthcare Celso Pereira and Ana Lúcia Dias, for the dataset annotation.

## Citation

```
@inproceedings{santos2021identification,
  title={De-Identification of Clinical Notes Using Contextualized Language Models and a Token Classifier},
  author={Santos, Joaquim and dos Santos, Henrique DP and Tabalipa, F{\'a}bio and Vieira, Renata},
  booktitle={Brazilian Conference on Intelligent Systems},
  pages={33--41},
  year={2021},
  organization={Springer}
}
```