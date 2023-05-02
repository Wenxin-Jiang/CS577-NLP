---
language: ["fr", "de"]
tags:
- feature-extraction
- embeddings
- sentence-similarity
---
# LaBSE for French and German
This is a shortened version of [sentence-transformers/LaBSE](https://huggingface.co/sentence-transformers/LaBSE). The model was prepaired with the direct help of [cointegrated](https://huggingface.co/cointegrated), the author of the [LaBSE-en-ru model](https://huggingface.co/cointegrated/LaBSE-en-ru).

The current model includes only French and German tokens, and the vocabulary is thus 10% of the original while number of parameters in the whole model is 27% of the original.
 
To get the sentence embeddings, you can  use the following code:
```python
import torch
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("EIStakovskii/LaBSE-fr-de")
model = AutoModel.from_pretrained("EIStakovskii/LaBSE-fr-de")
sentences = ["Wie geht es dir?", "Comment vas-tu?"]
encoded_input = tokenizer(sentences, padding=True, truncation=True, max_length=64, return_tensors='pt')
with torch.no_grad():
    model_output = model(**encoded_input)
embeddings = model_output.pooler_output
embeddings = torch.nn.functional.normalize(embeddings)
print(embeddings)
```

## Reference:
Fangxiaoyu Feng, Yinfei Yang, Daniel Cer, Narveen Ari, Wei Wang. [Language-agnostic BERT Sentence Embedding](https://arxiv.org/abs/2007.01852). July 2020

License: [https://tfhub.dev/google/LaBSE/1](https://tfhub.dev/google/LaBSE/1)
