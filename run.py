import pandas as pd
import json
import os

# Get the current working directory
current_dir = os.getcwd()

# Construct the path to the CSV file
file_path = os.path.join(current_dir, 'data_bible.csv')

# Read the CSV file
df = pd.read_csv(file_path)

# Function to process each row and create the JSON structure
def process_row(row, index):
    question_id = f"ppr001q{str(index+1).zfill(3)}"
    question = row['question']
    answers_list = row['answer'].split(',')
    correct_answer_raw = row['correct answer']

    # Remove brackets and extract the correct answer text
    correct_answer_text = correct_answer_raw.split('(')[0].strip()
    
    # Create the answers list with identifiers
    answers = []
    identifier_mapping = ['A', 'B', 'C', 'D']
    correct_identifier = None
    for i, answer in enumerate(answers_list):
        answer_text = answer.strip()
        identifier = identifier_mapping[i]
        answers.append({"identifier": identifier, "Answer": answer_text})
        if correct_answer_text == answer_text:
            correct_identifier = identifier

    # Create the final JSON structure for this question
    return {
        "id": question_id,
        "question": question,
        "answers": answers,
        "correct_answer": correct_identifier
    }

# Process all rows and create the JSON data
json_data = [process_row(row, idx) for idx, row in df.iterrows()]

output_file_path = os.path.join(current_dir, 'json_data.json')
with open(output_file_path, 'w') as json_file:
    json.dump(json_data, json_file, indent=4)

print(f"JSON data saved to {output_file_path}")