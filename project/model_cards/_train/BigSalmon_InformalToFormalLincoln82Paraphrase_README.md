data: https://github.com/BigSalmon2/InformalToFormalDataset

Text Generation Informal Formal

```
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("BigSalmon/InformalToFormalLincoln82Paraphrase")

model = AutoModelForCausalLM.from_pretrained("BigSalmon/InformalToFormalLincoln82Paraphrase")
```

```
Demo:
https://huggingface.co/spaces/BigSalmon/FormalInformalConciseWordy
```

```
prompt = """informal english: corn fields are all across illinois, visible once you leave chicago.\nTranslated into the Style of Abraham Lincoln:"""
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
prompt = """informal english: corn fields are all across illinois, visible once you leave chicago.\nTranslated into the Style of Abraham Lincoln:"""
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
original: microsoft word's [MASK] pricing invites competition.
Translated into the Style of Abraham Lincoln: microsoft word's unconscionable pricing invites competition.

***

original: the library’s quiet atmosphere encourages visitors to [blank] in their work.
Translated into the Style of Abraham Lincoln:  the library’s quiet atmosphere encourages visitors to immerse themselves in their work.
```

```
Essay Intro (Warriors vs. Rockets in Game 7):
text: eagerly anticipated by fans, game 7's are the highlight of the post-season.
text: ever-building in suspense, game 7's have the crowd captivated.

***

Essay Intro (South Korean TV Is Becoming Popular):
text: maturing into a bona fide paragon of programming, south korean television ( has much to offer / entertains without fail / never disappoints ).
text: increasingly held in critical esteem, south korean television continues to impress.
text: at the forefront of quality content, south korea is quickly achieving celebrity status.

***

Essay Intro (
```

```
Search: What is the definition of Checks and Balances?

https://en.wikipedia.org/wiki/Checks_and_balances
Checks and Balances is the idea of having a system where each and every action in government should be subject to one or more checks that would not allow one branch or the other to overly dominate.

https://www.harvard.edu/glossary/Checks_and_Balances
Checks and Balances is a system that allows each branch of government to limit the powers of the other branches in order to prevent abuse of power

https://www.law.cornell.edu/library/constitution/Checks_and_Balances
Checks and Balances is a system of separation through which branches of government can control the other, thus preventing excess power.

***

Search: What is the definition of Separation of Powers?

https://en.wikipedia.org/wiki/Separation_of_powers
The separation of powers is a principle in government, whereby governmental powers are separated into different branches, each with their own set of powers, that are prevent one branch from aggregating too much power.

https://www.yale.edu/tcf/Separation_of_Powers.html
Separation of Powers is the division of governmental functions between the executive, legislative and judicial branches, clearly demarcating each branch's authority, in the interest of ensuring that individual liberty or security is not undermined.

***

Search: What is the definition of Connection of Powers?

https://en.wikipedia.org/wiki/Connection_of_powers
Connection of Powers is a feature of some parliamentary forms of government where different branches of government are intermingled, typically the executive and legislative branches.

https://simple.wikipedia.org/wiki/Connection_of_powers
The term Connection of Powers describes a system of government in which there is overlap between different parts of the government.

***

Search: What is the definition of
```

```
Search: What are phrase synonyms for "second-guess"?
https://www.powerthesaurus.org/second-guess/synonyms
Shortest to Longest:
- feel dubious about
- raise an eyebrow at
- wrinkle their noses at
- cast a jaundiced eye at
- teeter on the fence about

***

Search: What are phrase synonyms for "mean to newbies"?
https://www.powerthesaurus.org/mean_to_newbies/synonyms
Shortest to Longest:
- readiness to balk at rookies
- absence of tolerance for novices
- hostile attitude toward newcomers

***

Search: What are phrase synonyms for "make use of"?
https://www.powerthesaurus.org/make_use_of/synonyms
Shortest to Longest:
- call upon
- glean value from
- reap benefits from
- derive utility from
- seize on the merits of
- draw on the strength of
- tap into the potential of

***

Search: What are phrase synonyms for "hurting itself"?
https://www.powerthesaurus.org/hurting_itself/synonyms
Shortest to Longest:
- erring
- slighting itself
- forfeiting its integrity
- doing itself a disservice
- evincing a lack of backbone

***

Search: What are phrase synonyms for "
```
```
- nebraska
- unicamerical legislature
- different from federal house and senate
text: featuring a unicameral legislature, nebraska's political system stands in stark contrast to the federal model, comprised of a house and senate.

***

- penny has practically no value
- should be taken out of circulation
- just as other coins have been in us history
- lost use
- value not enough
- to make environmental consequences worthy
text: all but valueless, the penny should be retired. as with other coins in american history, it has become defunct. too minute to warrant the environmental consequences of its production, it has outlived its usefulness.

***

-
```
```
original: sports teams are profitable for owners. [MASK], their valuations experience a dramatic uptick. 
infill: sports teams are profitable for owners. ( accumulating vast sums / stockpiling treasure / realizing benefits / cashing in / registering robust financials / scoring on balance sheets ), their valuations experience a dramatic uptick. 

***

original:
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

```
1: commercial space company spacex plans to launch a whopping 52 flights in 2022.
2: spacex, a commercial space company, intends to undertake a total of 52 flights in 2022.
3: in 2022, commercial space company spacex has its sights set on undertaking 52 flights.
4: 52 flights are in the pipeline for 2022, according to spacex, a commercial space company.
5: a commercial space company, spacex aims to conduct 52 flights in 2022.

