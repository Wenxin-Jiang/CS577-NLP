---
tags:
- text-to-image
- stable-diffusion
- diffusion-models-class
- dreambooth-hackathon
- wildcard
---

 # If you want to use this style , the prompt: wgz style
**I trianed this weight by using dreambooth**  
There are three models in the library, V1, V2, and beta    
V1:WOLP.ckpt    
V2:wgz v2.ckpt    
BEAT :wgz beta.ckpt    


Let me introduce these versions ,

V1 is the earliest. use 512 resolution for training,

Advantages: the generation logic is good, text2img is used well

Disadvantages: There will be less screen details and less imitation of strokes. The whites of the eyes turn red easily.

V2 adjusted the training set and used 768 resolution training

Advantages: more details, better facial portrayal

Disadvantages: Eyeballs tend to generate green, and the logic of text generation is not good, resulting in poor usability of text2img.

BETA: A version of the training map that is relatively complex has poor logic, but sometimes satisfactory results can be obtained in the img2 img. Try if you want!     

**v2**    
Next, I will show the nice output of V2, which is made by using the img2img. I will also give the configuration I use.

**parameters;**

Prompt :wgz style,portrait of a beautiful women highly detailed,perfect femine face,Classical oil painting,by masamune shirow, by William-tae Kim

Negative prompt: old,men,two poeple,Three dimensional facial features,deep shadows on the five senses,tall nose,Eye shadow,[High bridge], [narrow nose],Deep orbital fossa

Steps: 20, Sampler: DPM++ 2S a Karras, CFG scale: 9.5, Denoising strength: 0.51, Mask blur: 4     
I hope you guys enjoy this model and create works that satisfied


![BETA](https://huggingface.co/hhyxnh/wlop-style-stable-diffusion-weight/resolve/main/v2_sample.png)  
**BETA**  

Below I will show the nice output of a beta. I like its abstract color swatches, but the production rate is not high

![BETA](https://huggingface.co/hhyxnh/wlop-style-stable-diffusion-weight/resolve/main/beta_sample.png)  

I hope you guys enjoy this model and create works that satisfied


Below is the introduction about V1,and some nice output by using V1   
**v1**  

--------------------------

Training with the Elden ring Style ckpt （SD1.5）
  # link：[eldenring-ckpt](https://huggingface.co/nitrosocke/elden-ring-diffusion)
# Training parameters：  
steps： 12500 stpes    
Learning rate：1e-6    
int images number：about 100     
class image number ：200 


**There are some samples:**
![sample](https://huggingface.co/hhyxnh/wlop-style-stable-diffusion-weight/resolve/main/sample1.png)  
![sample](https://huggingface.co/hhyxnh/wlop-style-stable-diffusion-weight/resolve/main/sample2.jpg)

PS:I try hard to achieve the painting style I want by using stable diffusion. I have tried a lot, with failures and successes. With my current technology, I can hardly find progress now. So this model will not be updated in a short time. If you have ideas or want to improve together, you can contact me,happy new year guys.

Telegram: https://t.me/hhhyxnh      
QQ:1602821649

** More pictures in the image folder  

thank you.