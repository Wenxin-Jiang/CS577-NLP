Informal to Formal:
Wordy to Concise:
Fill Missing Phrase:
```
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("BigSalmon/InformalToFormalLincoln20")
model = AutoModelWithLMHead.from_pretrained("BigSalmon/InformalToFormalLincoln20")
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

informal english: corn fields are all across illinois, visible once you leave chicago.
Translated into the Style of Abraham Lincoln: corn fields ( permeate illinois / span the state of illinois / ( occupy / persist in ) all corners of illinois / line the horizon of illinois / envelop the landscape of illinois ), manifesting themselves visibly as one ventures beyond chicago.

informal english:
````

```
infill: increasing the number of sidewalks in suburban areas will [MASK].
Translated into the Style of Abraham Lincoln: increasing the number of sidewalks in suburban areas will ( ( enhance / maximize ) community cohesion / facilitate ( communal ties / the formation of neighborhood camaraderie ) / forge neighborly relations / lend themselves to the advancement of neighborly ties / plant the seeds of community building / flower anew the bonds of friendship / invite the budding of neighborhood rapport / enrich neighborhood life ).

infill: corn fields [MASK], [MASK] visibly as one ventures beyond chicago.
Translated into the Style of Abraham Lincoln: corn fields ( permeate illinois / span the state of illinois / ( occupy / persist in ) all corners of illinois / line the horizon of illinois / envelop the landscape of illinois ), ( manifesting themselves ) visibly as one ventures beyond chicago.

infill: the [MASK] the SAT will soon be [MASK]. [MASK] an examination undertaken on one's laptop. [MASK] will allow students to retrieve test results promptly.
Translated into the Style of Abraham Lincoln: the ( conventional form of ) the SAT will soon be ( consigned to history ). ( replacing it will be ) an examination undertaken on one's laptop. ( so doing ) will allow students to retrieve test results promptly.

infill:
```
```
***

wordy: chancing upon a linux user is a rare occurrence in the present day.
Translate into Concise Text: present-day linux users are rare.

***

wordy: an interest in classical music is becoming more and more less popular.
Translate into Concise Text: classical music appreciation is dwindling.
Translate into Concise Text: waning interest in classic music persists.
Translate into Concise Text: interest in classic music is fading.

***

wordy: the ice cream was only one dollar, but it was not a good value for the size.
Translate into Concise Text: the one dollar ice cream was overpriced for its size.
Translate into Concise Text: overpriced, the one dollar ice cream was small.

***
wordy:
```