---
language:
- en
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
- diffusers
inference: true
---

Introducing my new Vivid Watercolors dreambooth model.

The model is trained with beautiful, artist-agnostic watercolor images using the midjourney method.

The token is "wtrcolor style"


It can be challenging to use, but with the right prompts, but it can create stunning artwork.


See an example prompt that I use in tests: 

wtrcolor style, Digital art of (subject), official art, frontal, smiling, masterpiece, Beautiful, ((watercolor)), face paint, paint splatter, intricate details. Highly detailed, detailed eyes, [dripping:0.5], Trending on artstation, by [artist]


Using "watercolor" in the pronpt is necessary to get a good watercolor texture, try words like face (paint, paint splatter, dripping).

For a negative prompt I use this one:

(bad_prompt:0.8), ((((ugly)))), (((duplicate))), ((morbid)), ((mutilated)), [out of frame], extra fingers, mutated hands, ((poorly drawn hands)), ((poorly drawn face)), (((mutation))), (((deformed))), ((ugly)), blurry, ((bad anatomy)), (((bad proportions))), ((extra limbs)), cloned face, (((disfigured))), (((dead eyes))), (((out of frame))), ugly, extra limbs, (bad anatomy), gross proportions, (malformed limbs), ((missing arms)), ((missing legs)), (((extra arms))), (((extra legs))), mutated hands, (fused fingers), (too many fingers), (((long neck))), blur, (((watermarked)), ((out of focus)), (((low contrast))), (((zoomed in))), (((crossed eyes))), (((disfigured)), ((bad art)), (weird colors), (((oversaturated art))), multiple persons, multiple faces, (vector), (vector-art), (((high contrast)))


Here's some txt2img exemples: 


![01789-313339253-wtrcolor style, Beautiful girl walking on the street, watercolor.png](https://s3.amazonaws.com/moonup/production/uploads/1674343785833-635418b012edd0ed5dc1f5a1.png)
![01792-465168129-wtrcolor style, Beautiful girl portrait, watercolor, face paint, paint splatter.png](https://s3.amazonaws.com/moonup/production/uploads/1674343785836-635418b012edd0ed5dc1f5a1.png)
![01798-352490785-wtrcolor style, Digital art of (Margot Robie as Harley Queen) official art, frontal, smiling, masterpiece, Beautiful, watercolor.png](https://s3.amazonaws.com/moonup/production/uploads/1674343787003-635418b012edd0ed5dc1f5a1.png)
![01807-2954444586-wtrcolor style, Digital art of (Wonder Woman) official art, frontal, smiling, masterpiece, Beautiful, ((watercolor)), face paint.png](https://s3.amazonaws.com/moonup/production/uploads/1674343787004-635418b012edd0ed5dc1f5a1.png)
![01830-3282318438-wtrcolor style, Digital art of (Retrowave bunny girl with glasses and headphone character design), official art, frontal, smilin.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786969-635418b012edd0ed5dc1f5a1.png)
![01893-3282318438-wtrcolor style, Digital art of (dog character), official art, frontal, smiling, masterpiece, Beautiful, ((watercolor)), face pai.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786958-635418b012edd0ed5dc1f5a1.png)
![01894-3282318438-wtrcolor style, Digital art of (cat character), official art, frontal, smiling, masterpiece, Beautiful, ((watercolor)), face pai.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786968-635418b012edd0ed5dc1f5a1.png)
![01898-3384663569-wtrcolor style, Digital art of (Supergirl), official art, frontal, smiling, masterpiece, Beautiful, ((watercolor)), face paint,.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786939-635418b012edd0ed5dc1f5a1.png)
![01906-1806000013-wtrcolor style, Digital art of (black girl with the afro hairstyle, fallen angel girl, mermaid underwater, senior man, chubby gi.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786835-635418b012edd0ed5dc1f5a1.png)
![01908-3808560957-wtrcolor style, Digital art of (fallen angel girl with angel wings), official art, frontal, smiling, masterpiece, Beautiful, ((w.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786951-635418b012edd0ed5dc1f5a1.png)
![01932-1882495945-wtrcolor style, Digital art of (chubby woman), official art, frontal, smiling, masterpiece, Beautiful, ((watercolor)), face pain.png](https://s3.amazonaws.com/moonup/production/uploads/1674343786953-635418b012edd0ed5dc1f5a1.png)


Here an img2img exemple:

![bbebbebebebeb.png](https://s3.amazonaws.com/moonup/production/uploads/1674344139512-635418b012edd0ed5dc1f5a1.png)
![classic-blue-volkswagen-beetle-wallpaper-3750x3000_34.jpg](https://s3.amazonaws.com/moonup/production/uploads/1674344139339-635418b012edd0ed5dc1f5a1.jpeg)

In img2img you may need to increase the prompt like: (((wtrcolor style))) 

You can play with the settings, is easier to get good results with the right prompt:
For me, the sweet spot is around 30 steps, euler a, cfg 8-9. (Clip skip 2 kinda lead to softer results)

See the tests here: https://imgur.com/a/ghVhVhy