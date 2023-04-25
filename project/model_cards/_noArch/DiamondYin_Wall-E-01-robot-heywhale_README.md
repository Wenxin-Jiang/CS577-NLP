---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
widget:
- text: In space, there is a spaceship docked here, and Wall-E-01 walks in the spaceship，8K
    resolution, 16:9
---

# DreamBooth model for the Wall-E-01 concept trained by DiamondYin.

This is a Stable Diffusion model fine-tuned on the Wall-E-01 concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of Wall-E-01 robot**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `robot` images for the wildcard theme, 
for the Hugging Face DreamBooth Hackathon, from the HF CN Community, corporated with the HeyWhale.

The production cost of WALL-E is $180 million. It tells about a lonely robot designed to clean up the polluted earth. The unique feature of this film is that there is almost no dialogue in the first 40 minutes or so. On the contrary, the audience enters a world of robots; How it thinks, how it works, how it speaks (or doesn't speak). Pixar's classic film was a success. The film has a global box office of more than 520 million US dollars, won a number of Oscar nominations, and ranked first on Time magazine's list of the best films of the decade.
Now we can easily create Wally's pictures and present the script's pictures with the help of the Stable Diffusion model. We can write a series of stories for WALL-E, but we don't have to bear such expensive costs. This is the advantage of the Stable Diffusion model

机器总动员这部电影（WALL-E）的生产成本为1.8亿美元。它讲述了一个孤独的机器人被设计来清理被污染的地球。这部电影的独特之处在于，前40分钟左右几乎没有对话，相反，观众进入了一个机器人的世界；它如何思考，如何工作，如何说话（或不说话）。皮克斯的经典电影获得了成功。
该片全球票房超过5.2亿美元，获得多项奥斯卡提名，并在《时代》杂志十年最佳影片排行榜上排名第一。现在，我们可以通过Stable Diffusion model轻松创建WALL-E的图片并呈现脚本的图片。我们可以为WALL-E写一系列故事，但我们不必承担如此昂贵的成本。这是稳定扩散模型的优点

下面是相关实例，大家可以体验。

调用时请注意主体的名称是：Wall-E-01 robot

When calling, please note that the name of the subject is: Wall-E-01 robot

Prompt: Wall-E-01 robot on the moon 8K resolution, 16:9,Cyberpunk

![02.png](https://s3.amazonaws.com/moonup/production/uploads/1673799514124-636c3909181c81c337f0be90.png)

![11.png](https://s3.amazonaws.com/moonup/production/uploads/1673801747581-63bec1efda08ed0544f5a813.png)

Prompt: Wall-E-01 robot, the background is an old bridge and a pond, mist and swirly clouds in the background, fantastic landscape, hyperrealism, no blur, 4k resolution, ultra detailed, style of Anton Fadeev, Ivan Shishkin, John Berkey

![04.png](https://s3.amazonaws.com/moonup/production/uploads/1673799593235-636c3909181c81c337f0be90.png)

Prompt: illustration of a Wall-E robot sitting on top of the deck of a battle ship traveling through the open sea
![07.png](https://s3.amazonaws.com/moonup/production/uploads/1673799674000-636c3909181c81c337f0be90.png)

Prompt: Wall-E-01 robot cartoon image with rainbow background
![01.png](https://s3.amazonaws.com/moonup/production/uploads/1673799451032-636c3909181c81c337f0be90.png)

![08.png](https://s3.amazonaws.com/moonup/production/uploads/1673799761904-636c3909181c81c337f0be90.png)

![14.png](https://s3.amazonaws.com/moonup/production/uploads/1673801746877-63bec1efda08ed0544f5a813.png)

Prompt:"Wall-E, a small robot with a binocular-shaped head, sitting in the cockpit of a large spaceship, surrounded by high-tech controls and screens displaying various information about the ship's status and location, with a focus on Wall-E's expression and the intricate details of the ship's controls. The image should be in high resolution and have a realistic, futuristic aesthetic."

![15.png](https://s3.amazonaws.com/moonup/production/uploads/1673801745824-63bec1efda08ed0544f5a813.png)

![13.png](https://s3.amazonaws.com/moonup/production/uploads/1673801747231-63bec1efda08ed0544f5a813.png)

![12.png](https://s3.amazonaws.com/moonup/production/uploads/1673801747574-63bec1efda08ed0544f5a813.png)




## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('DiamondYin/Wall-E-01-robot-heywhale')
image = pipeline().images[0]
image
```
