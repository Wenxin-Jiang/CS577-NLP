# What does this model do?
This model generates a subject line for the email, given the whole email as input. It is fine-tuned T5-Base

Here is how to use this model

```python

from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

model = AutoModelForSeq2SeqLM.from_pretrained("Chirayu/subject-generator-t5-base")
tokenizer = AutoTokenizer.from_pretrained("Chirayu/subject-generator-t5-base")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

def get_subject(content, num_beams=5,max_length=512, repetition_penalty=2.5, length_penalty=1, early_stopping=True,top_p=.95, top_k=50, num_return_sequences=3):
  
  text =  "title: " + content + " </s>"
  
  input_ids = tokenizer.encode(
    text, return_tensors="pt", add_special_tokens=True
  )
  
  input_ids = input_ids.to(device)
  generated_ids = model.generate(
      input_ids=input_ids,
     
      num_beams=num_beams,
      max_length=max_length,
      repetition_penalty=repetition_penalty,
      length_penalty=length_penalty,
      early_stopping=early_stopping,
      top_p=top_p,
      top_k=top_k,
      num_return_sequences=num_return_sequences,
  )
  subjects = [tokenizer.decode(generated_id,skip_special_tokens=True,clean_up_tokenization_spaces=True,) for generated_id in generated_ids]
  return subjects
```


