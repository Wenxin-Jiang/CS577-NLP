---
license: mit
---

This model has been first pretrained on the BEIR corpus and fine-tuned on MS MARCO dataset following the approach described in the paper **COCO-DR: Combating Distribution Shifts in Zero-Shot Dense Retrieval with Contrastive and Distributionally Robust Learning**. The associated GitHub repository is available here https://github.com/OpenMatch/COCO-DR.

This model is trained with BERT-base as the backbone with 110M hyperparameters.


## Usage

Pre-trained models can be loaded through the HuggingFace transformers library:

```python
from transformers import AutoModel, AutoTokenizer

model = AutoModel.from_pretrained("OpenMatch/cocodr-base-msmarco") 
tokenizer = AutoTokenizer.from_pretrained("OpenMatch/cocodr-base-msmarco") 
```

Then embeddings for different sentences can be obtained by doing the following:

```python

sentences = [
    "Where was Marie Curie born?",
    "Maria Sklodowska, later known as Marie Curie, was born on November 7, 1867.",
    "Born in Paris on 15 May 1859, Pierre Curie was the son of Eugène Curie, a doctor of French Catholic origin from Alsace."
]

inputs = tokenizer(sentences, padding=True, truncation=True, return_tensors="pt")
embeddings = model(**inputs, output_hidden_states=True, return_dict=True).hidden_states[-1][:, :1].squeeze(1) # the embedding of the [CLS] token after the final layer
```

Then similarity scores between the different sentences are obtained with a dot product between the embeddings:
```python

score01 = embeddings[0] @ embeddings[1] # 216.9792
score02 = embeddings[0] @ embeddings[2] # 216.6684
```


