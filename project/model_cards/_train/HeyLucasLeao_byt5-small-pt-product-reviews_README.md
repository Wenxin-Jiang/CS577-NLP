Create README.md
## ByT5 Small Portuguese Product Reviews

#### Model Description
This is a finetuned version from ByT5 Small by Google for Sentimental Analysis from Product Reviews in Portuguese.
##### Paper: https://arxiv.org/abs/2105.13626

#### Training data
It was trained from products reviews from a Americanas.com. You can found the data here: https://github.com/HeyLucasLeao/finetuning-byt5-model.

#### Training Procedure
It was finetuned using the Trainer Class available on the Hugging Face library. For evaluation it was used accuracy, precision, recall and f1 score.

##### Learning Rate: **1e-4**
##### Epochs: **1**
##### Colab for Finetuning: https://colab.research.google.com/drive/1EChTeQkGeXi_52lClBNazHVuSNKEHN2f
##### Colab for Metrics: https://colab.research.google.com/drive/1o4tcsP3lpr1TobtE3Txhp9fllxPWXxlw#scrollTo=PXAoog5vQaTn
#### Score:
```python
Training Set:
'accuracy': 0.8974239585927603,
 'f1': 0.927229848590765,
 'precision': 0.9580290812115055,
 'recall': 0.8983492356469835
Test Set:
'accuracy': 0.8957881282882026,
 'f1': 0.9261366030421776,
 'precision': 0.9559431131213848,
 'recall': 0.8981326359661668

Validation Set:
'accuracy': 0.8925383190163382,
 'f1': 0.9239208204149773,
 'precision': 0.9525448733710351,
 'recall': 0.8969668904839083
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

tokenizer = AutoTokenizer.from_pretrained("HeyLucasLeao/byt5-small-pt-product-reviews")
model = AutoModelForSeq2SeqLM.from_pretrained("HeyLucasLeao/byt5-small-pt-product-reviews")
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