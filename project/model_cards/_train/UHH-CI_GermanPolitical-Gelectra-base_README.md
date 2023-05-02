---
language: de
license: mit
datasets:
- Wahl-o-Mat
- Wahlprogramme

widget:
- text: "cdu/csu: kohlekraftwerke sollten verboten werden"
  example_title: "Predict whether CDU/CSU would like to forbid coal-fired power plants"
- text: "grüne: geflüchtete weiter aufnehmen"
  example_title: "Predict whether grüne are positive to accept refugees"
- text: "die linke: vier tage woche"
  example_title: "Predict if 'die Linke' wants people to work 4 instead of 5 days per week"
---

# GermanPolitical-Gelectra-base

Released May 2022, we fine-tuned the german electra model pre-trained by german-nlp-group (orginal model can be found at 'german-nlp-group/electra-base-german-uncased') to classify political sentiment of popular german parties. 
Supported parties at the moment are "CDU/CSU", "SPD", "FDP", "Grüne", "Die Linke", "AfD".

## Overview  
**Architecture:** Gelectra-base (uncased)

**Language:** German  

## Datasets & Methodology
![Methodology for model](https://www.wahl-o-bot.de/img/Method.315efe28.jpg)

For more information about data and methodology visit: https://www.wahl-o-bot.de/Methodik

## Production

The model can be used for free at https://www.wahl-o-bot.de

## Authors

Feel free to contact us about questions or feedback. We are always happy to help.

* Maximilian Witte: `maximilian.witte@uni-hamburg.de`
* Jasper Schwenzow: `jasper.schwenzow@uni-hamburg.de`
* Mark Heitmann: `mark.heitmann@uni-hamburg.de`
* Matthias Assenmacher: `matthias@stat.uni-muenchen.de`

The model is built in collaboration of the University of Hamburg and Ludwig Maximilians University Munich. 

https://www.bwl.uni-hamburg.de/ci.html