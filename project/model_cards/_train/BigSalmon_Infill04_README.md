```
from transformers import AutoTokenizer, AutoModelForCausalLM
tokenizer = AutoTokenizer.from_pretrained("BigSalmon/Infill04")
model = AutoModelForCausalLM.from_pretrained("BigSalmon/Infill04")
```

```
Try it out here:
https://huggingface.co/spaces/BigSalmon/TestAnyGPTModel
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
His contention [blank] by the evidence [sep] was refuted [answer]
***
Few sights are as [blank] New York City as the colorful, flashing signage of its bodegas [sep] synonymous with [answer]
***
When rick won the lottery, all of his distant relatives [blank] his winnings [sep] clamored for [answer]
***
The library’s quiet atmosphere encourages visitors to [blank] in their work [sep] immerse themselves [answer]
***
```

```
original: Other film stars to have appeared in Scrubs include Heather Graham, while Friends actor Matthew Perry has guest-starred and directed an episode of the [MASK] star, who recently played the title role in historical blockbuster Alexander, will make a cameo appearance as an unruly Irishman. Its leading star, Zach Braff, has recently [MASK] the big screen in Garden State, which he also directed. Farrell is pencilled in to [MASK] of Crockett in a film version of 1980s police [MASK] Farrell's appearance is said to be a result of his friendship with Zach Braff, who stars in the programme. 
infill: Other film stars to have appeared in Scrubs include Heather Graham, while Friends actor Matthew Perry has guest-starred and directed an episode of the show. The film star, who recently played the title role in historical blockbuster Alexander, will make a cameo appearance as an unruly Irishman. Its leading star, Zach Braff, has recently been seen on the big screen in Garden State, which he also directed. Farrell is pencilled in to play the role of Crockett in a film version of 1980s police drama Miami Vice. Farrell's appearance is said to be a result of his friendship with Zach Braff, who stars in the programme. 
```