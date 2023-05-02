---
language: ko
tags:
- bert
- mrc
datasets:
- klue
license: cc-by-sa-4.0
---

# bert-base for QA 

**Code:**  See [Ainize Workspace](https://link.ainize.ai/3FjvBVn) 

**klue-bert-base-mrc DEMO**: [Ainize DEMO](https://main-klue-mrc-bert-scy6500.endpoint.ainize.ai/)

**klue-bert-base-mrc API**: [Ainize API](https://ainize.ai/scy6500/KLUE-MRC-BERT?branch=main)

## Overview
**Language model:** klue/bert-base  
**Language:** Korean  
**Downstream-task:** Extractive QA    
**Training data:** KLUE-MRC  
**Eval data:** KLUE-MRC  
 


## Usage
### In Transformers
```python
from transformers import AutoModelForQuestionAnswering, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("ainize/klue-bert-base-mrc")
model = AutoModelForQuestionAnswering.from_pretrained("ainize/klue-bert-base-mrc")

context = "your context"
question = "your question"

encodings = tokenizer(context, question, max_length=512, truncation=True,
                      padding="max_length", return_token_type_ids=False)
encodings = {key: torch.tensor([val]) for key, val in encodings.items()}             

input_ids = encodings["input_ids"]
attention_mask = encodings["attention_mask"]

pred = model(input_ids, attention_mask=attention_mask)

start_logits, end_logits = pred.start_logits, pred.end_logits

token_start_index, token_end_index = start_logits.argmax(dim=-1), end_logits.argmax(dim=-1)

pred_ids = input_ids[0][token_start_index: token_end_index + 1]

prediction = tokenizer.decode(pred_ids)
```

## About us
[Teachable NLP](https://ainize.ai/teachable-nlp) - Train NLP models with your own text without writing any code  
[Ainize](https://ainize.ai/) - Deploy ML project using free gpu
