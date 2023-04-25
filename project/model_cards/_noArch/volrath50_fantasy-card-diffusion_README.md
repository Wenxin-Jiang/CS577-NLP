---
language:
- en
license: creativeml-openrail-m
thumbnail: "https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/collage_sd_jpg.jpg"
tags:
- stable-diffusion
- text-to-image
- image-to-image
---
#fantasy-card-diffusion

### A comprehensive fine-tuned Stable Diffusion model for generating fantasy trading card style art, trained on all currently available Magic: the Gathering card art (~35k unique pieces of art) to 140,000 steps, using Stable Diffusion v1.5 as a base model. Trained on thousands of concepts, using tags from card data. Has a strong understanding of MTG Artists, planes, sets, colors, card types, creature types and much more.

  <b>Prompts:</b> For best results, prompt the model with card information, <i><b>like you were writing out a custom MtG card</b></i>, with the phrase "MTG card art" and an art description

  <b>Example:</b> "MTG card art, Fiery Merfolk, by Chris Rahn, 2021, creature - merfolk wizard, blue, red, ur, izzet, ravnica, gtp, rtr, grn, an izzet league merfolk, swimming in a ravnica river, casting a fire spell, flames, water, contrast, beautiful composition, intricate details"
 
  <b>For a detailed guide on using the model, and how it was trained, scroll down below</b>

![Collage](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/collage_sd_jpg.jpg)

## Features
- Incorporate the styles of artists you know and love from Magic: the Gathering
- Produce art that looks like it is from a given MtG plane, set or year
- Create fantasy creatures in the style as they exist in Magic the Gathering
- Draw fantasy creature types that are unique to MtG (like Eldrazi)
- Use well known MTG characters (such as the planeswalkers)
- Draw real-world or non-MtG characters, in the style of MTG art 
- Mix and match all of the above

## Updates
- 13 Dec 2022: I am currently training v2 of this model on top of Stable Diffusion 2.1 (512), using the Stable Tuner trainer. This has solved the cropping issue v1 had, and has allowed me to train on the full resolution, uncropped art from Scryfall. I expect to release v2 within the next few days, once I determine a good stopping point, and create new example images. v2 is currently at 25 Epochs (about 87,500 steps), and still showing good improvement each epoch.

## Using the Model

The model was trained on MtG card information, not art descriptions. This has the effect of preserving most non-MtG learning intact, allowing you to mix MtG card terms with an art description for great customization.

Each card was trained with card information pulled from Scryfall in the following format:

MTG card art, [Card Name], by [Artist], [year], [colors (words)], [colors (letters)], [card type], [rarity], [set name], [set code], [plane], [set type], [watermark], [mana cost], [security stamp], [power/toughness], [keywords], [promo type], [story spotlight]

A few examples of actual card data in this format:

MTG card art, Ayula, Queen Among Bears, by Jesper Ejsing, 2019, Green, G, Legendary Creature - Bear, rare, Modern Horizons, mh1, draft_innovation,  1G,  None, 2/2, Fight, 

MTG card art, Force of Will, by Terese Nielsen, 1996, Blue, U, Instant, uncommon, Alliances, all, Dominaria, Terisiare, Ice Age, expansion,  3UU,    

To briefly explain some of the entries:
Every card art is tagged at the start with "MTG card art". Usually you want to use this. It does generalize the image a bit, however. Experiment with using it and not using it. Sometimes, if you are having trouble making something look distinctly "Tarkir" or something, taking off this tag can help de-generalize the art. In a similar fashion, the more general the tag is (ie, rarity, the word "legendary", etc.), the more of a generalizing effect it has on the image. Play around and find out.

Artist: Every artist name is preceded in the training data with the word "by", as in "by Mark Tedin". The model has a really good understanding of the styles of MtG artists - that's actually how this project started. My exposure to art, frankly, is mostly through Magic: the Gathering, and back in August, was finding that the base Stable Diffusion model just did not have a great understanding of a lot of the artists I was trying to draw from, with some exceptions (Greg Rutkowski, of course, and Rebbecca Guay are well represented in the base Stable Diffusion model.) Even if not trying to create MtG-style art, this model should be great for using the art styles of MtG artists. It also works really well to mix artist styles. See the "Innistrad Moon Goddess" example below, where I used six different artist styles with varying weights to create the look I was going for.

Set type: this is usually "expansion". Other possibilities are "core", "funny", and some other. You can check the Scryfall API documents for more information.

