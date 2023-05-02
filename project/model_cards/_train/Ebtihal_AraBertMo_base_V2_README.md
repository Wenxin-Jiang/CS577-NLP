---
language: ar
tags: Fill-Mask 
datasets: OSCAR
widget:
- text: " السلام عليكم ورحمة[MASK] وبركاتة"
- text: " اهلا وسهلا بكم في [MASK] من سيربح المليون"
- text: " مرحبا بك عزيزي الزائر [MASK] موقعنا "

---

# Arabic BERT Model
**AraBERTMo** is an Arabic pre-trained language model based on [Google's BERT architechture](https://github.com/google-research/bert). 
AraBERTMo_base uses the same BERT-Base config. 
AraBERTMo_base now comes in 10 new variants
All models are available on the `HuggingFace` model page under the [Ebtihal](https://huggingface.co/Ebtihal/) name. 
Checkpoints are available in PyTorch formats.

## Pretraining Corpus
`AraBertMo_base_V2' model was pre-trained on ~3 million words:
- [OSCAR](https://traces1.inria.fr/oscar/) - Arabic version "unshuffled_deduplicated_ar". 

## Training results
this model achieves the following results:

| Task | Num examples | Num Epochs  | Batch Size | steps | Wall time  | training loss| 
|:----:|:----:|:----:|:----:|:-----:|:----:|:-----:|
| Fill-Mask| 20020|  2  | 64 | 626  | 19m 2s | 8.437  | 

## Load Pretrained Model
You can use this model by installing `torch` or `tensorflow` and Huggingface library `transformers`. And you can use it directly by initializing it like this:  
```python
from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("Ebtihal/AraBertMo_base_V2")
model = AutoModelForMaskedLM.from_pretrained("Ebtihal/AraBertMo_base_V2")
```

 ## This model was built for master's degree research in an organization:
- [University of kufa](https://uokufa.edu.iq/).
- [Faculty of Computer Science and Mathematics](https://mathcomp.uokufa.edu.iq/).
- **Department of Computer Science**

