import csv
import requests
import time
import os
from tqdm import tqdm

target_set = "_noTask"
input_csv = f"/depot/davisjam/data/wenxin/CS577-NLP/project/metadata{target_set}.csv"
output_csv = f"metadata{target_set}_WithREADME.csv"
readme_dir = f"./model_cards/{target_set}"

if not os.path.exists(readme_dir):
    os.makedirs(readme_dir)

delay = 2  # Delay in seconds between requests

# Create output directory if it doesn't exist
if not os.path.exists(readme_dir):
    os.makedirs(readme_dir)

with open(input_csv, "r") as input_file:
    total_rows = sum(1 for _ in input_file) - 1  # Subtract 1 to account for the header row


with open(input_csv, "r") as input_file, open(output_csv, "w", newline='') as output_file:
    reader = csv.DictReader(input_file)
    fieldnames = reader.fieldnames + ["readme_path"]  # Add a new column for the README path
    writer = csv.DictWriter(output_file, fieldnames=fieldnames)
    writer.writeheader()

    for row in tqdm(reader, total=total_rows):
        model_name = row["model_name"].replace("/", "_")  # Replace forward slashes with underscores
        model_url = row["model_url"]
        readme_url = f"{model_url}/raw/main/README.md"
        readme_file_name = f"{model_name}_README.md"
        readme_path = os.path.join(readme_dir, readme_file_name)
        if os.path.exists(readme_path):
            print(f"README for {model_name} already exists")
            row["readme_path"] = readme_path
            writer.writerow(row)
            continue
        response = requests.get(readme_url)
        if response.status_code == 200:
            with open(readme_path, "w") as readme_file:
                readme_file.write(response.text)
            print(f"Downloaded README for {model_name}")

            # Add the README path to the row and write it to the output CSV
            row["readme_path"] = readme_path
            writer.writerow(row)
        else:
            print(f"Error {response.status_code} for {model_name}")
            with open('/depot/davisjam/data/wenxin/CS577-NLP/project/readme_error.csv', mode='a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([model_name, response.status_code])
        time.sleep(delay)