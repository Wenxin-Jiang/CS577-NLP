---
license: mit
tags:
- vision
- image-classification
datasets:
- imagenet
---

# UniFormer (image model) 

UniFormer models are trained on ImageNet at resolution 224x224. 
It was introduced in the paper [UniFormer: Unifying Convolution and Self-attention for Visual Recognition](https://arxiv.org/abs/2201.09450) by Li et al,
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

[Source](https://paperswithcode.com/paper/uniformer-unifying-convolution-and-self)

## Intended uses & limitations

You can use the raw model for image classification.
We now only upload the models trained without Token Labeling and Layer Scale.
More powerful models can be found in [the model hub](https://github.com/Sense-X/UniFormer/tree/main/image_classification).

### ImageNet
| Model           | Pretrain    | Resolution | Top-1 | #Param. | FLOPs |
| --------------- | ----------- | ---------- | ----- | ------- | ----- |
| UniFormer-S     | ImageNet-1K | 224x224    | 82.9  | 22M     | 3.6G  |
| UniFormer-S†    | ImageNet-1K | 224x224    | 83.4  | 24M     | 4.2G  |
| UniFormer-B     | ImageNet-1K | 224x224    | 83.8  | 50M     | 8.3G  |


### How to use

You can followed our [demo](https://huggingface.co/spaces/Sense-X/uniformer_image_demo/tree/main) to use our models.

```python
from uniformer import uniformer_small
from imagenet_class_index import imagenet_classnames


model = uniformer_small()
# load state
model_path = hf_hub_download(repo_id="Sense-X/uniformer_image", filename="uniformer_small_in1k.pth")
state_dict = torch.load(model_path, map_location='cpu')
model.load_state_dict(state_dict)
# set to eval mode
model = model.to(device)
model = model.eval()

# process image
image = img
image_transform = T.Compose(
[
    T.Resize(224),
    T.CenterCrop(224),
    T.ToTensor(),
    T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
]
)
image = image_transform(image)
image = image.unsqueeze(0)


# model predicts one of the 1000 ImageNet classes
prediction = model(image)
predicted_class_idx = prediction.flatten().argmax(-1).item()
print("Predicted class:", imagenet_classnames[str(predicted_class_idx)][1])
```


### BibTeX entry and citation info

```bibtex
@misc{li2022uniformer,
      title={UniFormer: Unifying Convolution and Self-attention for Visual Recognition}, 
      author={Kunchang Li and Yali Wang and Junhao Zhang and Peng Gao and Guanglu Song and Yu Liu and Hongsheng Li and Yu Qiao},
      year={2022},
      eprint={2201.09450},
      archivePrefix={arXiv},
      primaryClass={cs.CV}
}
```