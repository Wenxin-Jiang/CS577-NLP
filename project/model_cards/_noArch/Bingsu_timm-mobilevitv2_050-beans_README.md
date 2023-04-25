---
tags:
- image-classification
- timm
library_tag: timm
datasets:
- beans
widget:
- src: https://huggingface.co/nateraw/vit-base-beans/resolve/main/healthy.jpeg
  example_title: Healthy
- src: https://huggingface.co/nateraw/vit-base-beans/resolve/main/angular_leaf_spot.jpeg
  example_title: Angular Leaf Spot
- src: https://huggingface.co/nateraw/vit-base-beans/resolve/main/bean_rust.jpeg
  example_title: Bean Rust
---
# Model card for timm-mobilevitv2_050-beans

This model is a fine-tuned version of `mobilevitv2_050` (from timm) on the `beans` dataset. It achieves the following results on the validation set:

- Loss: 0.08228
- Accuracy: 0.9850
- F1Score: 0.9846

## Image normalization

Imagenet

```python
mean = [0.485, 0.456, 0.406]
std = [0.229, 0.224, 0.225]
```