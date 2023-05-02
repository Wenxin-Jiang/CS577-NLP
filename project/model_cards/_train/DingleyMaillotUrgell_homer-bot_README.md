---
tags:
- conversational
language:
- en
---

# HomerBot: A conversational chatbot imitating Homer Simpson

This model is a fine-tuned [DialoGPT](https://huggingface.co/microsoft/DialoGPT-medium) (medium version) on Simpsons [scripts](https://www.kaggle.com/datasets/pierremegret/dialogue-lines-of-the-simpsons).

More specifically, we fine-tune DialoGPT-medium for 3 epochs on 10K **(character utterance, Homer's response)** pairs

For more details, check out our git [repo](https://github.com/jesseDingley/HomerBot) containing all the code.  

### How to use


```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch 

tokenizer = AutoTokenizer.from_pretrained("DingleyMaillotUrgell/homer-bot")
model = AutoModelForCausalLM.from_pretrained("DingleyMaillotUrgell/homer-bot")

# Let's chat for 5 lines
for step in range(5):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input(">> User: ") + tokenizer.eos_token, return_tensors='pt')
  
    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        bot_input_ids, 
        max_length=1000,                    
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3,
        do_sample=True, 
        top_k=100, 
        top_p=0.7,
        temperature = 0.8
    )
    
    # print last outpput tokens from bot
    print("Homer: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
```
 