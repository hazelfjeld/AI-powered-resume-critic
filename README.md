# AI-Powered Resume Critic

Upload your resume (PDF) and get instant AI feedback along with a hireability score — all powered by GPT-4.

## Features
- Upload any PDF resume
- Extracts text and analyzes with GPT-4
- Gives detailed feedback and a hireability score
- Simple web interface using Flask

## Tech Stack
- Python, Flask
- PyMuPDF (for PDF parsing)
- OpenAI API (GPT-4)
- HTML (with Jinja templates)

## Run Locally

```bash
git clone https://github.com/hazelfjeld/AI-powered-resume-critic.git
cd AI-powered-resume-critic
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows
pip install -r requirements.txt
```
## Create a .env file with your OpenAI key:

```ini
OPENAI_API_KEY=your-key-here
```
## Run the app
```bash
python app.py
```
## Visit http://localhost:5000


