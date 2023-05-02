---
language: "en"  # Example: en
license: "cc-by-4.0"  # Example: apache-2.0 or any license from https://hf.co/docs/hub/repositories-licenses
library_name: "transformers"  # Optional. Example: keras or any library from https://github.com/huggingface/hub-docs/blob/main/js/src/lib/interfaces/Libraries.ts

---

This is the T5-11B model described in our paper DREAM: Improving Situational QA by First Elaborating the Situation, NAACL 2022 (Arxiv link: https://arxiv.org/abs/2112.08656, ACL Anthology link: https://aclanthology.org/2022.naacl-main.82/)
  
  
  
# What is DREAM 💭?
DREAM can be used to:

* Build scene elaborations in a dataset-neutral way 🖼️

* 📈 Improve QA performance across different end-tasks and on different models 📈

When people 🧑‍💻 answer questions about a specific situation, cognitive science 🧠 suggests that they form a mental picture 🖼️ of that situation. Will language models 🤖 answer such questions more accurately if provided with additional details about the question situation 🖼️ ?

We train a new model, DREAM 💭 , to answer questions that elaborate the scenes 🖼️ that situated questions are about, and then provide those elaborations as additional context 📄 to a QA model 🤖 . Our results show that DREAM 💭 is able to create more ✅ accurate, ✅ useful, and ✅ consistent scene elaborations than a representative
SOTA 🌟, zero-shot model (Macaw 🦜 ).

Remarkably, using DREAM’s 💭 scene elaborations 🖼️ as additional context improves📈 the answer accuracy across different downstream QA systems 🤖 and on different end-tasks 📝 (including beyond that obtainable by further fine-tuning the QA system on DREAM’s training data 📚). Our approach is question-agnostic 💫, leaves end-task QA models unchanged ✨, and thus easily portable to other QA models 🌟, suggesting exciting opportunities for further improving and exploiting scene elaborations to better solve new problems. 💡

We invite you to try out DREAM 💭 for your own application!
    
    
    
# How to use DREAM 💭?
We provide a quick example of how you can try out DREAM with just a few lines of code:
```
>>> from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
>>> model = AutoModelForSeq2SeqLM.from_pretrained("allenai/DREAM")

>>> tokenizer = AutoTokenizer.from_pretrained("t5-11b")
>>> input_string = "$answer$ ; $question$ = [SITUATION] hitting someones car in the drive thru on purpose. [QUERY] rot"
>>> input_ids = tokenizer.encode(input_string, return_tensors="pt")
>>> output = model.generate(input_ids, max_length=200)
>>> tokenizer.batch_decode(output, skip_special_tokens=True)
["$answer$ = It's wrong to damage other people's property."]
```

As discussed in our paper, DREAM supports the following possible dimensions for each input situation S:
```
1. M : motivation of character(s) before S.
2. E: emotion of character(s) after S.
3. ROT : general Rule of Thumb (ROT) about whether action described in S is socially acceptable or not (also known as social norm).
4. Con: likely consequence of action in S.
```
To get DREAM's output for these dimensions, use the corresponding terms below after the "[QUERY] " tag in your input string:
```
motivation
emotion
rot
consequence
```
    
    
    
# More details about DREAM 💭 ...
For more details about DREAM, please refer to our:
* 📄Paper: https://aclanthology.org/2022.naacl-main.82/
* 💻Dataset & Model: https://github.com/allenai/dream/

For additional instructions about using the DREAM model and sample commands, please refer to https://github.com/allenai/dream/blob/main/model/README_DREAM_model.md.