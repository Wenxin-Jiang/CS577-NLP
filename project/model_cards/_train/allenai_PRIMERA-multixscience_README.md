---
language: en
license: apache-2.0
---


HF-version model for PRIMERA: Pyramid-based Masked Sentence Pre-training for Multi-document Summarization (ACL 2022). 

The original code can be found [here](https://github.com/allenai/PRIMER). You can find the script and notebook to train/evaluate the model in the original github repo.

* Note: due to the difference between the implementations of the original Longformer and the Huggingface LED model, the results of converted models are slightly different. We run a sanity check on both fine-tuned and non fine-tuned models on the **MultiNews dataset**, and show the results below:

| Model | Rouge-1 | Rouge-2 | Rouge-L |
| --- | ----------- |----------- |----------- |
| PRIMERA | 42.0 | 13.6 | 20.8| 
| PRIMERA-hf | 41.7 |13.6 | 20.5|
| PRIMERA(finetuned) | 49.9 | 21.1 | 25.9|
| PRIMERA-hf(finetuned) | 49.9 | 20.9 | 25.8|

You can use it by 
```
from transformers import (
    AutoTokenizer,
    LEDConfig,
    LEDForConditionalGeneration,
)
tokenizer = AutoTokenizer.from_pretrained('allenai/PRIMERA')
config=LEDConfig.from_pretrained('allenai/PRIMERA')
model = LEDForConditionalGeneration.from_pretrained('allenai/PRIMERA')
```