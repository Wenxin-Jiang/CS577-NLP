---
license: creativeml-openrail-m
tags:
- stable-diffusion
- stable-diffusion-diffusers
- text-to-image
inference: true
extra_gated_prompt: |-
  This model is open access and available to all, with a CreativeML OpenRAIL-M license further specifying rights and usage.
  The CreativeML OpenRAIL License specifies: 

  1. You can't use the model to deliberately produce nor share illegal or harmful outputs or content 
  2. CompVis claims no rights on the outputs you generate, you are free to use them and are accountable for their use which must not go against the provisions set in the license
  3. You may re-distribute the weights and use the model commercially and/or as a service. If you do, please be aware you have to include the same use restrictions as the ones in the license and share a copy of the CreativeML OpenRAIL-M to all your users (please read the license entirely and carefully)
  Please read the full license carefully here: https://huggingface.co/spaces/CompVis/stable-diffusion-license
---

[![Example][1]][1]

## Why Epic Diffusion

Epîc Diffusion is a general purpose model based on Stable Diffusion 1.x intended to replace the official SD releases 
as your default model. It is focused on providing high quality output in a wide range of different styles, with support 
for NFSW content.

Epîc Diffusion 1.1 is a heavily calibrated merge of SD 1.4, SD 1.5, Analog Diffusion, Wavy Diffusion, Redshift Diffusion, 
Openjourney Diffusion, Samdoesarts Ultramerge, Elldreth's Dream, postapocalypse, Inkpunk Diffusion, Ghibli Diffusion, Mo Di Diffusion, 
Archer Diffusion, Classic Animation Diffusion, Arcane Diffusion, Van Gogh Diffusion, 3DKX, HASDX, Flexible Diffusion, Cinematic Diffusion, 
Shady Art, dvMJv4, dvAuto & mj-v4-look + some dreambooth trained models of my own, blended and reblended multiple times until I got 
the quality & consistency I was looking for

