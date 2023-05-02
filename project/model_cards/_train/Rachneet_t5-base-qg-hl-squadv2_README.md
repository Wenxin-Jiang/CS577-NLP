---
datasets:
- squad
tags:
- question-generation
widget:
- text: "<hl> 42 <hl> is the answer to life, the universe and everything. </s>"
- text: "Python is a programming language. It is developed by <hl> Guido Van Rossum <hl>. </s>"
- text: "Although <hl> practicality <hl> beats purity </s>"
license: mit
---

### T5 for question-generation
This is [t5-base](https://arxiv.org/abs/1910.10683) model trained for answer aware question generation task. The answer spans are highlighted within the text with special highlight tokens. 

You can play with the model using the inference API, just highlight the answer spans with `<hl>` tokens and end the text with `</s>`. For example

`<hl> 42 <hl> is the answer to life, the universe and everything. </s>`

For more deatils see [this](https://github.com/patil-suraj/question_generation) repo.
