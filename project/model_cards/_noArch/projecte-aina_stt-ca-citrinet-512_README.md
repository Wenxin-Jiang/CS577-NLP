---
language:
- ca
library_name: nemo
datasets:
- mozilla-foundation/common_voice_11_0
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- CTC
- citrinet
- pytorch
- NeMo
license: cc-by-4.0
widget:
- example_title: CV sample 1
  src: https://huggingface.co/projecte-aina/stt-ca-citrinet-512/tree/main/samples/common_voice_ca_34667058.wav
model-index:
- name: stt-ca-citrinet-512 
  results:
  - task:
      name: Automatic Speech Recognition
      type: automatic-speech-recognition
    dataset:
      name: Mozilla Common Voice 11.0
      type: mozilla-foundation/common_voice_11_0
      config: ca
      split: test
      args:
        language: ca
    metrics:
    - name: Test WER
      type: wer
      value: 6.684
---

# Aina Project's Catalan text-to-speech model
## Model description

This model transcribes audio samples in Catalan to lowercase text without punctuation. The model was fine-tuned from a pre-trained Spanish [stt-es-citrinet-512](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_es_citrinet_512) model using the [NeMo](https://github.com/NVIDIA/NeMo) toolkit. It has around 36.5M parámeters and has been trained on [Common Voice 11.0](https://commonvoice.mozilla.org/en/datasets).

## Intended uses and limitations

You can use this model for Automatic Speech Recognition (ASR) in Catalan, to transcribe audio files in Catalan to plain text without punctuation.

## How to use
### Usage

Requiered libraries:

```bash
pip install nemo_toolkit['all']
```

Clone the repository to download the model:

```bash
git clone https://huggingface.co/projecte-aina/stt-ca-citrinet-512
```

Given that `NEMO_PATH` is the path that points to the downloaded `stt-ca-citrinet-512.nemo` file, to do inference over a set of `.wav` files you should:

```python
# Load the model
model = nemo_asr.models.EncDecCTCModel.restore_from(NEMO_PATH)

# Create a list pointing to the audio files
paths2audio_files = ["audio_1.wav", ..., "audio_n.wav"]

# Fix the batch size to whatever number suits your purpose
batch_size = 8

# Transcribe the audio files
transcriptions = model.transcribe(paths2audio_files=paths2audio_files,
                                 batch_size=batch_size)
# Visualize the transcriptions
print(transcriptions)

```

## Training data

This model has been trained on the training split of the Catalan version of [Common Voice 11.0](https://commonvoice.mozilla.org/en/datasets).

## Training
### Data preparation
We have processed [Common Voice 11.0](https://commonvoice.mozilla.org/en/datasets) using the NeMo toolkit. We used [get_commonvoice_data.py](https://github.com/NVIDIA/NeMo/blob/main/scripts/dataset_processing/get_commonvoice_data.py) to process the manifests and made a subsequent data cleaning step.

After cleaning the dataset and normalizing the `ñ` character to `ny`, we have used the following charset to create the final NeMo manifests for training.
```python
['c', ' ', 'ó', 'g', 'a', 'o', 'ü', 'v', 'p', 't', "'", '—', 'f', 'k', 'à', 'ï', 'í', 'ú', 'd', 'l', 'z', 'é', 'w', 'm', 'r', 'n', 'y', '-', 'u', 'i', 'h', 'ç', 'e', '·', 'q', 'è', 'ò', 'j', 'x', 's', 'b']
```

### Training procedure
This model was trained starting from a pre-trained Spanish [stt-es-citrinet-512](https://catalog.ngc.nvidia.com/orgs/nvidia/teams/nemo/models/stt_es_citrinet_512) model. The initial learning rate was set to 0.005 and the minimum lr for weight decay was set to 1e-7. 

The model was trained for 90 steps and then continued training for another 90 steps starting from a learning rate of 1e-4.

## Evaluation
After evaluation on the test split of Common Voice 11.0 we have obtained a WER of 6.684.

## Additional information

### Author
Text Mining Unit (TeMU) at the Barcelona Supercomputing Center (bsc-temu@bsc.es)

### Contact information
For further information, send an email to aina@bsc.es

### Copyright
Copyright (c) 2022 Text Mining Unit at Barcelona Supercomputing Center 

### Licensing Information
[Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/)

### Funding
This work was funded by the [Generalitat de Catalunya](https://politiquesdigitals.gencat.cat/ca/inici/index.html#googtrans(ca|en) within the framework of [Projecte AINA](https://politiquesdigitals.gencat.cat/ca/economia/catalonia-ai/aina).


## Disclaimer
<details>
<summary>Click to expand</summary>

The models published in this repository are intended for a generalist purpose and are available to third parties. These models may have bias and/or any other undesirable distortions.

When third parties, deploy or provide systems and/or services to other parties using any of these models (or using systems based on these models) or become users of the models, they should note that it is their responsibility to mitigate the risks arising from their use and, in any event, to comply with applicable regulations, including regulations regarding the use of Artificial Intelligence.

In no event shall the owner and creator of the models (BSC – Barcelona Supercomputing Center) be liable for any results arising from the use made by third parties of these models.
