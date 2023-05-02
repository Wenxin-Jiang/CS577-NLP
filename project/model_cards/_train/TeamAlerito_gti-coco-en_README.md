---
tags:
- image-classification
library_name: generic
---

## Example

The model is by no means a state-of-the-art model, but nevertheless
produces reasonable image captioning results. It was mainly fine-tuned 
as a proof-of-concept for the 🤗 FlaxVisionEncoderDecoder Framework.

The model can be used as follows:

**In PyTorch**
```python

import torch
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, AutoTokenizer, VisionEncoderDecoderModel


loc = "ydshieh/vit-gpt2-coco-en"

feature_extractor = ViTFeatureExtractor.from_pretrained(loc)
tokenizer = AutoTokenizer.from_pretrained(loc)
model = VisionEncoderDecoderModel.from_pretrained(loc)
model.eval()


def predict(image):

    pixel_values = feature_extractor(images=image, return_tensors="pt").pixel_values

    with torch.no_grad():
        output_ids = model.generate(pixel_values, max_length=16, num_beams=4, return_dict_in_generate=True).sequences

    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]

    return preds


# We will verify our results on an image of cute cats
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
with Image.open(requests.get(url, stream=True).raw) as image:
    preds = predict(image)

print(preds)
# should produce
# ['a cat laying on top of a couch next to another cat']

```

**In Flax**
```python

import jax
import requests
from PIL import Image
from transformers import ViTFeatureExtractor, AutoTokenizer, FlaxVisionEncoderDecoderModel


loc = "ydshieh/vit-gpt2-coco-en"

feature_extractor = ViTFeatureExtractor.from_pretrained(loc)
tokenizer = AutoTokenizer.from_pretrained(loc)
model = FlaxVisionEncoderDecoderModel.from_pretrained(loc)

gen_kwargs = {"max_length": 16, "num_beams": 4}


# This takes sometime when compiling the first time, but the subsequent inference will be much faster
@jax.jit
def generate(pixel_values):
    output_ids = model.generate(pixel_values, **gen_kwargs).sequences
    return output_ids
    
    
def predict(image):

    pixel_values = feature_extractor(images=image, return_tensors="np").pixel_values
    output_ids = generate(pixel_values)
    preds = tokenizer.batch_decode(output_ids, skip_special_tokens=True)
    preds = [pred.strip() for pred in preds]
    
    return preds
    
    
# We will verify our results on an image of cute cats
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
with Image.open(requests.get(url, stream=True).raw) as image:
    preds = predict(image)
    
print(preds)
# should produce
# ['a cat laying on top of a couch next to another cat']

```