***

1:
```

Keywords to sentences or sentence.

```
ngos are characterized by:
□ voluntary citizens' group that is organized on a local, national or international level
□ encourage political participation
□ often serve humanitarian functions
□ work for social, economic, or environmental change

***

what are the drawbacks of living near an airbnb?
□ noise
□ parking
□ traffic
□ security
□ strangers

***
```


```
original: musicals generally use spoken dialogue as well as songs to convey the story. operas are usually fully sung.
adapted: musicals generally use spoken dialogue as well as songs to convey the story. ( in a stark departure / on the other hand / in contrast / by comparison / at odds with this practice / far from being alike / in defiance of this standard / running counter to this convention ), operas are usually fully sung.

***

original: akoya and tahitian are types of pearls. akoya pearls are mostly white, and tahitian pearls are naturally dark.
adapted: akoya and tahitian are types of pearls. ( a far cry from being indistinguishable / easily distinguished / on closer inspection / setting them apart / not to be mistaken for one another / hardly an instance of mere synonymy  / differentiating the two ), akoya pearls are mostly white, and tahitian pearls are naturally dark.

***

original:
```

```
original: had trouble deciding.
translated into journalism speak: wrestled with the question, agonized over the matter, furrowed their brows in contemplation.

***

original:
```

```
input: not loyal
1800s english: ( two-faced / inimical / perfidious / duplicitous / mendacious / double-dealing / shifty ).

***

input:
```

```
first: ( was complicit in / was involved in ).
antonym: ( was blameless / was not an accomplice to / had no hand in / was uninvolved in ).

***

first: ( have no qualms about / see no issue with ).
antonym: ( are deeply troubled by / harbor grave reservations about / have a visceral aversion to / take ( umbrage at / exception to ) / are wary of  ).

***

first: ( do not see eye to eye / disagree often ).
antonym: ( are in sync / are united / have excellent rapport / are like-minded / are in step / are of one mind / are in lockstep / operate in perfect harmony / march in lockstep ).

***

first:
```

```
stiff with competition, law school {A} is the launching pad for countless careers, {B} is a crowded field, {C} ranks among the most sought-after professional degrees, {D} is a professional proving ground.

***

languishing in viewership, saturday night live {A} is due for a creative renaissance, {B} is no longer a ratings juggernaut, {C} has been eclipsed by its imitators, {C} can still find its mojo.

***

dubbed the "manhattan of the south," atlanta {A} is a bustling metropolis, {B} is known for its vibrant downtown, {C} is a city of rich history, {D} is the pride of georgia.

***

embattled by scandal, harvard {A} is feeling the heat, {B} cannot escape the media glare, {C} is facing its most intense scrutiny yet, {D} is in the spotlight for all the wrong reasons.
```

Infill / Infilling / Masking / Phrase Masking (Works pretty decently actually, especially when you use logprobs code from above):

```
his contention [blank] by the evidence [sep] was refuted [answer]

***

few sights are as [blank] new york city as the colorful, flashing signage of its bodegas [sep] synonymous with [answer]

***

when rick won the lottery, all of his distant relatives [blank] his winnings [sep] clamored for [answer]

***

the library’s quiet atmosphere encourages visitors to [blank] in their work [sep] immerse themselves [answer]

***

the joy of sport is that no two games are alike. for every exhilarating experience, however, there is an interminable one. the national pastime, unfortunately, has a penchant for the latter. what begins as a summer evening at the ballpark can quickly devolve into a game of tedium. the primary culprit is the [blank] of play. from batters readjusting their gloves to fielders spitting on their mitts, the action is [blank] unnecessary interruptions. the sport's future is [blank] if these tendencies are not addressed [sep] plodding pace [answer] riddled with [answer] bleak [answer]

***

microsoft word's [blank] pricing [blank] competition [sep] unconscionable [answer] invites [answer]

***
```

```
original: microsoft word's [MASK] pricing invites competition.
Translated into the Style of Abraham Lincoln: microsoft word's unconscionable pricing invites competition.

***

original: the library’s quiet atmosphere encourages visitors to [blank] in their work.
Translated into the Style of Abraham Lincoln:  the library’s quiet atmosphere encourages visitors to immerse themselves in their work.
```

Backwards
```
Essay Intro (National Parks):
text: tourists are at ease in the national parks, ( swept up in the beauty of their natural splendor ).

***

