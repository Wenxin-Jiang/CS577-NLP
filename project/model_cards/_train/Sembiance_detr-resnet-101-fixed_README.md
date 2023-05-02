---
license: apache-2.0
tags:
- object-detection
- vision
datasets:
- coco
widget:
- src: >-
    https://huggingface.co/datasets/mishig/sample_images/resolve/main/savanna.jpg
  example_title: Savanna
- src: >-
    https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  example_title: Football Match
- src: >-
    https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg
  example_title: Airport
duplicated_from: facebook/detr-resnet-101
---

# DETR (End-to-End Object Detection) model with ResNet-101 backbone

DEtection TRansformer (DETR) model trained end-to-end on COCO 2017 object detection (118k annotated images). It was introduced in the paper [End-to-End Object Detection with Transformers](https://arxiv.org/abs/2005.12872) by Carion et al. and first released in [this repository](https://github.com/facebookresearch/detr). 

Disclaimer: The team releasing DETR did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

The DETR model is an encoder-decoder transformer with a convolutional backbone. Two heads are added on top of the decoder outputs in order to perform object detection: a linear layer for the class labels and a MLP (multi-layer perceptron) for the bounding boxes. The model uses so-called object queries to detect objects in an image. Each object query looks for a particular object in the image. For COCO, the number of object queries is set to 100. 

The model is trained using a "bipartite matching loss": one compares the predicted classes + bounding boxes of each of the N = 100 object queries to the ground truth annotations, padded up to the same length N (so if an image only contains 4 objects, 96 annotations will just have a "no object" as class and "no bounding box" as bounding box). The Hungarian matching algorithm is used to create an optimal one-to-one mapping between each of the N queries and each of the N annotations. Next, standard cross-entropy (for the classes) and a linear combination of the L1 and generalized IoU loss (for the bounding boxes) are used to optimize the parameters of the model.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/model_doc/detr_architecture.png)

## Intended uses & limitations

You can use the raw model for object detection. See the [model hub](https://huggingface.co/models?search=facebook/detr) to look for all available DETR models.

### How to use

Here is how to use this model:

```python
from transformers import DetrFeatureExtractor, DetrForObjectDetection
import torch
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

feature_extractor = DetrFeatureExtractor.from_pretrained("facebook/detr-resnet-101")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-101")

inputs = feature_extractor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
target_sizes = torch.tensor([image.size[::-1]])
results = feature_extractor.post_process(outputs, target_sizes=target_sizes)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    # let's only keep detections with score > 0.9
    if score > 0.9:
        print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
        )
```
This should output (something along the lines of):
```
Detected cat with confidence 0.998 at location [344.06, 24.85, 640.34, 373.74]
Detected remote with confidence 0.997 at location [328.13, 75.93, 372.81, 187.66]
Detected remote with confidence 0.997 at location [39.34, 70.13, 175.56, 118.78]
Detected cat with confidence 0.998 at location [15.36, 51.75, 316.89, 471.16]
Detected couch with confidence 0.995 at location [-0.19, 0.71, 639.73, 474.17]
```

Currently, both the feature extractor and model support PyTorch. 

## Training data

The DETR model was trained on [COCO 2017 object detection](https://cocodataset.org/#download), a dataset consisting of 118k/5k annotated images for training/validation respectively. 

## Training procedure

### Preprocessing

The exact details of preprocessing of images during training/validation can be found [here](https://github.com/google-research/vision_transformer/blob/master/vit_jax/input_pipeline.py). 

Images are resized/rescaled such that the shortest side is at least 800 pixels and the largest side at most 1333 pixels, and normalized across the RGB channels with the ImageNet mean (0.485, 0.456, 0.406) and standard deviation (0.229, 0.224, 0.225).

### Training

The model was trained for 300 epochs on 16 V100 GPUs. This takes 3 days, with 4 images per GPU (hence a total batch size of 64).

## Evaluation results

This model achieves an AP (average precision) of **43.5** on COCO 2017 validation. For more details regarding evaluation results, we refer to table 1 of the original paper.
### BibTeX entry and citation info

```bibtex
@article{DBLP:journals/corr/abs-2005-12872,
  author    = {Nicolas Carion and
               Francisco Massa and
               Gabriel Synnaeve and
               Nicolas Usunier and
               Alexander Kirillov and
               Sergey Zagoruyko},
  title     = {End-to-End Object Detection with Transformers},
  journal   = {CoRR},
  volume    = {abs/2005.12872},
  year      = {2020},
  url       = {https://arxiv.org/abs/2005.12872},
  archivePrefix = {arXiv},
  eprint    = {2005.12872},
  timestamp = {Thu, 28 May 2020 17:38:09 +0200},
  biburl    = {https://dblp.org/rec/journals/corr/abs-2005-12872.bib},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
```