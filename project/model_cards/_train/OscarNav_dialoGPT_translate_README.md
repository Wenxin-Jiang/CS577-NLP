# Finetuned DialoGPT model for Eng-Spa translation

DialoGPT-small model was used and finetuned on English to Spanish translations, extracted from http://storage.googleapis.com/download.tensorflow.org/data/spa-eng.zip

some examples of translations

| Role  | Response  | 
| :---: |------------------------| 
| User  | please, sing me a song | 
| Bot   | Por favor, canta una canción. | 
| User  | I really want to go to China | 
| Bot   | Realmente quiero ir a China. | 
| User  | Can you do me a favor? | 
| Bot   | ¿Me puedes hacer un favor? |
| User  | I don't know what you are talking about | 
| Bot   | No sé de qué estás hablando. |
| User  | I don't want to go to China | 
| Bot   | No quiero ir a China. |
 

# Using the model
example code for trying out the model

```python
from transformers import AutoModelWithLMHead, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained('microsoft/DialoGPT-small')
model = AutoModelWithLMHead.from_pretrained('OscarNav/dialoGPT_translate')

# Let's traslate 5 sentences
for step in range(5):
    # encode the new user input, add the eos_token and return a tensor in Pytorch
    new_user_input_ids = tokenizer.encode(input(">> User:") + tokenizer.eos_token, return_tensors='pt')

    # generated a response while limiting the total chat history to 1000 tokens, 
    chat_history_ids = model.generate(
        new_user_input_ids, max_length=1000,
        pad_token_id=tokenizer.eos_token_id,
        top_p=0.92, top_k = 50
    )
    
    # pretty print last ouput tokens from bot
    print("DialoGPT: {}".format(tokenizer.decode(chat_history_ids[:, new_user_input_ids.shape[-1]:][0], skip_special_tokens=True)))
```