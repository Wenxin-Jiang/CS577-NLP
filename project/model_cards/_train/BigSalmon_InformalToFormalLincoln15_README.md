Informal to Formal:
```
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("BigSalmon/InformalToFormalLincoln15")
model = AutoModelWithLMHead.from_pretrained("BigSalmon/InformalToFormalLincoln15")
```

```
https://huggingface.co/spaces/BigSalmon/GPT2 (The model for this space changes over time)
```

```
https://huggingface.co/spaces/BigSalmon/GPT2_Most_Probable (The model for this space changes over time)
```

```
How To Make Prompt:
informal english: i am very ready to do that just that.
Translated into the Style of Abraham Lincoln: you can assure yourself of my readiness to work toward this end.
Translated into the Style of Abraham Lincoln: please be assured that i am most ready to undertake this laborious task.

informal english: space is huge and needs to be explored.
Translated into the Style of Abraham Lincoln: space awaits traversal, a new world whose boundaries are endless.
Translated into the Style of Abraham Lincoln: space is a ( limitless / boundless ) expanse, a vast virgin domain awaiting exploration.

The guys were ( enlisted to spearhead the cause / tasked with marshaling the movement forward / charged with driving the initiative onward /  vested with the assignment of forwarding the mission)

informal english: friday should no longer be a workday, but a day added to the weekend, suffusing people with the ability to spend time with their families.
Translated into the Style of Abraham Lincoln: the weekend should come to include friday, ( broadening the window of time for one to be in the company of their family / ( multiplying / swelling / turbocharging / maximizing ) the interval for one to ( reconnect with / feel the warmth of ) their loved ones ).

informal english:
````