Essay Intro (D.C. Statehood):
washington, d.c. is a city of outsize significance, ( ground zero for the nation's political life / center stage for the nation's political machinations ).
```

```
topic: the Golden State Warriors.
characterization 1: the reigning kings of the NBA.
characterization 2: possessed of a remarkable cohesion.
characterization 3: helmed by superstar Stephen Curry.
characterization 4: perched atop the league’s hierarchy.
characterization 5: boasting a litany of hall-of-famers.

***

topic: emojis.
characterization 1: shorthand for a digital generation.
characterization 2: more versatile than words.
characterization 3: the latest frontier in language.
characterization 4: a form of self-expression.
characterization 5: quintessentially millennial.
characterization 6: reflective of a tech-centric world.

***

topic:
```


```

regular: illinois went against the census' population-loss prediction by getting more residents.
VBG: defying the census' prediction of population loss, illinois experienced growth.

***

regular: microsoft word’s high pricing increases the likelihood of competition.
VBG: extortionately priced, microsoft word is inviting competition.

***

regular:
```

```
source: badminton should be more popular in the US.
QUERY: Based on the given topic, can you develop a story outline?
target: (1) games played with racquets are popular, (2) just look at tennis and ping pong, (3) but badminton underappreciated, (4) fun, fast-paced, competitive, (5) needs to be marketed more
text: the sporting arena is dominated by games that are played with racquets. tennis and ping pong, in particular, are immensely popular. somewhat curiously, however, badminton is absent from this pantheon. exciting, fast-paced, and competitive, it is an underappreciated pastime. all that it lacks is more effective marketing.

***

source: movies in theaters should be free.
QUERY: Based on the given topic, can you develop a story outline?
target: (1) movies provide vital life lessons, (2) many venues charge admission, (3) those without much money
text: the lessons that movies impart are far from trivial. the vast catalogue of cinematic classics is replete with inspiring sagas of friendship, bravery, and tenacity. it is regrettable, then, that admission to theaters is not free. in their current form, the doors of this most vital of institutions are closed to those who lack the means to pay.

***

source:
```

```

in the private sector, { transparency } is vital to the business’s credibility. the { disclosure of information } can be the difference between success and failure.

***

the labor market is changing, with { remote work } now the norm. this { flexible employment } allows the individual to design their own schedule.

***

the { cubicle } is the locus of countless grievances. many complain that the { enclosed workspace } restricts their freedom of movement.

***

```

```
it would be natural to assume that americans, as a people whose ancestors { immigrated to this country }, would be sympathetic to those seeking to do likewise.
question: what does “do likewise” mean in the above context?
(a) make the same journey
(b) share in the promise of the american dream
(c) start anew in the land of opportunity
(d) make landfall on the united states

***

in the private sector, { transparency } is vital to the business’s credibility. this orientation can be the difference between success and failure.
question: what does “this orientation” mean in the above context?
(a) visible business practices 
(b) candor with the public
(c) open, honest communication
(d) culture of accountability
```

```

example: suppose you are a teacher. further suppose you want to tell an accurate telling of history. then suppose a parent takes offense. they do so in the name of name of their kid. this happens a lot.
text: educators' responsibility to remain true to the historical record often clashes with the parent's desire to shelter their child from uncomfortable realities.

***

example: suppose you are a student at college. now suppose you have to buy textbooks. that is going to be worth hundreds of dollars. given how much you already spend on tuition, that is going to hard cost to bear.
text: the exorbitant cost of textbooks, which often reaches hundreds of dollars, imposes a sizable financial burden on the already-strapped college student.
```

```
<Prefix> the atlanta hawks may attribute <Prefix> <Suffix> trae young <Suffix> <Middle> their robust season to <Middle>

***

<Prefix> the nobel prize in literature <Prefix> <Suffix> honor <Suffix> <Middle> is a singularly prestigious <Middle>
```

```
accustomed to having its name uttered ______, harvard university is weathering a rare spell of reputational tumult
(a) in reverential tones
(b) with great affection
(c) in adulatory fashion
(d) in glowing terms
```

```
clarify: international ( {working together} / cooperation ) is called for when ( {issue go beyond lots of borders} / an issue transcends borders / a given matter has transnational implications  ).
```

```
description: when someone thinks that their view is the only right one.
synonyms: intolerant, opinionated, narrow-minded, insular, self-righteous.

***

description: when you put something off.
synonyms: shelve, defer, table, postpone.
```

```
organic sentence: crowdfunding is about winner of best ideas and it can test an entrepreneur’s idea.
rewrite phrases: meritocratic, viability, vision
rewritten with phrases: the meritocratic nature of crowdfunding empowers entrepreneurs to test their vision's viability.
```


*Note* Of all the masking techniques, this one works the best.
```
<Prefix> the atlanta hawks may attribute <Prefix> <Suffix> trae young <Suffix> <Middle> their robust season to <Middle>

***

<Prefix> the nobel prize in literature <Prefix> <Suffix> honor <Suffix> <Middle> is a singularly prestigious <Middle>
```