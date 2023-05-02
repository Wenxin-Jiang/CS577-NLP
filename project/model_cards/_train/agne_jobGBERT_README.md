
---
language: de
license: cc-by-nc-sa-4.0

---
## jobGBERT

This is a domain-adapted transformer-based language model for German-speaking job advertisements.

Is is based on [deepset/gbert-base](https://huggingface.co/deepset/gbert-base), and adapted to the domain of job advertisements trough continued in-domain pretraining on 4 million German-speaking job ads from Switzerland 1990-2020 (5.9 GB data).


### Overview

**Architecture:** BERT base <br>
**Language:** German <br>
**Domain:** Job advertisements <br>
**See also:** [agne/jobBERT-de](https://huggingface.co/agne/jobBERT-de)

### License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License (cc-by-nc-sa-4.0)

Please use the following citation when using our model:

```bibtex
@inproceedings{
    title = "Evaluation of Transfer Learning and Domain Adaptation for Analyzing German-Speaking Job Advertisements",
    author = "Gnehm, Ann-Sophie and
      Bühlmann, Eva and
      Clematide, Simon",
    booktitle = "Proceedings of the 13th Language Resources and Evaluation Conference",
    month = june,
    year = "2022",
    address = "Marseille, France",
    publisher = "European Language Resources Association",
}
```
### Intended usage and limitations

You can use the model for masked language modeling, but it's intended to be fine-tuned on a downstream task.

The model is trained on German-Speaking job ads from Switzerland. It inherits potential bias of its base model, and may contain biases and stereotypes common in job advertisements.

### About us

Ann-Sophie Gnehm: `gnehm [at] soziologie.uzh.ch` <br>
Eva Bühlmann: `bühlmann [at] soziologie.uzh.ch` <br>
Simon Clematide: `simon.clematide [at] cl.uzh.ch` <br>

The  [Swiss Job Market Monitor](https://www.stellenmarktmonitor.uzh.ch/en.html) aims at systematically expanding scientific knowledge about the job market and improving labour market transparency by informing the general public about current developments on the job market.

**Get in touch:** [Mail](mailto:gnehm@soziologie.uzh.ch)  [Website](https://www.stellenmarktmonitor.uzh.ch/en.html) [Zenodo](https://doi.org/10.5281/zenodo.6497853) [SWISSUbase](https://www.swissubase.ch/de/catalogue/studies/11998/18157/overview)
