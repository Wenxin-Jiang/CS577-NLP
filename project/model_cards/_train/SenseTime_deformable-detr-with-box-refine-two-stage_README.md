---
license: apache-2.0
tags:
- object-detection
- vision
datasets:
- coco
widget:
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/savanna.jpg
  example_title: Savanna
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  example_title: Football Match
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/airport.jpg
  example_title: Airport
---

# Deformable DETR model with ResNet-50 backbone, with box refinement and two stage

Deformable DEtection TRansformer (DETR), with box refinement and two stage model trained end-to-end on COCO 2017 object detection (118k annotated images). It was introduced in the paper [Deformable DETR: Deformable Transformers for End-to-End Object Detection](https://arxiv.org/abs/2010.04159) by Zhu et al. and first released in [this repository](https://github.com/fundamentalvision/Deformable-DETR). 

Disclaimer: The team releasing Deformable DETR did not write a model card for this model so this model card has been written by the Hugging Face team.

## Model description

The DETR model is an encoder-decoder transformer with a convolutional backbone. Two heads are added on top of the decoder outputs in order to perform object detection: a linear layer for the class labels and a MLP (multi-layer perceptron) for the bounding boxes. The model uses so-called object queries to detect objects in an image. Each object query looks for a particular object in the image. For COCO, the number of object queries is set to 100. 

The model is trained using a "bipartite matching loss": one compares the predicted classes + bounding boxes of each of the N = 100 object queries to the ground truth annotations, padded up to the same length N (so if an image only contains 4 objects, 96 annotations will just have a "no object" as class and "no bounding box" as bounding box). The Hungarian matching algorithm is used to create an optimal one-to-one mapping between each of the N queries and each of the N annotations. Next, standard cross-entropy (for the classes) and a linear combination of the L1 and generalized IoU loss (for the bounding boxes) are used to optimize the parameters of the model.

![model image](https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/deformable_detr_architecture.png)

## Intended uses & limitations

You can use the raw model for object detection. See the [model hub](https://huggingface.co/models?search=sensetime/deformable-detr) to look for all available Deformable DETR models.

### How to use

Here is how to use this model:

```python
from transformers import AutoImageProcessor, DeformableDetrForObjectDetection
import torch
from PIL import Image
import requests

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

processor = AutoImageProcessor.from_pretrained("SenseTime/deformable-detr-with-box-refine-two-stage")
model = DeformableDetrForObjectDetection.from_pretrained("SenseTime/deformable-detr-with-box-refine-two-stage")

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# convert outputs (bounding boxes and class logits) to COCO API
# let's only keep detections with score > 0.7
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.7)[0]

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
            f"Detected {model.config.id2label[label.item()]} with confidence "
            f"{round(score.item(), 3)} at location {box}"
    )
```

Currently, both the feature extractor and model support PyTorch. 

## Training data

The Deformable DETR model was trained on [COCO 2017 object detection](https://cocodataset.org/#download), a dataset consisting of 118k/5k annotated images for training/validation respectively. 

### BibTeX entry and citation info

```bibtex
@misc{https://doi.org/10.48550/arxiv.2010.04159,
  doi = {10.48550/ARXIV.2010.04159},
  url = {https://arxiv.org/abs/2010.04159}, 
  author = {Zhu, Xizhou and Su, Weijie and Lu, Lewei and Li, Bin and Wang, Xiaogang and Dai, Jifeng},
  keywords = {Computer Vision and Pattern Recognition (cs.CV), FOS: Computer and information sciences, FOS: Computer and information sciences},
  title = {Deformable DETR: Deformable Transformers for End-to-End Object Detection},
  publisher = {arXiv},
  year = {2020},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```