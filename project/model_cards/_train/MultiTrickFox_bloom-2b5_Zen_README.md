   #####
## Bloom2.5B Zen ##
   #####


Bloom (2.5 B) Scientific Model fine-tuned on Zen knowledge


   #####
## Usage ##
   #####


```python

from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("MultiTrickFox/bloom-2b5_Zen") 
model = AutoModelForCausalLM.from_pretrained("MultiTrickFox/bloom-2b5_Zen")

generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

inp = [ """Today""", """Yesterday""" ]

out = generator( 
    inp, 
    
    do_sample=True,
    temperature=.7,
    typical_p=.6,
    #top_p=.9,
    repetition_penalty=1.2,

    max_new_tokens=666,
    max_time=60, # seconds
)

for o in out: print(o[0]['generated_text'])
```