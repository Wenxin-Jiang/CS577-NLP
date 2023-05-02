```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("BigSalmon/InformalToFormalLincolnConciseWordy")

model = AutoModelForCausalLM.from_pretrained("BigSalmon/InformalToFormalLincolnConciseWordy")
```


```
wordy: classical music is becoming less popular more and more.
Translate into Concise Text: interest in classic music is fading.

***

wordy:
```

```
sweet: savvy voters ousted him.
longer: voters who were informed delivered his defeat.

***

sweet:
```


Keywords to sentences or sentence.