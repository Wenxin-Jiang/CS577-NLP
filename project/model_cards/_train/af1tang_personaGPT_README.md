---
tags:
- conversational
license: gpl-3.0
---
## A conversational agent with many personalities (PersonaGPT)
PersonaGPT is an open-domain conversational agent designed to do 2 tasks:

1. decoding _personalized_ responses based on input personality facts (the "persona" profile of the bot). 
2. incorporating _turn-level goals_ into its responses through "action codes" (e.g., "talk about work", "ask about favorite music").

It builds on the [DialoGPT-medium](https://huggingface.co/microsoft/DialoGPT-medium) pretrained model based on the [GPT-2](https://github.com/openai/gpt-2) architecture. 
This model is trained on the [Persona-Chat](https://arxiv.org/pdf/1801.07243) dataset, with added special tokens to better distinguish between conversational history and personality traits for dyadic conversations. Furthermore, some active learning was used to train the model to do _controlled_ decoding using turn-level goals.

## Full Repo

Preprocessing, training and implementation details can be found in the [personaGPT repo](https://github.com/af1tang/personaGPT).

### How to Use


1. Load the model and define some helper functions.

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
tokenizer = AutoTokenizer.from_pretrained("af1tang/personaGPT")
model = AutoModelForCausalLM.from_pretrained("af1tang/personaGPT")
if torch.cuda.is_available():
	model = model.cuda()
## utility functions ##
flatten = lambda l: [item for sublist in l for item in sublist]

def to_data(x):
    if torch.cuda.is_available():
        x = x.cpu()
    return x.data.numpy()

def to_var(x):
    if not torch.is_tensor(x):
        x = torch.Tensor(x)
    if torch.cuda.is_available():
        x = x.cuda()
    return x

def display_dialog_history(dialog_hx):
    for j, line in enumerate(dialog_hx):
        msg = tokenizer.decode(line)
        if j %2 == 0:
            print(">> User: "+ msg)
        else:
            print("Bot: "+msg)
            print()

def generate_next(bot_input_ids, do_sample=True, top_k=10, top_p=.92,
                  max_length=1000, pad_token=tokenizer.eos_token_id):
    full_msg = model.generate(bot_input_ids, do_sample=True,
                                              top_k=top_k, top_p=top_p, 
                                              max_length=max_length, pad_token_id=tokenizer.eos_token_id)
    msg = to_data(full_msg.detach()[0])[bot_input_ids.shape[-1]:]
    return msg
```

2. Give your chatbot partner a set of personalities. 


```python
# get personality facts for conversation
personas = []
for i in range(3):
    response = input(">> Fact %d: "%(i+1))+ tokenizer.eos_token
    personas.append(response)
personas = tokenizer.encode(''.join(['<|p2|>'] + personas + ['<|sep|>'] + ['<|start|>']))
```

3. The first use of PersonaGPT is to do _personalized_ dialog generation. Use the following loop to interact with the model.

```python
# converse for 8 turns
dialog_hx = []
for step in range(8):
    # encode the user input
    user_inp = tokenizer.encode(input(">> User: ") + tokenizer.eos_token)
    # append to the chat history
    dialog_hx.append(user_inp)
        
    # generated a response while limiting the total chat history to 1000 tokens, 
    bot_input_ids = to_var([personas + flatten(dialog_hx)]).long()
    msg = generate_next(bot_input_ids)
    dialog_hx.append(msg)
    print("Bot: {}".format(tokenizer.decode(msg, skip_special_tokens=True)))
```


Example of personalized decoding:

| | Persona Facts |
|---|---|
| 1 | i am 64 years old but feel quite young. |
| 2 | i try to eat healthy but limit mcdonalds to once a week. |
| 3 | i regret working as a doctor for the last 20 years. |
| 4 | my secret hobby is making self-help youtube videos. |
| 5 | i've been to spain many times and wish i could go again. |

| Role | Response|
|---|---|
| Human | yo whats good fam? |
| Bot | hello, how are you doing? |
| Human | not bad what you doing today?|
| Bot | eating a lot healthier now that i'm in my 60s |
| Human | i'm more of a fast food guy |
| Bot | me too but i'm very healthy so i try to avoid it |
| Human | what do you do for fun? |
| Bot | i make videos for fun and eat very healthy |
| Human | nice what kind of videos? |
| Bot | i love making videos about self help stuff |
| Human | i think i need some help | 
| Bot | what kind of help would you like to get |
| Human | i'm 21 and feel lost in life | 
| Bot | i can relate, i'm only 65 |


4. The second use of PersonaGPT is to do _controlled response generation_. Use the following program to interact with the model.

```python
## available actions ##
action_space = [ 'ask about kids.', "ask about pets.", 'talk about work.', 
               'ask about marital status.', 'talk about travel.', 'ask about age and gender.',
        'ask about hobbies.', 'ask about favorite food.', 'talk about movies.', 
        'talk about music.', 'talk about politics.']
# converse for 8 turns
dialog_hx = []
for step in range(8):
	# choose an action
    act = None
    while act not in action_space:
        display_dialog_history(dialog_hx)
        print()
        print(" actions: ")
        for k,v in enumerate(action_space): print(k,v)
        try:
            act = action_space[int(input(" input [0-10]: " ))]
        except:
            act = None
    print()
    # format into prefix code
    action_prefix = tokenizer.encode(''.join(['<|act|> '] + [act] + ['<|p1|>'] + [] + ['<|sep|>'] + ['<|start|>']))
    bot_input_ids = to_var([action_prefix + flatten(dialog_hx)]).long()
    
    # generate query conditioned on action
    msg = generate_next(bot_input_ids, top_k=top_k, top_p=top_p, max_length=max_length)
    dialog_hx.append(msg)
    
    # generate bot response
    bot_input_ids = to_var([personas+ flatten(dialog_hx)]).long()
    msg = generate_next(bot_input_ids, top_k=top_k, top_p=top_p, max_length=max_length)
    dialog_hx.append(msg)
display_dialog_history(dialog_hx)
```


Example of controlled response generation: 


| | Bot 2's Persona Facts |
|---|---|
| 1 | i am a quiet engineer. |
| 2 | i'm single and am looking for love. |
| 3 | sadly, i don't have any relatable hobbies. |
| 4 | luckily, however, i am tall and athletic. |
| 5 | on friday nights, i watch re-runs of the simpsons alone. |

| Role | Action | Response |
|---|---|---|
| Bot 1 | talk about movies | hello do you like movies? |
| Bot 2 | - | i love the simpsons. how about you? |
| Bot 1 | talk about music | i like the walking dead. do you play an instrument? |
| Bot 2 | - | yes i play the violin. |
| Bot 1 | ask about marital status | are you married or single? |
| Bot 2 | - | i am single but i am looking for love. |
| Bot 1 | talk about work | my job is working in a factory. what's your occupation? |
| Bot 2 | - | engineer. i'm very quiet so no one hears me. |
| Bot 1 | talk about hobbies | do you have any hobbies? |
| Bot 2 | - | i watch reruns of the simpsons. | 
| Bot 1 | ask about favorite food | what's your favorite food? |
| Bot 2 | - | i love pizza. how about yourself? |
| Bot 1 | ask about pets | i also love pizza. do you like animals? | 
| Bot 2 | - | i have two dogs. what is your occupation? | 
| Bot 1 | talk about work | i'm a factory worker. what's your dream job? |
| Bot 2 | - | i'd love to be a writer one day. |