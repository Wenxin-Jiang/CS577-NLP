---
license: other
tags:
- vision
- image-segmentation
datasets:
- pascal-voc
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-2.jpg
  example_title: Cat
---

# MobileNetV2 with DeepLabV3+

MobileNet V2 model pre-trained on PASCAL VOC at resolution 513x513. It was introduced in [MobileNetV2: Inverted Residuals and Linear Bottlenecks](https://arxiv.org/abs/1801.04381) by Mark Sandler, Andrew Howard, Menglong Zhu, Andrey Zhmoginov, Liang-Chieh Chen. It was first released in [this repository](https://github.com/tensorflow/models/tree/master/research/deeplab).

Disclaimer: The team releasing MobileNet V2 did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

From the [original README](https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md):

> MobileNets are small, low-latency, low-power models parameterized to meet the resource constraints of a variety of use cases. They can be built upon for classification, detection, embeddings and segmentation similar to how other popular large scale models, such as Inception, are used. MobileNets can be run efficiently on mobile devices [...] MobileNets trade off between latency, size and accuracy while comparing favorably with popular models from the literature.

The model in this repo adds a [DeepLabV3+](https://arxiv.org/abs/1802.02611) head to the MobileNetV2 backbone for semantic segmentation.

## Intended uses & limitations

You can use the raw model for semantic segmentation. See the [model hub](https://huggingface.co/models?search=mobilenet_v2) to look for fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model:

```python
from transformers import MobileNetV2FeatureExtractor, MobileNetV2ForSemanticSegmentation
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = MobileNetV2FeatureExtractor.from_pretrained("Matthijs/deeplabv3_mobilenet_v2_1.0_513")
model = MobileNetV2ForSemanticSegmentation.from_pretrained("Matthijs/deeplabv3_mobilenet_v2_1.0_513")

inputs = feature_extractor(images=image, return_tensors="pt")

outputs = model(**inputs)
logits = outputs.logits
predicted_mask = logits.argmax(1).squeeze(0)
```

Currently, both the feature extractor and model support PyTorch.

### BibTeX entry and citation info

```bibtex
@inproceedings{deeplabv3plus2018,
  title={Encoder-Decoder with Atrous Separable Convolution for Semantic Image Segmentation},
  author={Liang-Chieh Chen and Yukun Zhu and George Papandreou and Florian Schroff and Hartwig Adam},
  booktitle={ECCV},
  year={2018}
}
```
