**Usage HuggingFace Transformers for summarization task**
``` 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("AlekseyKulnevich/Pegasus-Summarization")
tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-large')
input_text # your text 
input_ = tokenizer.batch_encode_plus([input_text], max_length=1024, pad_to_max_length=True, 
                truncation=True, padding='longest', return_tensors='pt')
input_ids = input_['input_ids'] 
input_mask = input_['attention_mask']
summary = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         num_beams=32, 
                         min_length=100,
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         num_return_sequences=10)
questions = tokenizer.batch_decode(summary, skip_special_tokens=True)
```
**Decoder configuration examples:**  
[**Input text you can see here**](https://www.bbc.com/news/science-environment-59775105)  
```
summary = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         num_beams=32, 
                         min_length=100,
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         num_return_sequences=1)

tokenizer.batch_decode(summary, skip_special_tokens=True)
```
output: 
1. *global warming will expand the range of tropical cyclones in the mid-latitudes of the world, according to a new study published by the Intergovernmental Panel on Climate change (IPCC) and the US National Oceanic and Atmospheric Administration (NOAA) The study shows that a warming climate will allow more of these types of storms to form over a wider range than they have been able to do over the past three million years. "As the climate warms, it's likely that these storms will become more frequent and more intense," said the authors of this study.*

```
summary = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         top_k=30, 
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         min_length=100,
                         num_return_sequences=1)

tokenizer.batch_decode(summary, skip_special_tokens=True)
```
output:
1. *tropical cyclones in the mid-latitudes of the world will likely form more of these types of storms, according to a new study published by the Intergovernmental Panel on Climate change (IPCC) on the impact of human induced climate change on these storms. The study shows that a warming climate will increase the likelihood of a subtropical cyclone forming over a wider range of latitudes, including the equator, than it has been for the past three million years, and that it will be more likely to form over the tropics.*

Also you can play with the following parameters in generate method:   
-top_k  
-top_p  
[**Meaning of parameters to generate text you can see here**](https://huggingface.co/blog/how-to-generate)
