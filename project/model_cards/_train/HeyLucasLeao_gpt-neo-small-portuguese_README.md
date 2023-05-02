## GPT-Neo Small Portuguese

#### Model Description
This is a finetuned version from GPT-Neo 125M by EletheurAI to Portuguese language. 

#### Training data
It was trained from 227,382 selected texts from a PTWiki Dump. You can found all the data from here: https://archive.org/details/ptwiki-dump-20210520

#### Training Procedure
Every text was passed through a GPT2-Tokenizer with bos and eos tokens to separate them, with max sequence length that the GPT-Neo could support. It was finetuned using the default metrics of the Trainer Class, available on the Hugging Face library.

##### Learning Rate: **2e-4**
##### Epochs: **1**

#### Goals

My true intention was totally educational, thus making available a Portuguese version of this model.

How to use
``` python
from transformers import AutoTokenizer, AutoModelForCausalLM
  
tokenizer = AutoTokenizer.from_pretrained("HeyLucasLeao/gpt-neo-small-portuguese")

model = AutoModelForCausalLM.from_pretrained("HeyLucasLeao/gpt-neo-small-portuguese")

text = 'eu amo o brasil.'

generated = tokenizer(f'<|startoftext|> {text}',   
                      return_tensors='pt').input_ids.cuda()
                      
#Generating texts
sample_outputs = model.generate(generated, 
                 # Use sampling instead of greedy decoding 
                 do_sample=True, 
                 # Keep only top 3 token with the highest probability
                 top_k=3, 
                 # Maximum sequence length
                 max_length=200, 
                 # Keep only the most probable tokens with cumulative probability of 95%
                 top_p=0.95, 
                 # Changes randomness of generated sequences
                 temperature=1.9,
                 # Number of sequences to generate                 
                 num_return_sequences=3)

# Decoding and printing sequences
for i, sample_output in enumerate(sample_outputs):
    print(">> Generated text {}\\\\
\\\\
{}".format(i+1, tokenizer.decode(sample_output.tolist())))

# >> Generated text
#Setting `pad_token_id` to `eos_token_id`:50256 for open-end generation.
#>> Generated text 1

#<|startoftext|> eu amo o brasil. O termo foi usado por alguns autores como uma forma de designar a formação do poder político do Brasil. A partir da década de 1960, o termo passou a ser usado para designar a formação política do Brasil. A partir de meados da década de 1970 e até o inicio dos anos 2000, o termo foi aplicado à formação político-administrativo do país, sendo utilizado por alguns autores como uma expressão de "política de direita". História Antecedentes O termo "político-administrário" foi usado pela primeira vez em 1891 por um gru
#>> Generated text 2

#<|startoftext|> eu amo o brasil. É uma das muitas pessoas do mundo, ao contrário da maioria das pessoas, que são chamados de "pessoas do Brasil", que são chamados de "brincos do país" e que têm uma carreira de mais de um século. O termo "brincal de ouro" é usado em referências às pessoas que vivem no Brasil, e que são chamados "brincos do país", que são "cidade" e que vivem na cidade de Nova York e que vive em um país onde a maior parte das pessoas são chamados de "cidades". Hist
#>> Generated text 3

#<|startoftext|> eu amo o brasil. É uma expressão que se refere ao uso de um instrumento musical em particular para se referir à qualidade musical, o que é uma expressão da qualidade da qualidade musical de uma pessoa. A expressão "amor" (em inglês, amo), é a expressão que pode ser usada com o intuito empregado em qualquer situação em que a vontade de uma pessoa de se sentir amado ou amoroso é mais do que um desejo de uma vontade. Em geral, a expressão "amoro" (do inglês, amo) pode também se referir tanto a uma pessoa como um instrumento de cordas ou de uma
```