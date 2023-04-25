---
license: apache-2.0
# inference: false
# pipeline_tag: zero-shot-image-classification
pipeline_tag: feature-extraction

# inference:
#   parameters:
tags:
- text-to-image
- chinese
- diffusion
---

# Taiyi-Diffusion-532M-Nature-Chinese

- Github: [Fengshenbang-LM](https://github.com/IDEA-CCNL/Fengshenbang-LM)
- Docs: [Fengshenbang-Docs](https://fengshenbang-doc.readthedocs.io/)

## 简介 Brief Introduction

该模型由[Katherine Crowson's](https://github.com/openai/guided-diffusion)的无条件扩散模型在1k+张收集的自然风景图上微调而来。结合[IDEA-CCNL/Taiyi-CLIP-Roberta-large-326M-Chinese](https://huggingface.co/IDEA-CCNL/Taiyi-CLIP-Roberta-large-326M-Chinese)可以实现中文Guided Diffusion的生成方式。

This model is finetune from Katherine Crowson's fine-tuned 512x512 diffusion model (https://github.com/openai/guided-diffusion), using 1k+ nature image crawled from the InterNet. Combine With [IDEA-CCNL/Taiyi-CLIP-Roberta-large-326M-Chinese](https://huggingface.co/IDEA-CCNL/Taiyi-CLIP-Roberta-large-326M-Chinese) can generate image via guided diffusion in Chinese.

## 模型分类 Model Taxonomy

|  需求 Demand  | 任务 Task       | 系列 Series      | 模型 Model    | 参数 Parameter | 额外 Extra |
|  :----:  | :----:  | :----:  | :----:  | :----:  | :----:  |
| 特殊 Special | 多模态 Multimodal | 太乙 Taiyi | Diffusion Model |     532M      |    Nature     |

## 使用 Usage

使用示例见：https://github.com/IDEA-CCNL/Fengshenbang-LM/tree/main/fengshen/examples/disco_project

## 生成示例 Example
|  飞流直下三千尺   |  东临碣石，以观沧海 | 
|  ----  | ----  | 
| ![](feiliu.jpg)  | ![](jieshi.jpg)  | 


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

