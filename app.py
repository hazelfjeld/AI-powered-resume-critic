from flask import Flask, request, render_template
import fitz  # PyMuPDF
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_ai_feedback(text):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a resume expert. Give honest feedback and a hireability score out of 10."},
            {"role": "user", "content": f"Here is a resume:\n\n{text}\n\nPlease review it."}
        ]
    )
    return response.choices[0].message.content

@app.route("/", methods=["GET", "POST"])
def index():
    feedback = None
    if request.method == "POST":
        file = request.files["resume"]
        resume_text = extract_text_from_pdf(file)
        feedback = get_ai_feedback(resume_text)
    return render_template("index.html", feedback=feedback)

if __name__ == "__main__":
    app.run(debug=True)
