---
language: en
widget:
- text: $proof$ ; $hypothesis$ = a magnet will not attract a penny
license: apache-2.0
---

# entailer-large

## Model description

Entailer is a text-to-text model trained to create entailment-style explanations for a hypothesis 
(following the format of [EntailmentBank](https://allenai.org/data/entailmentbank)), as well as verifying both the reasoning and the factuality of the premises.

Entailer was built on top of [T5](https://github.com/google-research/text-to-text-transfer-transformer) and comes in 
two sizes: [entailer-11b](https://huggingface.co/allenai/entailer-11b) and
[entailer-large](https://huggingface.co/allenai/entailer-large).

See https://github.com/allenai/entailment_bank for more details.