Epic Diffusion is also [available on CivitAI](https://civitai.com/models/3855/epic-diffusion).

## License

This model is open access and available to all, with a CreativeML OpenRAIL-M
license further specifying rights and usage.

The CreativeML OpenRAIL License specifies: 

1. You can't use the model to deliberately produce nor share illegal or
harmful outputs or content 

2. CompVis claims no rights on the outputs you generate, you are free to use
them and are accountable for their use which must not go against the
provisions set in the license

3. You may re-distribute the weights and use the model commercially and/or as
a service. If you do, please be aware you have to include the same use
restrictions as the ones in the license and share a copy of the CreativeML
OpenRAIL-M to all your users (please read the license entirely and carefully)

<a href="https://www.buymeacoffee.com/johnslegers" target="_blank">
  <img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height: 45px !important;width: 162px !important;" >
</a>

## Example prompts

<table>
  <tr style="border: 1px solid;background:#e5e7eb">
    <th style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Prompt
    </th>
    <th style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Parameters
    </th>
    <th style="vertical-align:top;padding:.5714286em!important;border: 1px solid;min-width:270px">
      Output
    </th>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      scarlett johansson, in the style of Wes Anderson, highly detailed, unreal engine, octane render, 8k
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>2263657329<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/O4jXU.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      sansa angeline jolie gessica chastain mummy, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha and william - adolphe bouguereau
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>1310341382<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/JScKL.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Pokimane, Feminine, Mercy, Perfect Sexy Symmetrical Face, Detailed Pupils, Pensive Smirk, Look at Viewer, Leaf Armor, Ilya Kuvshinov, Gil Elvgren, Mucha. Intricate, Octane Render, 4KUHD, Centered, Oil Painting, Bokeh, Rim Lighting.
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>4142902194<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/rLqHN.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Mature babe,artgerm Style, gerald brom, atey ghailan, mike mignola, short cut off shirt knot, wide hips, showing off, exposing herself vulnerable, blushing, exited, confident, demanding, joyful, trending on artstation, double split complementary colors, intricate details, highly detailed,
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3954688283<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/eufe5.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      planet base, windows, night, ground level, no man's sky, digital art, highly detailed, intricate, sharp focus, Trending on Artstation HQ, deviantart, unreal engine 5, 4K UHD image
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>895811336<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/XbfYV.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      berchtesgaden, hyperdetailed, detailed faces, artgerm, wolfenstein, portal 2, Leartes Studios, assassin's creed, alphonse mucha, bouguereau, edmund blair leighton, greg kadel, dynamic lighting, delicate, unreal engine, octane render, 8k
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>1172925287<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/HMZVA.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      princess, detailed portrait, hyperdetailed, detailed faces, irakli nadar, magali villeneuve, Assassin's Creed, Tim Hildebrandt, Ilya Kuvshinov, artgem, greg kadel, dynamic lighting, delicate, unreal engine, octane render, 8k
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>2096567313<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/EqPBr.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      a Photorealistic dramatic hyperrealistic bright blue eyes, African American elegant girl, black hair, white veil,by WLOP,Artgerm,Greg Rutkowski,Alphonse Mucha, Beautiful dynamic dramatic bright sunset lighting,shadows,cinematic atmosphere,Artstation,concept design art,Octane render,8k
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>2999946689<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/1nn2e.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      cutest girl in the world outside, (detailed portrait), in the style of fernanda suarez and simon stalenhag and Ilya Kuvshinov and Wlop and Artgerm and Chie Yoshii and Greg Rutkowski and Waking Life, trending on artstation, featured on pixiv, dynamic lighting, highly detailed, ambient lighting, octane render, 8k
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>2249388004<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/MfLZS.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      military academy, (detailed portrait), steampunk, in the style of arcane and fernanda suarez and dishonored and bioshock and simon stalenhag and Ilya Kuvshinov and Wlop and Artgerm, trending on artstation, featured on pixiv, dynamic lighting, highly detailed, ambient lighting, octane render, 8k
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3877530043<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/BvA3s.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      beautiful female assassin wearing cyberpunk clothing, respirator, cybernetic respirator, (detailed portrait), cell shaded, 4 k, vivid colours, photorealistic concept art by wlop, ilya kuvshinov, artgerm, krenz cushart, greg rutkowski, pixiv. cinematic dramatic atmosphere, sharp focus, volumetric lighting, cinematic lighting, studio quality
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3388890157<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/KUm9A.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      cemetary, pen and ink, in the style of gustave dore highly detailed, octane render, 8k, trending on artstation, sharp focus, studio photo, intricate details, highly detailed, by greg rutkowski
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>568457114<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/90mH1.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      dubai, hyperdetailed, detailed faces, artgem, irakli nadar, mass effect, Tim Hildebrandt, Ilya Kuvshinov, liam wong, greg rutkowski, greg kadel, dynamic lighting, delicate, unreal engine, octane render, 8k, centered, symmetry, painted, intricate, volumetric lighting, beautiful, rich deep colors masterpiece, sharp focus, ultra detailed, in the style of dan mumford and marc simonetti, astrophotography
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>DPM++ SDE<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>4262868463<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/7TjmX.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Little cute forest fluffy chibi cuteness overload, sunny magical background, ultra precious details, intricate details, volumetric lighting, photo realistic, lifelike, photography, digital art, 8k, trending on artstation, sharp focus, studio photo, intricate details, highly detailed, by greg rutkowski, sharp focus, emitting diodes, smoke, artillery, sparks, racks, system unit, motherboard, by pascal blanche rutkowski repin artstation hyperrealism painting concept art of detailed character design matte painting, 4 k resolution blade runner
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>DPM++ SDE Karras<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3849507891<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/skddc.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      15 year old schoolgirl with short straight hair, blue eyes, cute, friendly, round face, cottagecore, intricate, enlightened, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>2276800560<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/L0kVH.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      extreme wide shot a futuristic containment building in a rainforest valley with a city in the distance, national geographic, hyper realistic, 4 k, harsh light
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3260458902<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/p66dH.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      portrait of a middle - eastern female cleric with straight black hair wearing blue and yellow vestments casting fireball, fantasy, highly detailed, digital painting, artstation, concept art, character art, art by greg rutkowski and tyler jacobson and alphonse mucha
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>1379894453<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/FBZuT.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      aSnowshoe Siamese Cat as the doomslayer, realistic scifi cyberpunk power armor robot, closeup portrait art by donato giancola and greg rutkowski, vintage retro scifi, realistic face, digital art, trending on artstation, symmetry
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>2122325442<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/ZjX2f.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Beautiful boy by René Magritte
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>1753689226<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/bgvsg.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      portrait of a dark god, copper wires, visible scars and nerves, intricate, headshot, highly detailed, digital painting, artstation, concept art, sharp focus, cinematic lighting, illustration, art by artgerm and greg rutkowski, alphonse mocha, cgsociety, Olivia
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3355776798<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/8yx4N.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      knight warrior helmet skyrim mask elder scrolls v nordic armor bethesda adam adamowicz illustration character design concept, unreal 5, daz, hyperrealistic, octane render, cosplay, rpg portrait, dynamic lighting, intricate detail, harvest fall vibrancy, cinematic volume inner glowing aura global illumination ray tracing hdr
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>1938574287<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/dY65d.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      berserker portrait, d&d style, fantasy, photorealistic, highly detailed, artstation, smooth, sharp focus, art by michael whelan, artgerm, greg rutkowski and alphonse mucha
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>DPM++ SDE Karras<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>156077154<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/76jz5.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      symmetry product render poster vivid colors classical proportion car, glowing fog intricate, elegant, highly detailed, digital painting, art station, concept art, smooth, sharp focus, illustration,
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>DPM++ SDE Karras<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>4294525772<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/f4jll.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Futuristic Vintage Medium Shot 1920's Poster with Cyberpunk, ovni, tron biker with helmet bike, black in color, with a cyberpunk city background, futuristic lighting, cinematic lighting, cozy lighting, 8k, cinematic poster vintage 1800s
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>1229558409<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/6N6kr.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      beautiful, young woman, cybernetic, cyberpunk, detailed gorgeous face, flowing hair, vaporwave aesthetic, synthwave , digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>264509871<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/IDgVX.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      strong warrior princess| centered| key visual| intricate| highly detailed| breathtaking beauty| precise lineart| vibrant| comprehensive cinematic| Carne Griffiths| Conrad Roset
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>16<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/oTVxB.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      portrait of a rugged 19th century man with mutton chops in a jacket, victorian, concept art, detailed face, fantasy, close up face, highly detailed, cinematic lighting, digital art painting by greg rutkowski
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>16<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/vKamr.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      side profile of cyberpunk body with cyborg skull | cyberpunk | styled in Art Nouveau | insanely detailed | embellishments | high definition | concept art | digital art | vibrant
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>16<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/fkxPX.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      a cute little matte low poly isometric cherry blossom forest island, pink waterfalls, mist, lat lighting, soft shadows, trending on artstation, 3d render, monument valley, fez video game,
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>16<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/M2PAq.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      high resolution concept art of an apartment living room overlooking a large futuristic city with floor to ceiling windows and mid century modern furniture cinematic lighting cgsociety
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>850995814<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/F6GMQ.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      hyperrealistic full length portrait of gorgeous watson from apex legends | blonde | detailed gorgeous face!! | full body!! | armor | intricate | elegant | realistic | hyperrealistic | cinematic | character design | concept art | highly detailed | illustration | digital art | digital painting | depth of field | illustrated by tim brown lee
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3002798343<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/nDe6M.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      Chibi spiderman, high redolution, 3D rendering, octane rendering, modern Disney style
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>20<br>
      <b>Sampler:</b><br>Euler a<br>
      <b>CFG scale:</b><br>7<br>
      <b>Seed:</b><br>3232863832<br>
      <b>Size:</b><br>512x512
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/ixo6D.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      photo of the most beautiful artwork in the world featuring soft lustrous, industrial mechanic real world, fantastic location, working environment, rugged harsh situation worker, full body 8k unity render, action shot, skin pores, detailed intricate iris, very dark lighting, heavy shadows, detailed, detailed face, (vibrant, photo realistic, realistic, dramatic, dark, sharp focus, 8k), (weathered greasy dirty damaged old worn technician worker outfit:1.1), (intricate:1.1), (highly detailed:1.1), digital painting, octane render, artstation, concept art, smooth, sharp focus, illustration, art by artgerm, (loish:0.23), wlop ilya kuvshinov., (global illumination, studio light, volumetric light)<br><br>
      <b>Negative prompt:</b> Asian, black and white, close up, cartoon, 3d, denim, (disfigured), (deformed), (poorly drawn), (extra limbs), blurry, boring, sketch, lackluster, signature, letters, watermark, low res , horrific , mutated , artifacts , bad art , gross , b&w , poor quality , low quality , cropped
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>30<br>
      <b>Sampler:</b><br>DPM++ SDE Karras<br>
      <b>CFG scale:</b><br>10<br>
      <b>Seed:</b><br>169686802<br>
      <b>Size:</b><br>512x640
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/1vx2U.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      photo of the most beautiful artwork in the world featuring soft lustrous, industrial mechanic real world, fantastic location, working environment, rugged harsh situation worker, full body 8k unity render, action shot, skin pores, detailed intricate iris, very dark lighting, heavy shadows, detailed, detailed face, (vibrant, photo realistic, realistic, dramatic, dark, sharp focus, 8k), (weathered greasy dirty damaged old worn technician worker outfit:1.1), (intricate:1.1), (highly detailed:1.1), digital painting, octane render, artstation, concept art, smooth, sharp focus, illustration, art by artgerm, (loish:0.23), wlop ilya kuvshinov., (global illumination, studio light, volumetric light)<br><br>
      <b>Negative prompt:</b> Asian, black and white, close up, cartoon, 3d, denim, (disfigured), (deformed), (poorly drawn), (extra limbs), blurry, boring, sketch, lackluster, signature, letters, watermark, low res , horrific , mutated , artifacts , bad art , gross , b&w , poor quality , low quality , cropped
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>30<br>
      <b>Sampler:</b><br>DPM++ SDE Karras<br>
      <b>CFG scale:</b><br>10<br>
      <b>Seed:</b><br>169686796<br>
      <b>Size:</b><br>512x640<br>
      <b>Denoising strength:</b><br>0.7<br>
      <b>Hires upscale:</b><br>2<br>
      <b>Hires upscaler:</b><br>Latent
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.imgur.com/AC1xKup.png">
    </td>
  </tr>
  <tr>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      dark and gloomy full body 8k unity render, female teen cyborg, Blue yonder hair, wearing broken battle armor, at cluttered and messy shack , action shot, tattered torn shirt, porcelain cracked skin, skin pores, detailed intricate iris, very dark lighting, heavy shadows, detailed, detailed face, (vibrant, photo realistic, realistic, dramatic, dark, sharp focus, 8k)<br><br>
      <b>Negative prompt:</b> nude, Asian, black and white, close up, cartoon, 3d, denim, (disfigured), (deformed), (poorly drawn), (extra limbs), blurry, boring, sketch, lackluster, signature, letters, watermark, low res , horrific , mutated , artifacts , bad art , gross , b&w , poor quality , low quality , cropped
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <b>Steps:</b><br>26<br>
      <b>Sampler:</b><br>DPM++ SDE Karras<br>
      <b>CFG scale:</b><br>7.5<br>
      <b>Seed:</b><br>2388736888<br>
      <b>Size:</b><br>768x1024
    </td>
    <td style="vertical-align:top;padding:.5714286em!important;border: 1px solid">
      <img style="vertical-align:top;margin:0;padding:0" src="https://i.stack.imgur.com/0AcN7.jpg">
    </td>
  </tr>
</table>

[1]: https://i.stack.imgur.com/p9mFM.jpg