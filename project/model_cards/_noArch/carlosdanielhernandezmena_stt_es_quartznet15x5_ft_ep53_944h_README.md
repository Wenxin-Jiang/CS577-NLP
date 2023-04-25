---
language:
- es
library_name: nemo
datasets:
- common_voice
- ciempiess_test
- hub4ne_es_LDC98S74
- callhome_es_LDC96S35
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- CTC
- pytorch
- NeMo
- QuartzNet
- QuartzNet15x5
- spanish
license: cc-by-4.0
widget:
model-index:
- name: stt_es_quartznet15x5_ft_ep53_944h
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 10.0 (Test)
      type: mozilla-foundation/common_voice_10_0
      split: test
      args: 
        language: es
    metrics:
    - name: WER
      type: wer
      value: 17.99 
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 10.0 (Dev)
      type: mozilla-foundation/common_voice_10_0
      split: validation
      args: 
        language: es
    metrics:
    - name: WER
      type: wer
      value: 15.97   
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: CIEMPIESS-TEST
      type: ciempiess/ciempiess_test
      split: test
      args: 
        language: es
    metrics:
    - name: WER
      type: wer
      value: 19.48
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: 1997 Spanish Broadcast News Speech (HUB4-NE)
      type: HUB4NE_LDC98S74
      split: test
      args: 
        language: es
    metrics:
    - name: WER
      type: wer
      value: 14.48
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: CALLHOME Spanish Speech (Test)
      type: callhome_LDC96S35
      split: test
      args: 
        language: es
    metrics:
    - name: WER
      type: wer
      value: 55.43
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: CALLHOME Spanish Speech (Dev)
      type: callhome_LDC96S35
      split: validation
      args: 
        language: es
    metrics:
    - name: WER
      type: wer
      value: 56.34  
---

# stt_es_quartznet15x5_ft_ep53_944h

**NOTE! This model was trained with the NeMo version: nemo-toolkit==1.10.0**

The "stt_es_quartznet15x5_ft_ep53_944h" is an acoustic model created with NeMo which is suitable for Automatic Speech Recognition in Spanish. 

It is the result of fine-tuning the model ["stt_es_quartznet15x5.nemo"](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_es_quartznet15x5) with around 944 hours of Spanish data gathered or developed by the [CIEMPIESS-UNAM Project](https://huggingface.co/ciempiess) since 2012. Most of the data is available at the the CIEMPIESS-UNAM Project homepage http://www.ciempiess.org/. The rest can be found in public repositories such as [LDC](https://www.ldc.upenn.edu/) or [OpenSLR](https://openslr.org/)

The specific list of corpora used to fine-tune the model is:

- [CIEMPIESS-LIGHT (18h25m)](https://catalog.ldc.upenn.edu/LDC2017S23)
- [CIEMPIESS-BALANCE (18h20m)](https://catalog.ldc.upenn.edu/LDC2018S11)
- [CIEMPIESS-FEM (13h54m)](https://catalog.ldc.upenn.edu/LDC2019S07)
- [CHM150 (1h38m)](https://catalog.ldc.upenn.edu/LDC2016S04)
- [TEDX_SPANISH (24h29m)](https://openslr.org/67/)
- [LIBRIVOX_SPANISH (73h01m)](https://catalog.ldc.upenn.edu/LDC2020S01)
- [WIKIPEDIA_SPANISH (25h37m)](https://catalog.ldc.upenn.edu/LDC2021S07)
- [VOXFORGE_SPANISH (49h42m)](http://www.voxforge.org/es)
- [MOZILLA COMMON VOICE 10.0 (320h22m)](https://commonvoice.mozilla.org/es)
- [HEROICO (16h33m)](https://catalog.ldc.upenn.edu/LDC2006S37)
- [LATINO-40 (6h48m)](https://catalog.ldc.upenn.edu/LDC95S28)
- [CALLHOME_SPANISH (13h22m)](https://catalog.ldc.upenn.edu/LDC96S35)
- [HUB4NE_SPANISH (31h41m)](https://catalog.ldc.upenn.edu/LDC98S74)
- [FISHER_SPANISH (127h22m)](https://catalog.ldc.upenn.edu/LDC2010S01)
- [Chilean Spanish speech data set (7h08m)](https://openslr.org/71/)
- [Colombian Spanish speech data set (7h34m)](https://openslr.org/72/)
- [Peruvian Spanish speech data set (9h13m)](https://openslr.org/73/)
- [Argentinian Spanish speech data set (8h01m)](https://openslr.org/61/)
- [Puerto Rico Spanish speech data set (1h00m)](https://openslr.org/74/)
- [MediaSpeech Spanish (10h00m)](https://openslr.org/108/)
- [DIMEX100-LIGHT (6h09m)](https://turing.iimas.unam.mx/~luis/DIME/CORPUS-DIMEX.html)
- [DIMEX100-NIÑOS (08h09m)](https://turing.iimas.unam.mx/~luis/DIME/CORPUS-DIMEX.html)
- [GOLEM-UNIVERSUM (00h10m)](https://turing.iimas.unam.mx/~luis/DIME/CORPUS-DIMEX.html)
- [GLISSANDO (6h40m)](https://glissando.labfon.uned.es/es)
- TELE_con_CIENCIA (28h16m) **Unplished Material**
- UNSHAREABLE MATERIAL (118h22m) **Not available for sharing**
	
The fine-tuning process was perform during October (2022) in the servers of the [Language and Voice Laboratory](https://lvl.ru.is/) at Reykjavík University (Iceland) by Carlos Daniel Hernández Mena.

```bibtex
@misc{mena2022quartznet15x5spanish,
      title={Acoustic Model in Spanish: stt_es_quartznet15x5_ft_ep53_944h.}, 
      author={Hernandez Mena, Carlos Daniel},
      year={2022},
      url={https://huggingface.co/carlosdanielhernandezmena/stt_es_quartznet15x5_ft_ep53_944h},
}
```

# Acknowledgements

The author wants to thank to the social service program ["Desarrollo de Tecnologías del Habla"](http://profesores.fi-b.unam.mx/carlos_mena/servicio.html) at the [Facultad de Ingeniería (FI)](https://www.ingenieria.unam.mx/) of the [Universidad Nacional Autónoma de México (UNAM)](https://www.unam.mx/). He also thanks to the social service students for all the hard work.

Special thanks to Jón Guðnason, head of the Language and Voice Lab for providing computational power to make this model possible. The author also thanks to the "Language Technology Programme for Icelandic 2019-2023" which is managed and coordinated by Almannarómur, and it is funded by the Icelandic Ministry of Education, Science and Culture.
