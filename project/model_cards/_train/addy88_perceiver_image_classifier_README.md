### How to use
Here is how to use this model in PyTorch:
```python
from transformers import PerceiverFeatureExtractor, PerceiverForImageClassificationLearned
import requests
from PIL import Image
feature_extractor = PerceiverFeatureExtractor.from_pretrained("addy88/perceiver_image_classifier")
model = PerceiverForImageClassificationLearned.from_pretrained("addy88/perceiver_image_classifier")
url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)
# prepare input
encoding = feature_extractor(image, return_tensors="pt")
inputs = encoding.pixel_values
# forward pass
outputs = model(inputs)
logits = outputs.logits
print("Predicted class:", model.config.id2label[logits.argmax(-1).item()])
>>> should print Predicted class: tabby, tabby cat
```