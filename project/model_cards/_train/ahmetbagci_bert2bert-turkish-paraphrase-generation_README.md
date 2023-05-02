---
language: 
- tr
tags:
- paraphrasing
- encoder-decoder
- seq2seq
- bert
---

#Bert2Bert Turkish Paraphrase Generation

#INISTA 2021

#Comparison of Turkish Paraphrase Generation Models

#Dataset

The dataset used in model training was created with the combination of the translation of the QQP dataset and manually generated dataset.
Dataset [Link](https://drive.google.com/file/d/1-2l9EwIzXZ7fUkNW1vdeF3lzQp2pygp_/view?usp=sharing) 

#How To Use
```python
from transformers import BertTokenizerFast,EncoderDecoderModel
tokenizer=BertTokenizerFast.from_pretrained("dbmdz/bert-base-turkish-cased")
model = EncoderDecoderModel.from_pretrained("ahmetbagci/bert2bert-turkish-paraphrase-generation")

text="son model arabalar çevreye daha mı az zarar veriyor?"
input_ids = tokenizer(text, return_tensors="pt").input_ids
output_ids = model.generate(input_ids)
print(tokenizer.decode(output_ids[0], skip_special_tokens=True))
#sample output
#son model arabalar çevre için daha az zararlı mı?
```
#Cite
```bibtex

@INPROCEEDINGS{9548335,  
author={Bağcı, Ahmet and Amasyali, Mehmet Fatih},  
booktitle={2021 International Conference on INnovations in Intelligent SysTems and Applications (INISTA)},   
title={Comparison of Turkish Paraphrase Generation Models},   
year={2021},  
volume={},  
number={},  
pages={1-6},  
doi={10.1109/INISTA52262.2021.9548335}
}
```