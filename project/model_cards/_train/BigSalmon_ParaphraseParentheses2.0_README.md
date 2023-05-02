This can be used to paraphrase. I recommend using the code I have attached below. You can generate it without using LogProbs, but you are likely to be best served by manually examining the most likely outputs.

If this interests you, check out https://huggingface.co/BigSalmon/MrLincoln12 or my other MrLincoln repos.

```
from transformers import AutoTokenizer, AutoModelWithLMHead
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelWithLMHead.from_pretrained("BigSalmon/ParaphraseParentheses2.0")
```

Example Prompt:
```
the nba is [mask] [mask] viewership.
the nba is ( facing / witnessing / confronted with / suffering from / grappling with ) ( lost / tanking ) viewership...

ai is certain to [mask] the third industrial revolution.
ai is certain to ( breed / catalyze / inaugurate / catalyze / usher in / call forth / turn loose / lend its name to ) the third industrial revolution.

the modern-day knicks are a disgrace to [mask].
the modern-day knicks are a disgrace to the franchise's ( rich legacy / tradition of excellence / uniquely distinguished record ).

HuggingFace is [mask].
HuggingFace is ( an amazing company /
```

```
import torch
prompt = "Insert Your Prompt Here. It is Best To Have a Few Examples Before Like The Example Prompt Shows."
text = tokenizer.encode(prompt)
myinput, past_key_values = torch.tensor([text]), None
myinput = myinput
myinput= myinput.to(device)
logits, past_key_values = model(myinput, past_key_values = past_key_values, return_dict=False)
logits = logits[0,-1]
probabilities = torch.nn.functional.softmax(logits)
best_logits, best_indices = logits.topk(500)
best_words = [tokenizer.decode([idx.item()]) for idx in best_indices]
text.append(best_indices[0].item())
best_probabilities = probabilities[best_indices].tolist()
words = []
for i in range(500):
    m = ([best_words[i]])
    m = str(m)
    m = m.replace("[' ", "").replace("']", "")
    print(m)
```