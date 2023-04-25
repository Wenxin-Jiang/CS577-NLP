---
tags:
- image-classification
library_name: generic
---

# Dog vs Cat Image Classification with FastAI CNN

Training is based in FastAI [Quick Start](https://docs.fast.ai/quick_start.html). Example training


## Training

The model was trained as follows

```python
path = untar_data(URLs.PETS)/'images'

def is_cat(x): return x[0].isupper()
dls = ImageDataLoaders.from_name_func(
    path, get_image_files(path), valid_pct=0.2, seed=42,
    label_func=is_cat, item_tfms=Resize(224))

learn = cnn_learner(dls, resnet34, metrics=error_rate)
learn.fine_tune(1)
```