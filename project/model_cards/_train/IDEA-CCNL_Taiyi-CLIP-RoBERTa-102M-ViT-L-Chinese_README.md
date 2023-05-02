---
license: apache-2.0
# inference: false
# pipeline_tag: zero-shot-image-classification
pipeline_tag: feature-extraction

# inference:
#   parameters:
tags:
- clip
- zh
- image-text
- feature-extraction
---

# Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

首个开源的中文CLIP模型，1.23亿图文对上进行预训练的文本端RoBERTa-base

The first open source Chinese CLIP, pre-training on 123M image-text pairs, the text encoder: RoBERTa-base.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 特殊 Special | 多模态 Multimodal | 太乙 Taiyi | CLIP (RoBERTa) |     102M    |     Chinese     |

## 模型信息 Model Information

我们遵循CLIP的实验设置，以获得强大的视觉-语言表征。在训练中文版的CLIP时，我们使用[chinese-roberta-wwm](https://huggingface.co/hfl/chinese-roberta-wwm-ext)作为语言的编码器，并将[open_clip](https://github.com/mlfoundations/open_clip)中的**ViT-L-14**应用于视觉的编码器。为了快速且稳定地进行预训练，我们冻结了视觉编码器并且只微调语言编码器。此外，我们将[Noah-Wukong](https://wukong-dataset.github.io/wukong-dataset/)数据集(100M)和[Zero](https://zero.so.com/)数据集(23M)用作预训练的数据集。在悟空数据集和zero数据集上预训练24轮,在A100x32上训练了6天。据我们所知，我们的Taiyi-CLIP是目前Huggingface社区中首个的开源中文CLIP。

We follow the experimental setup of CLIP to obtain powerful visual-language intelligence. To obtain the CLIP for Chinese, we employ [chinese-roberta-wwm](https://huggingface.co/hfl/chinese-roberta-wwm-ext) for the language encoder, and apply the **ViT-L-14** in [open_clip](https://github.com/mlfoundations/open_clip) for the vision encoder. We freeze the vision encoder and tune the language encoder to speed up and stabilize the pre-training process. Moreover, we apply [Noah-Wukong](https://wukong-dataset.github.io/wukong-dataset/) dataset (100M) and [Zero](https://zero.so.com/) dataset (23M) as the pre-training datasets. The model was first trained 24 epochs on wukong and zero, which takes 6 days to train on A100x32. To the best of our knowledge, our TaiyiCLIP is currently the only open-sourced Chinese CLIP in the huggingface community.

### 下游效果 Performance

**Zero-Shot Classification**

|  model   | dataset  | Top1 | Top5 |
|  ----  | ----  | ---- | ---- |
| Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese  | ImageNet1k-CN | 55.04% | 81.75% |

**Zero-Shot Text-to-Image Retrieval**

|  model   | dataset  | Top1 | Top5 | Top10 |
|  ----  | ----  | ---- | ---- | ---- |
| Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese  | Flickr30k-CNA-test | 58.32% | 82.96%  | 89.40% |
| Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese  | COCO-CN-test | 55.27% | 81.10%  | 90.78% |
| Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese  | wukong50k | 64.95% | 91.77% | 96.28% |

## 使用 Usage

```python3
from PIL import Image
import requests
import open_clip
import torch
from transformers import BertModel, BertConfig, BertTokenizer
from transformers import CLIPProcessor, CLIPModel
import numpy as np

query_texts = ["一只猫", "一只狗",'两只猫', '两只老虎','一只老虎']  # 这里是输入文本的，可以随意替换。
# 加载Taiyi 中文 text encoder
text_tokenizer = BertTokenizer.from_pretrained("IDEA-CCNL/Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese")
text_encoder = BertModel.from_pretrained("IDEA-CCNL/Taiyi-CLIP-RoBERTa-102M-ViT-L-Chinese").eval()

url = "http://images.cocodataset.org/val2017/000000039769.jpg"  # 这里可以换成任意图片的url
# 加载openclip的image encoder
clip_model, _, processor = open_clip.create_model_and_transforms('ViT-L-14', pretrained='openai')
clip_model = clip_model.eval()


text = text_tokenizer(query_texts, return_tensors='pt', padding=True)['input_ids']
image = processor(Image.open(requests.get(url, stream=True).raw)).unsqueeze(0)
with torch.no_grad():
    image_features = clip_model.encode_image(image)
    text_features = text_encoder(text)[1]
    # 归一化
    image_features = image_features / image_features.norm(dim=1, keepdim=True)
    text_features = text_features / text_features.norm(dim=1, keepdim=True)
    # 计算余弦相似度 logit_scale是尺度系数
    logit_scale = clip_model.logit_scale.exp()
    logits_per_image =  logit_scale * image_features @ text_features.t()
    logits_per_text = logits_per_image.t()
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()
    print(np.around(probs, 3))

```

## 引用 Citation

如果您在您的工作中使用了我们的模型，可以引用我们的[论文](https://arxiv.org/abs/2209.02970)：

If you are using the resource for your work, please cite the our [paper](https://arxiv.org/abs/2209.02970):

```text
@article{fengshenbang,
  author    = {Jiaxing Zhang and Ruyi Gan and Junjie Wang and Yuxiang Zhang and Lin Zhang and Ping Yang and Xinyu Gao and Ziwei Wu and Xiaoqun Dong and Junqing He and Jianheng Zhuo and Qi Yang and Yongfeng Huang and Xiayu Li and Yanghan Wu and Junyu Lu and Xinyu Zhu and Weifeng Chen and Ting Han and Kunhao Pan and Rui Wang and Hao Wang and Xiaojun Wu and Zhongshen Zeng and Chongpei Chen},
  title     = {Fengshenbang 1.0: Being the Foundation of Chinese Cognitive Intelligence},
  journal   = {CoRR},
  volume    = {abs/2209.02970},
  year      = {2022}
}
```

也可以引用我们的[网站](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

You can also cite our [website](https://github.com/IDEA-CCNL/Fengshenbang-LM/):

```text
@misc{Fengshenbang-LM,
  title={Fengshenbang-LM},
  author={IDEA-CCNL},
  year={2021},
  howpublished={\url{https://github.com/IDEA-CCNL/Fengshenbang-LM}},
}
```