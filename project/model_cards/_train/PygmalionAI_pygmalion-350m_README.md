---
language:
- en
thumbnail:
tags:
- convAI
- conversational
inference: false
---
# pygmalion-350m

# Model description

This is a proof-of-concept fine-tune of Facebook's OPT-350M model optimized for dialogue, to be used as a stepping stone to higher parameter models.

**Disclaimer:** NSFW data was included in the fine-tuning of this model. Although SFW inputs will usually result in SFW outputs, you are advised to **chat at your own risk. This model is not suitable for use by minors.**

# Fine-tuning process

This model was much easier than expected to create.

We used the [ColossalAI](https://www.colossalai.org/) library to fine-tune the [OPT-350M](https://huggingface.co/facebook/opt-350m) model originally trained by Facebook on The Pile. Though our initial dataset was sets of dialogue gathered from various sources totaling about 50 MB in size, early training runs revealed that the model converged after only 7% of the dataset was passed through. To alleviate this, we massively reduced the size of the dataset to only 273 KB.

ColossalAI's magic allowed for something incredible: this entire model was fine-tuned on a singular GPU with only 6 GB ***(!)*** of VRAM. Fine-tuning took less than an hour to complete.