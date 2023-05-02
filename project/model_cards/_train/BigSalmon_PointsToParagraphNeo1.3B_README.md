```
!pip install transformers
!pip install torch
```
```
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("BigSalmon/PointsToParagraphNeo1.3B")
model = AutoModelForCausalLM.from_pretrained("BigSalmon/PointsToParagraphNeo1.3B")
```

```
prompt = """
- advent
- podcasts
- entertainment
- is an industry transformed
- no longer
- consumers touch clicker or turn on radio
- people plug in their earbuds to listen to a podcast
- this changing mediums for reasons
- can be done anywhere
- more optionality in content
text: as podcasts have"""
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
prompt = """
- advent
- podcasts
- entertainment
- is an industry transformed
- no longer
- consumers touch clicker or turn on radio
- people plug in their earbuds to listen to a podcast
- this changing mediums for reasons
- can be done anywhere
- more optionality in content
text: as podcasts have"""
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

Example:
```
- advent
- podcasts
- entertainment
- is an industry transformed
- no longer
- consumers touch clicker or turn on radio
- people plug in their earbuds to listen to a podcast
- this changing mediums for reasons
- can be done anywhere
- more optionality in content
text: as podcasts have proliferated, the entertainment industry has been fundamentally reshaped. in place of flipping through channels or spinning the dial, consumers are plugging in their earbuds to enjoy audio content. this evolution in media consumption is not without explanation, but rather a function of greater portability and content optionality.

***

- newborn
- caring for
- full-time job
- parents
- often have to work normal job
- paid leave needs to be universal
- so parents not overworked
- child is cared for
- can spend special time together
text: tending to a newborn is a full-time job. regrettably, many parents must perform this duty alongside their conventional employment. to spare them from such strain, paid leave must be universal. in this way, children will be provided for, while the parent-child bond will be strengthened.
```