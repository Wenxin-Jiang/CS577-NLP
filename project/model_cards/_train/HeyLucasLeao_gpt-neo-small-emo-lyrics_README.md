Create README.md
## Emo Bot

#### Model Description
This is a finetuned version from GPT-Neo-125M for Generating Music Lyrics by Emo Genre.

#### Training data
It was trained with 2381 songs by 15 bands that were important to emo culture in the early 2000s, not necessary directly playing on the genre.

#### Training Procedure
It was finetuned using the Trainer Class available on the Hugging Face library.

##### Learning Rate: **2e-4**
##### Epochs: **40**
##### Colab for Finetuning: https://colab.research.google.com/drive/1jwTYI1AygQf7FV9vCHTWA4Gf5i--sjsD?usp=sharing
##### Colab for Testing: https://colab.research.google.com/drive/1wSP4Wyr1-DTTNQbQps_RCO3ThhH-eeZc?usp=sharing

#### Goals

My true intention was totally educational, thus making available a this version of the model as a example for future proposes.

How to use
``` python
from transformers import AutoTokenizer, AutoModelForCausalLM
import re

if torch.cuda.is_available():
    device = torch.device('cuda')
else:
    device = torch.device('cpu')
print(device)

tokenizer = AutoTokenizer.from_pretrained("HeyLucasLeao/gpt-neo-small-emo-lyrics")
model = AutoModelForCausalLM.from_pretrained("HeyLucasLeao/gpt-neo-small-emo-lyrics")
model.to('cuda')

generated = tokenizer('I miss you',return_tensors='pt').input_ids.cuda()

#Generating texts
sample_outputs = model.generate(generated, 
                 # Use sampling instead of greedy decoding 
                 do_sample=True, 
                 # Keep only top 3 token with the highest probability
                 top_k=10, 
                 # Maximum sequence length
                 max_length=200, 
                 # Keep only the most probable tokens with cumulative probability of 95%
                 top_p=0.95, 
                 # Changes randomness of generated sequences
                 temperature=2.,
                 # Number of sequences to generate                 
                 num_return_sequences=3)
                 
# Decoding and printing sequences
for i, sample_output in enumerate(sample_outputs):
    texto = tokenizer.decode(sample_output.tolist())
    regex_padding = re.sub('<|pad|>', '', texto)
    regex_barra = re.sub('[|+]', '', regex_padding)
    espaço = re.sub('[ +]', ' ', regex_barra)
    resultado = re.sub('[\n](2, )', '\n', espaço)
    print(">> Text {}: {}".format(i+1, resultado + '\n'))
  
""">> Texto 1: I miss you 
 I miss you more than anything 
 And if you change your mind 
 I do it like a change of mind 
 I always do it like theeah 
 Everybody wants a surprise 
 Everybody needs to stay collected 
 I keep your locked and numbered 
 Use this instead: Run like the wind 
 Use this instead: Run like the sun 
 And come back down: You've been replaced 
 Don't want to be the same 
 Tomorrow 
 I don't even need your name 
 The message is on the way 
 make it while you're holding on 
 It's better than it is 
 Everything more security than a parade 
 Im getting security 
angs the world like a damned soul 
 We're hanging on a queue 
 and the truth is on the way 
 Are you listening? 
 We're getting security 
 Send me your soldiers 
 We're getting blood on"""

""">> Texto 2: I miss you 
 And I could forget your name 
 All the words we'd hear 
 You miss me 
 I need you 
 And I need you 
 You were all by my side 
 When we'd talk to no one 
 And I 
 Just to talk to you 
 It's easier than it has to be 
 Except for you 
 You missed my know-all 
 You meant to hug me 
 And I 
 Just want to feel you touch me 
 We'll work up 
 Something wild, just from the inside 
 Just get closer to me 
 I need you 
 You were all by my side 
 When we*d talk to you 
, you better admit 
 That I'm too broken to be small 
 You're part of me 
 And I need you 
 But I 
 Don't know how 
 But I know I need you 
 Must"""

""">> Texto 3: I miss you 
 And I can't lie 
 Inside my head 
 All the hours you've been through 
 If I could change your mind 
 I would give it all away 
 And I'd give it all away 
 Just to give it away 
 To you 
 Now I wish that I could change 
 Just to you 
 I miss you so much 
 If I could change 
 So much 
 I'm looking down 
 At the road 
 The one that's already been 
 Searching for a better way to go 
 So much I need to see it clear 
  topk  wish me an ehive 
 I wish I wish I wish I knew 
 I can give well 
 In this lonely night 
 
 The lonely night 
 I miss you 
 I wish it well  
 If I could change   
 So much 
 I need you"""
```