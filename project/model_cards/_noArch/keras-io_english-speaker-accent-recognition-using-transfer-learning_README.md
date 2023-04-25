---
library_name: keras
tags:
- keras
- audio-classification
- accent-classification
---

## Model description

This model classifies UK & Ireland accents using feature extraction from [Yamnet](https://tfhub.dev/google/yamnet/1).

### Yamnet Model
Yamnet is an audio event classifier trained on the AudioSet dataset to predict audio events from the AudioSet ontology. It is available on TensorFlow Hub.
Yamnet accepts a 1-D tensor of audio samples with a sample rate of 16 kHz.   
As output, the model returns a 3-tuple:   
- Scores of shape `(N, 521)` representing the scores of the 521 classes.
- Embeddings of shape `(N, 1024)`.
- The log-mel spectrogram of the entire audio frame.

We will use the embeddings, which are the features extracted from the audio samples, as the input to our dense model.  

For more detailed information about Yamnet, please refer to its [TensorFlow Hub](https://tfhub.dev/google/yamnet/1) page.

### Dense Model
The dense model that we used consists of:
- An input layer which is embedding output of the Yamnet classifier.
- 4 dense hidden layers and 4 dropout layers.
- An output dense layer.


## Training and evaluation data

The dataset used is the
[Crowdsourced high-quality UK and Ireland English Dialect speech data set](https://openslr.org/83/)
which consists of a total of 17,877 high-quality audio wav files.

This dataset includes over 31 hours of recording from 120 vounteers who self-identify as
native speakers of Southern England, Midlands, Northern England, Wales, Scotland and Ireland.

For more info, please refer to the above link or to the following paper:
[Open-source Multi-speaker Corpora of the English Accents in the British Isles](https://aclanthology.org/2020.lrec-1.804.pdf)


## Training procedure

### Training hyperparameters
| Optimizer | learning_rate | decay | beta_1 | beta_2 | epsilon | amsgrad | training_precision |
|----|-------------|-----|------|------|-------|-------|------------------|
|Adam|1.9644e-05|0.0|0.9|0.999|1e-07|False|float32|

 ## Training Metrics
| Epochs | Training Loss | Training Accuracy | Training AUC |
|--- |--- |--- |--- |
| 1| 10.614| 0.343| 0.759|
| 2| 9.378| 0.396| 0.806|
| 3| 8.993| 0.422| 0.821|
| 4| 8.768| 0.433| 0.829|
| 5| 8.636| 0.438| 0.833|
| 6| 8.514| 0.442| 0.837|
| 7| 8.432| 0.444| 0.839|
| 8| 8.339| 0.446| 0.841|
| 9| 8.270| 0.448| 0.843|
| 10| 8.202| 0.449| 0.845|
| 11| 8.141| 0.451| 0.847|
| 12| 8.095| 0.452| 0.849|
| 13| 8.029| 0.454| 0.851|
| 14| 7.982| 0.454| 0.852|
| 15| 7.935| 0.456| 0.853|
| 16| 7.896| 0.456| 0.854|
| 17| 7.846| 0.459| 0.856|
| 18| 7.809| 0.460| 0.857|
| 19| 7.763| 0.460| 0.858|
| 20| 7.720| 0.462| 0.860|
| 21| 7.688| 0.463| 0.860|
| 22| 7.640| 0.464| 0.861|
| 23| 7.593| 0.467| 0.863|
| 24| 7.579| 0.467| 0.863|
| 25| 7.552| 0.468| 0.864|
| 26| 7.512| 0.468| 0.865|
| 27| 7.477| 0.469| 0.866|
| 28| 7.434| 0.470| 0.867|
| 29| 7.420| 0.471| 0.868|
| 30| 7.374| 0.471| 0.868|
| 31| 7.352| 0.473| 0.869|
| 32| 7.323| 0.474| 0.870|
| 33| 7.274| 0.475| 0.871|
| 34| 7.253| 0.476| 0.871|
| 35| 7.221| 0.477| 0.872|
| 36| 7.179| 0.480| 0.873|
| 37| 7.155| 0.481| 0.874|
| 38| 7.141| 0.481| 0.874|
| 39| 7.108| 0.482| 0.875|
| 40| 7.067| 0.483| 0.876|
| 41| 7.060| 0.483| 0.876|
| 42| 7.019| 0.485| 0.877|
| 43| 6.998| 0.484| 0.877|
| 44| 6.974| 0.486| 0.878|
| 45| 6.947| 0.487| 0.878|
| 46| 6.921| 0.488| 0.879|
| 47| 6.875| 0.490| 0.880|
| 48| 6.860| 0.490| 0.880|
| 49| 6.843| 0.491| 0.881|
| 50| 6.811| 0.492| 0.881|
| 51| 6.783| 0.494| 0.882|
| 52| 6.764| 0.494| 0.882|
| 53| 6.719| 0.497| 0.883|
| 54| 6.693| 0.497| 0.884|
| 55| 6.682| 0.498| 0.884|
| 56| 6.653| 0.497| 0.884|
| 57| 6.630| 0.499| 0.885|
| 58| 6.596| 0.500| 0.885|
| 59| 6.577| 0.500| 0.886|
| 60| 6.546| 0.501| 0.886|
| 61| 6.517| 0.502| 0.887|
| 62| 6.514| 0.504| 0.887|
| 63| 6.483| 0.504| 0.888|
| 64| 6.428| 0.506| 0.888|
| 65| 6.424| 0.507| 0.889|
| 66| 6.412| 0.508| 0.889|
| 67| 6.388| 0.507| 0.889|
| 68| 6.342| 0.509| 0.890|
| 69| 6.309| 0.510| 0.891|
| 70| 6.300| 0.510| 0.891|
| 71| 6.279| 0.512| 0.892|
| 72| 6.258| 0.510| 0.892|
| 73| 6.242| 0.513| 0.892|
| 74| 6.206| 0.514| 0.893|
| 75| 6.189| 0.516| 0.893|
| 76| 6.164| 0.517| 0.894|
| 77| 6.134| 0.517| 0.894|
| 78| 6.120| 0.517| 0.894|
| 79| 6.081| 0.520| 0.895|
| 80| 6.090| 0.518| 0.895|
| 81| 6.052| 0.521| 0.896|
| 82| 6.028| 0.521| 0.896|
| 83| 5.991| 0.521| 0.897|
| 84| 5.974| 0.524| 0.897|
| 85| 5.964| 0.524| 0.897|
| 86| 5.951| 0.524| 0.897|
| 87| 5.940| 0.524| 0.898|
| 88| 5.891| 0.525| 0.899|
| 89| 5.870| 0.526| 0.899|
| 90| 5.856| 0.528| 0.899|
| 91| 5.831| 0.528| 0.900|
| 92| 5.808| 0.529| 0.900|
| 93| 5.796| 0.529| 0.900|
| 94| 5.770| 0.530| 0.901|
| 95| 5.763| 0.529| 0.901|
| 96| 5.749| 0.530| 0.901|
| 97| 5.742| 0.530| 0.901|
| 98| 5.705| 0.531| 0.902|
| 99| 5.694| 0.533| 0.902|
| 100| 5.671| 0.534| 0.903|
 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>

## Validation Results
The model achieved the following results on the validation dataset:

Results    | Validation 
-----------|------------
Accuracy   | 50%
AUC        | 0.8909 
d-prime    | 1.742 

And the confusion matrix for the validation set is:
![Validation Confusion Matrix](./confusion_matrix.png)

## Credits

Author: [Fadi Badine](https://twitter.com/fadibadine).   
Based on the following Keras example [English speaker accent recognition using Transfer Learning](https://keras.io/examples/audio/uk_ireland_accent_recognition) by Fadi Badine    
Check out the demo space [here](https://huggingface.co/spaces/keras-io/english-speaker-accent-recognition-using-transfer-learning)