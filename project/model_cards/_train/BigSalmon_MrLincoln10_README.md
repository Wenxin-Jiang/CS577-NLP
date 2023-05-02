Informal to Formal:
```
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("gpt2")
model = AutoModelWithLMHead.from_pretrained("BigSalmon/MrLincoln10")
```

```
How To Make Prompt:
Original: freedom of the press is a check against political corruption.
Edited: fundamental to the spirit of democracy, freedom of the press is a check against political corruption.
Edited 2: ever at odds with tyranny, freedom of the press is a check against political corruption.
Edited 3: never to be neglected, freedom of the press is a check against political corruption.

Original: solar is a beacon of achievement.
Edited: central to decoupling from the perils of unsustainable energy, solar is a beacon of achievement.
Edited 2: key to a future beyond fossil fuels, solar is a beacon of achievement.

Original: milan is nevertheless ambivalent towards his costly terms.
Edited: keen on contracting him, milan is nevertheless ambivalent towards his costly terms.
Edited 2: intent on securing his services, milan is nevertheless ambivalent towards his costly terms.

Original:
```

```
How To Make Prompt:
informal english: i am very ready to do that just that.
Translated into the Style of Abraham Lincoln: you can assure yourself of my readiness to work toward this end.
Translated into the Style of Abraham Lincoln: please be assured that i am most ready to undertake this laborious task.

informal english: space is huge and needs to be explored.
Translated into the Style of Abraham Lincoln: space awaits traversal, a new world whose boundaries are endless.
Translated into the Style of Abraham Lincoln: space is a ( limitless / boundless ) expanse, a vast virgin domain awaiting exploration.

informal english: meteors are much harder to see, because they are only there for a fraction of a second.
Translated into the Style of Abraham Lincoln: meteors are not ( easily / readily ) detectable, lasting for mere fractions of a second.

informal english:
````