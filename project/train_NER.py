import pandas as pd
import torch
from transformers import BertTokenizer, BertForTokenClassification, Trainer, TrainingArguments, AutoTokenizer
from sklearn.metrics import accuracy_score, precision_recall_fscore_support
import matplotlib.pyplot as plt
import numpy as np

# Load the data
df = pd.read_csv("metadata_train_withREADME.csv", encoding="utf-8")

# Initialize the tokenizer
tokenizer = BertTokenizer.from_pretrained("bert-base-uncased")

# Tokenize the texts
tokenized_texts = []
for sent in df["readme_text"].values:
    try:
        # Convert the text to a string and truncate it if necessary
        sent = str(sent)
        max_length = tokenizer.max_len_single_sentence
        truncated_text = sent[:max_length-2]  # -2 to account for the special tokens [CLS] and [SEP]
        
        # Tokenize the truncated text
        tokenized_text = tokenizer.tokenize(truncated_text)
        tokenized_texts.append(tokenized_text)
    except:
        # If there's an error, add an empty list to tokenized_texts
        tokenized_texts.append([])

    
# Create labels
labels = [["O"]*len(sent) for sent in tokenized_texts]

# Extract the relevant fields from the data
sentences = df["readme_text"].values.tolist()
model_tasks = df["model_task"].values.tolist()
model_architectures = df["model_architecture"].values.tolist()

# Generate dummy labels for training
labels = [["O"]*len(sent.split()) for sent in sentences]

# Load the pre-trained tokenizer and tokenize the data
tokenizer = BertTokenizer.from_pretrained("bert-base-cased", do_lower_case=False)
tokenized_texts = [tokenizer.encode(sent, add_special_tokens=True) for sent in sentences]

# Pad the tokenized texts to a fixed length
MAX_LEN = 128
input_ids = torch.tensor([text + [0]*(MAX_LEN-len(text)) for text in tokenized_texts])
attention_masks = torch.tensor([[1]*len(text) + [0]*(MAX_LEN-len(text)) for text in tokenized_texts])
labels = torch.tensor([tokenizer.encode(" ".join(label)) + [-100]*(MAX_LEN-len(label)) for label in labels])

# Create data loaders
batch_size = 32
data = torch.utils.data.TensorDataset(input_ids, attention_masks, labels)
train_size = int(0.9*len(data))
train_dataset, val_dataset = torch.utils.data.random_split(data, [train_size, len(data)-train_size])
train_dataloader = torch.utils.data.DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
val_dataloader = torch.utils.data.DataLoader(val_dataset, batch_size=batch_size, shuffle=True)

# Load the pre-trained model
model = BertForTokenClassification.from_pretrained("bert-base-cased", num_labels=2)

# Define the training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=batch_size,
    per_device_eval_batch_size=batch_size,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy='epoch',
)

# Define the trainer and train the model
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=val_dataset,
    compute_metrics=lambda p: {"accuracy": accuracy_score(p[0], p[1])}
)

# Train the model
trainer.train()

# Evaluate the model on the validation set
y_true = []
y_pred = []
for batch in val_dataloader:
    input_ids = batch[0].to(device)
    attention_mask = batch[1].to(device)
    labels = batch[2].to(device)
    with torch.no_grad():
        outputs = model(input_ids, attention_mask=attention_mask, labels=labels)
    logits = outputs[1].detach().cpu().numpy()
    label_ids = labels.to('cpu').numpy()
    preds = np.argmax(logits, axis=2)
    for i, mask in enumerate(attention_mask):
        temp_1 = []
        temp_2 = []
        for j, m in enumerate(mask):
            if m:
                if tokenizer.convert_ids_to_tokens(input_ids[i][j]) == "[CLS]":
                    break
                else:
                    temp_1.append(tokenizer.convert_ids_to_tokens(input_ids[i][j]))
                    temp_2.append(tokenizer.id2label[preds[i][j]])
    y_true.append(temp_1)
    y_pred.append(temp_2)

# Flatten the list of true and predicted labels
y_true_flat = [label for sent in y_true for label in sent]
y_pred_flat = [label for sent in y_pred for label in sent]

# Compute precision, recall, F1 score and accuracy
precision, recall, f1_score, _ = precision_recall_fscore_support(y_true_flat, y_pred_flat, average="weighted")
accuracy = accuracy_score(y_true_flat, y_pred_flat)

print(f"Precision: {precision:.4f}")
print(f"Recall: {recall:.4f}")
print(f"F1 score: {f1_score:.4f}")
print(f"Accuracy: {accuracy:.4f}")

# Plot the learning curve
train_loss = trainer.state.log_history['train_loss']
eval_loss = trainer.state.log_history['eval_loss']
x_axis = np.arange(0, len(train_loss))*training_args.logging_steps
plt.plot(x_axis, train_loss, label='Training loss')
plt.plot(x_axis, eval_loss, label='Validation loss')
plt.title('Learning curve')
plt.xlabel('Training steps')
plt.ylabel('Loss')
plt.legend()
plt.show()
plt.savefig('NER learning_curve.png')
