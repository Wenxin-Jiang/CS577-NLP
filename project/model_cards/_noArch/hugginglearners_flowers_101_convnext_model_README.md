---
tags:
- fastai
- image-classification
---


# Model card

## Model description

This model has been trained with convnext_tiny_in22k with [Flowers-101 datasets in Kaggle](https://www.kaggle.com/competitions/tpu-getting-started).

**Useful graphs logged with wandb**

![image](https://user-images.githubusercontent.com/24592806/177065734-2d2920d2-adf2-4d73-8e89-a59e269544d4.png)
![image](https://user-images.githubusercontent.com/24592806/177065795-5c66ae3f-5e05-44c3-a6e5-0abb302c7d50.png)

## Intended uses & limitations

- The model can be used be for classifying flowers only.

**Limitations**

- Even if the picture uploaded is not of a flower, you can can notice [it will be predicted as of flower](https://www.kaggle.com/competitions/tpu-getting-started).
- The model on validation dataset has accuracy of 94.23%

![image](https://user-images.githubusercontent.com/24592806/177065484-1fae6a79-5dbe-471a-8c86-9c5aaa336bc6.png)


## Training and evaluation data

- The models has been trained and evaluated with [Flowers-101 datasets in Kaggle](https://www.kaggle.com/competitions/tpu-getting-started).
- We used a Random Splitter to train and evaluate data

