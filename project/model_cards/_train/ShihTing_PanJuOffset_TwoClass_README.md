---
license: apache-2.0
tags:
- vision
- image-classification
widget:
- src: https://datasets-server.huggingface.co/assets/ShihTing/IsCausewayOffset/--/ShihTing--IsCausewayOffset/validation/0/image/image.jpg
  example_title: Ex1
---
# PanJu offset detect by image
Use fintune from google/vit-base-patch16-224(https://huggingface.co/google/vit-base-patch16-224)

## Dataset
```python
DatasetDict({
    train: Dataset({
        features: ['image', 'label'],
        num_rows: 329
    })
    validation: Dataset({
        features: ['image', 'label'],
        num_rows: 56
    })
})

```
36 Break and 293 Normal in train
5 Break and 51 Normal in validation


## Intended uses 

### How to use

Here is how to use this model to classify an image of the COCO 2017 dataset into one of the 1,000 ImageNet classes:

```python
# Load image
import torch
from transformers import ViTFeatureExtractor, ViTForImageClassification,AutoModel
from PIL import Image
import requests
url='https://datasets-server.huggingface.co/assets/ShihTing/IsCausewayOffset/--/ShihTing--IsCausewayOffset/validation/0/image/image.jpg'
image = Image.open(requests.get(url, stream=True).raw)
# Load model
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
device = torch.device('cpu')
extractor = AutoFeatureExtractor.from_pretrained('ShihTing/PanJuOffset_TwoClass')
model = AutoModelForImageClassification.from_pretrained('ShihTing/PanJuOffset_TwoClass')
# Predict
inputs = extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits
Prob = outputs.logits.softmax(dim=-1).tolist()
print(Prob)
# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```

