---
license: apache-2.0
tags:
- vision
- image-classification
datasets:
- tarshnet
widget:
- src: https://www.estal.com/FitxersWeb/331958/estal_carroussel_wg_spirits_5.jpg
  example_title: Glass
- src: https://origamijapan.net/wp-content/uploads/2013/10/2_600-1.jpg
  example_title: Paper
- src: https://i0.wp.com/makezine.com/wp-content/uploads/2016/03/AdobeStock_79098618METAL.jpeg?ssl=1
  example_title: Metal
---

# Vision Transformer (base-sized model) 

Vision Transformer (ViT) model pre-trained on ImageNet-21k (14 million images, 21,843 classes) at resolution 224x224, and fine-tuned on ImageNet 2012 (1 million images, 1,000 classes) at resolution 224x224. It was introduced in the paper [An Image is Worth 16x16 Words: Transformers for Image Recognition at Scale](https://arxiv.org/abs/2010.11929) by Dosovitskiy et al. and first released in [this repository](https://github.com/google-research/vision_transformer). However, the weights were converted from the [timm repository](https://github.com/rwightman/pytorch-image-models) by Ross Wightman, who already converted the weights from JAX to PyTorch. Credits go to him. 

Disclaimer: The team releasing ViT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Dataset

The dataset used consist of  spans six classes: glass, paper, cardboard, plastic, metal, and trash. Currently, the dataset consists of 2527 images:

* 501 glass
* 594 paper
* 403 cardboard
* 482 plastic
* 410 metal
* 137 trash
## Fine_tuned Notebook

This notebook outlines the steps from preparing the data in the Vit-acceptable format to training the model [Notebook](https://colab.research.google.com/drive/1RbmRPJ9bFLA_qK9RGgPoHZRnUTy_md5O?usp=sharing)

### How to use

Just copy this lines below: 

```python
from transformers import AutoFeatureExtractor, AutoModelForImageClassification
from PIL import Image
import requests
url = 'https://www.estal.com/FitxersWeb/331958/estal_carroussel_wg_spirits_5.jpg'
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = AutoFeatureExtractor.from_pretrained("Aalaa/Fine_tuned_Vit_trash_classification")
model = AutoModelForImageClassification.from_pretrained("Aalaa/Fine_tuned_Vit_trash_classification")

inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits

predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```

For more code examples, we refer to the [documentation](https://huggingface.co/transformers/model_doc/vit.html#).
