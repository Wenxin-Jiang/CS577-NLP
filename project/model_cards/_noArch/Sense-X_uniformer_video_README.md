---
license: mit
tags:
- vision
- video-classification
datasets:
- kinetics-400
- kinetics-600
- something-something-v1
- something-something-v2
---

# UniFormer (video model) 

UniFormer models are trained on [Kinetics](https://deepmind.com/research/open-source/kinetics) and [Something-Something](https://20bn.com/datasets/something-something) at resolution 224x224. 
It was introduced in the paper [UniFormer: Unified Transformer for Efficient Spatial-Temporal Representation Learning](https://arxiv.org/abs/2201.04676) by Li et al,
and first released in [this repository](https://github.com/Sense-X/UniFormer). 


## Model description

The UniFormer is a type of Vision Transformer, which can seamlessly integrate merits of convolution and self-attention in a concise transformer format. 
It adopt local MHRA in shallow layers to largely reduce computation burden and global MHRA in deep layers to learn global token relation. 

Without any extra training data, 
UniFormer achieves **86.3** top-1 accuracy on ImageNet-1K classification. 
With only ImageNet-1K pre-training, it can simply achieve state-of-the-art performance in a broad range of downstream tasks. 
UniFormer obtains **82.9/84.8** top-1 accuracy on Kinetics-400/600, 
and **60.9/71.2** top-1 accuracy on Something-Something V1/V2 video classification tasks. 
It also achieves **53.8** box AP and **46.4** mask AP on COCO object detection task, 
**50.8** mIoU on ADE20K semantic segmentation task, 
and **77.4** AP on COCO pose estimation task. 

![teaser](framework.png)

[Source](https://paperswithcode.com/paper/uniformer-unified-transformer-for-efficient)

## Intended uses & limitations

You can use the raw model for video classification.
We now only upload the powerful models with **single clip**.
More models can be found in [the model hub](https://github.com/Sense-X/UniFormer/tree/main/video_classification).

### Kinetics
| Model       | #Frame | Sampling Stride | FLOPs | K400 Top-1 | K600 Top-1 |
| ----------- | ------ | --------------- | ----- | ---------- | ---------- |
| UniFormer-S | 16x1x1 | 8            | 41.8G  | 78.4       | 80.8       |
| UniFormer-B | 16x1x1 | 8            | 96.7G  | 79.3       | 81.7       |
| UniFormer-B | 32x1x1 | 4            | 259G | 80.9       | 82.4       |


### Something-Something
| Model       | #Frame | FLOPs | SSV1 Top-1 | SSV2 Top-1 |
| ----------- | ------ | ----- | ---------- | ---------- |
| UniFormer-S | 16x1x1 | 41.8G  | 54.4       | 65.0       |
| UniFormer-B | 32x1x1 | 259G   | 58.0       | 67.5       |


### How to use

You can followed our [demo](https://huggingface.co/spaces/Sense-X/uniformer_video_demo/tree/main) to use our models.

```python
from uniformer import uniformer_small
from kinetics_class_index import kinetics_classnames


model = uniformer_small()
# load state
model_path = hf_hub_download(repo_id="Sense-X/uniformer_video", filename="uniformer_small_k400_16x8.pth")
state_dict = torch.load(model_path, map_location='cpu')
model.load_state_dict(state_dict)
# set to eval mode
model = model.to(device)
model = model.eval()

# please refer to the following url to process video of Kinetics:
# https://huggingface.co/spaces/Sense-X/uniformer_video_demo/blob/main/app.py
vid = load_video(video)

# model predicts one of the 400 Kintics classes
prediction = model(vid)
predicted_class_idx = prediction.flatten().argmax(-1).item()
print("Predicted class:", kinetics_classnames[str(predicted_class_idx)])
```


### BibTeX entry and citation info

```bibtex
@misc{li2022uniformer,
      title={UniFormer: Unified Transformer for Efficient Spatiotemporal Representation Learning}, 
      author={Kunchang Li and Yali Wang and Peng Gao and Guanglu Song and Yu Liu and Hongsheng Li and Yu Qiao},
      year={2022},
      eprint={2201.04676},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```