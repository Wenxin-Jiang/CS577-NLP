---
license: creativeml-openrail-m
tags:
- pytorch
- diffusers
- stable-diffusion
- text-to-image
- diffusion-models-class
- dreambooth-hackathon
- wildcard
widget:
- text: gwsi necromancer
- text: gwsi
- text: gwsi necromancer car
---

# Game skill icon DreamBooth model trained by pharmapsychotic

This is a model trained on skill icons from the game [Guild Wars](https://guildwars.com). Prompt with just `gwsi` to get the game icon style or add one of the 10 character classes (`assassin`, `dervish`, `elementalist`, `mesmer`, `monk`, `necromancer`, `paragon`, `ranger`, `ritualist`, `warrior`) to summon its color and style. For example the first row in the examples section uses prompts starting with `gwsi necromancer`. 

The training data is much lower resolution than the 512x512 Stable Diffusion 1.5 model so the outputs are intended to be scaled down. 

This was made for the [DreamBooth Hackathon](https://huggingface.co/dreambooth-hackathon)! If you enjoy this or just find the results cool and interesting, drop a like on the model!

## Examples

|  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |  --- | --- | 
| ![](examples/necro1-gwsi_necromancer_feline_fiend.jpg) | ![](examples/necro2-gwsi_necromancer_feline_fiend.jpg) | ![](examples/necro3-gwsi_necromancer_hand.jpg) | ![](examples/necro4-gwsi_necromancer_corpse_explosion.jpg) | ![](examples/necro5-gwsi_necromancer_cthulu.jpg) | ![](examples/necro6-gwsi_necromancer_monster.jpg) | ![](examples/necro7-gwsi_necromancer_mark.jpg) | ![](examples/necro8-gwsi_necromancer_signet.jpg) | 
| ![](examples/war1-gwsi_warrior.jpg) | ![](examples/war2-gwsi_warrior_victory.jpg) | ![](examples/war3-gwsi_warrior_chain_break.jpg) | ![](examples/war4-gwsi_warrior_beat_down.jpg) | ![](examples/war5-gwsi_warrior.jpg) | ![](examples/war6-gwsi_warrior.jpg) | ![](examples/war7-gwsi.jpg) | ![](examples/war8-gwsi_elementalist_glyph.jpg) | 
| ![](examples/elem1-gwsi_elementalist_mind_shock.jpg) | ![](examples/elem2-gwsi_elementalist_immolate.jpg) | ![](examples/elem3-gwsi_elementalist_aura.jpg) | ![](examples/elem4-gwsi_elementalist_aura.jpg) | ![](examples/elem7-gwsi_demon.jpg) | ![](examples/elem5-gwsi_elementalist_lightning_strike.jpg) | ![](examples/elem6-gwsi_elementalist.jpg) | ![](examples/elem8-gwsi_elementalist_freeze.jpg) | 
| ![](examples/monk1-gwsi_monk_sorrow.jpg) | ![](examples/monk2-gwsi_monk_healing_vapors.jpg) | ![](examples/monk3-gwsi_monk_healing_vapors.jpg) | ![](examples/monk4-gwsi_monk_orb_of_healing.jpg) | ![](examples/c1-gwsi.jpg) | ![](examples/c2-gwsi.jpg) | ![](examples/c3-gwsi.jpg) | ![](examples/c4-gwsi.jpg) | 
| ![](examples/car1-gwsi_necromancer_car.jpg) | ![](examples/car2-gwsi_necromancer_car.jpg) | ![](examples/car3-gwsi_necromancer_car.jpg) | ![](examples/car4-gwsi_monk_car.jpg) | ![](examples/car5-gwsi_ritualist_car.jpg) | ![](examples/car6-gwsi_ritualstcar.jpg) | ![](examples/car7-gwsi_warrior_car.jpg) | ![](examples/car8-gwsi_warrior_car.jpg) | 




## Usage

#### With Diffusers

```python
from diffusers import StableDiffusionPipeline

pipeline = StableDiffusionPipeline.from_pretrained('pharma/gwsi')
image = pipeline().images[0]
image
```

#### With SD Web UI
To use with SD Web UI download [pharmapsychotic-gwsi.ckpt](https://huggingface.co/pharma/gwsi/resolve/main/pharmapsychotic-gwsi.ckpt) and put in your models folder.