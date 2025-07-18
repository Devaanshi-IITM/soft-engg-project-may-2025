# Running the app
python3 -m venv venv

source venv/bin/activate (Linux)
pip install -r requirements.txt

# Create a .env file in the root:

SMTP_EMAIL=your_gmail@gmail.com
SMTP_PASSWORD=your_gmail_app_password

# Running FastAPI (backend)

uvicorn backend.main:app --reload --port 8000

# For frontend

python3 app.py