import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load model and vectorizer
model = joblib.load("models/mars_model.pkl")
vectorizer = joblib.load("models/vectorizer.pkl")

def predict_fit(resume_data):
    combined_text = ' '.join(resume_data['skills']) + f" experience {resume_data['experience']} years"
    vectorized = vectorizer.transform([combined_text])
    prediction = model.predict(vectorized)[0]
    return "Strong" if prediction == 1 else "Weak"
