This model corresponds to **tapas_masklm_base_reset** of the [original repository](https://github.com/google-research/tapas).

Here's how you can use it:

```python
from transformers import TapasTokenizer, TapasForMaskedLM
import pandas as pd
import torch

tokenizer = TapasTokenizer.from_pretrained("google/tapas-base-masklm")
model = TapasForMaskedLM.from_pretrained("google/tapas-base-masklm")

data = {'Actors': ["Brad Pitt", "Leonardo Di Caprio", "George Clooney"],
        'Age': ["56", "45", "59"],
        'Number of movies': ["87", "53", "69"]
}
table = pd.DataFrame.from_dict(data)
query = "How many movies has Leonardo [MASK] Caprio played in?"

# prepare inputs
inputs = tokenizer(table=table, queries=query, padding="max_length", return_tensors="pt")

# forward pass
outputs = model(**inputs)

# return top 5 values and predictions
masked_index = torch.nonzero(inputs.input_ids.squeeze() == tokenizer.mask_token_id, as_tuple=False)
logits = outputs.logits[0, masked_index.item(), :]
probs = logits.softmax(dim=0)
values, predictions = probs.topk(5)

for value, pred in zip(values, predictions):
  print(f"{tokenizer.decode([pred])} with confidence {value}")
```