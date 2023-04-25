---
tags:
- image-classification
- timm
library_tag: timm
license: mit
datasets:
- imagenet-1k
- imagenet-22k
- imagenet-22k
---
# Model card for eva_large_patch14_196.in22k_ft_in22k_in1k

An EVA image classification model. Pretrained on ImageNet-22k with masked image modeling (using EVA-CLIP as a MIM teacher) and fine-tuned on ImageNet-22k then on ImageNet-1k by paper authors.

NOTE: `timm` checkpoints are float32 for consistency with other models. Original checkpoints are float16 or bfloat16 in some cases, see originals if that's preferred.


## Model Details
- **Model Type:** Image classification / feature backbone
- **Model Stats:**
  - Params (M): 304.1
  - GMACs: 61.6
  - Activations (M): 63.5
  - Image size: 196 x 196
- **Papers:**
  - EVA: Exploring the Limits of Masked Visual Representation Learning at Scale: https://arxiv.org/abs/2211.07636
- **Pretrain Dataset:**
  - ImageNet-22k
  - ImageNet-22k
- **Dataset:** ImageNet-1k
- **Original:**
  - https://github.com/baaivision/EVA
  - https://huggingface.co/BAAI/EVA

## Model Usage
### Image Classification
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model('eva_large_patch14_196.in22k_ft_in22k_in1k', pretrained=True)
model = model.eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))  # unsqueeze single image into batch of 1

top5_probabilities, top5_class_indices = torch.topk(output.softmax(dim=1) * 100, k=5)
```

### Image Embeddings
```python
from urllib.request import urlopen
from PIL import Image
import timm

img = Image.open(urlopen(
    'https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/beignets-task-guide.png'
))

model = timm.create_model(
    'eva_large_patch14_196.in22k_ft_in22k_in1k',
    pretrained=True,
    num_classes=0,  # remove classifier nn.Linear
)
model = model.eval()

# get model specific transforms (normalization, resize)
data_config = timm.data.resolve_model_data_config(model)
transforms = timm.data.create_transform(**data_config, is_training=False)

output = model(transforms(img).unsqueeze(0))  # output is (batch_size, num_features) shaped tensor

# or equivalently (without needing to set num_classes=0)

output = model.forward_features(transforms(img).unsqueeze(0))
# output is unpooled, a (1, 197, 1024) shaped tensor

output = model.forward_head(output, pre_logits=True)
# output is a (1, num_features) shaped tensor
```

## Model Comparison
Explore the dataset and runtime metrics of this model in timm [model results](https://github.com/huggingface/pytorch-image-models/tree/main/results).

|model                                          |top1  |top5  |param_count|img_size|
|-----------------------------------------------|------|------|-----------|--------|
|eva02_large_patch14_448.mim_m38m_ft_in22k_in1k |90.054|99.042|305.08     |448     |
|eva02_large_patch14_448.mim_in22k_ft_in22k_in1k|89.946|99.01 |305.08     |448     |
|eva_giant_patch14_560.m30m_ft_in22k_in1k       |89.792|98.992|1014.45    |560     |
|eva02_large_patch14_448.mim_in22k_ft_in1k      |89.626|98.954|305.08     |448     |
|eva02_large_patch14_448.mim_m38m_ft_in1k       |89.57 |98.918|305.08     |448     |
|eva_giant_patch14_336.m30m_ft_in22k_in1k       |89.56 |98.956|1013.01    |336     |
|eva_giant_patch14_336.clip_ft_in1k             |89.466|98.82 |1013.01    |336     |
|eva_large_patch14_336.in22k_ft_in22k_in1k      |89.214|98.854|304.53     |336     |
|eva_giant_patch14_224.clip_ft_in1k             |88.882|98.678|1012.56    |224     |
|eva02_base_patch14_448.mim_in22k_ft_in22k_in1k |88.692|98.722|87.12      |448     |
|eva_large_patch14_336.in22k_ft_in1k            |88.652|98.722|304.53     |336     |
|eva_large_patch14_196.in22k_ft_in22k_in1k      |88.592|98.656|304.14     |196     |
|eva02_base_patch14_448.mim_in22k_ft_in1k       |88.23 |98.564|87.12      |448     |
|eva_large_patch14_196.in22k_ft_in1k            |87.934|98.504|304.14     |196     |
|eva02_small_patch14_336.mim_in22k_ft_in1k      |85.74 |97.614|22.13      |336     |
|eva02_tiny_patch14_336.mim_in22k_ft_in1k       |80.658|95.524|5.76       |336     |

## Citation
```bibtex
@article{EVA,
  title={EVA: Exploring the Limits of Masked Visual Representation Learning at Scale},
  author={Fang, Yuxin and Wang, Wen and Xie, Binhui and Sun, Quan and Wu, Ledell and Wang, Xinggang and Huang, Tiejun and Wang, Xinlong and Cao, Yue},
  journal={arXiv preprint arXiv:2211.07636},
  year={2022}
}
```
```bibtex
@misc{rw2019timm,
  author = {Ross Wightman},
  title = {PyTorch Image Models},
  year = {2019},
  publisher = {GitHub},
  journal = {GitHub repository},
  doi = {10.5281/zenodo.4414861},
  howpublished = {\url{https://github.com/huggingface/pytorch-image-models}}
}
```
