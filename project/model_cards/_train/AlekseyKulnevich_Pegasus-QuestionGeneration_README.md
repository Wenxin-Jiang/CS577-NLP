**Usage HuggingFace Transformers for question generation task**
``` 
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
model = AutoModelForSeq2SeqLM.from_pretrained("AlekseyKulnevich/Pegasus-QuestionGeneration")
tokenizer = PegasusTokenizer.from_pretrained('google/pegasus-large')
input_text # your text 
input_ = tokenizer.batch_encode_plus([input_text], max_length=1024, pad_to_max_length=True, 
                truncation=True, padding='longest', return_tensors='pt')
input_ids = input_['input_ids'] 
input_mask = input_['attention_mask']
questions = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         num_beams=32, 
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         num_return_sequences=10)

questions = tokenizer.batch_decode(questions, skip_special_tokens=True)
```

**Decoder configuration examples:**  

[**Input text you can see here**](https://www.bbc.com/news/science-environment-59775105)  
```
questions = model.generate(input_ids=input_ids, 
                         attention_mask=input_mask, 
                         num_beams=32, 
                         no_repeat_ngram_size=2, 
                         early_stopping=True, 
                         num_return_sequences=10)

tokenizer.batch_decode(questions, skip_special_tokens=True)
```
output: 
1. *What is the impact of human induced climate change on tropical cyclones?*
2. *What is the impact of climate change on tropical cyclones?*
3. *What is the impact of human induced climate change on tropical cyclone formation?*
4. *How many tropical cyclones will occur in the mid-latitudes?*
5. *What is the impact of climate change on the formation of tropical cyclones?*
6. *Is it possible for a tropical cyclone to form in the middle latitudes?*
7. *How many tropical cyclones will be formed in the mid-latitudes?*
8. *How many tropical cyclones will there be in the mid-latitudes?*
9. *How many tropical cyclones will form in the mid-latitudes?*
10. *What is the impact of global warming on tropical cyclones?*
11. *How long does it take for a tropical cyclone to form?*
12. 'What are the impacts of climate change on tropical cyclones?*
13. *What are the effects of climate change on tropical cyclones?*
14. *How many tropical cyclones will be able to form in the middle latitudes?*
15. *What is the impact of climate change on tropical cyclone formation?*
16. *What is the effect of climate change on tropical cyclones?*
17. *How long does it take for a tropical cyclone to form in the middle latitude?*
18. *How many tropical cyclones will occur in the middle latitudes?*
19. *How many tropical cyclones are likely to form in the midlatitudes?*
20. *How many tropical cyclones are likely to form in the middle latitudes?*
21. *How many tropical cyclones are expected to form in the midlatitudes?*
22. *How many tropical cyclones will be formed in the middle latitudes?*
23. *How many tropical cyclones will there be in the middle latitudes?*
24. *How long will it take for a tropical cyclone to form in the middle latitude?*
25. *What is the impact of global warming on tropical cyclone formation?*
26. *How many tropical cyclones will form in the middle latitudes?*
27. *How many tropical cyclones can we expect to form in the middle latitudes?*
28. *Is it possible for a tropical cyclone to form in the middle latitude?*
29. *What is the effect of climate change on tropical cyclone formation?*
30. *What are the effects of climate change on tropical cyclone formation?*

Also you can play with the following parameters in generate method:   
-top_k  
-top_p  

[**Meaning of parameters to generate text you can see here**](https://huggingface.co/blog/how-to-generate)