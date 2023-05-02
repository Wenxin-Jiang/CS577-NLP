Create README.md
## ByT5 Base Portuguese Product Reviews

#### Model Description
This is a finetuned version from ByT5 Base by Google for Sentimental Analysis from Product Reviews in Portuguese.
##### Paper: https://arxiv.org/abs/2105.13626

#### Training data
It was trained from products reviews from a Americanas.com. You can found the data here: https://github.com/HeyLucasLeao/finetuning-byt5-model.

#### Training Procedure
It was finetuned using the Trainer Class available on the Hugging Face library. For evaluation it was used accuracy, precision, recall and f1 score.

##### Learning Rate: **1e-4**
##### Epochs: **1**
##### Colab for Finetuning: https://drive.google.com/file/d/17TcaN52moq7i7TE2EbcVbwQEQuAIQU63/view?usp=sharing
##### Colab for Metrics: https://colab.research.google.com/drive/1wbTDfOsE45UL8Q3ZD1_FTUmdVOKCcJFf#scrollTo=S4nuLkAFrlZ6
#### Score:
```python
Training Set:
'accuracy': 0.9019706922688226,
 'f1': 0.9305820610687022,
 'precision': 0.9596555965559656,
 'recall': 0.9032183375781431
Test Set:
'accuracy': 0.9019409684035312,
 'f1': 0.9303758732034697,
 'precision': 0.9006660401258529,
 'recall': 0.9621126145787866

Validation Set:
'accuracy': 0.9044948078526491,
 'f1': 0.9321924443009364,
 'precision': 0.9024426549173129,
 'recall': 0.9639705531617191
```

#### Goals

My true intention was totally educational, thus making available a this version of the model as a example for future proposes.

How to use
``` python
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
print(device)

tokenizer = AutoTokenizer.from_pretrained("HeyLucasLeao/byt5-base-pt-product-reviews")
model = AutoModelForSeq2SeqLM.from_pretrained("HeyLucasLeao/byt5-base-pt-product-reviews")
model.to(device)

def classificar_review(review):
  inputs = tokenizer([review], padding='max_length', truncation=True, max_length=512, return_tensors='pt')
  input_ids = inputs.input_ids.to(device)
  attention_mask = inputs.attention_mask.to(device)
  output = model.generate(input_ids, attention_mask=attention_mask)
  pred = np.argmax(output.cpu(), axis=1)
  dici = {0: 'Review Negativo', 1: 'Review Positivo'}
  return dici[pred.item()]
  
classificar_review(review)
```