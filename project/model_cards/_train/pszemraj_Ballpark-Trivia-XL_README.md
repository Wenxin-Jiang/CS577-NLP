---

language:
- en
tags:
- text-generation
- gpt2
- gpt
- trivia
- chatbot
license: mit

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
    do_sample: False
    num_beams: 4
    early_stopping: True
    repetition_penalty: 2.1
    

---

# Ballpark Trivia: Size XL

**Check out a demo on HF Spaces [here](https://huggingface.co/spaces/pszemraj/ballpark-trivia).**

Are you frequently asked google-able Trivia questions and annoyed by it? Well, this is the model for you! Ballpark Trivia Bot answers any trivia question with something that sounds plausible but is probably not 100% correct. One might say.. the answers are in the right ballpark. 

This is by far the largest model trained and should be _more_ credible in its answers or at least able to handle more kinds of questions.

``` 
what is the temperature of dry ice in kelvin

person beta: 
194.65 K
```

## Training 
This text gen model is a GPT-2 ~1.5 B Parameter Size XL Model, first trained on [Wizard of Wikipedia](https://parl.ai/projects/wizard_of_wikipedia/) for 40k steps (**33**/36 layers frozen for the fine-tuning), and then subsequently trained for 40k steps on a parsed variant of [Natural Questions](https://ai.google.com/research/NaturalQuestions)(then **34**/36 layers frozen for the second fine-tuning) to accidentally create this model. 

Note that because the model was originally trained for use in a [chatbot application](https://github.com/pszemraj/ai-msgbot), it uses a named conversation dialogue structure, _i.e. the questions are asked by person alpha, and responded to by person beta_. Even if you don't specify person alpha in the prompt, it hopefully responds to any question.


## Example Prompt

- the default examples are not great
- you can type in any trivia question or delete the example and write `what`  or `when` in there, and it will generate the rest of the trivia question **and the answer**!

