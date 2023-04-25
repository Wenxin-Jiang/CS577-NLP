## BLEURT

Pytorch version of the original BLEURT models from ACL paper ["BLEURT: Learning Robust Metrics for Text Generation"](https://aclanthology.org/2020.acl-main.704/) by 
Thibault Sellam, Dipanjan Das and Ankur P. Parikh of Google Research.

The code for model conversion was originated from [this notebook](https://colab.research.google.com/drive/1KsCUkFW45d5_ROSv2aHtXgeBa2Z98r03?usp=sharing) mentioned [here](https://github.com/huggingface/datasets/issues/224).

## Usage Example

```python
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

tokenizer = AutoTokenizer.from_pretrained("Elron/bleurt-large-512")
model = AutoModelForSequenceClassification.from_pretrained("Elron/bleurt-large-512")
model.eval()

references = ["hello world", "hello world"]
candidates = ["hi universe", "bye world"]

with torch.no_grad():
  scores = model(**tokenizer(references, candidates, return_tensors='pt'))[0].squeeze()
print(scores) # tensor([0.9877, 0.0475])
```
