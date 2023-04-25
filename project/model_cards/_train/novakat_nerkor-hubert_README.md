---

language: 
  - hu
tags:
- token-classification
license: gpl
metrics:
- F1
widget:
- text: "A jótékonysági szervezet által idézett Forbes-adatok szerint a világ tíz leggazdagabb embere: Elon Musk (Tesla, SpaceX), Jeff Bezos (Amazon, Blue Origin), Bernard Arnault és családja (LVMH, azaz Louis Vuitton és Moët Hennessy), Bill Gates (Microsoft), Larry Ellison (Oracle), Larry Page (Google), Sergey Brin (Google), Mark Zuckerberg (Facebook), Steve Ballmer (Microsoft) és Warren Buffett (befektető).
Miközben vagyonuk együttesen 700 milliárdról másfél ezer milliárd dollárra nőtt 2020 márciusa és 2021 novembere között, jelentős eltérések vannak közöttük: Musk vagyona több mint 1000 százalékos, míg Gatesé szerényebb, 30 százalékos növekedést mutatott."
inference:
  parameters:
    aggregation_strategy: "first"

---

# Hungarian named entity recognition model with four entity types: PER ORG LOC MISC

  - Pretrained model used: SZTAKI-HLT/hubert-base-cc 
  - Finetuned on NYTK-NerKor Corpus
  	
## Limitations

- max_seq_length = 448

## See [https://huggingface.co/novakat/nerkor-cars-onpp-hubert](https://huggingface.co/novakat/nerkor-cars-onpp-hubert) for a much more elaborate Hungarian named entity model.

