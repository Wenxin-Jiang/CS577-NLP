---
datasets:
- squad
tags:
- question-answer-generation
widget:
- text: "generate question: <hl> 42 <hl> is the answer to life, the universe and everything. </s>"
- text: "question: What is 42 context: 42 is the answer to life, the universe and everything. </s>"
license: mit
---

## T5 for multi-task QA and QG
This is multi-task [t5-base](https://arxiv.org/abs/1910.10683) model trained for question answering and answer aware question generation tasks. 

For question generation the answer spans are highlighted within the text with special highlight tokens (`<hl>`) and prefixed with 'generate question: '. For QA the input is processed like this `question: question_text context: context_text </s>` 

You can play with the model using the inference API. Here's how you can use it

For QG

`generate question: <hl> 42 <hl> is the answer to life, the universe and everything. </s>`

For QA

`question: What is 42 context: 42 is the answer to life, the universe and everything. </s>`

For more deatils see [this](https://github.com/patil-suraj/question_generation) repo.
