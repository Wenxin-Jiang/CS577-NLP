---
tags:
- flair
- token-classification
- sequence-tagger-model
language: en
datasets:
- conll2003
widget:
- text: "George Washington went to Washington"
---

This is a very small model I use for testing my [ner eval dashboard](https://github.com/helpmefindaname/ner-eval-dashboard)



F1-Score: **48,73** (CoNLL-03)

Predicts 4 tags:

| **tag**                        | **meaning** |
|---------------------------------|-----------|
| PER         | person name | 
| LOC         | location name | 
| ORG         | organization name | 
| MISC         | other name | 

Based on huggingface minimal testing embeddings

---

### Demo: How to use in Flair

Requires: **[Flair](https://github.com/flairNLP/flair/)** (`pip install flair`)

```python
from flair.data import Sentence
from flair.models import SequenceTagger
# load tagger
tagger = SequenceTagger.load("helpmefindaname/mini-sequence-tagger-conll03")
# make example sentence
sentence = Sentence("George Washington went to Washington")
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
Span [1,2]: "George Washington"   [− Labels: PER (1.0)]
Span [5]: "Washington"   [− Labels: LOC (1.0)]
```

So, the entities "*George Washington*" (labeled as a **person**) and "*Washington*" (labeled as a **location**) are found in the sentence "*George Washington went to Washington*". 


---

### Training: Script to train this model

The following command was used to train this model: 
where `examples\ner\run_ner.py` refers to [this script](https://github.com/flairNLP/flair/blob/master/examples/ner/run_ner.py)

```
python examples\ner\run_ner.py --model_name_or_path hf-internal-testing/tiny-random-bert --dataset_name CONLL_03 --learning_rate 0.002 --mini_batch_chunk_size 1024 --batch_size 64 --num_epochs 100
```



---