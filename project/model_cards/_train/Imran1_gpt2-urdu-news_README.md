---

language: 
    - "ur"
license: "mit"
datasets:
   - "Urdu-news-dataset"
   
---


# GPT-2
Fine tune gpt2 model on Urdu news dataset using a causal language modeling (CLM) objective.

### How to use

You can use this model directly with a pipeline for text generation. Since the generation relies on some randomness, we
set a seed for reproducibility:

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("Imran1/gpt2-urdu-news")

model = AutoModelForCausalLM.from_pretrained("Imran1/gpt2-urdu-news")
```
## Training data
I fine tune gpt2 for downstream task like text generation, only for 1000 sample so it may not be good. Due to resources limitation.


## Evaluation results
training loss 3.042 
