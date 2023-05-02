---
language: sv

widget:
    - text: "Jag har ätit en <mask>"
---

## KB-BART

A [BART](https://arxiv.org/abs/1910.13461) model trained on a Swedish corpus consisting of 15 billion tokens (about 80GB of text). The model was trained with [Fairseq](https://github.com/pytorch/fairseq), and converted to be compatible with Huggingface. 

Training code can be found [here](https://github.com/kb-labb/kb_bart).

## Usage

```python
from transformers import BartForConditionalGeneration, PreTrainedTokenizerFast, AutoTokenizer

model = BartForConditionalGeneration.from_pretrained("KBLab/bart-base-swedish-cased")
tok = AutoTokenizer.from_pretrained("KBLab/bart-base-swedish-cased")

model.eval()

input_ids = tok.encode(
    "Jag har ätit en utsökt <mask> på restaurang vid <mask> .", return_tensors="pt"
)

# Simple greedy search
output_ids = model.generate(
    input_ids,
    min_length=15,
    max_length=25,
    num_beams=1,
    do_sample=False,
)
tok.decode(output_ids[0])
# '</s><s> Jag har ätit en utsökt middag på restaurang vid havet på restaurang vid havet på restaurang vid havet.</s>'


# Sampling
output_ids = model.generate(
    input_ids,
    min_length=15,
    max_length=20,
    num_beams=1,
    do_sample=True,
)
tok.decode(output_ids[0])
#'</s><s> Jag har ätit en utsökt god mat som de tagit in på restaurang vid avröjda</s>'


# Beam search
output_ids = model.generate(
    input_ids,
    min_length=15,
    max_length=25,
    no_repeat_ngram_size=3,
    num_beams=8,
    early_stopping=True,
    do_sample=True,
    num_return_sequences=6
)
tok.decode(output_ids[0])
# '</s><s> Jag har ätit en utsökt middag på restaurang vid havet. Jag har varit ute och gått en sväng.</s><pad><pad>'


# Diverse beam generation
output_ids = model.generate(
    input_ids,
    min_length=50,
    max_length=100,
    no_repeat_ngram_size=3,
    num_beams=8,
    early_stopping=True,
    do_sample=False,
    num_return_sequences=6,
    num_beam_groups=8,
    diversity_penalty=2.0,
)
tok.decode(output_ids[0])
# '</s><s> Jag har ätit en utsökt middag på restaurang vid havet på restaurang. Jag har varit på restaurang i två dagar... Jag..,..!!!.. Så.. Nu.. Hej.. Vi.. Här.</s>'

```


## Acknowledgements

We gratefully acknowledge the HPC RIVR consortium ([www.hpc-rivr.si](https://www.hpc-rivr.si/)) and EuroHPC JU ([eurohpc-ju.europa.eu/](https://eurohpc-ju.europa.eu/)) for funding this research by providing computing resources of the HPC system Vega at the Institute of Information Science ([www.izum.si](https://www.izum.si/)).