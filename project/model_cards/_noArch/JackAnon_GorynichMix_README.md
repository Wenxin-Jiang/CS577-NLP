---
license: creativeml-openrail-m
tags:
  - stable-diffusion
  - text-to-image
---
----

# GorynichMix
Welcome to GorynichMix - a latent diffusion models mix for realistic/anime styles. The user has complete control over whether or not to generate NSFW content, and the user's decision to enjoy either SFW or NSFW is entirely up to the user.

# Recipe

**I used old Checkpoint Merger in AUTOMATIC1111 webui (commit hash: b6e5edd74657e3fd1fbd04f341b7a84625d4aa7a) and Merge Block Weighted plugin.**

- Step1: AnythingV4.5-FP32 + Elysium Anime V3 -> (Weighted Sum 0.5) = Tmp1
- Step2: Tmp1 + F222 + SD1.5-pruned-emaonly -> (Add Difference 1.0) = Tmp2
- Step3: (Merge Block Weighted) Derrida_final + Easter-E9 -> (In All 0.3 Out All 0.7 M00 0.50 Base Alpha 0.50) = Tmp3
- Step4: Tmp3 + Dreamlike Photoreal V2 -> (Weighted Sum 0.7) = Tmp4
- Step5: Tmp2 + Tmp4 -> (Weighted Sum 0.3) = GorynichMix

## Example outputs
<img src="https://i.imgur.com/yaUcvLY.jpg"  width="" height="" alt=”example_outputs”>