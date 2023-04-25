---
tags:
- autotrain
- vision
- image-classification
datasets:
- juliensimon/autotrain-data-food101
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/tiger.jpg
  example_title: Tiger
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/teapot.jpg
  example_title: Teapot
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/palace.jpg
  example_title: Palace
co2_eq_emissions:
  emissions: 179.11544810549532
---

# Usage

```
from transformers import pipeline
p = pipeline("image-classification", model="juliensimon/autotrain-food101-1471154053")
result = p("my_image.jpg")
```

# Model Trained Using AutoTrain

- Problem type: Multi-class Classification
- Model ID: 1471154053
- CO2 Emissions (in grams): 179.1154

## Validation Metrics

- Loss: 0.301
- Accuracy: 0.915
- Macro F1: 0.915
- Micro F1: 0.915
- Weighted F1: 0.915
- Macro Precision: 0.917
- Micro Precision: 0.915
- Weighted Precision: 0.917
- Macro Recall: 0.915
- Micro Recall: 0.915
- Weighted Recall: 0.915