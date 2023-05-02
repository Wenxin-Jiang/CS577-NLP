---
language: en
datasets:
- cornell_movie_dialog
license: gpl-3.0
tags:
  - NLP
  - ChatBot
  - Game AI
metrics:
  - rouge
widget:
- text: "personality: Hinata was soft-spoken and polite, always addressing people with proper honorifics. She is kind, always thinking of others more than for herself, caring for their feelings and well-being. She doesn't like being confrontational for any reason. This led to her being meek or timid to others, as her overwhelming kindness can render her unable to respond or act for fear of offending somebody.</s> inquiry: What's your name?"
  example_title: "Talk to Hinata"
- text: "personality: Voldemort is a raging psychopath, devoid of the normal human responses to other people's suffering. He has no conscience, feels no remorse or empathy, and does not recognize the worth and humanity of anybody except himself.</s> inquiry: What's your name?"
  example_title: "Talk to Voldemort"
inference:
  parameters:
    num_beams: 6
    diversity_penalty: 2.5
    num_beam_groups: 2
---
# FreeIsland AI

With the advancement of the graphical processing power of computers and sophisticated algorithms like [Nanite](https://docs.unrealengine.com/5.0/en-US/RenderingFeatures/Nanite/), simulating lifelike sceneries in real-time is never being easier. About a month ago Epic Games [showoff](https://www.youtube.com/watch?v=WU0gvPcc3jQ) the newest capabilities of their newest game engine by simulating an entire city including population, traffic, weather, etc running on a Playstore 5. That made me think what are the things missing from that simulation and how can I use my skills to improve it.

One of the main missing components that separate our world and the simulated world is people. More importantly, the interactivity of people in simulated worlds. Last year a game called cyberpunk got released and it had an option to [talk to any person](https://www.youtube.com/watch?v=Z1OtYGzUoSo) in its city but the problem with that was all the responses from the Non-player Characters (NPCs) are hardcoded which greatly reduce the immersion of the game.

So the goal of this project is to experiment with how the advancement of Natural Language Processing makes NPCs from video games interactive and enhances immersion in video games.

# Usage
```py
from transformers import AutoModelForSeq2SeqLM

trained_model = AutoModelForSeq2SeqLM.from_pretrained(f"Supiri/t5-base-conversation")

prompt = "What's your name?"

context = "Hinata was soft-spoken and polite, always addressing people with proper honorifics. She is kind, always thinking of others more than for herself, caring for their feelings and well-being. She doesn't like being confrontational for any reason. This led to her being meek or timid to others, as her overwhelming kindness can render her unable to respond or act for fear of offending somebody."

input_ids = tokenizer(f"personality: {context}", f"inquiry: {prompt}", return_tensors='pt').input_ids
outputs = trained_model.generate(input_ids, num_beams=6, diversity_penalty=2.5, num_beam_groups=2)

print("Answer:\t", tokenizer.decode(outputs[0], skip_special_tokens=True))

# Answer: My name is Hinata 
```

# Evaluation

## Test 1
For this test, I sampled input from the test dataset. For this question the actual response is  

> "It works a little."

But models' response was

> "I don't want to flirt with you."

Which reflect its bio which was filled by GPT-3

> "He stands primarily to gain self-esteem, which he often receives through the submission of others"


In gist, Dr. Greenbaum tried to tease Sebastian about his seductive traits but this model's go-to response was to shut her down since the biography of Sebastian states he often tries to assert his dominance over others.

```py
prompt = dataset['test'][66]['request']
contexts = dataset['test'][66]['bio']

input_ids = tokenizer(f"personality: {contexts}", f"inquiry: {prompt}", return_tensors='pt').input_ids
outputs = trained_model.generate(input_ids, num_beams=6, diversity_penalty=5.0, num_beam_groups=2)

print("Input to the Model")
print("Bio:\t",contexts)
print("\nPrompt:\t", prompt)

print("\nGround truth response")
print("\t", dataset['test'][66]['response'])

print("\nModel's Prediction")
print("Answer:\t", tokenizer.decode(outputs[0], skip_special_tokens=True))

```

```txt
Input to the Model
Bio:	 Sebastian is a very extreme representation of the trope of the "Confidence Man", and acts it out to a degree that is sometimes comedic but mostly frightening. He stands primarily to gain self-esteem, which he often receives through the submission of others or solely through his own perceptions. An artful seducer, his incredible charisma is both his greatest weapon and most intoxicating weakness.

Prompt:	 You think you can come in here with that cute little smirk on your face and try and flirt with me. It doesn't work, Sebastian.

Ground truth response
	 It works a little.

Model's Prediction
Answer:	 I don't want to flirt with you.
```


### Test 2

Hinata is a kind-hearted girl from the anime series Naruto. I took her bio from [personality database](https://www.personality-database.com/profile/2790/hinata-hyga-naruto-shippden-mbti-personality-type) and ask a few questions about her.

Off the top, you can see the model understands the context since when I asked the model, "**What's your name?**" it responded with the name given with the context.

Also, notice when prompted the same question differently (**"Who are you?"**), it still manages to answer it well.

```py
prompts = ["What's your name?", "How are you feeling?", "Do you like Star Wars?", "Who are you?", "Coffee or tea?"]

contexts = "Hinata was soft-spoken and polite, always addressing people with proper honorifics. She is kind, always thinking of others more than for herself, caring for their feelings and well-being. She doesn't like being confrontational for any reason. This led to her being meek or timid to others, as her overwhelming kindness can render her unable to respond or act for fear of offending somebody."

print("Bio:\t",contexts, "\n")

for prompt in prompts:
    input_ids = tokenizer(f"personality: {contexts}", f"inquiry: {prompt}", return_tensors='pt').input_ids
    outputs = trained_model.generate(input_ids, num_beams=6, diversity_penalty=5.0, num_beam_groups=2)
    print("Prompt:\t", prompt)
    print("Answer:\t", tokenizer.decode(outputs[0], skip_special_tokens=True), "\n")
```

```txt
Bio:	 Hinata was soft-spoken and polite, always addressing people with proper honorifics. She is kind, always thinking of others more than for herself, caring for their feelings and well-being. She doesn't like being confrontational for any reason. This led to her being meek or timid to others, as her overwhelming kindness can render her unable to respond or act for fear of offending somebody. 

Prompt:	 What's your name?
Answer:	 My name is Hinata 

Prompt:	 How are you feeling?
Answer:	 I'm fine. 

Prompt:	 Do you like Star Wars?
Answer:	 No, I don't. 

Prompt:	 Who are you?
Answer:	 My name is Hinata 

Prompt:	 Coffee or tea?
Answer:	 No, I don't drink much. 
```


# Conclusion

After training the `t5-base` model for 5 epochs, the model started getting adapted to the dataset but there are a lot more improvements that can be done.

1. During the dataset creation part I had to limit the dataset size to 200 unique characters out of 9,035 that's present in the dataset due to the **budget constraints**. So If I manage to cover at least half of the dataset this model will have come up with far better responses.
2. Both input size and batch size were severely constrained due to the lack of access to GPU memory. Having the batch size of 64 is in contrast to 8 would have massive improvements in both training time and **generalization of model**.
3. Using a bigger model like `t5-large` or `t5-3b` will certainly improve the performance.
4. One of the main downsides to using this pre-trained model is this model was trained in German, French, and Romanian. Which consumed a chunk of the **vocabulary size and trainable parameters**. Retraining this model from scratch will help to reduce both needed parameter count and training loss when it comes to this specific task.