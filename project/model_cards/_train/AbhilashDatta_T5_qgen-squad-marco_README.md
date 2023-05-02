---
license: afl-3.0
---

# Question generation using T5 transformer

<h2> <i>Input format: context: "..." answer: "..." </i></h2>

Import the pretrained model as well as tokenizer:
```
from transformers import T5ForConditionalGeneration, T5Tokenizer

model = T5ForConditionalGeneration.from_pretrained('AbhilashDatta/T5_qgen-squad-marco') 
tokenizer = T5Tokenizer.from_pretrained('AbhilashDatta/T5_qgen-squad-marco')
```

Then use the tokenizer to encode/decode and model to generate: 

```
input = "context: My name is Abhilash Datta. answer: Abhilash"
batch = tokenizer(input, padding='longest', max_length=512, return_tensors='pt')
inputs_batch = batch['input_ids'][0]
inputs_batch = torch.unsqueeze(inputs_batch, 0)

ques_id = model.generate(inputs_batch, max_length=100, early_stopping=True)
ques_batch = [tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=False) for g in ques_id]

print(ques_batch)
```

Output:
```
['what is my name']
```