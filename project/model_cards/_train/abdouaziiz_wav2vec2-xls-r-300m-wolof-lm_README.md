---
license: mit
tags:
- automatic-speech-recognition
- asr
- pytorch
- wav2vec2
- wolof
- wo
model-index:
- name: wav2vec2-xls-r-300m-wolof-lm
  results:
  - task: 
      name: Speech Recognition
      type: automatic-speech-recognition
 
    metrics:
       - name: Test WER
         type: wer
         value: 21.25
       - name: Validation Loss
         type: Loss
         value: 0.36

---
<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->
# wav2vec2-xls-r-300m-wolof-lm 

Wolof is a language spoken in Senegal and neighbouring countries, this language is not too well represented, there are few resources in the field of Text en speech
In this sense we aim to bring our contribution to this, it is in this sense that enters this repo. 

This model is a fine-tuned version of [facebook/wav2vec2-xls-r-300m](https://huggingface.co/facebook/wav2vec2-xls-r-300m) ,with a language model that is fine-tuned  with the largest available speech dataset of the  [ALFFA_PUBLIC](https://github.com/besacier/ALFFA_PUBLIC/tree/master/ASR/WOLOF)

It achieves the following results on the evaluation set:
- Loss: 0.367826	
- Wer: 0.212565

## Model description
The duration of the training data is 16.8 hours, which we have divided into 10,000 audio files for the training and 3,339 for the test.
## Training and evaluation data
We eval the model at every 1500 step , and log it .  and save at every 33340 step
### Training hyperparameters
The following hyperparameters were used during training:
- learning_rate: 1e-4
- train_batch_size: 3
- eval_batch_size : 8
- total_train_batch_size: 64
- total_eval_batch_size: 64
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- lr_scheduler_warmup_steps: 1000
- num_epochs: 10.0

### Training results

| Step    | Training Loss | Validation Loss | Wer    |
|:-------:|:-------------:|:---------------:|:------:|
| 1500	 | 2.854200	 |0.642243	 |0.543964  |
| 3000	| 0.599200 |  0.468138 |  	0.429549|
| 4500	| 0.468300 |	0.433436 |	0.405644|
| 6000	| 0.427000 |	0.384873 |	0.344150|
| 7500	| 0.377000 |	0.374003 |	0.323892|
| 9000	| 0.337000 |	0.363674 |	0.306189|
| 10500	| 0.302400	| 0.349884	 |0 .283908 |
| 12000	| 0.264100	| 0.344104  |0.277120|
| 13500	|0 .254000	|0.341820	 |0.271316|
| 15000 |	0.208400|	0.326502 |	0.260695|
| 16500 |	0.203500|	0.326209 |	0.250313|
| 18000	|0.159800	|0.323539 |	0.239851|
| 19500 |	0.158200 |	0.310694 |	0.230028|
| 21000 |	0.132800 |	0.338318 |	0.229283|
| 22500 |	0.112800 |	0.336765 |	0.224145|
| 24000 |	0.103600 |	0.350208 |	0.227073 |
| 25500 |	0.091400 |	0.353609 |	0.221589 |
| 27000 | 0.084400 |	0.367826 |	0.212565 |


## Usage
The model can be used directly as follows:
```python
import librosa
import warnings
from transformers import AutoProcessor, AutoModelForCTC
from datasets import Dataset, DatasetDict
from datasets import load_metric

wer_metric = load_metric("wer")

wolof = pd.read_csv('Test.csv') # wolof contains the columns of file , and transcription
wolof = DatasetDict({'test': Dataset.from_pandas(wolof)})

chars_to_ignore_regex = '[\"\?\.\!\-\;\:\(\)\,]'

def remove_special_characters(batch):
    batch["transcription"] = re.sub(chars_to_ignore_regex, '', batch["transcription"]).lower() + " "
    return batch
    
    
wolof = wolof.map(remove_special_characters)

processor = AutoProcessor.from_pretrained("abdouaziiz/wav2vec2-xls-r-300m-wolof-lm")
model = AutoModelForCTC.from_pretrained("abdouaziiz/wav2vec2-xls-r-300m-wolof-lm")

warnings.filterwarnings("ignore")
def speech_file_to_array_fn(batch):
    speech_array, sampling_rate = librosa.load(batch["file"], sr = 16000)
    batch["speech"] = speech_array.astype('float16')
    batch["sampling_rate"] = sampling_rate
    batch["target_text"] = batch["transcription"]
    return batch
 
wolof = wolof.map(speech_file_to_array_fn, remove_columns=wolof.column_names["test"], num_proc=1)   
  
def map_to_result(batch):
    model.to("cuda")
    input_values = processor(
      batch["speech"], 
      sampling_rate=batch["sampling_rate"], 
      return_tensors="pt"
    ).input_values.to("cuda")

    with torch.no_grad():
        logits = model(input_values).logits
        pred_ids = torch.argmax(logits, dim=-1)
        batch["pred_str"] = processor.batch_decode(pred_ids)[0]

    return batch
   
 results = wolof["test"].map(map_to_result) 
 
 print("Test WER: {:.3f}".format(wer_metric.compute(predictions=results["pred_str"], references=results["transcription"])))
 
```

## PS:

The results obtained can be improved by using :

- Wav2vec2 + language model . 
- Build a Spellcheker from the text of the data
- Sentence Edit Distance