import json
import os

def load_data(source_path):
    """Load the dataset from its source folder's path.

    Args:
        source_path (string): The path to the source folder

    Returns:
        (pd.DataFrame, pd.DataFrame): The complete dataframe and the dataframe of skills.
    """
    data = []
    dataskill = []

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.json'):
            with open(os.path.join(folder_path, file_name), 'r', encoding='utf-8') as file:
                json_data = json.load(file)
                text = json_data['text']
                annotations = json_data.get('annotations', [])
                skills = []
                for annotation in annotations:
                    start, end, label = annotation
                    skill = label.replace('SKILL: ', '').lower()
                    skills.append(skill)
                    dataskill.append({
                        'file_name': file_name,
                        'text': text,
                        'Skill': skill
                    })
                data.append({
                    'file_name': file_name,
                    'text': text,
                    'Skills': skills
                })

    df = pd.DataFrame(data)
    dfskill = pd.DataFrame(dataskill)
    return df, dfskill