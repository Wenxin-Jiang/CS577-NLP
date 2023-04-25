---
library_name: sklearn
tags:
- sklearn
- skops
- text-classification
---

# Model description

This is a neural net classifier and distilbert model chained with sklearn Pipeline trained on 20 news groups dataset.

## Intended uses & limitations

This model is trained for a tutorial and is not ready to be used in production.

## Training Procedure

### Hyperparameters

The model is trained with below hyperparameters.

<details>
<summary> Click to expand </summary>

| Hyperparameter                                 | Value                                                                                                                                   |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| memory                                         |                                                                                                                                         |
| steps                                          | [('tokenizer', HuggingfacePretrainedTokenizer(tokenizer='distilbert-base-uncased')), ('net', <class 'skorch.classifier.NeuralNetClassifier'>[initialized](
  module_=BertModule(
    (bert): DistilBertForSequenceClassification(
      (distilbert): DistilBertModel(
        (embeddings): Embeddings(
          (word_embeddings): Embedding(30522, 768, padding_idx=0)
          (position_embeddings): Embedding(512, 768)
          (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (dropout): Dropout(p=0.1, inplace=False)
        )
        (transformer): Transformer(
          (layer): ModuleList(
            (0): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (1): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (2): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (3): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (4): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (5): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
          )
        )
      )
      (pre_classifier): Linear(in_features=768, out_features=768, bias=True)
      (classifier): Linear(in_features=768, out_features=20, bias=True)
      (dropout): Dropout(p=0.2, inplace=False)
    )
  ),
))]                                                                                                                                         |
| verbose                                        | False                                                                                                                                   |
| tokenizer                                      | HuggingfacePretrainedTokenizer(tokenizer='distilbert-base-uncased')                                                                     |
| net                                            | <class 'skorch.classifier.NeuralNetClassifier'>[initialized](
  module_=BertModule(
    (bert): DistilBertForSequenceClassification(
      (distilbert): DistilBertModel(
        (embeddings): Embeddings(
          (word_embeddings): Embedding(30522, 768, padding_idx=0)
          (position_embeddings): Embedding(512, 768)
          (LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
          (dropout): Dropout(p=0.1, inplace=False)
        )
        (transformer): Transformer(
          (layer): ModuleList(
            (0): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (1): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (2): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (3): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (4): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
            (5): TransformerBlock(
              (attention): MultiHeadSelfAttention(
                (dropout): Dropout(p=0.1, inplace=False)
                (q_lin): Linear(in_features=768, out_features=768, bias=True)
                (k_lin): Linear(in_features=768, out_features=768, bias=True)
                (v_lin): Linear(in_features=768, out_features=768, bias=True)
                (out_lin): Linear(in_features=768, out_features=768, bias=True)
              )
              (sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
              (ffn): FFN(
                (dropout): Dropout(p=0.1, inplace=False)
                (lin1): Linear(in_features=768, out_features=3072, bias=True)
                (lin2): Linear(in_features=3072, out_features=768, bias=True)
                (activation): GELUActivation()
              )
              (output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)
            )
          )
        )
      )
      (pre_classifier): Linear(in_features=768, out_features=768, bias=True)
      (classifier): Linear(in_features=768, out_features=20, bias=True)
      (dropout): Dropout(p=0.2, inplace=False)
    )
  ),
)                                                                                                                                         |
| tokenizer__max_length                          | 256                                                                                                                                     |
| tokenizer__return_attention_mask               | True                                                                                                                                    |
| tokenizer__return_length                       | False                                                                                                                                   |
| tokenizer__return_tensors                      | pt                                                                                                                                      |
| tokenizer__return_token_type_ids               | False                                                                                                                                   |
| tokenizer__tokenizer                           | distilbert-base-uncased                                                                                                                 |
| tokenizer__train                               | False                                                                                                                                   |
| tokenizer__verbose                             | 0                                                                                                                                       |
| tokenizer__vocab_size                          |                                                                                                                                         |
| net__module                                    | <class '__main__.BertModule'>                                                                                                           |
| net__criterion                                 | <class 'torch.nn.modules.loss.CrossEntropyLoss'>                                                                                        |
| net__optimizer                                 | <class 'torch.optim.adamw.AdamW'>                                                                                                       |
| net__lr                                        | 5e-05                                                                                                                                   |
| net__max_epochs                                | 3                                                                                                                                       |
| net__batch_size                                | 8                                                                                                                                       |
| net__iterator_train                            | <class 'torch.utils.data.dataloader.DataLoader'>                                                                                        |
| net__iterator_valid                            | <class 'torch.utils.data.dataloader.DataLoader'>                                                                                        |
| net__dataset                                   | <class 'skorch.dataset.Dataset'>                                                                                                        |
| net__train_split                               | <skorch.dataset.ValidSplit object at 0x7f9945e18c90>                                                                                    |
| net__callbacks                                 | [<skorch.callbacks.lr_scheduler.LRScheduler object at 0x7f9945da85d0>, <skorch.callbacks.logging.ProgressBar object at 0x7f9945da8250>] |
| net__predict_nonlinearity                      | auto                                                                                                                                    |
| net__warm_start                                | False                                                                                                                                   |
| net__verbose                                   | 1                                                                                                                                       |
| net__device                                    | cuda                                                                                                                                    |
| net___params_to_validate                       | {'module__num_labels', 'module__name', 'iterator_train__shuffle'}                                                                       |
| net__module__name                              | distilbert-base-uncased                                                                                                                 |
| net__module__num_labels                        | 20                                                                                                                                      |
| net__iterator_train__shuffle                   | True                                                                                                                                    |
| net__classes                                   |                                                                                                                                         |
| net__callbacks__epoch_timer                    | <skorch.callbacks.logging.EpochTimer object at 0x7f993cb300d0>                                                                          |
| net__callbacks__train_loss                     | <skorch.callbacks.scoring.PassthroughScoring object at 0x7f993cb306d0>                                                                  |
| net__callbacks__train_loss__name               | train_loss                                                                                                                              |
| net__callbacks__train_loss__lower_is_better    | True                                                                                                                                    |
| net__callbacks__train_loss__on_train           | True                                                                                                                                    |
| net__callbacks__valid_loss                     | <skorch.callbacks.scoring.PassthroughScoring object at 0x7f993cb30ed0>                                                                  |
| net__callbacks__valid_loss__name               | valid_loss                                                                                                                              |
| net__callbacks__valid_loss__lower_is_better    | True                                                                                                                                    |
| net__callbacks__valid_loss__on_train           | False                                                                                                                                   |
| net__callbacks__valid_acc                      | <skorch.callbacks.scoring.EpochScoring object at 0x7f993cb30410>                                                                        |
| net__callbacks__valid_acc__scoring             | accuracy                                                                                                                                |
| net__callbacks__valid_acc__lower_is_better     | False                                                                                                                                   |
| net__callbacks__valid_acc__on_train            | False                                                                                                                                   |
| net__callbacks__valid_acc__name                | valid_acc                                                                                                                               |
| net__callbacks__valid_acc__target_extractor    | <function to_numpy at 0x7f9945e46a70>                                                                                                   |
| net__callbacks__valid_acc__use_caching         | True                                                                                                                                    |
| net__callbacks__LRScheduler                    | <skorch.callbacks.lr_scheduler.LRScheduler object at 0x7f9945da85d0>                                                                    |
| net__callbacks__LRScheduler__policy            | <class 'torch.optim.lr_scheduler.LambdaLR'>                                                                                             |
| net__callbacks__LRScheduler__monitor           | train_loss                                                                                                                              |
| net__callbacks__LRScheduler__event_name        | event_lr                                                                                                                                |
| net__callbacks__LRScheduler__step_every        | batch                                                                                                                                   |
| net__callbacks__LRScheduler__lr_lambda         | <function lr_schedule at 0x7f9945d9c440>                                                                                                |
| net__callbacks__ProgressBar                    | <skorch.callbacks.logging.ProgressBar object at 0x7f9945da8250>                                                                         |
| net__callbacks__ProgressBar__batches_per_epoch | auto                                                                                                                                    |
| net__callbacks__ProgressBar__detect_notebook   | True                                                                                                                                    |
| net__callbacks__ProgressBar__postfix_keys      | ['train_loss', 'valid_loss']                                                                                                            |
| net__callbacks__print_log                      | <skorch.callbacks.logging.PrintLog object at 0x7f993cb30dd0>                                                                            |
| net__callbacks__print_log__keys_ignored        |                                                                                                                                         |
| net__callbacks__print_log__sink                | <built-in function print>                                                                                                               |
| net__callbacks__print_log__tablefmt            | simple                                                                                                                                  |
| net__callbacks__print_log__floatfmt            | .4f                                                                                                                                     |
| net__callbacks__print_log__stralign            | right                                                                                                                                   |

</details>

### Model Plot

The model plot is below.

<style>#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb {color: black;background-color: white;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb pre{padding: 0;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-toggleable {background-color: white;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb label.sk-toggleable__label {cursor: pointer;display: block;width: 100%;margin-bottom: 0;padding: 0.3em;box-sizing: border-box;text-align: center;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb label.sk-toggleable__label-arrow:before {content: "▸";float: left;margin-right: 0.25em;color: #696969;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb label.sk-toggleable__label-arrow:hover:before {color: black;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-estimator:hover label.sk-toggleable__label-arrow:before {color: black;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-toggleable__content {max-height: 0;max-width: 0;overflow: hidden;text-align: left;background-color: #f0f8ff;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-toggleable__content pre {margin: 0.2em;color: black;border-radius: 0.25em;background-color: #f0f8ff;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb input.sk-toggleable__control:checked~div.sk-toggleable__content {max-height: 200px;max-width: 100%;overflow: auto;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb input.sk-toggleable__control:checked~label.sk-toggleable__label-arrow:before {content: "▾";}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-estimator input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-label input.sk-toggleable__control:checked~label.sk-toggleable__label {background-color: #d4ebff;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb input.sk-hidden--visually {border: 0;clip: rect(1px 1px 1px 1px);clip: rect(1px, 1px, 1px, 1px);height: 1px;margin: -1px;overflow: hidden;padding: 0;position: absolute;width: 1px;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-estimator {font-family: monospace;background-color: #f0f8ff;border: 1px dotted black;border-radius: 0.25em;box-sizing: border-box;margin-bottom: 0.5em;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-estimator:hover {background-color: #d4ebff;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel-item::after {content: "";width: 100%;border-bottom: 1px solid gray;flex-grow: 1;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-label:hover label.sk-toggleable__label {background-color: #d4ebff;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-serial::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-serial {display: flex;flex-direction: column;align-items: center;background-color: white;padding-right: 0.2em;padding-left: 0.2em;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-item {z-index: 1;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel {display: flex;align-items: stretch;justify-content: center;background-color: white;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel::before {content: "";position: absolute;border-left: 1px solid gray;box-sizing: border-box;top: 2em;bottom: 0;left: 50%;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel-item {display: flex;flex-direction: column;position: relative;background-color: white;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel-item:first-child::after {align-self: flex-end;width: 50%;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel-item:last-child::after {align-self: flex-start;width: 50%;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-parallel-item:only-child::after {width: 0;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-dashed-wrapped {border: 1px dashed gray;margin: 0 0.4em 0.5em 0.4em;box-sizing: border-box;padding-bottom: 0.4em;background-color: white;position: relative;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-label label {font-family: monospace;font-weight: bold;background-color: white;display: inline-block;line-height: 1.2em;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-label-container {position: relative;z-index: 2;text-align: center;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-container {/* jupyter's `normalize.less` sets `[hidden] { display: none; }` but bootstrap.min.css set `[hidden] { display: none !important; }` so we also need the `!important` here to be able to override the default hidden behavior on the sphinx rendered scikit-learn.org. See: https://github.com/scikit-learn/scikit-learn/issues/21755 */display: inline-block !important;position: relative;}#sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb div.sk-text-repr-fallback {display: none;}</style><div id="sk-4e25a02e-dd88-4cf5-9fc1-aa5db6749fbb" class="sk-top-container"><div class="sk-text-repr-fallback"><pre>Pipeline(steps=[(&#x27;tokenizer&#x27;,HuggingfacePretrainedTokenizer(tokenizer=&#x27;distilbert-base-uncased&#x27;)),(&#x27;net&#x27;,&lt;class &#x27;skorch.classifier.NeuralNetClassifier&#x27;&gt;[initialized](module_=BertModule((bert): DistilBertForSequenceClassification((distilbert): DistilBertModel((embeddings): Embeddings((word_embeddings): Embedding(30522, 768, padding_idx=0)(position_embeddin...(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)))))(pre_classifier): Linear(in_features=768, out_features=768, bias=True)(classifier): Linear(in_features=768, out_features=20, bias=True)(dropout): Dropout(p=0.2, inplace=False))),
))])</pre><b>Please rerun this cell to show the HTML repr or trust the notebook.</b></div><div class="sk-container" hidden><div class="sk-item sk-dashed-wrapped"><div class="sk-label-container"><div class="sk-label sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="4905268f-3ec2-45fc-8bc7-80d9200ae5a5" type="checkbox" ><label for="4905268f-3ec2-45fc-8bc7-80d9200ae5a5" class="sk-toggleable__label sk-toggleable__label-arrow">Pipeline</label><div class="sk-toggleable__content"><pre>Pipeline(steps=[(&#x27;tokenizer&#x27;,HuggingfacePretrainedTokenizer(tokenizer=&#x27;distilbert-base-uncased&#x27;)),(&#x27;net&#x27;,&lt;class &#x27;skorch.classifier.NeuralNetClassifier&#x27;&gt;[initialized](module_=BertModule((bert): DistilBertForSequenceClassification((distilbert): DistilBertModel((embeddings): Embeddings((word_embeddings): Embedding(30522, 768, padding_idx=0)(position_embeddin...(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)))))(pre_classifier): Linear(in_features=768, out_features=768, bias=True)(classifier): Linear(in_features=768, out_features=20, bias=True)(dropout): Dropout(p=0.2, inplace=False))),
))])</pre></div></div></div><div class="sk-serial"><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="4c9a801f-37d5-4fdb-9892-222c86b927bf" type="checkbox" ><label for="4c9a801f-37d5-4fdb-9892-222c86b927bf" class="sk-toggleable__label sk-toggleable__label-arrow">HuggingfacePretrainedTokenizer</label><div class="sk-toggleable__content"><pre>HuggingfacePretrainedTokenizer(tokenizer=&#x27;distilbert-base-uncased&#x27;)</pre></div></div></div><div class="sk-item"><div class="sk-estimator sk-toggleable"><input class="sk-toggleable__control sk-hidden--visually" id="062dd9ff-2b54-4166-90fc-fa3276cd482a" type="checkbox" ><label for="062dd9ff-2b54-4166-90fc-fa3276cd482a" class="sk-toggleable__label sk-toggleable__label-arrow">NeuralNetClassifier</label><div class="sk-toggleable__content"><pre>&lt;class &#x27;skorch.classifier.NeuralNetClassifier&#x27;&gt;[initialized](module_=BertModule((bert): DistilBertForSequenceClassification((distilbert): DistilBertModel((embeddings): Embeddings((word_embeddings): Embedding(30522, 768, padding_idx=0)(position_embeddings): Embedding(512, 768)(LayerNorm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(dropout): Dropout(p=0.1, inplace=False))(transformer): Transformer((layer): ModuleList((0): TransformerBlock((attention): MultiHeadSelfAttention((dropout): Dropout(p=0.1, inplace=False)(q_lin): Linear(in_features=768, out_features=768, bias=True)(k_lin): Linear(in_features=768, out_features=768, bias=True)(v_lin): Linear(in_features=768, out_features=768, bias=True)(out_lin): Linear(in_features=768, out_features=768, bias=True))(sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(ffn): FFN((dropout): Dropout(p=0.1, inplace=False)(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True))(1): TransformerBlock((attention): MultiHeadSelfAttention((dropout): Dropout(p=0.1, inplace=False)(q_lin): Linear(in_features=768, out_features=768, bias=True)(k_lin): Linear(in_features=768, out_features=768, bias=True)(v_lin): Linear(in_features=768, out_features=768, bias=True)(out_lin): Linear(in_features=768, out_features=768, bias=True))(sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(ffn): FFN((dropout): Dropout(p=0.1, inplace=False)(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True))(2): TransformerBlock((attention): MultiHeadSelfAttention((dropout): Dropout(p=0.1, inplace=False)(q_lin): Linear(in_features=768, out_features=768, bias=True)(k_lin): Linear(in_features=768, out_features=768, bias=True)(v_lin): Linear(in_features=768, out_features=768, bias=True)(out_lin): Linear(in_features=768, out_features=768, bias=True))(sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(ffn): FFN((dropout): Dropout(p=0.1, inplace=False)(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True))(3): TransformerBlock((attention): MultiHeadSelfAttention((dropout): Dropout(p=0.1, inplace=False)(q_lin): Linear(in_features=768, out_features=768, bias=True)(k_lin): Linear(in_features=768, out_features=768, bias=True)(v_lin): Linear(in_features=768, out_features=768, bias=True)(out_lin): Linear(in_features=768, out_features=768, bias=True))(sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(ffn): FFN((dropout): Dropout(p=0.1, inplace=False)(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True))(4): TransformerBlock((attention): MultiHeadSelfAttention((dropout): Dropout(p=0.1, inplace=False)(q_lin): Linear(in_features=768, out_features=768, bias=True)(k_lin): Linear(in_features=768, out_features=768, bias=True)(v_lin): Linear(in_features=768, out_features=768, bias=True)(out_lin): Linear(in_features=768, out_features=768, bias=True))(sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(ffn): FFN((dropout): Dropout(p=0.1, inplace=False)(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True))(5): TransformerBlock((attention): MultiHeadSelfAttention((dropout): Dropout(p=0.1, inplace=False)(q_lin): Linear(in_features=768, out_features=768, bias=True)(k_lin): Linear(in_features=768, out_features=768, bias=True)(v_lin): Linear(in_features=768, out_features=768, bias=True)(out_lin): Linear(in_features=768, out_features=768, bias=True))(sa_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)(ffn): FFN((dropout): Dropout(p=0.1, inplace=False)(lin1): Linear(in_features=768, out_features=3072, bias=True)(lin2): Linear(in_features=3072, out_features=768, bias=True)(activation): GELUActivation())(output_layer_norm): LayerNorm((768,), eps=1e-12, elementwise_affine=True)))))(pre_classifier): Linear(in_features=768, out_features=768, bias=True)(classifier): Linear(in_features=768, out_features=20, bias=True)(dropout): Dropout(p=0.2, inplace=False))),
)</pre></div></div></div></div></div></div></div>

