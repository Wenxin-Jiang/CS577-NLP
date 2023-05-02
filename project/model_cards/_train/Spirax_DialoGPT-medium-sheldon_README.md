---

thumbnail: https://i.imgur.com/7HAcbbD.gif

tags:

- conversational

license: mit

---

# DialoGPT Trained on the Speech of a TV Series Character

This is an instance of [microsoft/DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) trained on a TV series character, Sheldon from [The Big Bang Theory](https://en.wikipedia.org/wiki/The_Big_Bang_Theory). The data comes from [a Kaggle TV series script dataset](https://www.kaggle.com/mitramir5/the-big-bang-theory-series-transcript).


Chat with the model:

```python
from transformers import AutoTokenizer, AutoModelWithLMHead
  
tokenizer = AutoTokenizer.from_pretrained("spirax/DialoGPT-medium-sheldon")

model = AutoModelWithLMHead.from_pretrained("spirax/DialoGPT-medium-sheldon")

# Let's chat for 4 lines
for step in range(4):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')
    # print(new_user_input_ids)

    # append the new user input tokens to the chat history
    bot_input_ids = torch.cat([chat_history_ids, new_user_input_ids], dim=-1) if step > 0 else new_user_input_ids

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        bot_input_ids, max_length=200,
        pad_token_id=tokenizer.eos_token_id,  
        no_repeat_ngram_size=3,       
        do_sample=True, 
        top_k=100, 
        top_p=0.7,
        temperature=0.8
    )
    
    # pretty print last ouput tokens from bot
    print("SheldorBot: {}".format(tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)))
```