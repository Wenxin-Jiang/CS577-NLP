---
language: 
  - en
thumbnail: "url to a thumbnail used in social sharing"
tags:
- hupd
- roberta
- distilroberta
- patents
license: cc-by-sa-4.0
datasets:
- HUPD/hupd
---

# HUPD DistilRoBERTa-Base Model

This HUPD DistilRoBERTa model was fine-tuned on the HUPD dataset with a masked language modeling objective. It was originally introduced in [this paper](TBD). 

For more information about the Harvard USPTO Patent Dataset, please feel free to visit the [project website](https://patentdataset.org/) or the [project's GitHub repository](https://github.com/suzgunmirac/hupd).


### How to Use

You can use this model directly with a pipeline for masked language modeling:

```python
from transformers import pipeline
model = pipeline(task="fill-mask", model="hupd/hupd-distilroberta-base")
model("Improved <mask> for playing a game of thumb wrestling.")
```

Here is the output:
```python
[{'score': 0.4274042248725891,
  'sequence': 'Improved method for playing a game of thumb wrestling.',
  'token': 5448,
  'token_str': ' method'},
 {'score': 0.06967400759458542,
  'sequence': 'Improved system for playing a game of thumb wrestling.',
  'token': 467,
  'token_str': ' system'},
 {'score': 0.06849079579114914,
  'sequence': 'Improved device for playing a game of thumb wrestling.',
  'token': 2187,
  'token_str': ' device'},
 {'score': 0.04544765502214432,
  'sequence': 'Improved apparatus for playing a game of thumb wrestling.',
  'token': 26529,
  'token_str': ' apparatus'},
 {'score': 0.025765646249055862,
  'sequence': 'Improved means for playing a game of thumb wrestling.',
  'token': 839,
  'token_str': ' means'}]
```

Alternatively, you can load the model and use it as follows:

```python
import torch
from transformers import AutoTokenizer, AutoModelForMaskedLM

# cuda/cpu
device = 'cuda' if torch.cuda.is_available() else 'cpu'

tokenizer = AutoTokenizer.from_pretrained("hupd/hupd-distilroberta-base")
model = AutoModelForMaskedLM.from_pretrained("hupd/hupd-distilroberta-base").to(device)

TEXT = "Improved <mask> for playing a game of thumb wrestling."

inputs = tokenizer(TEXT, return_tensors="pt").to(device)

with torch.no_grad():
    logits = model(**inputs).logits

# retrieve indices of <mask>
mask_token_indxs = (inputs.input_ids == tokenizer.mask_token_id)[0].nonzero(as_tuple=True)[0]

for mask_idx in mask_token_indxs:
    predicted_token_id = logits[0, mask_idx].argmax(axis=-1)
    output = tokenizer.decode(predicted_token_id)
    print(f'Prediction for the <mask> token at index {mask_idx}: "{output}"')
```
Here is the output:
```python
Prediction for the <mask> token at index 2: " method"
```

## Citation

For more information, please take a look at the original paper.

* Paper: [The Harvard USPTO Patent Dataset: A Large-Scale, Well-Structured, and Multi-Purpose Corpus of Patent Applications](TBD)

* Authors: *Mirac Suzgun, Luke Melas-Kyriazi, Suproteem K. Sarkar, Scott Duke Kominers, and Stuart M. Shieber* 

* BibTeX:
```
@article{suzgun2022hupd,
  title={The Harvard USPTO Patent Dataset: A Large-Scale, Well-Structured, and Multi-Purpose Corpus of Patent Applications},
  author={Suzgun, Mirac and Melas-Kyriazi, Luke and Sarkar, Suproteem K and Kominers, Scott and Shieber, Stuart},
  year={2022}
}
```