## German NER Albert Model For Token Classification

This is a trained Albert model for Token Classification in German ,[Germeval](https://sites.google.com/site/germeval2014ner/) and can be used for Inference.


## Model Specifications

- MAX_LENGTH=128
- MODEL='albert-base-v1'
- BATCH_SIZE=32
- NUM_EPOCHS=3
- SAVE_STEPS=750
- SEED=1
- SAVE_STEPS = 100 
- LOGGING_STEPS = 100 
- SEED = 42 



### Usage Specifications

This model is trained on Tensorflow version and is compatible with the 'ner' pipeline of huggingface.

```python
from transformers import AutoTokenizer,TFAutoModelForTokenClassification
from transformers import pipeline

model=TFAutoModelForTokenClassification.from_pretrained('abhilash1910/albert-german-ner')
tokenizer=AutoTokenizer.from_pretrained('abhilash1910/albert-german-ner')
ner_model = pipeline('ner', model=model, tokenizer=tokenizer)
seq='Berlin ist die Hauptstadt von Deutschland'
ner_model(seq)
```

The Tensorflow version of Albert is used for training the model and the output for the above mentioned segment is as follows:

```
[{'entity': 'B-PERderiv',
  'index': 1,
  'score': 0.09580112248659134,
  'word': '▁berlin'},
 {'entity': 'B-ORGpart',
  'index': 2,
  'score': 0.08364498615264893,
  'word': '▁is'},
 {'entity': 'B-LOCderiv',
  'index': 3,
  'score': 0.07593920826911926,
  'word': 't'},
 {'entity': 'B-PERderiv',
  'index': 4,
  'score': 0.09574996680021286,
  'word': '▁die'},
 {'entity': 'B-LOCderiv',
  'index': 5,
  'score': 0.07097965478897095,
  'word': '▁'},
 {'entity': 'B-PERderiv',
  'index': 6,
  'score': 0.07122448086738586,
  'word': 'haupt'},
 {'entity': 'B-PERderiv',
  'index': 7,
  'score': 0.12397754937410355,
  'word': 'stadt'},
 {'entity': 'I-OTHderiv',
  'index': 8,
  'score': 0.0818650871515274,
  'word': '▁von'},
 {'entity': 'I-LOCderiv',
  'index': 9,
  'score': 0.08271490037441254,
  'word': '▁'},
 {'entity': 'B-LOCderiv',
  'index': 10,
  'score': 0.08616268634796143,
  'word': 'deutschland'}]
  ```

## Resources

For all resources , please look into [huggingface](https://huggingface.com).


---
language:
- de
tags:
- Token Classification
license: apache-2.0
datasets:
- germeval_14
---
