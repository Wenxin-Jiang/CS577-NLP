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
The Rapgenerator is trained for [nullsechsroy](https://genius.com/artists/Nullsechsroy) on [german-poetry-gpt2](https://huggingface.co/Anjoe/german-poetry-gpt2) for 20 epochs.

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

# Source code to create a song

```
from transformers import pipeline, AutoTokenizer,AutoModelForCausalLM

# load the model from huggingface
rap_model = AutoModelForCausalLM.from_pretrained("Bachstelze/poetryRapGPT")
tokenizer = AutoTokenizer.from_pretrained("Anjoe/german-poetry-gpt2")
rap_pipe = pipeline('text-generation',
                    model=rap_model,
                    tokenizer=german_gpt_model,
                    pad_token_id=tokenizer.eos_token_id,
                    max_length=250)
                    
# set the artist 
song_artist = "nullsechsroy" # "nullsechsroy Deluxe"
# add a title idea or leave it blank
title = "" # "Kristall" "Fit"

# definition of the song structure
type_with_linenumbers = [("Intro",4),
                        ("Hook",4),
                        ("Part 1",6),
                        ("Part 2",6),
                        ("Outro",4)]
                

def set_title(song_parts):
  """
  we create a title if it isn't set already
  and add the title to the songs parts dictionary
  """
  if len(title) > 0:
    song_parts["Title"] = "\n[Title_" + song_artist + "_" + title + "]\n"
    song_parts["artist_with_title"] = song_artist + "_" + title
  else:
    title_input = "\n[Title_" + song_artist + "_"
    title_lines = rap_pipe(title_input)[0]['generated_text']
    index_title_end = title_lines.index("]\n")
    artist_with_title = title_lines[8:index_title_end]
    song_parts["Title"] =  title_lines[:index_title_end+1]
    song_parts["artist_with_title"] = artist_with_title
  
def create_song_by_parts():
  """
  we iterate over the song structure
  and return the dictionary with the song parts
  """
  song_parts = {}
  set_title(song_parts)

  for (part_type, line_number) in type_with_linenumbers:
    new_song_part = create_song_part(part_type, song_parts["artist_with_title"], line_number)
    song_parts[part_type] = new_song_part

  return song_parts

def get_line(pipe_input, line_number):
  """
  We generate a new song line.
  This function could be scaled to more lines.
  """
  new_lines = rap_pipe(pipe_input)[0]['generated_text'].split("\n")
  if len(new_lines) > line_number + 3:
    new_line = new_lines[line_number+3] + "\n"
    return new_line
  else: #retry
    return get_line(pipe_input, line_number)

def create_song_part(part_type, artist_with_title, lines_number):
  """
  we generate one song part
  """
  start_type = "\n["+part_type+"_"+artist_with_title+"]\n"
  song_part = start_type # + preset start line
  lines = [""]
  
  for line_number in range(lines_number):
    pipe_input = start_type + lines[-1]
    new_line = get_line(pipe_input, line_number)
    lines.append(new_line)
    song_part += new_line
  return song_part

def print_song(song_parts):
  """
  Let's print the generated song
  """
  print(song_parts["Title"])
  print(song_parts["Intro"])
  print(song_parts["Part 1"])
  print(song_parts["Hook"])
  print(song_parts["Part 2"])
  print(song_parts["Hook"])
  print(song_parts["Outro"])

# start the generation of one song
song_parts = create_song_by_parts()
print_song(song_parts)
```