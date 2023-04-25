---
license: creativeml-openrail-m
tags:
- text-to-image
---
### Contain Real Ingredients on Stable Diffusion 2 via Dreambooth
#### model by estelleflores

![image 20](https://i.ibb.co/6b0ZBtr/1.png)

This is a Stable Diffusion 2 model fine-tuned to the CRIsimsEstelle concept taught to Stable Diffusion with Dreambooth.

![image 21](https://i.ibb.co/7tL6Vs4/59.png)

It can be used by modifying the `instance_prompt`: **3d render in \<cri-sims> style** or just using the initializer \'\<cri-sims> style' somewhere in your prompt will work.

![image 22](https://i.ibb.co/H21FX8Q/37.png)

Images used for training this concept come from the [project Contain Real Ingredients](https://teia.art/estelle), an art practice inside the game The Sims 4 by artist Estelle Flores:
![image 0](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/13.jpeg)
![image 1](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/0.jpeg)
![image 2](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/7.jpeg)
![image 3](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/11.jpeg)
![image 4](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/10.jpeg)
![image 5](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/2.jpeg)
![image 6](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/8.jpeg)
![image 7](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/3.jpeg)
![image 8](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/12.jpeg)
![image 9](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/4.jpeg)
![image 10](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/5.jpeg)
![image 11](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/1.jpeg)
![image 12](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/14.jpeg)
![image 13](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/9.jpeg)
![image 14](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/17.jpeg)
![image 15](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/16.jpeg)
![image 16](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/18.jpeg)
![image 17](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/6.jpeg)
![image 18](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/15.jpeg)
![image 19](https://huggingface.co/sd-dreambooth-library/crisimsestelle/resolve/main/concept_images/19.jpeg)


You can also train your own concepts and upload them to the library by using [this notebook](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_training.ipynb).
And you can run your new concept via `diffusers`: [Colab Notebook for Inference](https://colab.research.google.com/github/huggingface/notebooks/blob/main/diffusers/sd_dreambooth_inference.ipynb)