Buchwald-Hartwig-Yield-prediction is a finetuned model based on 'DeepChem/ChemBERTa-77M-MLM' for yield prediction.
For training and testing the model, 'https://tdcommons.ai/single_pred_tasks/yields' data was used with 70/30 random splitting for the train and test dataset.
the R2 score is equal to 97.2879% and val_loss is equal to 0.0020.
for using it, your input should look like the following: 'reactant smiles''>>''product' with no spaces. For using it, do not use the Hosted inference API. instead, download it yourself or use the colab link below.

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1UyQwPaHmH5BiEa0yZyuZPmMsVi-hIms0#scrollTo=DKy4QptyYTqz)

Github repo: https://github.com/mephisto121/Buchwald-Hartwig-Yield-prediction
