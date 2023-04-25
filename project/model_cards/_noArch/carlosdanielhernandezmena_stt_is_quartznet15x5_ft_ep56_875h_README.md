---
language:
- is
library_name: nemo
datasets:
  - language-and-voice-lab/samromur_children
  - language-and-voice-lab/malromur_asr
  - language-and-voice-lab/althingi_asr
  - language-and-voice-lab/samromur_asr
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
- icelandic
license: cc-by-4.0
widget:
model-index:
- name: stt_is_quartznet15x5_ft_ep56_875h
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Samrómur (Test)
      type: language-and-voice-lab/samromur_asr
      split: test
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 28.56
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Samrómur (Dev)
      type: language-and-voice-lab/samromur_asr
      split: validation
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 25.10
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Samrómur Children (Test)
      type: language-and-voice-lab/samromur_children
      split: test
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 32.51
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Samrómur Children (Dev)
      type: language-and-voice-lab/samromur_children
      split: validation
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 21.99
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Malrómur (Test)
      type: language-and-voice-lab/malromur_asr
      split: test
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 22.88
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Malrómur (Dev)
      type: language-and-voice-lab/malromur_asr
      split: validation
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 22.82
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Althingi (Test)
      type: language-and-voice-lab/althingi_asr
      split: test
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 20.74  
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Althingi (Dev)
      type: language-and-voice-lab/althingi_asr
      split: validation
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 20.68
---

# stt_is_quartznet15x5_ft_ep56_875h

**NOTE! This model was trained with the NeMo version: nemo-toolkit==1.10.0**

The "stt_is_quartznet15x5_ft_ep56_875h" is an acoustic model created with NeMo which is suitable for Automatic Speech Recognition in Icelandic. 

It is the result of fine-tuning the model ["QuartzNet15x5Base-En.nemo"](https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels/files) with around 875 hours of Icelandic data developed by the [Language and Voice Laboratory](https://huggingface.co/language-and-voice-lab). Most of the data is available at public repositories such as [LDC](https://www.ldc.upenn.edu/) or [OpenSLR](https://openslr.org/)

The specific list of corpora used to fine-tune the model is:

- [Samrómur 21.05 (114h34m)](http://www.openslr.org/112/)
- [Samrómur Children (127h25m)](https://catalog.ldc.upenn.edu/LDC2022S11)
- [Malrómur (119hh03m)](https://clarin.is/en/resources/malromur/)
- [Althingi Parliamentary Speech (514h29m)](https://catalog.ldc.upenn.edu/LDC2021S01)
	
The fine-tuning process was performed during September (2022) in the servers of the Language and Voice Laboratory (https://lvl.ru.is/) at Reykjavík University (Iceland) by Carlos Daniel Hernández Mena.

```bibtex
@misc{mena2022quartznet15x5icelandic,
      title={Acoustic Model in Icelandic: stt_is_quartznet15x5_ft_ep56_875h.}, 
      author={Hernandez Mena, Carlos Daniel},
      year={2022},
      url={https://huggingface.co/carlosdanielhernandezmena/stt_is_quartznet15x5_ft_ep56_875h},
}
```

# Acknowledgements

Special thanks to Jón Guðnason, head of the Language and Voice Lab for providing computational power to make this model possible. We also want to thank to the "Language Technology Programme for Icelandic 2019-2023" which is managed and coordinated by Almannarómur, and it is funded by the Icelandic Ministry of Education, Science and Culture.
