# PyTorch version of the code
import json
import torch
from torch.utils.data import Dataset, DataLoader
from transformers import AutoTokenizer

def find_start_end_positions(context, answer):
    start_position = context.find(answer)
    if start_position == -1:
        return -1, -1
    end_position = start_position + len(answer) - 1
    return start_position, end_position

def update_answer_positions(squad_file):
    with open(squad_file, 'r') as f:
        data = json.load(f)

    valid_answers = []
    for article in data['data']:
        for paragraph in article['paragraphs']:
            context = paragraph['context']
            for qa in paragraph['qas']:
                for answer in qa['answers']:
                    answer_text = answer['text']
                    answer_start, answer_end = find_start_end_positions(context, answer_text)

                    answer['answer_start'] = answer_start
                    answer['answer_end'] = answer_end
                    


    # Save the updated dataset  
    with open("updated_" + squad_file.split('/')[-1], 'w') as f:
        json.dump(data, f)
    return data

def remove_invalid_answer_positions(squad_file):
    with open(squad_file, 'r') as f:
        data = json.load(f)

    for article in data['data']:
        for paragraph in article['paragraphs']:
            context = paragraph['context']
            valid_qas = []  # Store valid question-answer pairs
            for qa in paragraph['qas']:
                valid_answers = []  # Store valid answers
                for answer in qa['answers']:
                    answer_text = answer['text']
                    answer_start, answer_end = find_start_end_positions(context, answer_text)

                    # If answer_start is not -1, update the answer object and add it to valid_answers
                    if answer_start != -1:
                        answer['answer_start'] = answer_start
                        answer['answer_end'] = answer_end
                        valid_answers.append(answer)

                # If there are valid answers, update the question-answer object and add it to valid_qas
                if valid_answers:
                    qa['answers'] = valid_answers
                    valid_qas.append(qa)

            # Update the paragraph with valid question-answer pairs
            paragraph['qas'] = valid_qas

    # Save the updated dataset
    with open("updated_" + squad_file.split('/')[-1], 'w') as f:
        json.dump(data, f)
    return data

if __name__ == '__main__':
    updated_data = update_answer_positions('/depot/davisjam/data/wenxin/CS577-NLP/project/QAmodel/data/squad_format_data.json')
    updated_data = remove_invalid_answer_positions('/depot/davisjam/data/wenxin/CS577-NLP/project/QAmodel/updated_squad_format_data.json')