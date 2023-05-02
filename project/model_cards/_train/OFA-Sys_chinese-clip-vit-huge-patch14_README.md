---
tags:
- vision
widget:
- src: https://huggingface.co/OFA-Sys/chinese-clip-vit-base-patch16/resolve/main/festival.jpg
  candidate_labels: 灯笼, 鞭炮, 对联
  example_title: festival
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/cat-dog-music.png
  candidate_labels: 音乐表演, 体育运动
  example_title: cat & dog
- src: https://huggingface.co/datasets/mishig/sample_images/resolve/main/football-match.jpg
  candidate_labels: 梅西, C罗, 马奎尔
  example_title: football
---



# Chinese-CLIP-ViT-Huge-Patch14

## Introduction
This is the huge-version of the Chinese CLIP, with ViT-H/14 as the image encoder and RoBERTa-wwm-large as the text encoder. Chinese CLIP is a simple implementation of CLIP on a large-scale dataset of around 200 million Chinese image-text pairs. For more details, please refer to our technical report https://arxiv.org/abs/2211.01335 and our official github repo https://github.com/OFA-Sys/Chinese-CLIP (Welcome to star! 🔥🔥)

## Use with the official API
We provide a simple code snippet to show how to use the API of Chinese-CLIP to compute the image & text embeddings and similarities. 

```python
from PIL import Image
import requests
from transformers import ChineseCLIPProcessor, ChineseCLIPModel

model = ChineseCLIPModel.from_pretrained("OFA-Sys/chinese-clip-vit-huge-patch14")
processor = ChineseCLIPProcessor.from_pretrained("OFA-Sys/chinese-clip-vit-huge-patch14")

url = "https://clip-cn-beijing.oss-cn-beijing.aliyuncs.com/pokemon.jpeg"
image = Image.open(requests.get(url, stream=True).raw)
# Squirtle, Bulbasaur, Charmander, Pikachu in English
texts = ["杰尼龟", "妙蛙种子", "小火龙", "皮卡丘"]

# compute image feature
inputs = processor(images=image, return_tensors="pt")
image_features = model.get_image_features(**inputs)
image_features = image_features / image_features.norm(p=2, dim=-1, keepdim=True)  # normalize

# compute text features
inputs = processor(text=texts, padding=True, return_tensors="pt")
text_features = model.get_text_features(**inputs)
text_features = text_features / text_features.norm(p=2, dim=-1, keepdim=True)  # normalize

# compute image-text similarity scores
inputs = processor(text=texts, images=image, return_tensors="pt", padding=True)
outputs = model(**inputs)
logits_per_image = outputs.logits_per_image  # this is the image-text similarity score
probs = logits_per_image.softmax(dim=1)  # probs: [[1.1419e-02, 1.0478e-02, 5.2018e-04, 9.7758e-01]]
```

However, if you are not satisfied with only using the API, feel free to check our github repo https://github.com/OFA-Sys/Chinese-CLIP for more details about training and inference. 
<br><br>

## Results
**MUGE Text-to-Image Retrieval**:
<table border="1" width="100%">
    <tr align="center">
        <th>Setup</th><th colspan="4">Zero-shot</th><th colspan="4">Finetune</th>
    </tr>
    <tr align="center">
        <td>Metric</td><td>R@1</td><td>R@5</td><td>R@10</td><td>MR</td><td>R@1</td><td>R@5</td><td>R@10</td><td>MR</td>
    </tr>
	<tr align="center">
        <td width="120%">Wukong</td><td>42.7</td><td>69.0</td><td>78.0</td><td>63.2</td><td>52.7</td><td>77.9</td><td>85.6</td><td>72.1</td>
    </tr>
	<tr align="center">
        <td width="120%">R2D2</td><td>49.5</td><td>75.7</td><td>83.2</td><td>69.5</td><td>60.1</td><td>82.9</td><td>89.4</td><td>77.5</td>
    </tr>
	<tr align="center">
        <td width="120%">CN-CLIP</td><td>63.0</td><td>84.1</td><td>89.2</td><td>78.8</td><td>68.9</td><td>88.7</td><td>93.1</td><td>83.6</td>
    </tr>
</table>
<br>

