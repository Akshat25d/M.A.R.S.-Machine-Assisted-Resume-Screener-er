import docx2txt
import pdfplumber
import re
from spacy.lang.en import English

nlp = English()

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        with pdfplumber.open(file_path) as pdf:
            text = ' '.join(page.extract_text() or '' for page in pdf.pages)
    elif file_path.endswith('.docx'):
        text = docx2txt.process(file_path)
    else:
        raise ValueError("Unsupported file format")
    return text

def extract_skills(text, skills_list):
    tokens = [token.text.lower() for token in nlp(text)]
    found_skills = set(skill.lower() for skill in skills_list if skill.lower() in tokens)
    return list(found_skills)

def parse_resume(file_path):
    text = extract_text(file_path)

    # Custom skill list
    skills_list = ['python', 'java', 'c++', 'sql', 'machine learning', 'excel', 'flask', 'tensorflow']
    skills = extract_skills(text, skills_list)

    experience = re.findall(r'(\d+)\s*(years|yrs)', text.lower())
    years_exp = max([int(x[0]) for x in experience], default=0)

    return {
        "text": text,
        "skills": skills,
        "experience": years_exp
    }