Security stamp: I translated some of these for ease of use. The main two of note are "acorn" and "universes beyond". There are a few other rare stamps, like one for the My Little Pony cards.

Story Spotlight: cards that are a story spotlight are tagged as such. This wasn't really worth including, and I'll probably take it out of a future version of the model.

Pretty much every tag from normal Stable Diffusion still works as expected (ie, extremely detailed, intricate details). I've found adding "beautiful composition" tends to make things look nice, but I'm sure everyone has their own set of personal tags they like to use - they should work with this model.

I like to write my prompts like an art description - you can see in the examples I made up below.

## Example Images and Prompts

This model is trained on so many things, I'm just scratching the surface of figuring out what it can do. I thought it would be helpful to show a gallery of the sort of things I've been able to create with it.

Full generation parameters, seeds, etc, should be in the images. All these examples were made with Automatic1111's UI, fantasycarddiffusion-140000.ckpt, and the "DPM++2S a Karras" sampler. CFG varies - I find around 11 works as a good baseline. Most of these were done with around 40-50 steps - probably overkill.

<b>Note:</b> The example prompts were done with Automatic1111's WebUI, and use both prompt weighting and negative prompts, and will not work the same out of the box in the demo on this page.

# Ascended Eldrazi
(an Eldrazi that has somehow made his way to Theros, chilled out, and attained godhood)

![Ascended-Eldrazi](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/ascended-eldrazi.png)

MTG card art, ascended eldrazi, (by eric deschamps:1.1), (legendary enchantment creature - god:1.2) (eldrazi:1.2), colorless, theros, ths, jou, bng, thb, mythic, indestructible, annihilator, trample, a wise eldrazi titan emerging from the horizon, ascended to godhood, now looking serene, calm, divine, powerful, beautiful composition, emrakul, kozilek, ulamog, (sense of scale:1.2), sense of wonder, overwhelming, extremely detailed, intricate details

Negative prompt: weak, angry, scary, underwhelming, powerless

# Speedy Sliver
(a Mardu sliver that gives dash, on Tarkir)

![Speedy-Sliver](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/speedy-sliver.png)

MTG card art, speedy sliver, by John avon, Creature - (sliver:1.3), white, black, red, wbr, (Mardu:1.1), Khans of tarkir, ktk, dash, a fast sliver is speeding through the Mardu (steppe:1.1) landscape, beautiful composition

Negative prompt: human, humanoid, m14

# Taylor Swift, Wandering Bard
(self explanatory, Taylor Swift, as a bard, on Eldraine. Future Secret Lair?)

![Taylor-Swift](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/taylor-swift.png)

mtg card art, (Taylor Swift:1.2), wandering bard, legendary creature - human (bard:1.2), white, red, green, wrg, throne of eldraine, eld, by chris rahn, by volkan baga, by zoltan boros, armored bard taylor swift holding her weapons and instruments, beautiful composition, detailed, realistic fantasy painting, masterpiece, best quality,

Negative prompt: guitar, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry

# Emrakul, Compleated Doom
(The Phyrexians have sprung Emrakul from Innistrad's moon, compleated her, and are now attacking Strixhaven. It's a bad day to go to school.)

![Phyrexian-Emrakul](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/pyrexian-emrakul.png)

mtg card art, (emrakul:1.2), (compleated:1.1) doom, (by seb mckinnon:1.1), legendary creature - (phyrexian:1.1) (eldrazi:1.2) (horror:1.1), black, (strixhaven, arcivos:1.2), annihilator, (infect:1.2), 15/15, a (phyrexianized:1.1), compleated Emrakul, attacking (strixhaven school, university campus:1.2), stx, beautiful composition, detailed painting, (sense of scale:1.2), horror, dark, terrifying, eldritch horror, new phyrexia, nph, rise of the eldrazi, roe, extremely detailed, intricate details, masterpiece, best quality, emrakul, the aeons torn, emrakul, the promised end

Negative prompt: zendikar, water, ocean, funny, happy, optimistic, bright, tentacles, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, octopus, spikes, urchin, tentacles, arms, hands, legs

# Ayula, Ascended Bear
(Ayula, Queen Among Bears is now a Planeswalker, and has taken up residence in Kaladesh)

![Ayula-Kaladesh](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/ayula-kaladesh.png)

mtg card art, ayula, ascended (bear,:1.1) (by jesper ejsing,:1.1) green, g, legendary planeswalker - (bear:1.1), kaladesh, aether revolt, kld, aer, mythic, beautiful composition, a powerful bear planeswalker riding in a kaladesh (vehicle:1.1), looking very serious, intricate details, ayula, queen among bears, mh1, 2/2, 1g, masterpiece, best quality

