```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("BigSalmon/PointsOneSent")

model = AutoModelForCausalLM.from_pretrained("BigSalmon/PointsOneSent")
```

```
- moviepass to return
- this summer
- swooped up by
- original co-founder stacy spikes
text: the re-launch of moviepass is set to transpire this summer, ( rescued at the hands of / under the stewardship of / spearheaded by ) its founding father, stacy spikes.

***
-
```

It should also be able to do all that this can: https://huggingface.co/BigSalmon/InformalToFormalLincoln27