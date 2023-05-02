
---
language: bn
tags:
- collaborative
- bengali
- NER
license: apache-2.0
datasets: xtreme 
metrics:
- Loss
- Accuracy
- Precision
- Recall
---

# sahajBERT Named Entity Recognition

## Model description

[sahajBERT](https://huggingface.co/neuropark/sahajBERT-NER) fine-tuned for NER using the bengali split of [WikiANN ](https://huggingface.co/datasets/wikiann). 

Named Entities predicted by the model:

| Label id | Label |
|:--------:|:----:|
|0 |O|
|1 |B-PER|
|2 |I-PER|
|3 |B-ORG|
|4 |I-ORG|
|5 |B-LOC|
|6 |I-LOC|

## Intended uses & limitations

#### How to use

You can use this model directly with a pipeline for masked language modeling:
```python
from transformers import AlbertForTokenClassification, TokenClassificationPipeline, PreTrainedTokenizerFast

# Initialize tokenizer
tokenizer = PreTrainedTokenizerFast.from_pretrained("neuropark/sahajBERT-NER")

# Initialize model
model = AlbertForTokenClassification.from_pretrained("neuropark/sahajBERT-NER")

# Initialize pipeline
pipeline = TokenClassificationPipeline(tokenizer=tokenizer, model=model)

raw_text = "এই ইউনিয়নে ৩ টি মৌজা ও ১০ টি গ্রাম আছে ।" # Change me
output = pipeline(raw_text)
```

#### Limitations and bias

<!-- Provide examples of latent issues and potential remediations. -->
WIP

## Training data

The model was initialized it with pre-trained weights of [sahajBERT](https://huggingface.co/neuropark/sahajBERT-NER) at step 19519 and trained on the bengali of [WikiANN ](https://huggingface.co/datasets/wikiann)

## Training procedure

Coming soon! 
<!-- ```bibtex
@inproceedings{...,
  year={2020}
}
``` -->

## Eval results


loss: 0.11714419722557068

accuracy: 0.9772286821705426

precision: 0.9585365853658536

recall: 0.9651277013752456

f1 : 0.9618208516886931


### BibTeX entry and citation info

Coming soon! 
<!-- ```bibtex
@inproceedings{...,
  year={2020}
}
``` -->
