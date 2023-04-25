---
license: other
tags:
- text-to-speech
- neural-vocoder
- diffusion probabilistic model
inference: false
datasets: 
- LJSpeech
extra_gated_prompt: |-
  One more step before getting this model.
  This model is open access and available to all, with a license further specifying rights and usage.

  Any organization or individual is prohibited from using any technology mentioned in this paper to generate someone's speech without his/her consent, including but not limited to government leaders, political figures, and celebrities. If you do not comply with this item, you could be in violation of copyright laws.

  
  By clicking on "Access repository" below, you accept that your *contact information* (email address and username) can be shared with the model authors as well.
    
extra_gated_fields:
 I have read the License and agree with its terms: checkbox
---

# ProDiff and FastDiff Model Card

## Key Features
  - **Extremely-Fast** diffusion text-to-speech synthesis pipeline for potential **industrial deployment**.
  - **Tutorial and code base** for speech diffusion models.
  - More **supported diffusion mechanism** (e.g., guided diffusion) will be available.


## Model Details
- **Model type:** Diffusion-based text-to-speech generation model
- **Language(s):** English
- **Model Description:** A conditional diffusion probabilistic model capable of generating high fidelity speech efficiently.
- **Resources for more information:** [FastDiff GitHub Repository](https://github.com/Rongjiehuang/FastDiff), [FastDiff Paper](https://arxiv.org/abs/2204.09934).  [ProDiff GitHub Repository](https://github.com/Rongjiehuang/ProDiff), [ProDiff Paper](https://arxiv.org/abs/2207.06389).
- **Cite as:**

      @inproceedings{huang2022prodiff,
         title={ProDiff: Progressive Fast Diffusion Model For High-Quality Text-to-Speech},
         author={Huang, Rongjie and Zhao, Zhou and Liu, Huadai and Liu, Jinglin and Cui, Chenye and Ren, Yi},
         booktitle={Proceedings of the 30th ACM International Conference on Multimedia},
         year={2022}

      @inproceedings{huang2022fastdiff,
         title={FastDiff: A Fast Conditional Diffusion Model for High-Quality Speech Synthesis},
         author={Huang, Rongjie and Lam, Max WY and Wang, Jun and Su, Dan and Yu, Dong and Ren, Yi and Zhao, Zhou},
         booktitle = {Proceedings of the Thirty-First International Joint Conference on Artificial Intelligence, {IJCAI-22}},
         year={2022}
- 


*This model card was written based on the [DALL-E Mini model card](https://huggingface.co/dalle-mini/dalle-mini).*