Negative prompt: silly, human, humanoid, breasts, anthropomorphic, bipedal, funny, lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, watermark, blurry

# Neltharion, Deathwing
(My attempt at imagining Deathwing as a classic Elder Dragon Legend, with the World of Warcraft: Cataclysm Cinematic scene)

![Legends-Deathwing](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/legends-deathwing.png)

mtg card art, neltharion, (deathwing:1.2), (by edward beard, jr:1.1), 1994, legendary creature - (elder dragon:1.1), black, red, br, legends, leg, flying, trample, (world of warcraft cataclysm:1.2), large Firey flaming black dragon perched on stormwind castle rampart, roaring, breathing fire, flames, destruction, beautiful composition, extremely detailed, intricate details, masterpiece, best quality, terrifying, epic, cinematic

Negative prompt: lowres, text, error, cropped, worst quality, low quality, normal quality, jpeg artifacts, watermark, blurry, human, humanoid, deformed, mutant, (ugly:1.3)

# Harambe, Simian Champion of Tarkir
(Harambe did not die, his planeswalker spark ignited.)

![Harambe](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/harambe.png)

(harambe:1.1), simian champion of tarkir, by magali villeneuve, legendary planeswalker - ape (monk:1.2), white, blue, red, wur, (jeskai:1.2), khans of tarkir, ktk, planeswalker harambe training with the jeskai, in a (monastery:1.2), in the mountains, wearing robes, martial arts, beautiful composition, extremely detailed, intricate details, masterpiece, best quality,

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry

# Gabe Newell, Techno-Wizard
(Apologies to Gabe for the prompt - I wanted to make him look kind of like he does today, and the model kept trying to make him look like he did years ago.)

![Gabe](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/gabe.png)

mtg card art, (gabe newell:1.3), techno-wizard, by zezhou chen, legendary creature - human wizard, blue, red, ur, izzet, ravnica, beautiful composition, (grey beard:1.1), (gray hair:1.1), elderly izzet techno wizard gabe newell is casting a spell, powerful, intelligent, epic composition, cinematic, dramatic, masterpiece, best quality, extremely detailed, intricate details

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry, young, silly, goofy, funny

# Luna, Blind Lunar Goddess of Innistrad's Moon
(Or maybe just Emrakul in disguise?)

![Moon-Goddess](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/moon-goddess.png)

mtg card art, luna, blind lunar goddess of innistrad's moon, legendary enchantment creature - (god:1.1), by howard lyon, (by chris rahn:1.1), (by seb mckinnon:1.1), (by terese nielsen:0.8), (by rebecca guay:0.8), (by richard kane ferguson:1.1), (innistrad:1.3), dark ascension, shadows over innistrad, inn, dka, soi, white, blue, black, wub, mythic, (blindfolded cute young woman:1.2) as smug (moon goddess:1.1), sitting on throne, dark lighting, full moon night, long white hair, pale skin, (silver blindfold:1.1), opalescent robes, ethereal, celestial, mysterious, beautiful composition

Negative prompt: orange

# Goblin Flamethrower
(the model can generate instants and sorceries, too)

![Goblin Flamethrower](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/goblin-flamethrower.png)

mtg card art, (goblin flamethrower:1.1), red, r, instant, sorcery, onslaught, legions, scourge, ons, lgn, scg, a crazed, intense, happy goblin is shooting fire from a flamethrower, dangerous, reckless, beautiful composition

Negative prompt: (ugly:1.5), lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry

