### How to use
Here is how to use this model in PyTorch:
```python
from transformers import T5Tokenizer, T5ForConditionalGeneration

model = T5ForConditionalGeneration.from_pretrained("addy88/T5-23-emotions-detections")

tokenizer = T5Tokenizer.from_pretrained("addy88/T5-23-emotions-detections")

text_to_summarize="emotion: i don't like it this is nonsense."

input_ids = tokenizer.encode(text_to_summarize, return_tensors="pt", add_special_tokens=True)
         
         
input_ids = input_ids.to(self.device)

generated_ids = model.generate(
     input_ids=input_ids,
     num_beams=2,
     max_length=512,
     repetition_penalty=2.5,
     length_penalty=1.0,
     early_stopping=True,
     top_p=0.95,
     top_k=50,
     num_return_sequences=1,
)


preds = [tokenizer.decode(g,skip_special_tokens=True,clean_up_tokenization_spaces=True,)for g in generated_ids]
```