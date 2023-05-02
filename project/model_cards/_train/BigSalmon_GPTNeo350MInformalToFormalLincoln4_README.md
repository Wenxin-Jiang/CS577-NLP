Trained on this model: https://huggingface.co/xhyi/PT_GPTNEO350_ATG/tree/main

```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("BigSalmon/GPTNeo350MInformalToFormalLincoln3")

model = AutoModelForCausalLM.from_pretrained("BigSalmon/GPTNeo350MInformalToFormalLincoln3")

```

```
How To Make Prompt:
informal english: i am very ready to do that just that.
Translated into the Style of Abraham Lincoln: you can assure yourself of my readiness to work toward this end.
Translated into the Style of Abraham Lincoln: please be assured that i am most ready to undertake this laborious task.

***

informal english: space is huge and needs to be explored.
Translated into the Style of Abraham Lincoln: space awaits traversal, a new world whose boundaries are endless.
Translated into the Style of Abraham Lincoln: space is a ( limitless / boundless ) expanse, a vast virgin domain awaiting exploration.

***

informal english: corn fields are all across illinois, visible once you leave chicago.
Translated into the Style of Abraham Lincoln: corn fields ( permeate illinois / span the state of illinois / ( occupy / persist in ) all corners of illinois / line the horizon of illinois / envelop the landscape of illinois ), manifesting themselves visibly as one ventures beyond chicago.

informal english:
```
```
- declining viewership facing the nba.
- does not have to be this way.
- in fact, many solutions exist.
- the four point line would surely draw in eyes.
Text: failing to draw in the masses, the NBA has fallen into disrepair. such does not have to be the case, however. in fact, a myriad of simple, relatively cheap solutions could revive the league. the addition of the much-hyped four-point line would surely juice viewership.

***
-

```

```
infill: chrome extensions [MASK] accomplish everyday tasks.
Translated into the Style of Abraham Lincoln: chrome extensions ( expedite the ability to / unlock the means to more readily ) accomplish everyday tasks.

infill: at a time when nintendo has become inflexible, [MASK] consoles that are tethered to a fixed iteration, sega diligently curates its legacy of classic video games on handheld devices.
Translated into the Style of Abraham Lincoln: at a time when nintendo has become inflexible, ( stubbornly [MASK] on / firmly set on / unyielding in its insistence on ) consoles that are tethered to a fixed iteration, sega diligently curates its legacy of classic video games on handheld devices.

infill:

```
```
Essay Intro (California High-Speed Rail): built with an eye on the future, california's high-speed rail service resolves to change the face of travel.

Essay Intro (YIMBY's Need To Win): home to the most expensive housing market in the united states, san francisco is the city in which the yimby and anti-yimby hordes wage an eternal battle.

Essay Intro (
```