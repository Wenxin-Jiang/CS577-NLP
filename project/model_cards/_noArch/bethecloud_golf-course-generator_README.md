---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- landscape
widget:
- text: a photo of golf course with the Acropolis from Ancient Greece in the background
---

## About the Author (Kevin Leffew)

- **Project Announcement & Homepage: https://mirror.xyz/bitkevin.eth/rmqxOCzeefxu53TEBaFByyxNJ9ynOdJ_5CAVhUbuER8**
- **Notebook Repository: https://colab.research.google.com/drive/1EnqpDiKOVYhR0c6f4CgmDg2zqcbYZJpB?usp=sharing**
- **Point of Contact: kleffew94@gmail.com**

![https://mirror.xyz/bitkevin.eth/rmqxOCzeefxu53TEBaFByyxNJ9ynOdJ_5CAVhUbuER8](https://link.storjshare.io/raw/jxn2ciwljrooxfppp4372xoswpmq/golf-course-output/new-banner.jpg)

# A DreamBooth model to power a historic/mythological golf-course image generator

Trained by bethecloud on the bethecloud/golf-courses dataset, this is a Stable Diffusion model fine-tuned on the golf concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a photo of golf course**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Usage

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('bethecloud/golf-course-generator')
image = pipeline().images[0]
image
```

### Dataset Summary: golf-course-generator

This dataset (bethecloud/golf-courses) includes 21 unique images of golf courses pulled from Unsplash.

The dataset is a collection of photographs taken at various golf courses around the world. The images depict a variety of scenes, including fairways, greens, bunkers, water hazards, and clubhouse facilities. The images are high resolution and have been carefully selected to provide a diverse range of visual content for fine-tuning a machine learning model.

The dataset is intended to be used in the context of the Hugging Face Dream Booth hackathon, a competition that challenges participants to build innovative applications using the Hugging Face transformers library. The submission is for the category of landscape.

Overall, this dataset provides a rich source of visual data for machine learning models looking to understand and classify elements of golf courses. Its diverse range of images and high-quality resolution make it well-suited for use in fine-tuning models for tasks such as image classification, object detection, and image segmentation.

By using the golf course images as part of their training data, participants can fine-tune their models to recognize and classify specific features and elements commonly found on golf courses.  The image training dataset is stored on decentralized cloud storage (like Storj DCS), increasing its accessibility, performance, and resilience by distributing across an edge of over 17,000 uncorrelated participants.  You can find a link to the dataset [here](https://link.storjshare.io/s/juo7ynuvpe5svxj3hh454v6fnhba/golf-courses/)

### Languages

The language data in golf-courses is in English (BCP-47 en)

## Dataset Structure

The complete dataset is GBs and consists of 21 objects, representing 0.05GB of stored data across 21 in-line segments on Storj DCS.

### Parallelized download using Decentralized Object Storage (Storj DCS)

A direct download for the dataset is located at https://link.storjshare.io/juo7ynuvpe5svxj3hh454v6fnhba/golf-courses.

In the future, Storj DCS will be used to download large datasets (exceeding 1TB) in a highly parallel, highly performant, and highly economical manner (by utilizing a network of over 17,000 diverse and economically incentivized datacenter node endpoints.

# Examples of image output stored on Storj DCS


Prompt: "a photo of golf course with the Acropolis from Ancient Greece in the background"
![acropolis.jpg](https://link.storjshare.io/raw/juzllxjjzaqf2mh6d77q7chikqda/golf-course-output/golf-acropolis.png)

Prompt: "a photo of golf course with the The Taj Mahal from India in the background"
![taj.jpg](https://link.storjshare.io/raw/jv5uvfvlg4styb5now23g44usvgq/golf-course-output/taj-mahal.png)

Prompt: "a photo of golf course with the Statue of Zeus from Ancient Greece in the background"
![zeus.jpeg](https://link.storjshare.io/raw/jxji4ijudh2n7xrzw55hkjt3cvjq/golf-course-output/statue%20of%20zeus.png)

Prompt: "a photo of golf course with the Pyramids of Giza in the background"
![giza.jpeg](https://link.storjshare.io/raw/jx2lqkhk4fr2tjswcjqjhgtaxepa/golf-course-output/giza.png)


### Curation Rationale

This model was created as a sample by Kevin Leffew as part of the DreamBooth Hackathon.

### Source Data

The source data for the dataset is simply pulled from Unsplash

### Licensing Information

MIT License

## Thanks to John Whitaker and Lewis Tunstall
Thanks to [John Whitaker](https://github.com/johnowhitaker) and [Lewis Tunstall](https://github.com/lewtun) for writing out and describing the initial hackathon parameters at https://huggingface.co/dreambooth-hackathon.
