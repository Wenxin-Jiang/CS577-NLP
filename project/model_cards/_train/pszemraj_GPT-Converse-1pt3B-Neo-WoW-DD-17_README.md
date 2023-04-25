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
- text: "hi, how are you doing bruh?\nperson beta:\n\n"
  example_title: "greeting"
- text: "Can you actually take me for dinner somewhere nice this time?\nperson beta:\n\n"
  example_title: "dinner"
- text: "Honey, I have clogged the toilet for the third time this month.. sorry..\nperson beta:\n\n"
  example_title: "overflow"
- text: "A man pushes his car to a hotel and tells the owner he’s bankrupt. Why?\nperson beta:\n\n"
  example_title: "brain teaser"

inference:
  parameters:
    min_length: 2
    max_length: 64
    length_penalty: 0.7
    no_repeat_ngram_size: 3
    do_sample: True
    top_p: 0.85
    top_k: 10
    repetition_penalty: 2.1
    

---

# GPT-Neo 1.3 B Conversational - 17 total epochs

- trained on the Wizard of Wikipedia parl.ai dataset + Daily Dialogues dataset
  - 13 on WoW 4 on Daily Dialogues
- the aim is to use the model as a customizable chatbot with the personID labels as pseudo-SOT/EOT tokens, i.e. ending the prompt with `person beta:` means that it is extremely likely that _person beta:_ responds, as opposed to the entered prompt being added on to.
- a link to the project repo that details how to effectively use such a trained model is [here](https://github.com/pszemraj/ai-msgbot)