# Mox Topaz, Mirage
(If there had been a Mox Topaz in the Mirage block, drawing inspiration from Volkan Baga's Vintage Masters mox art)

![Mox-Topaz-Mirage](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/mox-topaz-mirage.png)

Mtg card art, two african hands cupped together holding a (mox topaz:1.1) on a gold chain, in the middle of the palm, in front of the (African savannah:1.1), by Terese Nielsen, (by Volkan baga:1.1), by Dan Frazier, artifact, beautiful composition, jamuraa, mirage, mir, vma

Negative prompt: deformed, bad anatomy

# Mox Topaz, Alpha
(similarly, if there had been a sixth color of Magic, Orange, way back in Alpha)

![Mox-Topaz-Alpha](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/mox-topaz-alpha.png)

(mox topaz:1.1) ( by dan frazier:1.2), artifact, rare, (limited edition alpha, lea:1.1), (1993,:1.1) a mox topaz on a chain

Negative prompt: lowres, cropped, worst quality, low quality, normal quality, jpeg artifacts, watermark, blurry

# Island (Phyrexian Toronto)
(the Phyrexians have invaded and compleated Toronto)

![Pyrexian-Toronto](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/pyrexian-toronto.png)

mtg card art, (toronto:1.2), (basic land - island:1.1), new phyrexia, nph, by adam paquette, (toronto skyline:1.2), (phyrexian:1.1), dark, horror, cn tower, rogers centre, extremely detailed, intricate details, masterpiece, best quality

# Ariel, the Little Mermaid
(Give it time and I'm sure there will be a secret lair.)

![Ariel](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/ariel.png)

mtg card art, (ariel, the little mermaid:1.2), legendary creature - (merfolk:1.1), blue, white, red, uwr, (theros:1.1), by Greg Staples, beautiful composition, ariel sitting on a rock with waves, theros temple in background, masterpiece, best quality,

Negative prompt: green skin, blue skin, red tail, lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry

# Batman, the Dark Knight
(Likewise, the Secret Lair is only a matter of time.)

![Batman](https://huggingface.co/volrath50/fantasy-card-diffusion/resolve/main/images/batman.png)

mtg card art, batman, the dark knight, by justine cruz, by zoltan boros, legendary creature - human ninja, white, blue, black, (ub:1.1), (dimir,:1.1), (ravnica:1.1), (kamigawa:0.9), neon dynasty, neo, innistrad, investigate, ninjutsu, (at night:1.3), on roof, dark lighting, masterpiece, best quality,

Negative prompt: lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry

## Training and dataset
Training was done on a dataset consisting of cropped, 512x512 versions of the art for every MtG card (about 35,000 images), each of which was tagged using a custom python script, from data pulled from Scryfall. Training was done with the Dreambooth extension for Automatic1111's wonderful UI, to 140,000 steps, over the course of a couple days, on my 4090. I changed settings several times as I went, generally increasing batch size and lowering learning rate. At the moment, I am at batch size 10, gradient accumulation 5, and learning rate 4e-7, and that seems to be working well.

The result is a comprehensive model that has a good understanding of MTG artists, sets, planes, card types, creature types, years, colors, and more. If you had ever wondered what a Merfolk, drawn by Ron Spencer, would have looked like on Tarkir, as part of the Mardu clan, with dash, haste, and trample - this model can deliver what you want.

I have uploaded the python script that I used to generate the training data set, which should get you uncropped images and identical text (or near identical) text files, with used with the "unique artwork" json from https://scryfall.com/docs/api/bulk-data

The script is simple, and could probably be improved and cleaned up. Prior to this project, I hadn't done any coding in 20 years, when I was a teenager, and had never used Python prior to hacking this together with vague memories of Perl in 2000-2001, liberal use of Github co-pilot and lots of googling.

Cropping was done with ImageMagick (see below, under issues).

## Issues
- This was intended to be a second test run on the full data set (the first did not go well), so some corners were cut for the purpose of starting my "testing." The model turned out far better than I had expected, so I've decided to release it as is, and hope other people enjoy it as much as I have. But there are some issues that I am aware of and intend to work on fixing for future releases
- Cropping: MTG art is rectangular. I initially tried to use a trainer that could handle different aspect ratios, but after a couple failed tries, I just did a quick mass cropping job with ImageMagick, resizing and cropping everything to 512x512, so I could get training running. I forget what exactly I did, but it appears it focused on the left side of the card, universally cutting off the right side. You'll see this in lots of images, that tend to have everything on the right as a result
- Plane information was only added around step 70,000, so it may be less trained than other information - basically, I wanted a way to group sets together by plane, as I was finding how well it knew the look of a set depended on whether WotC had incorporated the name of the plane into the set itself - ie: using "Theros" would only get you "Theros" and "Theros: Beyond Death" and not "Born of the Gods" or "Journey into Nyx"
- Some artists use special characters in their name. I tried to take away all accents, but I missed at least one, Tom Wänerstrand, who is trained as Tom Wänerstrand, with the umlaut
- Greg Rutkowski: Not an issue, but the poster boy for AI art, Greg Rutkowski, is an MTG artist. He uses the Polish form of his name on MTG cards, Grzegorz Rutkowski, and that is what this model was trained with. So you'll get different results using "by Greg Rutkowski" vs "by Grzegorz Rutkowski"
