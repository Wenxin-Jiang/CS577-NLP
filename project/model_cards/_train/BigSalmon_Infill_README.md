```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("BigSalmon/Infill")

model = AutoModelForCausalLM.from_pretrained("BigSalmon/Infill")
```

```
Demo:
https://huggingface.co/spaces/BigSalmon/FormalInformalConciseWordy
```

```
prompt = """few sights are as [blank] new york city as the colorful, flashing signage of its bodegas [sep]"""
input_ids = tokenizer.encode(prompt, return_tensors='pt')
outputs = model.generate(input_ids=input_ids,
                             max_length=10 + len(prompt),
                             temperature=1.0,
                             top_k=50,
                             top_p=0.95,
                             do_sample=True,
                             num_return_sequences=5,
                             early_stopping=True)
for i in range(5):
  print(tokenizer.decode(outputs[i]))
```
Most likely outputs (Disclaimer: I highly recommend using this over just generating):
```
prompt = """few sights are as [blank] new york city as the colorful, flashing signage of its bodegas [sep]"""
text = tokenizer.encode(prompt)
myinput, past_key_values = torch.tensor([text]), None
myinput = myinput
myinput= myinput.to(device)
logits, past_key_values = model(myinput, past_key_values = past_key_values, return_dict=False)
logits = logits[0,-1]
probabilities = torch.nn.functional.softmax(logits)
best_logits, best_indices = logits.topk(250)
best_words = [tokenizer.decode([idx.item()]) for idx in best_indices]
text.append(best_indices[0].item())
best_probabilities = probabilities[best_indices].tolist()
words = []   
print(best_words)
```

Infill / Infilling / Masking / Phrase Masking

```
when rick won the lottery, all of his distant relatives [blank] his winnings [sep] clamored for [answer]

***
```