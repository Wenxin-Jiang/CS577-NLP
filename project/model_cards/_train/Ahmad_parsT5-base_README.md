A monolingual T5 model for Persian trained on OSCAR 21.09 (https://oscar-corpus.com/) corpus with self-supervised method. 35 Gig deduplicated version of Persian data was used for pre-training the model.

It's similar to the English T5 model but just for Persian. You may need to fine-tune it on your specific task. 

Example code:

```
from transformers import T5ForConditionalGeneration,AutoTokenizer

import torch

model_name = "Ahmad/parsT5-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

input_ids = tokenizer.encode('دانش آموزان به <extra_id_0> میروند و <extra_id_1> میخوانند.', return_tensors='pt')
with torch.no_grad():
    hypotheses = model.generate(input_ids)
for h in hypotheses:
    print(tokenizer.decode(h))
```




Steps: 725000

Accuracy: 0.66

Training More?
========

To train the model further please refer to its github repository at:

https://github.com/puraminy/parsT5
