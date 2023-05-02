---
license: mit
language: 
- en
task_categories:
- fill-mask
task_ids:
- masked-language-modeling
pipeline_tag: fill-mask
widget:
- text: "M67 is one of the most studied [MASK] clusters."
  example_title: "M67"
- text: "A solar twin is a star with [MASK] parameters and chemical composition very similar to our Sun."
  example_title: "solar twin"
- text: "The dynamical evolution of planets close to their star is affected by [MASK] effects"
  example_title: "dynamical evolution"
- text: "The Kepler satellite collected high-precision long-term and continuous light [MASK] for more than 100,000 solar-type stars"
  example_title: "Kepler satellite"
- text: "The Local Group is composed of the Milky Way, the [MASK] Galaxy, and numerous smaller satellite galaxies."
  example_title: "Local Group"
- text: "Cepheid variables are used to determine the [MASK] to galaxies in the local universe."
  example_title: "Cepheid"
- text: "Jets are created and sustained by [MASK] of matter onto a compact massive object."
  example_title: "Jets"
- text: "A single star of one solar mass will evolve into a [MASK] dwarf."
  example_title: "single star"
- text: "The Very Large Array observes the sky at [MASK] wavelengths."
  example_title: "Very Large Array"
- text: "Elements heavier than [MASK] are generated in supernovae explosions."
  example_title: "Elements"
- text: "Spitzer was the first [MASK] to fly in an Earth-trailing orbit."
  example_title: "Spitzer"
- text: "Galaxy [MASK] can occur when two (or more) galaxies collide"
  example_title: "galaxies collide"
- text: "Dark [MASK] is a hypothetical form of matter thought to account for approximately 85% of the matter in the universe."
  example_title: "hypothetical matter"
- text: "The cosmic microwave background (CMB, CMBR), in Big Bang cosmology, is electromagnetic radiation which is a remnant from an early stage of the [MASK]."
  example_title: "CMBR"
- text: "The Local Group of galaxies is pulled toward The Great [MASK]."
  example_title: "galaxies pulled"
- text: "The Moon is the only [MASK] of the Earth."
  example_title: "Moon"
- text: "Galaxies are categorized according to their visual morphology as [MASK], spiral, or irregular."
  example_title: "morphology"
- text: "Stars are made mostly of [MASK]."
  example_title: "Stars moslyl"
- text: "Comet tails are created as comets approach the [MASK]."
  example_title: "Comet tails"
- text: "Pluto is a dwarf [MASK] in the Kuiper Belt."
  example_title: "Pluto"
- text: "The Large and Small Magellanic Clouds are irregular [MASK] galaxies and are two satellite galaxies of the Milky Way."
  example_title: "Magellanic Clouds"
- text: "The Milky Way has a [MASK] black hole, Sagittarius A*, at its center."
  example_title: "Milky Way"
- text: "Andromeda is the nearest large [MASK] to the Milky Way and is roughly its equal in mass."
  example_title: "Andromeda"
- text: "The [MASK] medium is the gas and dust between stars."
  example_title: "gast and dust"
---

# ***astroBERT: a language model for astrophysics***
This public repository contains the work of the [NASA/ADS](https://ui.adsabs.harvard.edu/) on building an NLP language model tailored to astrophysics, along with tutorials and miscellaneous related files. 
This model is **cased** (it treats `ads` and `ADS` differently). 

## astroBERT models
0. **Base model**: Pretrained model on English language using a masked language modeling (MLM) and next sentence prediction (NSP) objective. It was introduced in [this paper at ADASS 2021](https://arxiv.org/abs/2112.00590) and made public at ADASS 2022.  
1. **NER-DEAL model**: This model adds a token classification head to the base model finetuned on the [DEAL@WIESP2022 named entity recognition](https://ui.adsabs.harvard.edu/WIESP/2022/SharedTasks) task. Must be loaded from the `revision='NER-DEAL'` branch (see tutorial 2).

### Tutorials
0. [generate text embedding (for downstream tasks)](https://nbviewer.org/urls/huggingface.co/adsabs/astroBERT/raw/main/Tutorials/0_Embeddings.ipynb)
1. [use astroBERT for the Fill-Mask task](https://nbviewer.org/urls/huggingface.co/adsabs/astroBERT/raw/main/Tutorials/1_Fill-Mask.ipynb)
2. [make NER-DEAL predictions](https://nbviewer.org/urls/huggingface.co/adsabs/astroBERT/raw/main/Tutorials/2_NER_DEAL.ipynb)


### BibTeX
```bibtex
@ARTICLE{2021arXiv211200590G,
       author = {{Grezes}, Felix and {Blanco-Cuaresma}, Sergi and {Accomazzi}, Alberto and {Kurtz}, Michael J. and {Shapurian}, Golnaz and {Henneken}, Edwin and {Grant}, Carolyn S. and {Thompson}, Donna M. and {Chyla}, Roman and {McDonald}, Stephen and {Hostetler}, Timothy W. and {Templeton}, Matthew R. and {Lockhart}, Kelly E. and {Martinovic}, Nemanja and {Chen}, Shinyi and {Tanner}, Chris and {Protopapas}, Pavlos},
        title = "{Building astroBERT, a language model for Astronomy \& Astrophysics}",
      journal = {arXiv e-prints},
     keywords = {Computer Science - Computation and Language, Astrophysics - Instrumentation and Methods for Astrophysics},
         year = 2021,
        month = dec,
          eid = {arXiv:2112.00590},
        pages = {arXiv:2112.00590},
archivePrefix = {arXiv},
       eprint = {2112.00590},
 primaryClass = {cs.CL},
       adsurl = {https://ui.adsabs.harvard.edu/abs/2021arXiv211200590G},
      adsnote = {Provided by the SAO/NASA Astrophysics Data System}
}
```