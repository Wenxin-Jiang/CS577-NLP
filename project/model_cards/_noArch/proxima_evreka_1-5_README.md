---
license: creativeml-openrail-m
tags:
- stable-diffusion
- text-to-image
- textual-inversion
- embedding
---

# cherrypicked examples:

[<img src="https://huggingface.co/proxima/evreka_1-5/resolve/main/cherrypicked_examples.jpg">](https://huggingface.co/proxima/evreka_1-5/blob/main/cherrypicked_examples.jpg)


# about

- this textual inversion embedding was made with SD 1.5
- has more zazz with [Protogen x3.4](https://huggingface.co/darkstorm2150/Protogen_x3.4_Official_Release) (as seen with the results above), probably works nicely with other custom models too
- dataset was mostly landscapes, does influence other things tho, but might have a weaker effect on them
- not great with quokkas

# how to use
- place evreka15.pt **or** evreka15.png in your embeddings folder
- use as `“art by evreka15, [your prompt]”`; it does work better with that structure as opposed to just using "evreka15". this is due to the filewords training afaik, where the prompts in the template follow that syntax
- if the style doesn’t come through strong enough it helps to add `“painting of”`, so the prompt would be `“art by evreka15, painting of [the rest of your prompt]”` or `“painting of [your prompt], art by evreka15,”` (these both express the style differently, most of my examples use the former but you might enjoy the latter more)
- negative prompts that can help: `border, frame, blurry, pixelated, low quality`


# comparisons
[<img src="https://huggingface.co/proxima/evreka_1-5/resolve/main/model_comparisons.jpg">](https://huggingface.co/proxima/evreka_1-5/blob/main/model_comparisons.jpg)

----

[<img src="https://huggingface.co/proxima/evreka_1-5/resolve/main/portrait_comparison.jpg">](https://huggingface.co/proxima/evreka_1-5/blob/main/portrait_comparison.jpg)
# settings
- all examples use Euler_a
- steps between 20 - 52
- CFG scale 7 - 10
- made with highres fix in the [A1111 web ui](https://github.com/AUTOMATIC1111/stable-diffusion-webui)

  
----

if you enjoy this consider buying me a coffee (ノ◕ヮ◕)ノ*:・゚✧
<a href='https://ko-fi.com/S6S6FUYKY' target='_blank'><img height='36' style='border:0px;height:36px;' src='https://storage.ko-fi.com/cdn/kofi3.png?v=3' border='0' alt='Buy Me a Coffee at ko-fi.com' /></a>

----