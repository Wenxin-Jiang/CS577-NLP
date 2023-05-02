import json

dataset_path = '/depot/davisjam/data/wenxin/CS577-NLP/project/QAmodel/updated_updated_squad_format_data.json'

with open(dataset_path, 'r') as infile:
    dataset = json.load(infile)

for item in dataset['data']:
    for paragraph in item['paragraphs']:
        filtered_qas = [qa for qa in paragraph['qas'] if qa['id'] != 'q2' and qa['id'] != 'q3']
        paragraph['qas'] = filtered_qas

with open('RemovedQ2Q3_dataset.json', 'w') as outfile:
    json.dump(dataset, outfile, indent=2)
