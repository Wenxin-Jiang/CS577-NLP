---
language: de

widget:
- text: "[Title_nullsechsroy feat. YFG Pave_"

tags:
- Text Generation

datasets:
- genius lyrics

license: mit
---
# GPT-Rapgenerator
The Rapgenerator is trained for [nullsechsroy](https://genius.com/artists/Nullsechsroy) on an english [GPT2](https://huggingface.co/transformers/model_doc/gpt2.html) that is converted to a german [GerPT2](https://github.com/bminixhofer/gerpt2).

# Usage
```
from transformers import pipeline, AutoTokenizer,AutoModelForCausalLM

german_gpt_model = "stefan-it/german-gpt2-larger"
rap_model = AutoModelForCausalLM.from_pretrained("Bachstelze/Rapgenerator")
tokenizer = AutoTokenizer.from_pretrained(german_gpt_model)

rap_pipe = pipeline('text-generation',
                    model=rap_model,
                    tokenizer=german_gpt_model,
                    pad_token_id=tokenizer.eos_token_id,
                    max_length=250)
                    
# create a new title with Deluxe as rap-feature
title_line = rap_pipe("[Title_nullsechsroy feat. Deluxe_")[0]['generated_text']
raw_title_line= title_line[33 : int(title_line.index("]"))]
```

We used the [genius](https://docs.genius.com/#/songs-h2) songlyrics from the following artists:

['Ace Tee', 'Aligatoah', 'AnnenMayKantereit', 'Apache 207', 'Azad', 'Badmómzjay', 'Bausa', 'Blumentopf', 'Blumio', 'Capital Bra', 'Casper', 'Celo & Abdi', 'Cro', 'Dardan', 'Dendemann', 'Die P', 'Dondon', 'Dynamite Deluxe', 'Edgar Wasser', 'Eko Fresh', 'Farid Bang', 'Favorite', 'Genetikk', 'Haftbefehl', 'Haiyti', 'Huss und Hodn', 'Jamule', 'Jamule', 'Juju', 'Kasimir1441', 'Katja Krasavice', 'Kay One', 'Kitty Kat', 'Kool Savas', 'LX & Maxwell', 'Leila Akinyi', 'Loredana', 'Loredana & Mozzik', 'Luciano', 'Marsimoto', 'Marteria', 'Morlockk Dilemma', 'Moses Pelham', 'Nimo', 'NullSechsRoy', 'Prinz Pi', 'SSIO', 'SXTN', 'Sabrina Setlur', 'Samy Deluxe', 'Sanito', 'Sebastian Fitzek', 'Shirin David', 'Summer Cem', 'T-Low', 'Ufo361', 'YBRE', 'YFG Pave']

# Example song structure

```
[Title_nullsechsroy_Goodies]
[Part 1_nullsechsroy_Goodies]
Soulja Boy – „Pretty Boy Swag“
Heute bei ihr, aber morgen schon weg, ja
..
[Hook_nullsechsroy_Goodies]
Ich hab' Jungs in der Trap, ich hab' Jungs an der Uni (Ahh)
...
[Part 2_nullsechsroy_Goodies]
Ja, Soulja Boy – „Pretty Boy Swag“
...
[Hook_nullsechsroy_Goodies]
Ich hab' Jungs in der Trap, ich hab' Jungs an der Uni (Ahh)
...
[Post-Hook_nullsechsroy_Goodies]
Ja, ich weiß, sie findet niemals ein'n wie mich (Ahh)
...
```