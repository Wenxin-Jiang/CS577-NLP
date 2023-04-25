---
license: creativeml-openrail-m
pipeline_tag: text-to-image
---
# Doctor Shotgun's LoRAs

This repository will serve as a location for uploading my personal LoRAs and Dreambooth models.

Check out some of my AI-generated works on Pixiv: https://www.pixiv.net/en/users/90447503

# Model Description and Usage

What is a LoRA? https://github.com/cloneofsimo/lora

e1-e5 represent training length in number of epochs. You may need to lower the network weight on further trained LoRAs if the effects are too strong.

"legacy" LoRAs are approximations extracted from model diffs from my old Dreambooth models, included for completeness.

Automatic1111's WebUI now has native LoRA support. Install them in .\stable-diffusion-webui\models\Lora\ and activate them by prompting \<lora:name_of_your_lora:network_weight\>

If you are on an older version, you will need to use the additional networks extension to load LoRAs: https://github.com/kohya-ss/sd-webui-additional-networks

If the LoRAs seem to not work, make sure you have updated to the latest version of Automatic1111's WebUI and additional networks extension.

# Training Details

LoRAs trained locally using bmaltais GUI for kohya_ss sd-scripts:

https://github.com/bmaltais/kohya_ss

https://github.com/kohya-ss/sd-scripts

Using ACertainty as a base model:

https://huggingface.co/JosephusCheung/ACertainty

Preview images generated using a modified Corneo's 7th Heaven Mix:

https://civitai.com/models/4669/corneos-7th-heaven-mix

# Table of Contents
Persona 5
   - [Ann Takamaki](#ann-takamaki)
   - [Futaba Sakura](#futaba-sakura)
   - [Haru Okumura](#haru-okumura)
   - [Joker (Ren Amamiya)](#joker)
   - [Kasumi Yoshizawa](#kasumi-yoshizawa)
   - [Makoto Niijima](#makoto-niijima)

# Ann Takamaki

Trigger Word: dsann

<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/ann01.png" width="240" height="320" alt=”ann01”>
<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/ann02.png" width="256" height="256" alt=”ann02”>

# Futaba Sakura

Trigger Word: dsfutaba

<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/futaba01.png" width="320" height="240" alt=”futaba01”>
<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/futaba02.png" width="240" height="320" alt=”futaba02”>

# Haru Okumura

Trigger Word: dsharu

<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/haru01.png" width="240" height="320" alt=”haru01”>
<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/haru02.png" width="320" height="240" alt=”haru02”>

# Joker

Trigger Word: dsjoker

<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/joker01.png" width="240" height="320" alt=”joker01”>
<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/joker02.png" width="320" height="240" alt=”joker02”>

# Kasumi Yoshizawa

Trigger Word: dskasumi

<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/kasumi01.png" width="240" height="320" alt=”kasumi01”>
<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/kasumi02.png" width="240" height="320" alt=”kasumi02”>

# Makoto Niijima

Trigger Word: dsmakoto

<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/makoto01.png" width="320" height="240" alt=”makoto01”>
<img src="https://huggingface.co/Doctor-Shotgun/ds-LoRA/resolve/main/Previews/makoto02.png" width="320" height="240" alt=”makoto02”>