## Evaluation Results

You can find the details about evaluation process and the evaluation results.



| Metric   |   Value |
|----------|---------|
| accuracy | 0.90562 |
| f1 score | 0.90562 |

# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

```python
[More Information Needed]
```

</details>


# Additional Content

## Confusion matrix

![Confusion matrix](confusion_matrix.png)

## Classification Report

<details>
<summary> Click to expand </summary>

| index                    |   precision |   recall |   f1-score |   support |
|--------------------------|-------------|----------|------------|-----------|
| alt.atheism              |    0.927273 | 0.85     |   0.886957 |       120 |
| comp.graphics            |    0.85906  | 0.876712 |   0.867797 |       146 |
| comp.os.ms-windows.misc  |    0.893617 | 0.851351 |   0.871972 |       148 |
| comp.sys.ibm.pc.hardware |    0.666667 | 0.837838 |   0.742515 |       148 |
| comp.sys.mac.hardware    |    0.901515 | 0.826389 |   0.862319 |       144 |
| comp.windows.x           |    0.923077 | 0.891892 |   0.907216 |       148 |
| misc.forsale             |    0.875862 | 0.869863 |   0.872852 |       146 |
| rec.autos                |    0.893082 | 0.95302  |   0.922078 |       149 |
| rec.motorcycles          |    0.937931 | 0.906667 |   0.922034 |       150 |
| rec.sport.baseball       |    0.954248 | 0.979866 |   0.966887 |       149 |
| rec.sport.hockey         |    0.979866 | 0.973333 |   0.976589 |       150 |
| sci.crypt                |    0.993103 | 0.966443 |   0.979592 |       149 |
| sci.electronics          |    0.869565 | 0.810811 |   0.839161 |       148 |
| sci.med                  |    0.973154 | 0.973154 |   0.973154 |       149 |
| sci.space                |    0.973333 | 0.986486 |   0.979866 |       148 |
| soc.religion.christian   |    0.927152 | 0.933333 |   0.930233 |       150 |
| talk.politics.guns       |    0.961538 | 0.919118 |   0.93985  |       136 |
| talk.politics.mideast    |    0.978571 | 0.971631 |   0.975089 |       141 |
| talk.politics.misc       |    0.925234 | 0.853448 |   0.887892 |       116 |
| talk.religion.misc       |    0.728972 | 0.829787 |   0.776119 |        94 |
| macro avg                |    0.907141 | 0.903057 |   0.904009 |      2829 |
| weighted avg             |    0.909947 | 0.90562  |   0.906742 |      2829 |

</details>