---
language: en
datasets:
- ljspeech
tags:
- audio
- text-to-speech
license: creativeml-openrail-m
---

This is a simple model created using [xVATrainer](https://github.com/DanRuta/xva-trainer) for use with [xVASynth](https://github.com/DanRuta/xVA-Synth) (this can be used with anything that supports this model but the output is designed to work with xVASynth)

This model is designed to replicate the voice of the Engineer from Team Fortress 2, this was a first test for possibly creating more models of this style.

This was fine tuned from the HiFi-GAN and Fastpitch male models built into xVATrainer, finetrained on a dataset of every engineer line from Team Fortress 2 [which can be found here](https://gamebanana.com/mods/294859), the link features voice lines of every class which means that this can be done for every class in a similar way.

I hope that this is one of many models that I end up releasing in this way as I do truely believe in projects such as this to be avaliable for all. I am also refraining from uploading this to NexusMods because of their very heavy restrictions on downloads, I can't stop anyone else from doing so but here is currently the only place this model is uploaded to by myself.

# Usage
## xVASynth
Go to where xVASynth is setup, if it was installed using [the Steam storefront](https://store.steampowered.com/app/1765720/xVASynth_v2/), this will be within the steamapps folder.

Put the files from the tf2_engineer folder into

> [xVASynth folder]\resources\app\models\teamfortress2

If the teamfortress2 folder does not exist then please create it.
The files should be extracted into the folder and not the folder itself so all of the checkpoint files for Team Fortress 2 will be in the same folder

Now launch xVASynth and change the selected game to Team Fortress 2 and the engineer model will now be shown in the left pane

# Creation process
I created a basic script to convert every file to the correct format and run every line through the [OpenAI Wisper model](https://github.com/openai/whisper) and output the lines in a format for xVATrainer to use, manually adjusting incorrect lines (xVATrainer has it's own model for this but I found it to be less accurate).  This resulted in roughly 300 voice snippets.

I then moved to training, on and off over 2 weeks, I ran the training on a laptop RTX 3080 with 16GB of VRAM, as xVATainer makes frequent checkpoints of the model in progress, stopping and starting is a simple process