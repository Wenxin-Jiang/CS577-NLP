---
language:
- mt
library_name: nemo
datasets:
- common_voice
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
- maltese
license: cc-by-nc-sa-4.0
widget: null
model-index:
- name: stt_mt_quartznet15x5_sp_ep255_64h
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 11.0 (Test)
      type: mozilla-foundation/common_voice_11_0
      split: test
      args:
        language: mt
    metrics:
    - name: WER
      type: wer
      value: 5
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 11.0 (Dev)
      type: mozilla-foundation/common_voice_11_0
      split: validation
      args:
        language: mt
    metrics:
    - name: WER
      type: wer
      value: 4.89
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: MASRI-TEST Corpus
      type: MLRS/masri_test
      split: test
      args:
        language: mt
    metrics:
    - name: WER
      type: wer
      value: 45.2
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: MASRI-DEV Corpus
      type: MLRS/masri_dev
      split: validation
      args:
        language: mt
    metrics:
    - name: WER
      type: wer
      value: 43.08
---

# stt_mt_quartznet15x5_sp_ep255_64h

**NOTE! This model was trained with the NeMo version: nemo-toolkit==1.10.0**

The "stt_mt_quartznet15x5_sp_ep255_64h" is an acoustic model created with NeMo which is suitable for Automatic Speech Recognition in Maltese. 

It is the result of fine-tuning the model ["QuartzNet15x5Base-En.nemo"](https://catalog.ngc.nvidia.com/orgs/nvidia/models/nemospeechmodels/files) with around 64 hours of Maltese data developed by the MASRI Project at the University of Malta between 2019 and 2021. The 64 hours of data were augmented using speed perturbation at speed rates of 0.9 and 1.1. Most of the data is available at the the MASRI Project homepage https://www.um.edu.mt/projects/masri/.

The specific list of corpora used to fine-tune the model is:

- MASRI-HEADSET v2 (6h39m)
- MASRI-Farfield (9h37m)
- MASRI-Booths (2h27m)
- MASRI-MEP (1h17m)
- MASRI-COMVO (7h29m)
- MASRI-TUBE (13h17m)
- MASRI-MERLIN (25h18m) *Not available at the MASRI Project homepage
	
The fine-tuning process was perform during October (2022) in the servers of the Language and Voice Lab (https://lvl.ru.is/) at Reykjavík University (Iceland) by Carlos Daniel Hernández Mena.

```bibtex
@misc{mena2022quartznet15x5maltese,
      title={Acoustic Model in Maltese: stt_mt_quartznet15x5_sp_ep255_64h.}, 
      author={Hernandez Mena, Carlos Daniel},
      year={2022},
      url={https://huggingface.co/carlosdanielhernandezmena/stt_mt_quartznet15x5_sp_ep255_64h},
}
```

# Acknowledgements

The MASRI Project is funded by the University of Malta Research Fund Awards. We want to thank to Merlin Publishers (Malta) for provinding the audiobooks used to create the MASRI-MERLIN Corpus.

Special thanks to Jón Guðnason, head of the Language and Voice Lab for providing computational power to make this model possible. We also want to thank to the "Language Technology Programme for Icelandic 2019-2023" which is managed and coordinated by Almannarómur, and it is funded by the Icelandic Ministry of Education, Science and Culture.