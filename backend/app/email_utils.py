import smtplib, os
from dotenv import load_dotenv

load_dotenv()

GMAIL_USER = os.getenv("GMAIL_USER","dummy_user@example.com")
GMAIL_PASS = os.getenv("GMAIL_PASS","dummy_password")

def send_otp_email(email, otp, user_type):
    subject = f"{user_type} Email Verification OTP"
    body = f"Hello,\n\nYour OTP is: {otp}\nPlease use it to complete the verification.\n\nThanks!"
    message = f"Subject: {subject}\n\n{body}"

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(GMAIL_USER, GMAIL_PASS)
        server.sendmail(GMAIL_USER, email, message)
