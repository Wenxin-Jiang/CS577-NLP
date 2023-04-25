---
tags:
- image-classification
widget:
- src: https://upload.wikimedia.org/wikipedia/commons/0/0c/About_The_Dog.jpg
  example_title: Dog-1
- src: https://yt3.ggpht.com/ytc/AKedOLRvxGYSdEHqu0X4EYcJ2kq7BttRKBNpfwdHJf3FSg=s900-c-k-c0x00ffffff-no-rj
  example_title: Dog-2
- src: https://upload.wikimedia.org/wikipedia/commons/c/c7/Tabby_cat_with_blue_eyes-3336579.jpg
  example_title: Cat-1
- src: https://pixabay.com/get/g31cf3b945cf9b9144eb6c1ecf514b4db668875b75d0c615e0330aec74bef5edde11567ef4a6f5fdb61a828b8086a39d3a0e72fb326d78467786dcdde4e6fa23c5c4c309d0abc089a8663809c175aee22_1920.jpg
  example_title: Cat-2
---

# Classify Cats and Dogs

VGG16 fine tuned to classify cats and dogs

Notebook

https://www.kaggle.com/carlosaguayo/cats-vs-dogs-transfer-learning-pre-trained-vgg16

### How to use

Here is how to use this model to classify an image as a cat or dog:

```python
from skimage import io
import cv2
import matplotlib.pyplot as plt
from huggingface_hub import from_pretrained_keras
%matplotlib inline 

ROWS, COLS = 150, 150

model = from_pretrained_keras("carlosaguayo/cats_vs_dogs")

img_url = 'https://upload.wikimedia.org/wikipedia/commons/0/0c/About_The_Dog.jpg'
# img_url = 'https://upload.wikimedia.org/wikipedia/commons/c/c7/Tabby_cat_with_blue_eyes-3336579.jpg'

img = io.imread(img_url)
img = cv2.resize(img, (ROWS, COLS), interpolation=cv2.INTER_CUBIC)
img = img / 255.0
img = img.reshape(1,ROWS,COLS,3)

prediction = model.predict(img)[0][0]
if prediction >= 0.5:
    print('I am {:.2%} sure this is a Cat'.format(prediction))
else: 
    print('I am {:.2%} sure this is a Dog'.format(1-prediction))
        
plt.imshow(img[0], 'Blues')
plt.axis("off")
plt.show()
```