**Flickr30K-CN Retrieval**:
<table border="1" width="120%">
	<tr align="center">
        <th>Task</th><th colspan="6">Text-to-Image</th><th colspan="6">Image-to-Text</th>
    </tr>
    <tr align="center">
        <th>Setup</th><th colspan="3">Zero-shot</th><th colspan="3">Finetune</th><th colspan="3">Zero-shot</th><th colspan="3">Finetune</th>
    </tr>
    <tr align="center">
        <td>Metric</td><td>R@1</td><td>R@5</td><td>R@10</td><td>R@1</td><td>R@5</td><td>R@10</td><td>R@1</td><td>R@5</td><td>R@10</td><td>R@1</td><td>R@5</td><td>R@10</td>
    </tr>
	<tr align="center">
        <td width="120%">Wukong</td><td>51.7</td><td>78.9</td><td>86.3</td><td>77.4</td><td>94.5</td><td>97.0</td><td>76.1</td><td>94.8</td><td>97.5</td><td>92.7</td><td>99.1</td><td>99.6</td>
    </tr>
	<tr align="center">
        <td width="120%">R2D2</td><td>60.9</td><td>86.8</td><td>92.7</td><td>84.4</td><td>96.7</td><td>98.4</td><td>77.6</td><td>96.7</td><td>98.9</td><td>95.6</td><td>99.8</td><td>100.0</td>
    </tr>
	<tr align="center">
        <td width="120%">CN-CLIP</td><td>71.2</td><td>91.4</td><td>95.5</td><td>83.8</td><td>96.9</td><td>98.6</td><td>81.6</td><td>97.5</td><td>98.8</td><td>95.3</td><td>99.7</td><td>100.0</td>
    </tr>
</table>
<br>

**COCO-CN Retrieval**:
<table border="1" width="100%">
	<tr align="center">
        <th>Task</th><th colspan="6">Text-to-Image</th><th colspan="6">Image-to-Text</th>
    </tr>
    <tr align="center">
        <th>Setup</th><th colspan="3">Zero-shot</th><th colspan="3">Finetune</th><th colspan="3">Zero-shot</th><th colspan="3">Finetune</th>
    </tr>
    <tr align="center">
        <td>Metric</td><td>R@1</td><td>R@5</td><td>R@10</td><td>R@1</td><td>R@5</td><td>R@10</td><td>R@1</td><td>R@5</td><td>R@10</td><td>R@1</td><td>R@5</td><td>R@10</td>
    </tr>
	<tr align="center">
        <td width="120%">Wukong</td><td>53.4</td><td>80.2</td><td>90.1</td><td>74.0</td><td>94.4</td><td>98.1</td><td>55.2</td><td>81.0</td><td>90.6</td><td>73.3</td><td>94.0</td><td>98.0</td>
    </tr>
	<tr align="center">
        <td width="120%">R2D2</td><td>56.4</td><td>85.0</td><td>93.1</td><td>79.1</td><td>96.5</td><td>98.9</td><td>63.3</td><td>89.3</td><td>95.7</td><td>79.3</td><td>97.1</td><td>98.7</td>
    </tr>
	<tr align="center">
        <td width="120%">CN-CLIP</td><td>69.2</td><td>89.9</td><td>96.1</td><td>81.5</td><td>96.9</td><td>99.1</td><td>63.0</td><td>86.6</td><td>92.9</td><td>83.5</td><td>97.3</td><td>99.2</td>
    </tr>
</table>
<br>

**Zero-shot Image Classification**:
<table border="1" width="100%">
	<tr align="center">
        <th>Task</th><th>CIFAR10</th><th>CIFAR100</th><th>DTD</th><th>EuroSAT</th><th>FER</th><th>FGVC</th><th>KITTI</th><th>MNIST</th><th>PC</th><th>VOC</th>
    </tr>
	<tr align="center">
        <td width="150%">GIT</td><td>88.5</td><td>61.1</td><td>42.9</td><td>43.4</td><td>41.4</td><td>6.7</td><td>22.1</td><td>68.9</td><td>50.0</td><td>80.2</td>
    </tr>
    	<tr align="center">
        <td width="150%">ALIGN</td><td>94.9</td><td>76.8</td><td>66.1</td><td>52.1</td><td>50.8</td><td>25.0</td><td>41.2</td><td>74.0</td><td>55.2</td><td>83.0</td>
    </tr>
	<tr align="center">
        <td width="150%">CLIP</td><td>94.9</td><td>77.0</td><td>56.0</td><td>63.0</td><td>48.3</td><td>33.3</td><td>11.5</td><td>79.0</td><td>62.3</td><td>84.0</td>
    </tr>
    	<tr align="center">
        <td width="150%">Wukong</td><td>95.4</td><td>77.1</td><td>40.9</td><td>50.3</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td><td>-</td>
    </tr>
    	<tr align="center">
        <td width="150%">CN-CLIP</td><td>96.0</td><td>79.7</td><td>51.2</td><td>52.0</td><td>55.1</td><td>26.2</td><td>49.9</td><td>79.4</td><td>63.5</td><td>84.9</td>
    </tr>
</table>
<br>

## Citation
If you find Chinese CLIP helpful, feel free to cite our paper. Thanks for your support!

```
@article{chinese-clip,
  title={Chinese CLIP: Contrastive Vision-Language Pretraining in Chinese},
  author={Yang, An and Pan, Junshu and Lin, Junyang and Men, Rui and Zhang, Yichang and Zhou, Jingren and Zhou, Chang},
  journal={arXiv preprint arXiv:2211.01335},
  year={2022}
}
```
<br>