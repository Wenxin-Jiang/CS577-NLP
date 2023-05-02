---
language: zh
license: creativeml-openrail-m

tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- zh
- Chinese
- multilingual
- English(En)
- Chinese(Zh)
- Spanish(Es)
- French(Fr)
- Russian(Ru)
- Japanese(Ja)
- Korean(Ko)
- Arabic(Ar)
- Italian(It)
inference: false
extra_gated_prompt: |-
  One more step before getting this model.
  This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
  The CreativeML OpenRAIL License specifies: 

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. BAAI claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
  
  By clicking on "Access repository" below, you accept that your *contact information* (email address and username) can be shared with the model authors as well.
extra_gated_fields:
 I have read the License and agree with its terms: checkbox
---


# AltCLIP-m9
It supports English(En), Chinese(Zh), Spanish(Es), French(Fr), Russian(Ru), Japanese(Ja), Korean(Ko), Arabic(Ar) and Italian(It) languages.

|      名称 Name       |  任务 Task   |   语言 Language(s)    | 模型 Model | Github |
|:------------------:|:----------:|:-------------------:|:--------:|:------:|
| AltCLIP-m9 |  Text-Image | Multilingual |   CLIP   |   [FlagAI](https://github.com/FlagAI-Open/FlagAI)   |

## 简介 Brief Introduction

我们提出了一个简单高效的方法去训练更加优秀的九语CLIP模型。命名为AltCLIP-m9。AltCLIP训练数据来自 [WuDao数据集](https://data.baai.ac.cn/details/WuDaoCorporaText) 和 [LIAON](https://huggingface.co/datasets/ChristophSchuhmann/improved_aesthetics_6plus) 

AltCLIP-m9模型可以为本项目中的AltDiffusion-m9模型提供支持，关于AltDiffusion-m9模型的具体信息可查看[此教程](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltDiffusion/README.md) 。

模型代码已经在 [FlagAI](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP) 上开源，权重位于我们搭建的 [modelhub](https://model.baai.ac.cn/model-detail/100077) 上。我们还提供了微调，推理，验证的脚本，欢迎试用。


We propose a simple and efficient method to train a better multilingua CLIP model. Named AltCLIP-m9. AltCLIP-m9 is trained with training data from [WuDao dataset](https://data.baai.ac.cn/details/WuDaoCorporaText) and [Liaon](https://huggingface.co/datasets/laion/laion2B-en).

The AltCLIP-m9 model can provide support for the AltDiffusion-m9 model in this project. Specific information on the AltDiffusion model can be found in [this tutorial](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltDiffusion/README.md).

The model code has been open sourced on [FlagAI](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP) and the weights are located on [modelhub](https://model.baai.ac.cn/model-detail/100077). We also provide scripts for fine-tuning, inference, and validation, so feel free to try them out.

## 引用
关于AltCLIP，我们已经推出了相关报告，有更多细节可以查阅，如对您的工作有帮助，欢迎引用。

If you find this work helpful, please consider to cite
```
@article{https://doi.org/10.48550/arxiv.2211.06679,
  doi = {10.48550/ARXIV.2211.06679},
  url = {https://arxiv.org/abs/2211.06679},
  author = {Chen, Zhongzhi and Liu, Guang and Zhang, Bo-Wen and Ye, Fulong and Yang, Qinghong and Wu, Ledell},
  keywords = {Computation and Language (cs.CL), FOS: Computer and information sciences},
  title = {AltCLIP: Altering the Language Encoder in CLIP for Extended Language Capabilities},
  publisher = {arXiv},
  year = {2022},
  copyright = {arXiv.org perpetual, non-exclusive license}
}
```

## 训练 Training

训练共有两个阶段。
在平行知识蒸馏阶段，我们只是使用平行语料文本来进行蒸馏（平行语料相对于图文对更容易获取且数量更大）。在多语对比学习阶段，我们使用少量的中-英 图像-文本对（每种语言6百万）来训练我们的文本编码器以更好地适应图像编码器。

There are two phases of training.
In the parallel knowledge distillation phase, we only use parallel corpus texts for distillation (parallel corpus is easier to obtain and larger in number compared to image text pairs). In the multilingual comparison learning phase, we use a small number of text-image pairs (about 6 million in each language) to train our text encoder to better fit the image encoder.



## 下游效果 Performance

![](./xtd.png)




## 可视化效果 Visualization effects

基于AltCLIP，我们还开发了AltDiffusion模型，可视化效果如下。

Based on AltCLIP, we have also developed the AltDiffusion model, visualized as follows.

![](m9.png)

## 模型推理 Inference
Please download the code from [FlagAI AltCLIP](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP)
```python
from PIL import Image
import requests

# transformers version >= 4.21.0
from modeling_altclip import AltCLIP
from processing_altclip import AltCLIPProcessor

# now our repo's in private, so we need `use_auth_token=True`
model = AltCLIP.from_pretrained("BAAI/AltCLIP-m9")
processor = AltCLIPProcessor.from_pretrained("BAAI/AltCLIP-m9")

url = "http://images.cocodataset.org/val2017/000000039769.jpg"
image = Image.open(requests.get(url, stream=True).raw)

inputs = processor(text=["a photo of a cat", "a photo of a dog"], images=image, return_tensors="pt", padding=True)

outputs = model(**inputs)
logits_per_image = outputs.logits_per_image # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1) # we can take the softmax to get the label probabilities
```


