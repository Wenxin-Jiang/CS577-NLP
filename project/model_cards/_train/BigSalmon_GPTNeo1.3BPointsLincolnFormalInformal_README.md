It works worse than the GPT-2 Large & Medium models I have been training, because I don't have the compute needed to train the entire dataset I have. I had to resort to using bits.

```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("BigSalmon/GPTNeo1.3BPointsLincolnFormalInformal")

model = AutoModelForCausalLM.from_pretrained("BigSalmon/GPTNeo1.3BPointsLincolnFormalInformal")
```

```
- moviepass to return
- this summer
- swooped up by
- original co-founder stacy spikes
text: the re-launch of moviepass is set to transpire this summer, ( rescued at the hands of / under the stewardship of / spearheaded by ) its founding father, stacy spikes.

***

- middle schools do not have recess
- should get back to doing it
- amazing for communication
- and getting kids to move around
text: a casualty of the education reform craze, recess has been excised from middle schools. this is tragic, for it is instrumental in honing children's communication skills and encouraging physical activity.

***

-
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

Points and keywords. Informal to formal.