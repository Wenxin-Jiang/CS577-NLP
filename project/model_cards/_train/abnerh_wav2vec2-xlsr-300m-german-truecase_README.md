Fine-tuned [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) on German using the Common Voice dataset. When using this model, make sure that your speech input is sampled at 16kHz.

As capitalization is an important part of the German language (eg. Sie vs. sie).
I trained a model using a vocab that includes both lower case and upper case letters in hopes that the model would learn the correct casing. 
This removes the need to do any post-processing like truecasing.


| Reference | Prediction |
| ------------- | ------------- |
| **Die** zoologische **Einordnung** der **Spezies** ist seit **Jahrzehnten** umstritten | **Die** psoologische **Einordnung** der **Spezies** ist seit **Jahrzehnten** umstritten |
| **Hauptgeschäftsfeld** war ursprünglich der öffentliche **Sektor** in **Irland** | **Hauptgeschäftsfeld** war ursprünglich der öffentliche **Sektor** in **Irland** |
| **Er** vertrat den **Wahlkreis Donauwörth** im **Parlament** | **Er** vertrat den **Wahlkreis DonauWört** im **Parlament** |
| **Ich** bin gespannt welche **Lieder** sie wählt | **Ich** bin gespannt welche **Lieder** see wählt |
| **Eine** allgemein verbindliche **Definition** gibt es nicht | **Eine** allgemeinverbindliche **Definition** gibt es nicht |

```
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
import soundfile as sf
import torch
 
# load model and processor
processor = Wav2Vec2Processor.from_pretrained("abnerh/wav2vec2-xlsr-300m-german-truecase")
model = Wav2Vec2ForCTC.from_pretrained("abnerh/wav2vec2-xlsr-300m-german-truecase")
 
speech, sr = sf.read('audio.wav') 
# tokenize
input_values = processor(speech, return_tensors="pt", padding="longest").input_values  # Batch size 1

# retrieve logits
logits = model(input_values).logits
 
# take argmax and decode
predicted_ids = torch.argmax(logits, dim=-1)
transcription = processor.batch_decode(predicted_ids)

# print transcription results
print(transcription)
```