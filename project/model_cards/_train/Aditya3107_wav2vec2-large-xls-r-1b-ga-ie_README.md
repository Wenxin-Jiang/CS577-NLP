---
language: ga
datasets:
- common_voice
- living-audio-Irish
metrics:
- wer
tags:
- audio
- automatic-speech-recognition
- ga-IE 
- speech
- Irish
- Gaelic
model-index:
- name: Wav2vec 2.0 large 300m XLS-R
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Common Voice 10.0
      type: common_voice
      args: ga-IE
    metrics:
    - name: Test WER
      type: wer
      value: 25.94
---

# Irish-Gaelic Automatic Speech Recognition

This is the model for Irish ASR. It has been trained on the Common-voice dataset and living Irish audio dataset. The Common-voice code for the Irish language is ga-IE. From the Common voice dataset, all the Validated audio clips and all the living audio clips were taken into account and after a random train-test split, 90% of the total dataset (5156 utterances) were taken for training, and the rest of the 10% of real data (579 utterances) were taken for testing. 

This dataset was finetuned on wav2vec2-large-xls-r-300m. On the testing dataset, 25.94% of WER could be achieved. 

### How to use
Example of transcribing the Common Voice audio clip from the invalidated dataset, using GPU if available. The model expects 16kHz audio.

```python
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

model = Wav2Vec2ForCTC.from_pretrained("Aditya3107/wav2vec2-large-xls-r-1b-ga-ie")
processor = Wav2Vec2Processor.from_pretrained("Aditya3107/wav2vec2-large-xls-r-1b-ga-ie")

# Reading taken audio clip
import librosa, torch
audio, rate = librosa.load("common-voice-irish/common_voice/cv-corpus-10.0-2022-07-04/ga-IE/clips/common_voice_ga-IE_1818627.mp3", sr = 16000)

# Taking an input value
input_values = processor(audio, sampling_rate=16_000, return_tensors = "pt", padding="longest").input_values
# Storing logits (non-normalized prediction values)
logits = model(input_values).logits
# Storing predicted ids
prediction = torch.argmax(logits, dim = -1)

# Passing the prediction to the tokenizer decode to get the transcription
transcription = processor.batch_decode(prediction)[0]
print(transcription)
```
### Results
Example of the transcribed audio clips and testing on SCLITE. 
```
Speaker sentences   0:     #utts: 1
           
id: (common_voice_ga-IE_17401296.mp3)
Scores: (#C #S #D #I) 4 1 0 0
Attributes: Case_sensitve 
REF:  an bhfuil cóta bán óir 
HYP:  an bhfuil cóta bán air  
Eval:                      S    

id: (common_voice_ga-IE_17410244.mp3)
Scores: (#C #S #D #I) 3 1 0 2
Attributes: Case_sensitve 
REF:  *** ** an bud é sin 
HYP:  cad é an rud é sin 
Eval: I   I     S          

id: (common_voice_ga-IE_17410257.mp3)
Scores: (#C #S #D #I) 9 2 1 2
Attributes: Case_sensitve 
REF:  i gabhaim buíochas libh a chairde ******* ** támindéagtstruth le tuilleadh uaibh ar baá 
HYP:  * gabhaim buíochas libh a chairde táimid ag tsnúth            le tuilleadh uaibh ar ball 
Eval: D                                  I       I  S                                        S    

id: (common_voice_ga-IE_17410401.mp3)
Scores: (#C #S #D #I) 6 1 0 0
Attributes: Case_sensitve 
REF:  níl ach tá peann ina phóca uige 
HYP:  níl ach tá peann ina phóca aige 
Eval:                               S    

id: (common_voice_ga-IE_17410403.mp3)
Scores: (#C #S #D #I) 5 1 0 1
Attributes: Case_sensitve 
REF:  agus *** cadé an dath atá air 
HYP:  agus cad é    an dath atá air 
Eval:      I   S                      

id: (common_voice_ga-IE_17410412.mp3)
Scores: (#C #S #D #I) 6 2 0 0
Attributes: Case_sensitve 
REF:  is lá é seo chun ceiliúradh  a dhéan    
HYP:  is lá é seo chun céiliúradh a dhéanamh 
Eval:                    S              S         

id: (common_voice_ga-IE_17444712.mp3)
Scores: (#C #S #D #I) 4 6 0 0
Attributes: Case_sensitve 
REF:  don chathaoileach  mirín   de brom  don stiúrdhóirat liam ón maoladha  
HYP:  don chathaoirleach máirín de brún don stiúrthóir   liam ó  maolaodha 
Eval:     S              S           S         S                   S   S         

id: (common_voice_ga-IE_17449454.mp3)
Scores: (#C #S #D #I) 4 0 0 0
Attributes: Case_sensitve 
REF:  ceacht a trí déag 
HYP:  ceacht a trí déag 
Eval:                     
```
### Future Tasks
The language model with KenLM will be added if any good resource of Irish text is found. 

### Citation
If you want to cite this model you can use this:

```
@MISC {,
    author       = "Aditya Parikh",
    title        = "Finetuned XLS-R model for Irish (Ga-IE) language for Automatic Speech Recognition",
    howpublished = "{\url{https://huggingface.co/Aditya3107/wav2vec2-large-xls-r-1b-ga-ie}}",
    month        = "aug",
    year         = "2022"
}
```