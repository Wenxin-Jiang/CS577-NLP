---

language: en

tags:

- ELI5

license:  	gpl-3.0

datasets:
- eli5

Task: Summarization

widget:
- text: "<|BOS|><|SEP|>Consulting,business,Fraud<|SEP|>"

inference:
  parameters:
    temperature: 0.9
    return_full_text: False
    repetition_penalty: 1
---
# Conditional ELI5 Generator

Given a few keywords, it generates an Eli5 question with a corresponding answer.

The model is mainly used for [SeemsPhishy](https://github.com/madhour/seemsphishy) to auto generate newsletters for phishing/penetration-testing.

# How to use

```Python
from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
from torch import tensor

tokenizer = AutoTokenizer.from_pretrained("Madhour/gpt2-eli5")
model = AutoModelForCausalLM.from_pretrained("Madhour/gpt2-eli5")
prompt = <|BOS|> +"I have a question."+ <|SEP|> + "keyword1,keyword2,keyword3" + <|SEP|>
prompt = tensor(tokenizer.encode(prompt)).unsqueeze(0)
text = model.generate(prompt, 
                            do_sample=True,   
                            min_length=50, 
                            max_length=768,
                            top_k=30,                                 
                            top_p=0.7,        
                            temperature=0.9,
                            repetition_penalty=2.0,
                            num_return_sequences=3)
```