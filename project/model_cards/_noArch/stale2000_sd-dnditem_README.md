---
inference: true
language:
  - en
tags:
  - stable-diffusion
  - text-to-image
license: other
---

dnditem
---



Examples                   |  Examples
:-------------------------:|:-------------------------:
<img src="https://i.imgur.com/XCg4JmW.png" width="50%"/>  |  <img src="https://i.imgur.com/HRoKRlY.png" width="50%"/>
<img src="https://i.imgur.com/9KTpaIZ.png" width="50%"/>  |
<img src="https://i.imgur.com/rZOJMQD.jpg" width="50%"/>  |


MORE results here!  Hundreds of images!!  https://imgur.com/a/HvhOOjJ  


This is a model (dnditem) for creating magic items, for the game Dungeons and Dragons!  It was trained to be very similar to the official results that are available here:  https://www.dndbeyond.com/magic-items

The model was trained in a pretty specific way though, and requires a specific way of prompting to get good results.  

##Prompting 
---
The keywork is "dnditem", and the prompts should be done in the following way:

"dnditem, [item type], [item style], [background]"

So, for example, a prompt could look like:

"dnditem, a pair of boots, spellguard style, light red circle inner background with white outer background".  
or
"dnditem, a shield, shooting star style, light blue stripe inner background with white outer background".  

##item type
---
Currently the model supports and was trained on the following types:

"a pair of boots", "a cloak", "a pair of gloves", "a helmet", "a necklace", "a ring", "a robe", "a rod", "a shield", "a staff", "a sword", "a wand"


##item_styles
---

The item styles, or abilities, can be found in the itemstyles.txt file.  There are over 100 of them, of all sorts of different types of dnditems.  

Some cool ones to check out are "ultimate evil style", "blue and green transparent animated style", and "spell storing style". 


##background
--- 

Backgrounds should be promopted with an inner and an other background, as well as a "shape" that is either "circle" or "stripe".

So Something like "light blue circle inner background with white outer background".  

