# CodeTrans transfer learning pre-trained model
Pretrained model on programming languages using the t5 small model architecture. It was first released in
[this repository](https://github.com/agemagician/CodeTrans). 


## Model description

This CodeTrans model is based on the `t5-small` model. It has its own SentencePiece vocabulary model. It used transfer-learning pre-training on 7 unsupervised datasets in the software development domain. 

The model was trained on a single TPU Pod V3-8 for half million steps in total, using sequence length 512 (batch size 4096).
It has a total of approximately 220M parameters and was trained using the encoder-decoder architecture.
The optimizer used is AdaFactor with inverse square root learning rate schedule for pre-training. 

It could be used to fine-tune other tasks in the software development domain.


> Created by [Ahmed Elnaggar](https://twitter.com/Elnaggar_AI) | [LinkedIn](https://www.linkedin.com/in/prof-ahmed-elnaggar/) and Wei Ding | [LinkedIn](https://www.linkedin.com/in/wei-ding-92561270/)


