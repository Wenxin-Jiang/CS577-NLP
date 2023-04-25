---
tags:
- dit
- vision
- image-classification
datasets:
- rvl_cdip
widget:
- src: https://huggingface.co/microsoft/dit-base-finetuned-rvlcdip/resolve/main/coca_cola_advertisement.png
  example_title: Advertisement
- src: https://huggingface.co/microsoft/dit-base-finetuned-rvlcdip/resolve/main/scientific_publication.png
  example_title: Scientific publication
---

# Document Image Transformer (base-sized model) 

Document Image Transformer (DiT) model pre-trained on IIT-CDIP (Lewis et al., 2006), a dataset that includes 42 million document images and fine-tuned on [RVL-CDIP](https://www.cs.cmu.edu/~aharley/rvl-cdip/), a dataset consisting of 400,000 grayscale images in 16 classes, with 25,000 images per class. It was introduced in the paper [DiT: Self-supervised Pre-training for Document Image Transformer](https://arxiv.org/abs/2203.02378) by Li et al. and first released in [this repository](https://github.com/microsoft/unilm/tree/master/dit). Note that DiT is identical to the architecture of [BEiT](https://huggingface.co/docs/transformers/model_doc/beit). 

Disclaimer: The team releasing DiT did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

The Document Image Transformer (DiT) is a transformer encoder model (BERT-like) pre-trained on a large collection of images in a self-supervised fashion. The pre-training objective for the model is to predict visual tokens from the encoder of a discrete VAE (dVAE), based on masked patches.

Images are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. One also adds absolute position embeddings before feeding the sequence to the layers of the Transformer encoder.

By pre-training the model, it learns an inner representation of images that can then be used to extract features useful for downstream tasks: if you have a dataset of labeled document images for instance, you can train a standard classifier by placing a linear layer on top of the pre-trained encoder.

## Intended uses & limitations

You can use the raw model for encoding document images into a vector space, but it's mostly meant to be fine-tuned on tasks like document image classification, table detection or document layout analysis. See the [model hub](https://huggingface.co/models?search=microsoft/dit) to look for fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model in PyTorch:

```python
from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from PIL import Image

image = Image.open('path_to_your_document_image').convert('RGB')

processor = AutoImageProcessor.from_pretrained("microsoft/dit-base-finetuned-rvlcdip")
model = AutoModelForImageClassification.from_pretrained("microsoft/dit-base-finetuned-rvlcdip")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)
logits = outputs.logits

# model predicts one of the 16 RVL-CDIP classes
predicted_class_idx = logits.argmax(-1).item()
print("Predicted class:", model.config.id2label[predicted_class_idx])
```

### BibTeX entry and citation info

```bibtex
@article{Lewis2006BuildingAT,
  title={Building a test collection for complex document information processing},
  author={David D. Lewis and Gady Agam and Shlomo Engelson Argamon and Ophir Frieder and David A. Grossman and Jefferson Heard},
  journal={Proceedings of the 29th annual international ACM SIGIR conference on Research and development in information retrieval},
  year={2006}
}
```