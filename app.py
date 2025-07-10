from flask import Flask, request, render_template
from resume_parser import parse_resume
from model import predict_fit

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_resume():
    file = request.files['resume']
    if not file:
        return "No file uploaded"

    # Save resume
    filepath = f"resumes/{file.filename}"
    file.save(filepath)

    # Parse and predict
    resume_data = parse_resume(filepath)
    fit_score = predict_fit(resume_data)

    return render_template('result.html', data=resume_data, score=fit_score)

if __name__ == '__main__':
    app.run(debug=True)
