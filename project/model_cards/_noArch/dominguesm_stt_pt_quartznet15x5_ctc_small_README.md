---
language:
- pt
license: cc-by-4.0
library_name: nemo
datasets:
- mozilla-foundation/common_voice_9_0
thumbnail: null
tags:
- automatic-speech-recognition
- speech
- audio
- CTC
- QuartzNet
- Transformer
- NeMo
- pytorch
model-index:
- name: stt_pt_quartznet15x5_ctc_small
  results:
  - task:
      type: automatic-speech-recognition
    dataset:
      type: common_voice
      name: Common Voice Portuguese
      config: clean
      split: test
      args:
        language: pt
    metrics:
    - type: wer
      value: 49.17
      name: Test WER
    - type: cer
      value: 18.59
      name: Test CER
---


## Model Overview

This model transcribes speech in lower case Portuguese alphabet along with spaces. It is a "small" versions of QuartzNet-CTC model. 

## NVIDIA NeMo: Training

To train, fine-tune or play with the model you will need to install [NVIDIA NeMo](https://github.com/NVIDIA/NeMo). We recommend you install it after you've installed latest Pytorch version.
```
pip install nemo_toolkit['all']
``` 

## How to Use this Model

The model is available for use in the NeMo toolkit [1], and can be used as a pre-trained checkpoint for inference or for fine-tuning on another dataset.

### Automatically instantiate the model

```python
import nemo.collections.asr as nemo_asr
asr_model = nemo_asr.models.ASRModel.from_pretrained("dominguesm/stt_pt_quartznet15x5_ctc_small")
```

### Transcribing using Python
First, let's get a sample
```
wget https://github.com/DominguesM/stt_pt_quartznet15x5_ctc_small/raw/main/audios/common_voice_pt_25555332.mp3
```
Then simply do:
```
asr_model.transcribe(['common_voice_pt_25555332.mp3'])
```

### Transcribing many audio files

```shell
python [NEMO_GIT_FOLDER]/examples/asr/transcribe_speech.py  pretrained_name="dominguesm/stt_pt_quartznet15x5_ctc_small"  audio_dir="<DIRECTORY CONTAINING AUDIO FILES>"
```

### Input

This model accepts 16000 KHz Mono-channel Audio (wav files) as input.

### Output

This model provides transcribed speech as a string for a given audio sample.

## Model Architecture

This model are based on the QuartzNet architecture, which is a variant of Jasper that uses 1D time-channel separable convolutional layers in its convolutional residual blocks and are therefore smaller than Jasper models.

QuartzNet models take in audio segments and transcribe them to letter, byte pair, or word piece sequences.

## Training

All training scripts will be available at: [DominguesM/stt_pt_quartznet15x5_ctc_small](https://github.com/DominguesM/stt_pt_quartznet15x5_ctc_small)


### Datasets

The model was trained with a part of the Common Voices 9.0 dataset in Portuguese, totaling 26 hours of audio.

* Mozilla Common Voice (v9.0)

## Performance

| Metric | Score |
| ------- | ----- |
| WER     | 49%   |
| CER     | 18%   |

The metrics were obtained using the following code:

**Attention**: The steps below must be performed after downloading the dataset (Mozilla Commom Voices 9.0 PT) and following the steps of pre-processing the audio data and `manifest` files contained in the file [`notebooks/Finetuning CTC model Portuguese.ipynb`](https://github.com/DominguesM/stt_pt_quartznet15x5_ctc_small)

```bash
$ wget -P scripts/ "https://raw.githubusercontent.com/NVIDIA/NeMo/v1.9.0/examples/asr/speech_to_text_eval.py"

$ wget -P scripts/ "https://raw.githubusercontent.com/NVIDIA/NeMo/v1.9.0/examples/asr/transcribe_speech.py"

$ python scripts/speech_to_text_eval.py \
    pretrained_name="dominguesm/stt_pt_quartznet15x5_ctc_small" \
    dataset_manifest="manifests/pt/commonvoice_test_manifest_processed.json" \
    output_filename="./evaluation_transcripts.json" \
    batch_size=32 \
    amp=true \
    use_cer=false
```

## Limitations

Since this model was trained on publically available speech datasets, the performance of this model might degrade for speech which includes technical terms, or vernacular that the model has not been trained on. The model might also perform worse for accented speech.

## Citation

If you use our work, please cite:

```cite
@misc{domingues2022quartznet15x15-small-portuguese,
  title={Fine-tuned {Quartznet}-15x5 CTC small model for speech recognition in {P}ortuguese},
  author={Domingues, Maicon},
  howpublished={\url{https://huggingface.co/dominguesm/stt_pt_quartznet15x5_ctc_small}},
  year={2022}
}
```

## References

[1] [NVIDIA NeMo Toolkit](https://github.com/NVIDIA/NeMo)

