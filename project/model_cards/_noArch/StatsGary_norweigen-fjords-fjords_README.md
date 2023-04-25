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
- text: a photo of norweigen-fjords fjords
---

# DreamBooth model for the norweigen-fjords concept trained by StatsGary on the StatsGary/dreambooth-hackathon-images dataset.

This is a Stable Diffusion model fine-tuned on the norweigen-fjords concept with DreamBooth. It can be used by modifying the `instance_prompt`: **a viking on the fjords**

This model was created as part of the DreamBooth Hackathon 🔥. Visit the [organisation page](https://huggingface.co/dreambooth-hackathon) for instructions on how to take part!

## Description


This is a Stable Diffusion model fine-tuned on `fjords` images for the landscape theme. Below are some examples of the images generated on the back of the model:

### Lobster swimming in a Fjord

The below example uses a prompt similar to *lobster swimming in a fjord* to generate the output: 

![lobster.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1673018851087-63b83d10e60862785afef49f.jpeg)

### Viking warrior in a Fjord

This represents a generated Viking warrior on or near a Fjord. The prompt used to generate is **prompt**=*a viking warrior on a fjord*:
![viking_on_fjord.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1673019199954-627cebc6cecd686d4cd7411c.jpeg)

### A yellow submarine (inspired by The Beetles)

Here, we see a yellow submarine inspired by the popular Beetles album. The prompt used to generate is **prompt**=a beetles like yellow submarines on a fjord*:
![Beetles_submarine.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1673019576047-627cebc6cecd686d4cd7411c.jpeg)

### A cruise ship on a fjord

This is based on the **prompt**=*a cruise ship on a fjord*:

![6bd7a6b7-9716-478e-81ea-7f58b59707e8.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1673271806453-627cebc6cecd686d4cd7411c.jpeg)

### Taj Mahal on a Fjord

This generates landmarks near or on the fjord: 

![68dd6b17-bb8c-45e7-bfe6-79442f633121.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674057958178-627cebc6cecd686d4cd7411c.jpeg)

### Watersports on a Fjord

This is an example of a kayaker on a fjord - generated using *prompt*="a kayaker on a fjord":
![1e730131-63c4-4095-9f36-61e8659c946a.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674058117373-627cebc6cecd686d4cd7411c.jpeg)

What about a surfer on a fjord:
![surfer.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674058620579-627cebc6cecd686d4cd7411c.jpeg)

### Godzilla wading through a Fjord
This one is a generated image of Godzilla wading through a Fjord:
![45618490-f4d3-44e4-ac8b-a0375b983576.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674058731220-627cebc6cecd686d4cd7411c.jpeg)

### How about T-Rex
On the theme of Godzilla, what about T-Rex:
![eef051e5-267b-426e-97a1-fbd947185dba.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674058942184-627cebc6cecd686d4cd7411c.jpeg)

## Paintings on a Fjord
We could explore what a **Da Vinci** type painting would look like on a Fjord: 
![davinci.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674664480840-627cebc6cecd686d4cd7411c.jpeg)


## A pet rabbit on a Fjord

What about your pet rabit: 
![rabbit.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674664175251-627cebc6cecd686d4cd7411c.jpeg)

## Pop Art of a Fjord

This is a pop art of a Fjord: 
![pop_art.jpeg](https://s3.amazonaws.com/moonup/production/uploads/1674664922159-627cebc6cecd686d4cd7411c.jpeg).

## Generating your own predictions

The following Python code will allow you to get up and running quickly, just replace the *prompt* field for your own generation, wait for HuggingFace to compute and you should have your own Stable Diffusion object generated against a backdrop of the fjords. Idyllic!

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('StatsGary/norweigen-fjords-fjords')
image = pipeline(prompt='a viking on a fjord').images[0]
image
```

## Supporting article(s)

I have undertaken a blog to explain this: 

- Fjord stable diffusion model: https://hutsons-hacks.info/stable-diffusion-model-for-generating-images-of-fjords
- Stable diffusion application with Streamlit: https://hutsons-hacks.info/stable-diffusion-application-with-streamlit
