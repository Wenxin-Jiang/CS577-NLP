import json

def count_question_answers(json_file):
    with open(json_file, 'r') as f:
        data = json.load(f)

    count = 0
    for article in data['data']:
        for paragraph in article['paragraphs']:
            count += len(paragraph['qas'])

    return count

# Example usage
updated_ = "/depot/davisjam/data/wenxin/CS577-NLP/project/QAmodel/updated_squad_format_data.json"
updated_updated_ = "/depot/davisjam/data/wenxin/CS577-NLP/project/QAmodel/updated_updated_squad_format_data.json"
udpated_count = count_question_answers(updated_)
updated_updated_count = count_question_answers(updated_updated_)
print("updated_count: ", udpated_count)
print("updated_updated_count: ", updated_updated_count)