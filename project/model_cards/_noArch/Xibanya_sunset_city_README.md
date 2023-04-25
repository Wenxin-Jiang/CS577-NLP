---
license: cc-by-sa-4.0
language:
- ru
- en
pipeline_tag: text-to-image
tags:
- PyTorch
- Transformers
---
# Sunset Cities
This is the [Malevich](https://huggingface.co/sberbank-ai/rudalle-Malevich) ruDALL-E model finetuned on anime screenshots of big cities at sunset.
<img style="text-align:center; display:block;" src="https://huggingface.co/Xibanya/sunset_city/resolve/main/citysunset.png" width="256">

### installation
```
pip install rudalle
```

### How to use
Basic implementation to get a list of image data objects.

```python
from translate import Translator
from rudalle import get_rudalle_model, get_tokenizer, get_vae
from rudalle.pipelines import generate_images

model = get_rudalle_model('Malevich', pretrained=True, fp16=True, device='cuda')
model.load_state_dict(torch.load(CHECKPOINT_PATH))
vae = get_vae().to('cuda')
tokenizer = get_tokenizer()
input_text = Translator(to_lang='ru').translate('city at sunset')
images, _ = generate_images(
        text=input_text,
        tokenizer=tokenizer, dalle=model, vae=vae,
        images_num=1,
        top_k=2048,
        top_p=0.95,
        temperature=1.0
    )
```

the Malevich model only recognizes input in Russian. If you're going to paste Cyrillic directly into the code rather than filter an English prompt through the translate API, you will need to put this at the top of the file:

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
```