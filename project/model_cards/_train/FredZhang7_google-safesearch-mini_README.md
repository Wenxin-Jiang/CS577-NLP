---
license: creativeml-openrail-m
tags:
- safety-checker
- tensorflow
- node.js
pipeline_tag: image-classification
---
# Google Safesearch Mini Model Card

<a href="https://huggingface.co/FredZhang7/google-safesearch-mini-v2"> <font size="4"> <bold> Version 2 is here! </bold> </font> </a>

This model is trained on 2,220,000+ images scraped from Google Images, Reddit, Imgur, and Github.
The InceptionV3 and Xception models have been fine-tuned to predict the likelihood of an image falling into one of three categories: nsfw_gore, nsfw_suggestive, and safe.

After 20 epochs on PyTorch, the finetuned InceptionV3 model achieves 94% acc on both training and test data. After 3.3 epochs on Keras, the finetuned Xception model scores 94% acc on training set and 92% on test set.

Not only is this model accurate, but it also offers a significant advantage over stable diffusion safety checkers. By using our model, users can save 1.12GB of RAM and disk space.

<br>

# PyTorch
The PyTorch model runs much slower with transformers, so downloading it externally is a better option.
```bash
pip install --upgrade torchvision
```
```python
import torch, os, warnings, requests
from io import BytesIO
from PIL import Image
from urllib.request import urlretrieve
from torchvision import transforms

PATH_TO_IMAGE = 'https://images.unsplash.com/photo-1594568284297-7c64464062b1'
USE_CUDA = False

warnings.filterwarnings("ignore")
def download_model():
    print("Downloading google_safesearch_mini.bin...")
    urlretrieve("https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/pytorch_model.bin", "google_safesearch_mini.bin")

def eval():
    if not os.path.exists("google_safesearch_mini.bin"):
        download_model()
    model = torch.jit.load('./google_safesearch_mini.bin')
    img = Image.open(PATH_TO_IMAGE).convert('RGB') if not (PATH_TO_IMAGE.startswith('http://') or PATH_TO_IMAGE.startswith('https://')) else Image.open(BytesIO(requests.get(PATH_TO_IMAGE).content)).convert('RGB')
    transform = transforms.Compose([transforms.Resize(299), transforms.ToTensor(), transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))])
    img = transform(img).unsqueeze(0)
    if USE_CUDA:
        img, model = img.cuda(), model.cuda()
    else:
        img, model = img.cpu(), model.cpu()
    model.eval()
    with torch.no_grad():
        out, _ = model(img)
        _, predicted = torch.max(out.data, 1)
        classes = {0: 'nsfw_gore', 1: 'nsfw_suggestive', 2: 'safe'}

        # account for edge cases
        if predicted[0] != 2 and abs(out[0][2] - out[0][predicted[0]]) > 0.20:
            img = Image.new('RGB', image.size, color = (0, 255, 255))
            print("\033[93m" + "safe" + "\033[0m")
        else:
            print('\n\033[1;31m' + classes[predicted.item()] + '\033[0m' if predicted.item() != 2 else '\033[1;32m' + classes[predicted.item()] + '\033[0m\n')

if __name__ == '__main__':
    eval()
```
Output Example:
![prediction](./output_example.png)

<br>

# Keras
```python
import tensorflow as tf
from PIL import Image
import requests, os

# download the model
url = "https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/tensorflow/saved_model.pb"
r = requests.get(url, allow_redirects=True)
if not os.path.exists('tensorflow'):
    os.makedirs('tensorflow')
open('tensorflow/saved_model.pb', 'wb').write(r.content)

# download the variables
url = "https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/tensorflow/variables/variables.data-00000-of-00001"
r = requests.get(url, allow_redirects=True)
if not os.path.exists('tensorflow/variables'):
    os.makedirs('tensorflow/variables')
open('tensorflow/variables/variables.data-00000-of-00001', 'wb').write(r.content)

url = "https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/tensorflow/variables/variables.index"
r = requests.get(url, allow_redirects=True)
open('tensorflow/variables/variables.index', 'wb').write(r.content)

# load the model
model = tf.saved_model.load('./tensorflow')
image = Image.open('cat.jpg')
image = image.resize((299, 299))
image = tf.convert_to_tensor(image)
image = tf.expand_dims(image, 0)

# run the model
tensor = model(image)
classes = ['nsfw_gore', 'nsfw_suggestive', 'safe']
prediction = classes[tf.argmax(tensor, 1)[0]]
print('\033[1;32m' + prediction + '\033[0m' if prediction == 'safe' else '\033[1;33m' + prediction + '\033[0m')
```
Output Example:
![prediction](./output_example.png)

<br>

# Tensorflow.js
```bash
npm i @tensorflow/tfjs-node
```
```javascript
const tf = require('@tensorflow/tfjs-node');
const fs = require('fs');
const { pipeline } = require('stream');
const { promisify } = require('util');


const download = async (url, path) => {
    // Taken from https://levelup.gitconnected.com/how-to-download-a-file-with-node-js-e2b88fe55409

    const streamPipeline = promisify(pipeline);
    const response = await fetch(url);

    if (!response.ok) {
        throw new Error(`unexpected response ${response.statusText}`);
    }

    await streamPipeline(response.body, fs.createWriteStream(path));
};


async function run() {
    // download saved model and variables from https://huggingface.co/FredZhang7/google-safesearch-mini/tree/main/tensorflow
    if (!fs.existsSync('tensorflow')) {
        fs.mkdirSync('tensorflow');
        await download('https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/tensorflow/saved_model.pb', 'tensorflow/saved_model.pb');
        fs.mkdirSync('tensorflow/variables');
        await download('https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/tensorflow/variables/variables.data-00000-of-00001', 'tensorflow/variables/variables.data-00000-of-00001');
        await download('https://huggingface.co/FredZhang7/google-safesearch-mini/resolve/main/tensorflow/variables/variables.index', 'tensorflow/variables/variables.index');
    }

    // load model and image
    const model = await tf.node.loadSavedModel('./tensorflow/');
    const image = tf.node.decodeImage(fs.readFileSync('cat.jpg'), 3);

    // predict
    const input = tf.expandDims(image, 0);
    const tensor = model.predict(input);
    const max = tensor.argMax(1);
    const classes = ['nsfw_gore', 'nsfw_suggestive', 'safe'];
    console.log('\x1b[32m%s\x1b[0m', classes[max.dataSync()[0]], '\n');
}

run();
```
Output Example:
![tfjs output](./tfjs_output.png)

<br>

# Bias and Limitations
Each person's definition of "safe" is different. The images in the dataset are classified as safe/unsafe by Google SafeSearch, Reddit, and Imgur.
It is possible that some images may be safe to others but not to you. Also, when a model encounters an image with things it hasn't seen, it likely makes wrong predictions.
This is why in the PyTorch example, I accounted for the "edge cases" before printing the predictions.