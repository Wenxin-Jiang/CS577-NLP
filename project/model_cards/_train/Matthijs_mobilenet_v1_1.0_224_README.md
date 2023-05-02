---
license: other
tags:
- vision
- image-classification
datasets:
- imagenet-1k
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg
  example_title: Tiger
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/teapot.jpg
  example_title: Teapot
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg
  example_title: Palace
---

# MobileNet V1

MobileNet V1 model pre-trained on ImageNet-1k at resolution 224x224. It was introduced in [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) by Howard et al, and first released in [this repository](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md).

Disclaimer: The team releasing MobileNet V1 did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

From the [original README](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md):

> MobileNets are small, low-latency, low-power models parameterized to meet the resource constraints of a variety of use cases. They can be built upon for classification, detection, embeddings and segmentation similar to how other popular large scale models, such as Inception, are used. MobileNets can be run efficiently on mobile devices [...] MobileNets trade off between latency, size and accuracy while comparing favorably with popular models from the literature.

## Intended uses & limitations

You can use the raw model for image classification. See the [model hub](https://huggingface.co/models?search=mobilenet_v1) to look for fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model to classify an image of the COCO 2017 dataset into one of the 1,000 ImageNet classes:

```python
from transformers import MobileNetV1FeatureExtractor, MobileNetV1ForImageClassification
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = MobileNetV1FeatureExtractor.from_pretrained("Matthijs/mobilenet_v1_1.0_224")
model = MobileNetV1ForImageClassification.from_pretrained("Matthijs/mobilenet_v1_1.0_224")

inputs = feature_extractor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits

# model predicts one of the 1000 ImageNet classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```

Note: This model actually predicts 1001 classes, the 1000 classes from ImageNet plus an extra “background” class (index 0).

Currently, both the feature extractor and model support PyTorch.
