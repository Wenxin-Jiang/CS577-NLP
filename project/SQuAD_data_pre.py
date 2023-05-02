import csv
import json

csv_file = "/depot/davisjam/data/wenxin/CS577-NLP/project/metadata_train_withREADME.csv"
output_file = "squad_format_output.json"

def convert_to_squad_format(csv_file):
    squad_data = {"version": "1.1", "data": []}

    with open(csv_file, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            readme_text = row["readme_text"]

            # Skip rows with None readme_text
            if readme_text == "None":
                continue

            model_name = row["model_name"]
            model_url = row["model_url"]
            model_architecture = row["model_architecture"]
            model_task = row["model_task"]
            model_category = row["model_category"]
            readme_path = row["readme_path"]


            qas = [
                {"id": "q1", "question": f"What is the model architecture of {model_name}?", "answers": [{"text": model_architecture, "answer_start": -1}]},
                {"id": "q2", "question": f"What is the model task of {model_name}?", "answers": [{"text": model_task, "answer_start": -1}]},
                {"id": "q3", "question": f"What is the model category of {model_name}?", "answers": [{"text": model_category, "answer_start": -1}]},
            ]

            data_entry = {
                "title": model_name,
                "paragraphs": [
                    {
                        "context": readme_text,
                        "qas": qas
                    }
                ]
            }

            squad_data["data"].append(data_entry)

    return squad_data

squad_data = convert_to_squad_format(csv_file)

with open(output_file, "w", encoding="utf-8") as outfile:
    json.dump(squad_data, outfile, ensure_ascii=False, indent=2)