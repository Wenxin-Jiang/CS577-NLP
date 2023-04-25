---

language:
- en
tags:
- text-generation
- gpt2
- gpt
license: mit
datasets:
- natural questions

widget:
- text: "how many ping-pong balls fit inside a standard 747 jet aeroplane?\nperson beta:\n\n"
  example_title: "ping-pong"
- text: "What is the capital of Uganda?\nperson beta:\n\n"
  example_title: "geography"
- text: "What is the most popular TV show of all time?\nperson beta:\n\n"
  example_title: "pseudo-culture"
- text: "A man pushes his car to a hotel and tells the owner he’s bankrupt. Why?\nperson beta:\n\n"
  example_title: "brain teaser"

inference:
  parameters:
    min_length: 2
    max_length: 32
    no_repeat_ngram_size: 2
    do_sample: True
    top_p: 0.90
    top_k: 10
    repetition_penalty: 2.1
    

---




# Ballpark Trivia: Size L

Are you frequently asked google-able Trivia questions and annoyed by it? Well, this is the model for you! Ballpark Trivia Bot answers any trivia question with something that sounds plausible but is probably not 100% correct. One might say.. the answers are in the right ballpark. Check out a demo of it [here](https://huggingface.co/spaces/pszemraj/ballpark-trivia).

```
how many varieties of eggplant are there?

person beta: 
about 4,000
```

## Training 

This text gen model is a GPT-2 774M Parameter Size L Model, first trained on [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia/) for 40k steps (34/36 layers frozen for the fine-tuning), and then subsequently trained for 40k steps on a parsed variant of [Natural Questions](https://ai.google.com/research/NaturalQuestions)(**also** 34/36 layers frozen for the fine-tuning) to accidentally create this model. 

Note that because the model was originally trained for use in a [chatbot application](https://github.com/pszemraj/ai-msgbot), it uses a named conversation dialogue structure, _, i.e. the questions are asked by person alpha, and responded to by person beta_. Even if you don't specify person alpha, it should hopefully respond to any question.

## Example Prompt

- the default examples are not great
- you can type in any trivia question or delete the example and write `what`  or `when` in there, and it will generate the rest of the trivia question **and the answer**!

```
where is the tv show the arrow filmed

person beta: 
Vancouver, British Columbia
```