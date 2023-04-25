---
language:
- ru
- en
pipeline_tag: text-to-image
tags:
- PyTorch
- Transformers
thumbnail: "https://github.com/sberbank-ai/ru-dalle"

---
# ruDALL-E Malevich (XL)
## Generate images from text

<img style="text-align:center; display:block;" src="https://huggingface.co/sberbank-ai/rudalle-Malevich/resolve/main/dalle-malevich.jpg" width="200">
"Avocado painting in the style of Malevich"

* [Technical Report (Russian)](https://habr.com/ru/company/sberbank/blog/586926)
* [Demo](https://rudalle.ru)

Model was trained by [Sber AI](https://github.com/sberbank-ai) and [SberDevices](https://sberdevices.ru/) teams.  
* Task: `text2image generation`
* Type: `encoder-decoder`
* Num Parameters: `1.3 B`
* Training Data Volume: `120 million text-image pairs`

### Model Description
This is a 1.3 billion parameter model for Russian, recreating OpenAI's [DALL·E](https://openai.com/blog/dall-e/), a model capable of generating arbitrary images from a text prompt that describes the desired result. 

The generation pipeline includes ruDALL-E, ruCLIP for ranging results, and a superresolution model. 
You can use automatic translation into Russian to create desired images with ruDALL-E.

### How to Use
The easiest way to get familiar with the code and the models is to follow the inference notebook we provide in our [github repo](https://github.com/sberbank-ai/ru-dalle). 

## Motivation
One might say that “investigate, master, and train” is our engineering motto.  Well, we caught the scent, and today we can say that we created from scratch a complete pipeline for generating images from descriptive textual input written in Russian.

Teams at SberAI, SberDevices, Samara University, AIRI and SberCloud all actively contributed.

We trained two versions of the model, each a different size, and named them after Russia’s great abstractionists: Vasily Kandinsky and Kazimir Malevich.
* ruDALL-E Kandinsky (XXL), with 12 billion parameters
* ruDALL-E Malevich (XL), having 1.3 billion parameters

Some of our models are already freely available:
* ruDALL-E Malevich (XL) [[GitHub](https://github.com/sberbank-ai/ru-dalle), [HuggingFace](https://huggingface.co/sberbank-ai/rudalle-Malevich)]
* Sber VQ-GAN [[GitHub](https://github.com/sberbank-ai/sber-vq-gan), [HuggingFace](https://huggingface.co/sberbank-ai/Sber-VQGAN)]
* ruCLIP Small [[GitHub](https://github.com/sberbank-ai/ru-clip), [HuggingFace](https://huggingface.co/sberbank-ai/ru-clip)]
* Super Resolution (Real ESRGAN) [[GitHub](https://github.com/sberbank-ai/Real-ESRGAN), [HuggingFace](https://huggingface.co/sberbank-ai/Real-ESRGAN)]
The latter two models are included in the pipeline for generating images from text (as you’ll see later on).

The models ruDALL-E Malevich (XL), ruDALL-E Kandinsky (XXL), ruCLIP Small, ruCLIP Large, and Super Resolution (Real ESRGAN) will also soon be available on [DataHub](https://mlspace.aicloud.sbercloud.ru/mlspace/datahub).

Training the ruDALL-E neural networks on the Christofari cluster has become the largest calculation task in Russia:
* ruDALL-E Kandinsky (XXL) was trained for 37 days on the 512 GPU TESLA V100, and then also for 11 more days on the 128 GPU TESLA V100, for a total of 20,352 GPU-days;
* ruDALL-E Malevich (XL) was trained for 8 days on the 128 GPU TESLA V100, and then also for 15 more days on the 192 GPU TESLA V100, for a total of 3,904 GPU-days.

Accordingly, training for both models totalled 24,256 GPU-days.

## Model capabilities
The long term goal of this research is the creation of multimodal neural networks. They will be able to pull on concepts from a variety of mediums---from text and visuals at first---in order to better understand the world as a whole.

Image generation might seem like the wrong rabbit hole in our century of big data and search engines.  But it actually addresses two important requirements that search is currently unable to cope with:
1. Being able to describe in writing exactly what you’re looking for and getting a completely new image created personally for you.
2. Being able to create at any time as many license-free illustrations as you could possibly want

"Grand Canyon"
<img style="text-align:center; display:block;" src="https://habrastorage.org/webt/kb/sv/ih/kbsvihfsmz3fx5mvitii0seimi0.jpeg" width="800">

"Salvador Dali picture"
<img style="text-align:center; display:block;" src="https://habrastorage.org/webt/r8/nl/oi/r8nloiq-l8j2ckg6pzh2pufsklm.jpeg" width="800">

"An eagle sits in a tree, looking to the side"
<img style="text-align:center; display:block;" src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/10a/19c/fa2/10a19cfa2cc84aa7c8b99820890e908d.png" width="800">

"Elegant living room with green stuffed chairs"
<img style="text-align:center; display:block;" src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/6fe/e69/d7c/6fee69d7c392239d587725799e0e41e4.png" width="800">

“Raccoon with a gun”
<img style="text-align:center; display:block;" src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/3bb/1b8/7c4/3bb1b87c45bf9305cd342ae9900ac245.png" width="800">

“Pretty lake at sunset”
<img style="text-align:center; display:block;" src="https://habrastorage.org/r/w1560/getpro/habr/upload_files/241/781/fe9/241781fe99da510d4d5fea03af635e88.png" width="800">
