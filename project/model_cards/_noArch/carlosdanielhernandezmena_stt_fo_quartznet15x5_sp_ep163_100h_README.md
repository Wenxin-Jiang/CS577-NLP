---
language:
- fo
library_name: nemo
datasets:
- carlosdanielhernandezmena/ravnursson_asr
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
- faroese
- faroe islands
license: cc-by-4.0
widget:
model-index:
- name: stt_fo_quartznet15x5_sp_ep163_100h
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Ravnursson Corpus (Test)
      type: carlosdanielhernandezmena/ravnursson_asr
      split: test
      args: 
        language: fo
    metrics:
    - name: WER
      type: wer
      value: 22.81
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Ravnursson Corpus (Dev)
      type: carlosdanielhernandezmena/ravnursson_asr
      split: validation
      args: 
        language: is
    metrics:
    - name: WER
      type: wer
      value: 20.51
---
# stt_fo_quartznet15x5_sp_ep163_100h
**NOTE! This model was trained with the NeMo version: nemo-toolkit==1.10.0**

The "stt_fo_quartznet15x5_sp_ep163_100h" is an acoustic model created with NeMo which is suitable for Automatic Speech Recognition in Faroese. 

It is the result of fine-tuning the model ["QuartzNet15x5Base-En.nemo"](https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels/files) with 100 hours of Faroese data developed by the [Ravnur Project](https://maltokni.fo/en/the-ravnur-project) from the Faroe Islands and curated by Carlos Mena during 2022. Most of the data is available at public repositories such as [Clarin.is](http://hdl.handle.net/20.500.12537/276) or [Hugging Face](https://huggingface.co/datasets/carlosdanielhernandezmena/ravnursson_asr).

The specific corpus used to fine-tune the model is:

- [The Ravnursson Corpus: Faroese Speech and Transcripts (100h34m)](http://hdl.handle.net/20.500.12537/276)

The fine-tuning process was perform during November (2022) in the servers of the [Language and Voice Laboratory](https://lvl.ru.is/) at [Reykjavík University](https://en.ru.is/) (Iceland) by Carlos Daniel Hernández Mena.
```bibtex
@misc{mena2022quartznet15x5faroese,
      title={Acoustic Model in Faroese: stt_fo_quartznet15x5_sp_ep163_100h.}, 
      author={Hernandez Mena, Carlos Daniel},
      year={2022},
      url={https://huggingface.co/carlosdanielhernandezmena/stt_fo_quartznet15x5_sp_ep163_100h},
}
```

# Acknowledgements

Special thanks to Jón Guðnason, head of the Language and Voice Lab for providing computational power to make this model possible. We also want to thank to the "Language Technology Programme for Icelandic 2019-2023" which is managed and coordinated by Almannarómur, and it is funded by the Icelandic Ministry of Education, Science and Culture.

