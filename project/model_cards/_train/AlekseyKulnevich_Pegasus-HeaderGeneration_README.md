**Usage HuggingFace Transformers for header generation task**
``` 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("AlekseyKulnevich/Pegasus-HeaderGeneration")
tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-large')
input_text # your text 
input_ = tokenizer.batch_encode_plus([input_text], max_length=1024, pad_to_max_length=True, 
                truncation=True, padding='longest', return_tensors='pt')
input_ids = input_['input_ids'] 
input_mask = input_['attention_mask']
headers = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         num_beams=32, 
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         num_return_sequences=10)
headers = tokenizer.batch_decode(headers, skip_special_tokens=True)
```
**Decoder configuration examples:**  
[**Input text you can see here**](https://www.bbc.com/news/science-environment-59775105)  
```
headers = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         num_beams=32, 
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         num_return_sequences=20)
tokenizer.batch_decode(headers, skip_special_tokens=True)
```
output: 
1. *the impact of climate change on tropical cyclones*
2. *the impact of human induced climate change on tropical cyclones*
3. *the impact of climate change on tropical cyclone formation in the midlatitudes*
4. *how climate change will expand the range of tropical cyclones?*
5. *the impact of climate change on tropical cyclones in the midlatitudes*
6. *global warming will expand the range of tropical cyclones*
7. *climate change will expand the range of tropical cyclones*
8. *the impact of climate change on tropical cyclone formation*
9. *the impact of human induced climate change on tropical cyclone formation*
10. *tropical cyclones in the mid-latitudes*
11. *climate change will expand the range of tropical cyclones in the middle latitudes*
12. *global warming will expand the range of tropical cyclones, a new study says*
13. *the impacts of climate change on tropical cyclones*
14. *the impact of global warming on tropical cyclones*
15. *climate change will expand the range of tropical cyclones, a new study says*
16. *global warming will expand the range of tropical cyclones in the middle latitudes*
17. *the effects of climate change on tropical cyclones*
18. *how climate change will expand the range of tropical cyclones*
19. *climate change will expand the range of tropical cyclones over the equator*
20. *the impact of human induced climate change on tropical cyclones.*
Also you can play with the following parameters in generate method:   
-top_k  
-top_p  
[**Meaning of parameters to generate text you can see here**](https://huggingface.co/blog/how-to-generate)