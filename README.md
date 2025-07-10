# 🛰️ M.A.R.S - Machine Assisted Resume Screener

An **AI-powered resume screening bot** built using **Python**, **NLP**, **Scikit-learn**, and **Flask**, designed to automatically extract, analyze, and evaluate resumes based on candidate skills and experience.

> ⚡ Powered by Machine Learning and Natural Language Processing

---

## 📌 Features

* ✅ Upload and parse `.pdf` or `.docx` resumes
* ✅ Extract key information: skills and years of experience
* ✅ Match resumes to job requirements using a trained ML model
* ✅ Get candidate fit score: **Strong** or **Weak**
* ✅ Clean and simple web interface with HTML & CSS

---

## 📂 Project Structure

```
MARS/
├── app.py                 # Flask backend
├── resume_parser.py       # Resume text & NLP processing
├── model.py               # ML model loader & predictor
├── train_model.ipynb      # Model training code (TF-IDF + Logistic Regression)
├── requirements.txt       # Python dependencies
├── templates/
│   ├── index.html         # Upload UI
│   └── result.html        # Output page
├── static/
│   └── style.css          # Custom CSS styling
├── models/
│   ├── mars_model.pkl     # Trained ML model
│   └── vectorizer.pkl     # TF-IDF vectorizer
├── resumes/               # Folder to store uploaded resumes
└── README.md              # Project documentation
```

---

## 🚀 Getting Started

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/yourusername/mars-resume-screener.git
cd mars-resume-screener
```

### 2️⃣ Set Up Environment

```bash
python -m venv venv
venv\Scripts\activate    # On Windows
# or
source venv/bin/activate # On macOS/Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

---

## 🧠 Train the Model

Run the training notebook to create your ML model:

```bash
jupyter notebook train_model.ipynb
```

This generates:

* `mars_model.pkl`
* `vectorizer.pkl`

Stored in the `models/` folder.

---

## 🌐 Run the App

```bash
python app.py
```

Now open your browser and go to:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖼️ Sample UI

| Upload Page                                                           | Result Page                                                              |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| ![Upload](https://via.placeholder.com/400x200.png?text=Upload+Resume) | ![Result](https://via.placeholder.com/400x200.png?text=Screening+Result) |

---

## 🛠️ Technologies Used

* **Python 3**
* **Flask**
* **Scikit-learn**
* **spaCy**
* **TF-IDF Vectorization**
* **Logistic Regression**
* **HTML/CSS**

---

## 📈 Model Logic

1. Extract `skills` and `experience` from resume
2. Combine them into a single string:

   ```
   "python flask experience 3 years"
   ```
3. TF-IDF vectorize the string
4. Predict fit using logistic regression:

   * `1` → Strong
   * `0` → Weak

---

## 📑 Example Resume Input

```
Name: John Doe  
Email: john@example.com  
Skills: Python, Machine Learning, Flask  
Experience: 3 years as a Data Scientist
```

---

## ✨ Future Improvements

* Match against a job description file
* Add support for image-based resumes using OCR
* Resume ranking system
* Deploy on Hugging Face Spaces / Render

---

## 🙌 Contributing

Pull requests are welcome! For major changes, please open an issue first.

---

## 📜 License

This project is licensed under the MIT License.

---

Would you like me to:

* Add badges (e.g. Python version, License)?
* Make a GitHub repo + push it for you?
* Prepare deployable version for Hugging Face or Render?

Let me know!
