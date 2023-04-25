---
license: apache-2.0
datasets:
- go_emotions

metrics:
- accuracy
model-index:
- name: xtremedistil-emotion
  results:
  - task:
      name: Multi Label Text Classification
      type: multi_label_classification
    dataset:
      name: go_emotions
      type: emotion
      args: default
    metrics:
    - name: Accuracy
      type: accuracy
      value: NaN
      
---
# xtremedistil-l6-h384-go-emotion
This model is a fine-tuned version of [microsoft/xtremedistil-l6-h384-uncased](https://huggingface.co/microsoft/xtremedistil-l6-h384-uncased) on the 
[go_emotions dataset](https://huggingface.co/datasets/go_emotions). 

See notebook for how the model was trained and converted to ONNX format [![Training Notebook](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jobergum/emotion/blob/main/TrainGoEmotions.ipynb)

This model is deployed to [aiserv.cloud](https://aiserv.cloud/) for live demo of the model. 

See [https://github.com/jobergum/browser-ml-inference](https://github.com/jobergum/browser-ml-inference) for how to reproduce. 


### Training hyperparameters
- batch size 128 
- learning_rate=3e-05
- epocs 4 
<pre>
  Num examples = 211225
  Num Epochs = 4
  Instantaneous batch size per device = 128
  Total train batch size (w. parallel, distributed & accumulation) = 128
  Gradient Accumulation steps = 1
  Total optimization steps = 6604
 [6604/6604 53:23, Epoch 4/4]
Step	Training Loss
500	0.263200
1000	0.156900
1500	0.152500
2000	0.145400
2500	0.140500
3000	0.135900
3500	0.132800
4000	0.129400
4500	0.127200
5000	0.125700
5500	0.124400
6000	0.124100
6500	0.123400
</pre>