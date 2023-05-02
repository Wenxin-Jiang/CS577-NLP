---
language: 
  - en
tags:
- hupd
- t5
- summarization
- conditional-generation
- patents
license: cc-by-sa-4.0
datasets:
- HUPD/hupd
---

# HUPD T5-Small Summarization Model

This HUPD T5-Small summarization model was fine-tuned on the HUPD dataset. It was originally introduced in [this paper](TBD). 

For more information about the Harvard USPTO Patent Dataset, please feel free to visit the [project website](https://patentdataset.org/) or the [project's GitHub repository](https://github.com/suzgunmirac/hupd).


### How to Use

You can use this model directly with a pipeline for masked language modeling:

```python
from transformers import pipeline
summarizer = pipeline(task="summarization", model="HUPD/hupd-t5-small")

TEXT = "1. An optical coherent receiver for an optical communication network, said optical coherent receiver being configured to receive a modulated optical signal and to process said modulated optical signal for generating an in-phase component and a quadrature component, said in-phase component and said quadrature component being electrical signals, said optical coherent receiver comprising a power adjuster in turn comprising: a multiplying unit configured to multiply said in-phase component by an in-phase gain thereby providing a power-adjusted in-phase component, and to multiply said quadrature component by a quadrature gain thereby providing a power-adjusted quadrature component; and a digital circuit connected between output and input of said multiplying unit and configured to compute: a common gain indicative of a sum of a power of said power-adjusted in-phase component and a power of said power-adjusted quadrature component, and a differential gain indicative of a difference between said power of said power-adjusted in-phase component and said power of said power-adjusted quadrature component; and said in-phase gain as a product between said common gain and said differential gain, and said quadrature gain as a ratio between said common gain and said differential gain. 2. An optical coherent receiver according to claim 1, wherein it further comprises an analog-to-digital unit connected at the input of said power adjuster, said analog-to-digital unit being configured to ..."

summarizer(TEXT)
```

Here is the output:
```python
[{'summary_text': 'An optical coherent receiver for an optical communication network includes a power adjuster and a digital circuit connected between output and input of the multiplying unit and configured to compute a common gain indicative of a sum of the power of an in-phase component and the power-adjusted quadrature component, and the differential gain as a product between the common gain and the diffractive gain.'}]
```

Alternatively, you can load the model and use it as follows:

```python
import torch
from transformers import AutoTokenizer, AutoModelWithLMHead
# cuda/cpu
device = 'cuda' if torch.cuda.is_available() else 'cpu'
tokenizer = AutoTokenizer.from_pretrained("HUPD/hupd-t5-small")
model = AutoModelWithLMHead.from_pretrained("HUPD/hupd-t5-small").to(device)

inputs = tokenizer(TEXT, return_tensors="pt").to(device)

with torch.no_grad():
    outputs = model.generate(inputs.input_ids, max_new_tokens=256)

generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
```

## Citation

For more information, please take a look at the original paper.

* Paper: [The Harvard USPTO Patent Dataset: A Large-Scale, Well-Structured, and Multi-Purpose Corpus of Patent Applications](TBD)

* Authors: *Mirac Suzgun, Luke Melas-Kyriazi, Suproteem K. Sarkar, Scott Duke Kominers, and Stuart M. Shieber* 

* BibTeX:
```
@article{suzgun2022hupd,
  title={The Harvard USPTO Patent Dataset: A Large-Scale, Well-Structured, and Multi-Purpose Corpus of Patent Applications},
  author={Suzgun, Mirac and Melas-Kyriazi, Luke and Sarkar, Suproteem K and Kominers, Scott Duke and Shieber, Stuart M},
  journal={arXiv preprint arXiv:2207.04043},
  year={2022}
}
```