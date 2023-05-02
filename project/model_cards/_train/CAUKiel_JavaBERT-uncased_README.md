---
language:
  - java
  - code
license: apache-2.0
widget:
  - text: 'public [MASK] isOdd(Integer num){if (num % 2 == 0) {return "even";} else {return "odd";}}'
---
## JavaBERT
A BERT-like model pretrained on Java software code.

### Training Data
The model was trained on 2,998,345 Java files retrieved from open source projects on GitHub. A ```bert-base-uncased``` tokenizer is used by this model.

### Training Objective
A MLM (Masked Language Model) objective was used to train this model.

### Usage
```python
from transformers import pipeline
pipe = pipeline('fill-mask', model='CAUKiel/JavaBERT')
output = pipe(CODE) # Replace with Java code; Use '[MASK]' to mask tokens/words in the code.
```