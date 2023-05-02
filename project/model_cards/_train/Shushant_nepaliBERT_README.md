---
license: mit
datasets:
- Shushant/nepali
language:
- ne
metrics:
- perplexity
library_name: transformers
pipeline_tag: fill-mask
---
# NEPALI BERT
## Masked Language Model for nepali language trained on nepali news scrapped from different nepali news website. The data set contained about 10 million of nepali sentences mainly related to nepali news.

This model is a fine-tuned version of [Bert Base Uncased](https://huggingface.co/bert-base-uncased) on dataset composed of different news scrapped from nepali news portals comprising of 4.6 GB of textual data.
It achieves the following results on the evaluation set:
- Loss: 1.0495

## Model description

Pretraining done on bert base architecture. 

## Intended uses & limitations
This transformer model can be used for any NLP tasks related to Devenagari language. At the time of training, this is the state of the art model developed 
for Devanagari dataset. Intrinsic evaluation with Perplexity of 8.56 achieves this state of the art whereas extrinsit evaluation done on sentiment analysis of Nepali tweets outperformed other existing 
masked language models on Nepali dataset. 
## Training and evaluation data
THe training corpus is developed using 85467 news scrapped from different job portals. This is a preliminary dataset 
for the experimentation. THe corpus size is about 4.3 GB of textual data. Similary evaluation data contains few news articles about 12 mb of textual data.

## Training procedure
For the pretraining of masked language model, Trainer API from Huggingface is used. The pretraining took about 3 days 8 hours 57 minutes. Training was done on Tesla V100 GPU. 
With 640 Tensor Cores, Tesla V100 is the world's first GPU to break the 100 teraFLOPS (TFLOPS) barrier of deep learning performance. This GPU was faciliated by Kathmandu University (KU) supercomputer. 
Thanks to KU administration.

Usage
```
from transformers import AutoTokenizer, AutoModelForMaskedLM
tokenizer = AutoTokenizer.from_pretrained("Shushant/nepaliBERT")
model = AutoModelForMaskedLM.from_pretrained("Shushant/nepaliBERT")

from transformers import pipeline

fill_mask = pipeline( "fill-mask", model=model, tokenizer=tokenizer, ) 
from pprint import pprint pprint(fill_mask(f"तिमीलाई कस्तो {tokenizer.mask_token}."))
```

## Data Description
Trained on about 4.6 GB of Nepali text corpus collected from various sources
These data were collected from nepali news site, OSCAR nepali corpus