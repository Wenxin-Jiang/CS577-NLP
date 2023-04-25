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
library_name: diffusers
---

# Model Card for ranma_diffusion

<!-- Provide a quick summary of what the model is/does. [Optional] -->
A fine tuned diffusion model that attempts to imitate the style of late &#39;80s early 90&#39;s anime specifically, the Ranma 1/2 anime.



## Model Description

<!-- Provide a longer summary of what this model is/does. -->
A fine tuned diffusion model that attempts to imitate the style of late &#39;80s early 90&#39;s anime specifically, the Ranma 1/2 anime. Use &#34;80sanimestyle&#34; in your prompt.  This model benefits a lot from playing around with different sampling methods, but I feel like DPM2, DPM++ and their various ititerations, work the best with this model. 



This model was trained using  TheLastBen&#39;s fast-stable-diffusion for dreambooth. Model was trained on  121 screenshots from Ranma 1/2, with 3000 steps, and Anything-V3.0 as the base model. 


![diff_ex_1 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829393-6317f5cd83d8d2fd9035dc7d.png)
![diff_ex_2 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829707-6317f5cd83d8d2fd9035dc7d.png)
![diff_ex_3 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829715-6317f5cd83d8d2fd9035dc7d.png)
![diff_ex_4 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829270-6317f5cd83d8d2fd9035dc7d.png)
![diff_ex_5 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829474-6317f5cd83d8d2fd9035dc7d.png)
![diff_ex_6 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829690-6317f5cd83d8d2fd9035dc7d.png)
![diff_ex_7 copy.png](https://s3.amazonaws.com/moonup/production/uploads/1668994829290-6317f5cd83d8d2fd9035dc7d.png)



- **Language(s) (NLP):** en
- **License:** creativeml-openrail-m
- **Parent Model:** Linaqruf/anything-v3.0