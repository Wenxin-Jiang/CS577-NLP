---
tags: 
- keras
- image-to-image
- pixelwise-segmentation
datasets:
- DIBCO
- H-DIBCO
license: apache-2.0
---






# Model Card for sbb_binarization

<!-- Provide a quick summary of what the model is/does. [Optional] -->
This is a pixelwise segmentation model for document image binarization. 
The model is a hybrid CNN-Transformer encoder-decoder model (Resnet50-Unet) developed by the Berlin State Library (SBB) in the [QURATOR](https://staatsbibliothek-berlin.de/die-staatsbibliothek/projekte/project-id-1060-2018) project. It can be used to convert all pixels in a color or grayscale document image to only black or white pixels. 
The main aim is to improve the contrast between foreground (text) and background (paper) for purposes of Optical Character Recognition (OCR).




#  Table of Contents

- [Model Card for sbb_binarization](#model-card-for-sbb_binarization)
- [Table of Contents](#table-of-contents)
- [Model Details](#model-details)
  - [Model Description](#model-description)
- [Uses](#uses)
  - [Direct Use](#direct-use)
  - [Downstream Use](#downstream-use)
  - [Out-of-Scope Use](#out-of-scope-use)
- [Bias, Risks, and Limitations](#bias-risks-and-limitations)
  - [Recommendations](#recommendations)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Training Procedure](#training-procedure)
    - [Preprocessing](#preprocessing)
    - [Speeds, Sizes, Times](#speeds-sizes-times)
- [Evaluation](#evaluation)
  - [Testing Data, Factors & Metrics](#testing-data-factors--metrics)
    - [Testing Data](#testing-data)
    - [Factors](#factors)
    - [Metrics](#metrics)
  - [Results](#results)
- [Model Examination](#model-examination)
- [Environmental Impact](#environmental-impact)
- [Technical Specifications](#technical-specifications)
  - [Model Architecture and Objective](#model-architecture-and-objective)
  - [Compute Infrastructure](#compute-infrastructure)
    - [Hardware](#hardware)
    - [Software](#software)
- [Citation](#citation)
- [Glossary [optional]](#glossary-optional)
- [More Information [optional]](#more-information-optional)
- [Model Card Authors](#model-card-authors)
- [Model Card Contact](#model-card-contact)
- [How to Get Started with the Model](#how-to-get-started-with-the-model)


# Model Details

## Model Description

<!-- Provide a longer summary of what this model is/does. -->
Document image binarization is one of the main pre-processing steps for text recognition in document image analysis. 
Noise, faint characters, bad scanning conditions, uneven light exposure or paper aging can cause artifacts that negatively impact text recognition algorithms. 
The task of binarization is to segment the foreground (text) from these degradations in order to improve Optical Character Recognition (OCR) results. 
Convolutional neural networks (CNNs) are one popular method for binarization, while Vision Transformers are gaining performance. 
The sbb_binarization model therefore applies a hybrid CNN-Transformer encoder-decoder model architecture.

- **Developed by:** [Vahid Rezanezhad](vahid.rezanezhad@sbb.spk-berlin.de)
- **Shared by [Optional]:** [Staatsbibliothek zu Berlin / Berlin State Library](https://huggingface.co/SBB)
- **Model type:** Neural Network
- **Language(s) (NLP):** Irrelevant; works on all languages
- **License:** apache-2.0
- **Parent Model:** [ResNet-50, see the paper by Zhang et al](https://arxiv.org/abs/1512.03385)
- **Resources for more information:** More information needed
    - [GitHub Repo](https://github.com/qurator-spk/sbb_binarization)
    - Associated Paper 1 [Time-Quality Binarization Competition](https://dib.cin.ufpe.br/docs/DocEng21_bin_competition_report.pdf)
	- Associated Paper 2 [Time-Quality Document Image Binarization](https://dib.cin.ufpe.br/docs/papers/ICDAR2021-TQDIB_final_published.pdf)

# Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

Document image binarization is the main use case of this model. The architecture of this model alongside with training techniques like model weights ensembling can reach or outperform state-of-the-art results on standard Document Binarization Competition (DIBCO) datasets in the both machine-printed and handwritten documents.



## Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->
<!-- If the user enters content, print that. If not, but they enter a task in the list, use that. If neither, say "more info needed." -->

The intended use is the binarization of document images, particularly of historical documents, understood as one of the main pre-processing steps for text recognition.


## Downstream Use

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->
<!-- If the user enters content, print that. If not, but they enter a task in the list, use that. If neither, say "more info needed." -->
 
A possible downstream use of this model might lie with the binarization of illustrative elements contained in document images such as digitized newspapers, magazines or books. In such cases, binarization might support analysis of creator attribution, artistic style (e.g., in line drawings), or analysis of image similarity. Furthermore, the model can be used or trained for any other image enhancement use cases too.


## Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->
<!-- If the user enters content, print that. If not, but they enter a task in the list, use that. If neither, say "more info needed." -->

This model does **NOT** perform any Optical Character Recognition (OCR), it is an image-to-image model only.


# Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

The aim of the development of this model was to improve document image binarization as a necessary pre-processing step. Since the content of the document images is not touched, ethical challenges cannot be identified. The endeavor of developing the model was not undertaken for profit; though a product based on this model might be developed in the future, it will always remain openly accessible without any commercial interest. 
This algorithm performs a pixelwise segmentation which is done in patches. Therefore, one technical limitation of this model is that it is unable to capture and see long range dependencies.


## Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

The application of machine learning models to convert a document image into a binary output is a process which can still be improved. We have used many pseudo-labeled images to train our model, so any improvement or ground truth extension would probably lead to better results.


# Training Details

## Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->
The dataset used for training is a combination of training sets from previous [DIBCO](https://dib.cin.ufpe.br/#!/datasets) binarization competitions alongside with the [Palm Leaf dataset](https://ieeexplore.ieee.org/abstract/document/7814130) and the Persian Heritage Image Binarization Competition [PHIBC](https://arxiv.org/abs/1306.6263) dataset, with additional pseudo-labeled images from the Berlin State Library (SBB; datasets to be published). Furthermore, a dataset for very dark or very bright images has been produced for training.


## Training Procedure

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

We have used a batch size of 8 with learning rate of 1e − 4 for 20 epochs. A soft dice is applied as loss function. In the training we have taken advantage of dataset augmentation. The augmentation includes flipping, scaling and blurring. The best model weights are chosen based on some problematic documents from the SBB dataset. The final model results of the ensemble of the best weights.


### Preprocessing
In order to use this model for binarization no preprocessing is needed for the input image. 

### Speeds, Sizes, Times

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

More information needed

### Training hyperparameters

In the training process, the hyperparameters were patch size, learning rate, number of epochs and depth of encoder part.

### Training results

See the two papers listed below in the evaluation section.

# Evaluation

In the DocEng’2021 [Time-Quality Binarization Competition](https://dib.cin.ufpe.br/docs/DocEng21_bin_competition_report.pdf), the model ranked twelve times under the top 8 of 63 methods, winning 2 tasks.

In the ICDAR 2021 Competition on [Time-Quality Document Image Binarization](https://dib.cin.ufpe.br/docs/papers/ICDAR2021-TQDIB_final_published.pdf), the model ranked two times under the top 20 of 61 methods, winning 1 task.


<!-- This section describes the evaluation protocols and provides the results. -->

## Testing Data, Factors & Metrics

### Testing Data

<!-- This should link to a Data Card if possible. -->

The testing data are the ones used in the [Time-Quality Binarization Competition](https://dib.cin.ufpe.br/docs/DocEng21_bin_competition_report.pdf) and listed in the paper on [Time-Quality Document Image Binarization](https://dib.cin.ufpe.br/docs/papers/ICDAR2021-TQDIB_final_published.pdf).


### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

More information needed.

### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

The model has been evaluated both based on OCR and pixelwise segmentation results. The metrics which have been used in the case of visual evaluation are pixel proportion error and Cohen's Kappa value, and Levenshtein distance error in the case of OCR. 

## Results 

See the two papers listed above in the evaluation section.

# Model Examination

More information needed.

# Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** Nvidia 2080.
- **Hours used:** Two days.
- **Cloud Provider:** No cloud.
- **Compute Region:** Germany.
- **Carbon Emitted:** More information needed.

# Technical Specifications

## Model Architecture and Objective

The proposed model is a hybrid CNN-Transformer encoder-decoder model. The encoder part consists of a ResNet-50 model. The ResNet-50 includes convolutional neural networks and is responsible for extracting as many features as possible from the input image. After that the input image goes through the CNN part, then the output undergoes upsampling convolutional layers until the same output size as in the input image is reached.

## Compute Infrastructure

Training has been performed on a single Nvidia 2080 GPU.

### Hardware

See above.

### Software

See the code published on [GitHub](https://github.com/qurator-spk/sbb_binarization).

# Citation

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

Coming soon.

**BibTeX:**

More information needed.

**APA:**

More information needed.

# Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

More information needed

# More Information [optional]

More information needed.

# Model Card Authors

<!-- This section provides another layer of transparency and accountability. Whose views is this model card representing? How many voices were included in its construction? Etc. -->

[Vahid Rezanezhad](vahid.rezanezhad@sbb.spk-berlin.de), [Clemens Neudecker](https://huggingface.co/cneud), [Konstantin Baierer](konstantin.baierer@sbb.spk-berlin.de) and [Jörg Lehmann](joerg.lehmann@sbb.spk-berlin.de)

# Model Card Contact

Questions and comments about the model can be directed to Clemens Neudecker at clemens.neudecker@sbb.spk-berlin.de, questions and comments about the model card can be directed to Jörg Lehmann at joerg.lehmann@sbb.spk-berlin.de

# How to Get Started with the Model

Use the code below to get started with the model.

sbb_binarize \
  -m <from_pretrained_keras(&#34;sbb_binarization&#34;)> \
  <input image> \
  <output image>

<details>
How to get started with this model is explained in the ReadMe file of the GitHub repository [over here](https://github.com/qurator-spk/sbb_binarization).
</details>
