---
language: 
- en
widget:
- text: Tesla range
- text: Nissan Leaf is
- text: Tesla is
- text: The best electric car
---

# Neo-GPT-Title-Generation-Electric-Car

Title generator based on Neo-GPT 125M fine-tuned on a dataset of 39k url's title. All urls are selected on the TOP 10 google on a list of Keywords about "Electric car" - "Electric car for sale".

# Pipeline example

```python
import pandas as pd
from transformers import AutoModelForMaskedLM
from transformers import GPT2Tokenizer, TrainingArguments, AutoModelForCausalLM, AutoConfig 

model = AutoModelForCausalLM.from_pretrained('Martian/Neo-GPT-Title-Generation-Electric-Car')

tokenizer = GPT2Tokenizer.from_pretrained('Martian/Neo-GPT-Title-Generation-Electric-Car', bos_token='<|startoftext|>',
                                          eos_token='<|endoftext|>', pad_token='<|pad|>')

prompt = "<|startoftext|> Electric car"

input_ids = tokenizer(prompt, return_tensors="pt").input_ids

gen_tokens = model.generate(input_ids, do_sample=True, top_k=100, min_length = 30, max_length=150, top_p=0.90, num_return_sequences=20, skip_special_tokens=True)

list_title_gen = []

for i, sample_output in enumerate(gen_tokens):
    title = tokenizer.decode(sample_output, skip_special_tokens=True)
    list_title_gen.append(title)
    
for i in list_title_gen:
    try:
        list_title_gen[list_title_gen.index(i)] = i.split(' | ')[0]       
    except:
        continue
    try:
        list_title_gen[list_title_gen.index(i)] = i.split(' - ')[0]
    except:
        continue
    try:
        list_title_gen[list_title_gen.index(i)] = i.split(' — ')[0]
    except:
        continue        

list_title_gen = [sub.replace('�', ' ').replace('\\r',' ').replace('\
',' ').replace('\\t', ' ').replace('\\xa0', '') for sub in list_title_gen]    
list_title_gen = [sub if sub != '<|startoftext|> Electric car' else '' for sub in list_title_gen]  

for i in list_title_gen:
    print(i)

```

# Todo
- Improve the quality of the training sample
- Add more data

