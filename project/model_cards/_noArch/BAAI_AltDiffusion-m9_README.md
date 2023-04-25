---
language: zh
license: creativeml-openrail-m

tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
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
- diffusers

extra_gated_prompt: |-
  This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
  The CreativeML OpenRAIL License specifies: 
  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. The authors claim no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license carefully here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
      
extra_gated_heading: Please read the LICENSE to access this model
---

# AltDiffusion

|  名称 Name   | 任务 Task       |   语言 Language(s)    | 模型 Model    | Github |
|:----------:| :----:  |:-------------------:| :----:  |:------:|
| AltDiffusion-m9 | 多模态 Multimodal | Multilingual | Stable Diffusion |   [FlagAI](https://github.com/FlagAI-Open/FlagAI)   |

# Gradio

We support a [Gradio](https://github.com/gradio-app/gradio) Web UI to run AltDiffusion-m9:
[![Open In Spaces](https://camo.githubusercontent.com/00380c35e60d6b04be65d3d94a58332be5cc93779f630bcdfc18ab9a3a7d3388/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f25463025394625413425393725323048756767696e67253230466163652d5370616365732d626c7565)](https://huggingface.co/spaces/akhaliq/AltDiffusion-m9)

#  模型信息 Model Information

我们使用 [AltCLIP-m9](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP/README.md)，基于 [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion) 训练了双语Diffusion模型，训练数据来自 [WuDao数据集](https://data.baai.ac.cn/details/WuDaoCorporaText) 和 [LAION](https://huggingface.co/datasets/ChristophSchuhmann/improved_aesthetics_6plus) 。

我们的版本在多语言对齐方面表现非常出色，是目前市面上开源的最强多语言版本，保留了原版stable diffusion的大部分能力，并且在某些例子上比有着比原版模型更出色的能力。

AltDiffusion-m9 模型由名为 AltCLIP-m9 的多语 CLIP 模型支持，该模型也可在本项目中访问。您可以阅读 [此教程](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP/README.md) 了解更多信息。

We used [AltCLIP-m9](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP/README.md), and trained a bilingual Diffusion model based on [Stable Diffusion](https://huggingface.co/CompVis/stable-diffusion), with training data from [WuDao dataset](https://data.baai.ac.cn/details/WuDaoCorporaText) and [LAION](https://huggingface.co/datasets/laion/laion2B-en).

Our model performs well in aligning multilanguage and is the strongest open-source version on the market today, retaining most of the stable diffusion capabilities of the original, and in some cases even better than the original model.

AltDiffusion-m9 model is backed by a multilingual CLIP model named AltCLIP-m9, which is also accessible in FlagAI. You can read [this tutorial](https://github.com/FlagAI-Open/FlagAI/tree/master/examples/AltCLIP/README.md) for more information. 


## 引用
关于AltCLIP-m9，我们已经推出了相关报告，有更多细节可以查阅，如对您的工作有帮助，欢迎引用。

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

# 模型权重 Model Weights

第一次运行AltDiffusion-m9模型时会自动从huggingface下载如下权重,  

The following weights are automatically downloaded from HF when the AltDiffusion-m9 model is run for the first time: 

| 模型名称 Model name              | 大小 Size | 描述 Description                                        |
|------------------------------|---------|-------------------------------------------------------|
| StableDiffusionSafetyChecker | 1.13G   | 图片的安全检查器；Safety checker for image                     |
| AltDiffusion-m9                 | 8.0G    |  support English(En), Chinese(Zh), Spanish(Es), French(Fr), Russian(Ru), Japanese(Ja), Korean(Ko), Arabic(Ar) and Italian(It) |
| AltCLIP-m9                      | 3.22G   | support English(En), Chinese(Zh), Spanish(Es), French(Fr), Russian(Ru), Japanese(Ja), Korean(Ko), Arabic(Ar) and Italian(It)           |


# 示例 Example

##  🧨Diffusers Example

**AltDiffusion-m9** 已被添加到 🧨Diffusers! 

我们的[代码示例](https://colab.research.google.com/drive/1htPovT5YNutl2i31mIYrOzlIgGLm06IX#scrollTo=1TrIQp9N1Bnm)已放到colab上，欢迎使用。

您可以在 [此处](https://huggingface.co/docs/diffusers/main/en/api/pipelines/alt_diffusion) 查看文档页面。

以下示例将使用fast DPM 调度程序生成图像,  在V100 上耗时大约为 2 秒。

You can run our diffusers example through [here](https://colab.research.google.com/drive/1htPovT5YNutl2i31mIYrOzlIgGLm06IX#scrollTo=1TrIQp9N1Bnm) in colab.

You can see the documentation page [here](https://huggingface.co/docs/diffusers/main/en/api/pipelines/alt_diffusion).

The following example will use the fast DPM scheduler to generate an image in ca. 2 seconds on a V100.

First you should install diffusers main branch and some dependencies:
```
pip install git+https://github.com/huggingface/diffusers.git torch transformers accelerate sentencepiece
```

then you can run the following example:

```python
from diffusers import AltDiffusionPipeline, DPMSolverMultistepScheduler
import torch

pipe = AltDiffusionPipeline.from_pretrained("BAAI/AltDiffusion-m9", torch_dtype=torch.float16, revision="fp16")
pipe = pipe.to("cuda")

pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

prompt = "黑暗精灵公主，非常详细，幻想，非常详细，数字绘画，概念艺术，敏锐的焦点，插图"
# or in English:
# prompt = "dark elf princess, highly detailed, d & d, fantasy, highly detailed, digital painting, trending on artstation, concept art, sharp focus, illustration, art by artgerm and greg rutkowski and fuji choko and viktoria gavrilenko and hoang lap"

image = pipe(prompt, num_inference_steps=25).images[0]
image.save("./alt.png")
```

![alt](https://huggingface.co/datasets/patrickvonplaten/images/resolve/main/hub/alt.png)

## Transformers Example

```python
import os
import torch
import transformers
from transformers import BertPreTrainedModel
from transformers.models.clip.modeling_clip import CLIPPreTrainedModel
from transformers.models.xlm_roberta.tokenization_xlm_roberta import XLMRobertaTokenizer
from diffusers.schedulers import DDIMScheduler, LMSDiscreteScheduler, PNDMScheduler
from diffusers import StableDiffusionPipeline
from transformers import BertPreTrainedModel,BertModel,BertConfig
import torch.nn as nn
import torch
from transformers.models.xlm_roberta.configuration_xlm_roberta import XLMRobertaConfig
from transformers import XLMRobertaModel
from transformers.activations import ACT2FN
from typing import Optional


class RobertaSeriesConfig(XLMRobertaConfig):
    def __init__(self, pad_token_id=1, bos_token_id=0, eos_token_id=2,project_dim=768,pooler_fn='cls',learn_encoder=False, **kwargs):
        super().__init__(pad_token_id=pad_token_id, bos_token_id=bos_token_id, eos_token_id=eos_token_id, **kwargs)
        self.project_dim = project_dim
        self.pooler_fn = pooler_fn
        # self.learn_encoder = learn_encoder

class RobertaSeriesModelWithTransformation(BertPreTrainedModel):
    _keys_to_ignore_on_load_unexpected = [r"pooler"]
    _keys_to_ignore_on_load_missing = [r"position_ids", r"predictions.decoder.bias"]
    base_model_prefix = 'roberta'
    config_class= XLMRobertaConfig
    def __init__(self, config):
        super().__init__(config)
        self.roberta = XLMRobertaModel(config)
        self.transformation = nn.Linear(config.hidden_size, config.project_dim)
        self.post_init()
        
    def get_text_embeds(self,bert_embeds,clip_embeds):
        return self.merge_head(torch.cat((bert_embeds,clip_embeds)))

    def set_tokenizer(self, tokenizer):
        self.tokenizer = tokenizer

    def forward(self, input_ids: Optional[torch.Tensor] = None) :
        attention_mask = (input_ids != self.tokenizer.pad_token_id).to(torch.int64)
        outputs = self.base_model(
            input_ids=input_ids,
            attention_mask=attention_mask,
        )
        
        projection_state = self.transformation(outputs.last_hidden_state)
        
        return (projection_state,)

model_path_encoder = "BAAI/RobertaSeriesModelWithTransformation"
model_path_diffusion = "BAAI/AltDiffusion-m9"
device = "cuda"

seed = 12345
tokenizer = XLMRobertaTokenizer.from_pretrained(model_path_encoder, use_auth_token=True)
tokenizer.model_max_length = 77

text_encoder = RobertaSeriesModelWithTransformation.from_pretrained(model_path_encoder, use_auth_token=True)
text_encoder.set_tokenizer(tokenizer)
print("text encode loaded")
pipe = StableDiffusionPipeline.from_pretrained(model_path_diffusion,
                                               tokenizer=tokenizer,
                                               text_encoder=text_encoder,
                                               use_auth_token=True,
                                               )
print("diffusion pipeline loaded")
pipe = pipe.to(device)

prompt = "Thirty years old lee evans as a sad 19th century postman. detailed, soft focus, candle light, interesting lights, realistic, oil canvas, character concept art by munkácsy mihály, csók istván, john everett millais, henry meynell rheam, and da vinci"
with torch.no_grad():
    image = pipe(prompt, guidance_scale=7.5).images[0]  
    
image.save("3.png")
```


您可以在`predict_generate_images`函数里通过改变参数来调整设置，具体信息如下:

More parameters of predict_generate_images for you to adjust for `predict_generate_images` are listed below:


| 参数名 Parameter             | 类型 Type | 描述 Description                                        |
|--------------------------------|------------|-------------------------------------------------------|
| prompt | str   | 提示文本; The prompt text                    |
| out_path | str   | 输出路径; The output path to save images                  |
| n_samples | int   | 输出图片数量; Number of images to be generate                   |
| skip_grid | bool   | 如果为True, 会将所有图片拼接在一起，输出一张新的图片; If set to true, image gridding step will be skipped                    |
| ddim_step | int   | DDIM模型的步数; Number of steps in ddim model                    |
| plms | bool  | 如果为True, 则会使用plms模型; If set to true, PLMS Sampler instead of DDIM Sampler will be applied                    |
| scale | float   | 这个值决定了文本在多大程度上影响生成的图片，值越大影响力越强; This value determines how important the prompt incluences generate images                    |
| H | int   | 图片的高度; Height of image                    |
| W | int   | 图片的宽度; Width of image                    |
| C | int   | 图片的channel数; Numeber of channels of generated images                    |
| seed | int   | 随机种子; Random seed number                     |

注意：模型推理要求一张至少10G以上的GPU。

Note that the model inference requires a GPU of at least 10G above.


# 更多生成结果 More Results
## multilanguage examples
同一句prompts不同语言生成的人脸不一样！

One prompts in different languages generates different faces!
![image](./m9.png)
## 中英文对齐能力 Chinese and English alignment ability

### prompt:dark elf princess, highly detailed, d & d, fantasy, highly detailed, digital painting, trending on artstation, concept art, sharp focus, illustration, art by artgerm and greg rutkowski and fuji choko and viktoria gavrilenko and hoang lap
### 英文生成结果/Generated results from English prompts

![image](https://raw.githubusercontent.com/BAAI-OpenPlatform/test_open/main/en_dark_elf.png)

### prompt:黑暗精灵公主，非常详细，幻想，非常详细，数字绘画，概念艺术，敏锐的焦点，插图
### 中文生成结果/Generated results from Chinese prompts
![image](https://raw.githubusercontent.com/BAAI-OpenPlatform/test_open/main/cn_dark_elf.png)

## 中文表现能力/The performance for Chinese prompts

## prompt:带墨镜的男孩肖像，充满细节，8K高清
![image](https://raw.githubusercontent.com/BAAI-OpenPlatform/test_open/main/boy.png)


## prompt:带墨镜的中国男孩肖像，充满细节，8K高清
![image](https://raw.githubusercontent.com/BAAI-OpenPlatform/test_open/main/cn_boy.png)

## 长图生成能力/The ability to generate long images

### prompt: 一只带着帽子的小狗 
### 原版 stable diffusion：
![image](https://raw.githubusercontent.com/BAAI-OpenPlatform/test_open/main/dog_other.png)

### Ours:
![image](https://raw.githubusercontent.com/BAAI-OpenPlatform/test_open/main/dog.png)

注: 此处长图生成技术由右脑科技(RightBrain AI)提供。

Note: The long image generation technology here is provided by Right Brain Technology.

# 许可/License

该模型通过 [CreativeML Open RAIL-M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) 获得许可。作者对您生成的输出不主张任何权利，您可以自由使用它们并对它们的使用负责，不得违反本许可中的规定。该许可证禁止您分享任何违反任何法律、对他人造成伤害、传播任何可能造成伤害的个人信息、传播错误信息和针对弱势群体的任何内容。您可以出于商业目的修改和使用模型，但必须包含相同使用限制的副本。有关限制的完整列表，请[阅读许可证](https://huggingface.co/spaces/CompVis/stable-diffusion-license) 。

The model is licensed with a [CreativeML Open RAIL-M license](https://huggingface.co/spaces/CompVis/stable-diffusion-license). The authors claim no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in this license. The license forbids you from sharing any content that violates any laws, produce any harm to a person, disseminate any personal information that would be meant for harm, spread misinformation and target vulnerable groups. You can modify and use the model for commercial purposes, but a copy of the same use restrictions must be included. For the full list of restrictions please [read the license](https://huggingface.co/spaces/CompVis/stable-diffusion-license) .