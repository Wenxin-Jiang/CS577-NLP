---
language:
- en
tags:
- stable-diffusion
- text-to-image
license: creativeml-openrail-m
inference: false

---

# Art Model

This model combines three different artstyles

1. [Flower Style](https://huggingface.co/datasets/Nerfgun3/flower_style)
2. [Wlop Style](https://huggingface.co/datasets/Nerfgun3/wlop_style)
3. [Sciamano Style](https://huggingface.co/datasets/Nerfgun3/sciamano)

## Usage
To use this model you have to download the file aswell as drop it into the "\stable-diffusion-webui\models\Stable-diffusion" folder

Class names:

1. ```m_flower``` - For more Flower Style Art
2. ```m_wlop``` - For more Wlop Style Art
3. ```m_sas``` - For more Sciamano Style Art

If it is to strong just add [] around it.

Trained until 9000 steps

Have fun :)

## Example Pictures

<table>
  <tr>
    <td><img src=https://i.imgur.com/2PFk7WC.png width=100% height=100%/></td>
    <td><img src=https://i.imgur.com/qSFfDGC.png width=100% height=100%/></td>
    <td><img src=https://i.imgur.com/PLzVdu5.png width=100% height=100%/></td>
    <td><img src=https://i.imgur.com/kmu1Huy.png width=100% height=100%/></td>
    <td><img src=https://i.imgur.com/QVU5zs2.png width=100% height=100%/></td>
   </tr>
</table>

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the embedding commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)