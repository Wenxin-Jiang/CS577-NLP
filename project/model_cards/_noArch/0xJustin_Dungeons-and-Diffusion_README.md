---
license: creativeml-openrail-m
tags:
  - text-to-image
---

FOR THE NEW VERSION DOWNLOAD 'D&Diffusion3.0_Protogen.ckpt'

The newest version is finetuned from Protogen to great effect. Also works great at resolutions great than 512x512!

Species in new version: aarakocra, aasimar, air_genasi, centaur, dragonborn, drow, dwarf, earth_genasi, elf, firbolg, fire_genasi, gith, gnome, goblin, goliath, halfling, human, illithid, kenku, kobold, lizardfolk, minotaur, orc, tabaxi, thrikreen, tiefling, tortle, warforged, water_genasi
Classes in new version: Artificer, Bard, Barbarian, Cleric, Fighter, Druid, Monk, Paladin, Rogue, Ranger, Sorcerer, Warlock, Wizard, Noble, Townsperson

See the training dataset here for a list of races: https://huggingface.co/datasets/0xJustin/Dungeons-and-Diffusion

Model16000 is trained used `D&D character` as the class prompt, and for whatever reason it ~ seems ~ to work better for centaurs and aarakocra

Model30000 is trained using all of the images as the class images, and I think it emulates the commission DnD character style better. It works VERY well for most races, though sometimes I have to fight to get aarakocra to not be birds or centaurs to not be horses. Tieflings work great, but reining in their horns can be trouble. There is some bleed through between classes- especially for elf ears and horns. Including `elf ears` and `horns` as negative prompts seems to help. 

Good prompts to try things out:

modelshoot style, (extremely detailed CG unity 8k wallpaper), full shot body photo of the most beautiful artwork in the world, english medieval pink (dragonborn druid) witch, black silk robe, nature magic, medieval era, painting by Ed Blinkey, Atey Ghailan, Studio Ghibli, by Jeremy Mann, Greg Manchess, Antonio Moro, trending on ArtStation, trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic, painting art by midjourney and greg rutkowski, teal and gold, petals, countryside, action pose, casting a spell, green swirling magic
Negative prompt: canvas frame, cartoon, 3d, photorealistic
Steps: 20, Sampler: DPM++ 2M Karras, CFG scale: 10, Seed: 2603924688, Size: 512x768, Batch size: 4, Batch pos: 1, Clip skip: 2


`[natural colors], full body tiefling (knight), [watercolor digital 2D painting], (strong shading), hard shadows, blurry, elegant, wearing robes, style of (saga comic) Lois van Baarle and charlie bowater and Sui Ishida, messy, disheveled, thick brushwork, detailed face and eyes, concept art`

`portrait (painting) of tabaxi, de Rivia closeup, suit, collar, formal attire, D&D, fantasy, intricate, elegant, highly detailed, artstation, concept art, matte, sharp focus, (brush strokes), (oil on canvas), hearthstone, art by Titian and Greg Rutkowski and Rembrandt van Rijn and Alphonse Mucha` (inspired by Reddit post) 
 
