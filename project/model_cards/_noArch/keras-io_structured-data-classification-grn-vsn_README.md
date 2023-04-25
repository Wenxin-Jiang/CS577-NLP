---
library_name: keras
tags:
- GRN-VSN
- tabular-classification
- classification
---

## Model description

This model is built using two important architectural components proposed by Bryan Lim et al. in  [Temporal Fusion Transformers (TFT) for Interpretable Multi-horizon Time Series Forecasting](https://arxiv.org/abs/1912.09363) called GRN and VSN which are very useful for structured data learning tasks.

1. **Gated Residual Networks(GRN)**: consists of skip connections and gating layers that facilitate information flow efficiently. They have the flexibility to apply non-linear processing only where needed.
GRNs make use of [Gated Linear Units](https://arxiv.org/abs/1612.08083) (or GLUs) to suppress the input that are not relevant for a given task.

   The GRN works as follows:
     - It first applies Non-linear ELU tranformation on its inputs
     - It then applies a linear transformation followed by dropout
     - Next it applies GLU and adds the original inputs to the output of the GLU to perform skip (residual) connection
     - Finally, it applies layer normalization and produces its output


2. **Variable Selection Networks(VSN)**: help in carefully selecting the most important features from the input and getting rid of any unnecessary noisy inputs which could harm the model's performance.
The VSN works as follows:
    - First, it applies a Gated Residual Network (GRN) to each feature individually. 
    - Then it concatenates all features and applies a GRN on the concatenated features, followed by a softmax to produce feature weights 
    - It produces a weighted sum of the output of the individual GRN

**Note:** This model is not based on the whole TFT model described in the mentioned paper on top but only uses its GRN and VSN components demonstrating that GRN and VSNs can be very useful on their own also for structured data learning tasks.

## Intended uses 

This model can be used for binary classification task to determine whether a person makes over $500K a year or not.

## Training and evaluation data

This model was trained using the [United States Census Income Dataset](https://archive.ics.uci.edu/ml/datasets/Census-Income+%28KDD%29) provided by the UCI Machine Learning Repository. 
The dataset consists of weighted census data containing demographic and employment related variables extracted from 1994 and 1995 Current Population Surveys conducted by the US Census Bureau.
The dataset comprises of ~299K samples with 41 input variables and 1 target variable called *income_level* 
The variable *instance_weight* is not used as an input for the model so finally the model uses 40 input features containing 7 numerical features and 33 categorical features:

| Numerical Features | Categorical Features |
| :-- | :-- |
| age | class of worker |
| wage per hour | industry code |
| capital gains | occupation code |
| capital losses | adjusted gross income |
| dividends from stocks | education |
| num persons worked for employer | veterans benefits |
| weeks worked in year | enrolled in edu inst last wk
|| marital status |
|| major industry code |
|| major occupation code |
|| mace |
|| hispanic Origin |
|| sex |
|| member of a labor union |
|| reason for unemployment |
|| full or part time employment stat |
|| federal income tax liability |
|| tax filer status |
|| region of previous residence |
|| state of previous residence |
|| detailed household and family stat |
|| detailed household summary in household |
|| migration code-change in msa |
|| migration code-change in reg |
|| migration code-move within reg |
|| live in this house 1 year ago |
|| migration prev res in sunbelt |
|| family members under 18 |
|| total person earnings |
|| country of birth father |
|| country of birth mother |
|| country of birth self |
|| citizenship |
|| total person income |
|| own business or self employed |
|| taxable income amount |
|| fill inc questionnaire for veteran's admin |

The dataset already comes in two parts meant for training and testing.
The training dataset has 199523 samples whereas the test dataset has 99762 samples.

## Training procedure

1. **Prepare Data:** Load the training and test datasets and convert the target column *income_level* from string to integer. The training dataset is further split into train and validation sets.
Finally, the training and validation datasets are then converted into a tf.data.Dataset meant to be used for model training and evaluation.

2. **Define logic for Encoding input features:** We encode the categorical and numerical features as follows:
   
   - **Categorical Features:** are encoded using *Embedding* layer provided by Keras. The output dimension of the embedding is equal to *encoding_size*
  
   - **Numerical Features:** are projected into a *encoding_size* dimensional vector by applying a linear transformation using *Dense* layer provided by Keras
   
   Therefore, all the encoded features will have the same dimensionality equal to the value of *encoding_size*.

3. **Create Model:** 
   - The model will have input layers corresponding to both numerical and categorical features of the given dataset
   - The features received by the input layers are then encoded using the encoding logic defined in Step 2 with an *encoding_size* of 16 indicating the output dimension of the encoded features. 
   - The encoded features pass through the Variable Selection Network(VSN). The VSN internally makes use of the GRN as well, as explained in the *Model Description* section.
   - The features produced by the VSN are passed through a final *Dense* layer with sigmoid activation to produce the final output of the model indicating the probability for whether the income of a person is >500K or not.

4. **Compile, Train and Evaluate Model**: 
   - Since the model is meant to binary classification, the loss function chosen was Binary Cross Entropy.
   - The metric chosen for evaluating the model's performance was *accuracy*.
   - The optimizer chosen was Adam with a learning rate of 0.001.
   - The dropout_rate for the Dropout Layers of the GRN was 0.15
   - The batch_size chosen was 265 and the model was trained for 20 epochs.
   - The training was done with a Keras callback for *EarlyStopping* which means the training would be interrupted as soon as the validation metrics have stopped improving.
   - Finally the performance of the model was also evaluated on the test_dataset reaching an accuracy of ~95%

### Training hyperparameters

The following hyperparameters were used during training:

| Hyperparameters | Value |
| :-- | :-- |
| name | Adam |
| learning_rate | 0.0010000000474974513 |
| decay | 0.0 |
| beta_1 | 0.8999999761581421 |
| beta_2 | 0.9990000128746033 |
| epsilon | 1e-07 |
| amsgrad | False |
| training_precision | float32 |


 ## Model Plot

<details>
<summary>View Model Plot</summary>

![Model Image](./model.png)

</details>

## Credits:

- HF Contribution: [Shivalika Singh](https://www.linkedin.com/in/shivalika-singh)
- Full credits to original [Keras example](https://keras.io/examples/structured_data/classification_with_grn_and_vsn) by [Khalid Salama](https://www.linkedin.com/in/khalid-salama-24403144)
- Check out the demo space [here](https://huggingface.co/spaces/keras-io/structured-data-classification-grn-vsn)
