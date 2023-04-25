---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - text-to-image
---

# ProtoThing_200

This model is made using the same formula as Berry's Mix, but replaced NovelAI with AnythingV3, and F222 with Protogen_X3.4.

Edit: fp16 safetensors version added! You can find it under the 'Files' section

## Examples

Below are some examples of images generated using this model (with the Anything V3 VAE):
![Examples](https://huggingface.co/NiteStormz/ProtoThing_200/resolve/main/example.png)

# AmbrosiaFusion
This model is a derivative of ProtoThing_200, merging ProtoThing_200 and Midnight Mixer Alt V2 .safetensors using the sdweb-merge-block-weighted-gui.

## Examples

Below are some examples of images generated using this model (with the Anything V3 VAE):
![Examples](https://huggingface.co/NiteStormz/ProtoThing_200/resolve/main/example%20(ambrosia).png)

# ZestyFusion_200
A product of AutoMBW that merges ProtoThing_200 with another merged model containing [Dreamlike Anime 1.0](https://huggingface.co/dreamlike-art/dreamlike-anime-1.0), animefull-final-pruned, YuzuGinger_v4-pruned and LoRAs merged into it. All credits go to the respective creators of the models and LoRAs.
_Note: due to inclusion of a Dreamlike-art model, a modified license is applied to this particular model as well_

## Examples

Below are some examples of images generated using this model **(using the Anything V3 VAE)**:
![Examples](https://huggingface.co/NiteStormz/ProtoThing_200/resolve/main/example%20(zesty).png)

## License (same as what is written on Anything V3 page)

This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
2. The authors claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
[Please read the full license here](https://huggingface.co/spaces/CompVis/stable-diffusion-license)