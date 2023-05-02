---
license: "cc-by-nc-4.0"
tags:
- vision
- video-classification
---

# VideoMAE (base-sized model, pre-trained only) 

VideoMAE model pre-trained on Something-Something-v2 for 2400 epochs in a self-supervised way. It was introduced in the paper [VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training](https://arxiv.org/abs/2203.12602) by Tong et al. and first released in [this repository](https://github.com/MCG-NJU/VideoMAE). 

Disclaimer: The team releasing VideoMAE did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

VideoMAE is an extension of [Masked Autoencoders (MAE)](https://arxiv.org/abs/2111.06377) to video. The architecture of the model is very similar to that of a standard Vision Transformer (ViT), with a decoder on top for predicting pixel values for masked patches.

Videos are presented to the model as a sequence of fixed-size patches (resolution 16x16), which are linearly embedded. One also adds a [CLS] token to the beginning of a sequence to use it for classification tasks. One also adds fixed sinus/cosinus position embeddings before feeding the sequence to the layers of the Transformer encoder.

By pre-training the model, it learns an inner representation of videos that can then be used to extract features useful for downstream tasks: if you have a dataset of labeled videos for instance, you can train a standard classifier by placing a linear layer on top of the pre-trained encoder. One typically places a linear layer on top of the [CLS] token, as the last hidden state of this token can be seen as a representation of an entire video.

## Intended uses & limitations

You can use the raw model for predicting pixel values for masked patches of a video, but it's mostly intended to be fine-tuned on a downstream task. See the [model hub](https://huggingface.co/models?filter=videomae) to look for fine-tuned versions on a task that interests you.

### How to use

Here is how to use this model to predict pixel values for randomly masked patches:

```python
from transformers import VideoMAEFeatureExtractor, VideoMAEForPreTraining
import numpy as np
import torch

num_frames = 16
video = list(np.random.randn(16, 3, 224, 224))

feature_extractor = VideoMAEFeatureExtractor.from_pretrained("MCG-NJU/videomae-base-short-ssv2")
model = VideoMAEForPreTraining.from_pretrained("MCG-NJU/videomae-base-short-ssv2")

pixel_values = feature_extractor(video, return_tensors="pt").pixel_values

num_patches_per_frame = (model.config.image_size // model.config.patch_size) ** 2
seq_length = (num_frames // model.config.tubelet_size) * num_patches_per_frame
bool_masked_pos = torch.randint(0, 2, (1, seq_length)).bool()

outputs = model(pixel_values, bool_masked_pos=bool_masked_pos)
loss = outputs.loss
```

For more code examples, we refer to the [documentation](https://huggingface.co/transformers/main/model_doc/videomae.html#).

## Training data

(to do, feel free to open a PR)

## Training procedure

### Preprocessing

(to do, feel free to open a PR)

### Pretraining

(to do, feel free to open a PR)

## Evaluation results

(to do, feel free to open a PR)

### BibTeX entry and citation info

```bibtex
misc{https://doi.org/10.48550/arxiv.2203.12602,
  doi = {10.48550/ARXIV.2203.12602},
  url = {https://arxiv.org/abs/2203.12602},
  author = {Tong, Zhan and Song, Yibing and Wang, Jue and Wang, Limin},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {VideoMAE: Masked Autoencoders are Data-Efficient Learners for Self-Supervised Video Pre-Training},
  publisher = {arXiv},
  year = {2022},
  copyright = {Creative Commons Attribution 4.0 International}
}
```