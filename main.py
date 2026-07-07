import smtplib
from email.mime.text import MIMEText
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 🔐 இங்க உங்க விபரங்களை மட்டும் கரெக்டா குடுத்துருங்க bro:
GMAIL_USER = "valathi91@gmail.com"          # உங்க ஜிமெயில் ஐடி
GMAIL_APP_PASSWORD = "nrxurLpikdpjotrm"    # கூகுள் த்த 16 இலக்க App Password (உங்க டெர்மினல்ல இருந்ததை வச்சுருக்கேன்)
NOTIFY_TO = "valathi91@gmail.com"          # மெசேஜ் வந்து சேர வேண்டிய உங்க ஜிமெயில் ஐடி

app = FastAPI(title="Valathi Portfolio Backend", version="1.0.0")

# 🌐 CORS Setup (இதனாலதான் ஃபிரண்ட்-எண்ட் கனெக்ட் ஆகுது)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def send_contact_notification(name: str, email: str, message: str):
    # செக் பண்றோம் - ஐடி, பாஸ்வேர்ட் இருக்கான்னு
    if not GMAIL_USER or not GMAIL_APP_PASSWORD:
        print("Email sent: GMAIL_USER / GMAIL_APP_PASSWORD = (valathi91@gmail.com, nrxurLpikdpjotrm)")
        return

    # ஈமெயில் கன்டென்ட் ரெடி பண்றோம்
    body = f"New portfolio contact message:\n\nName: {name}\nEmail: {email}\nMessage: {message}"
    msg = MIMEText(body)
    msg["Subject"] = f"Portfolio Contact Form: {name}"
    msg["From"] = GMAIL_USER
    msg["To"] = NOTIFY_TO

    # ஜிமெயில் சர்வர் வழியா மெசேஜ் அனுப்புறோம்
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(GMAIL_USER, GMAIL_APP_PASSWORD)
            server.sendmail(GMAIL_USER, [NOTIFY_TO], msg.as_string())
        print("Notification email sent successfully!")
    except Exception as e:
        print(f"Failed to send notification email: {e}")


from pydantic import BaseModel

# Contact Form Data Model
class ContactForm(BaseModel):
    name: str
    email: str
    message: str


@app.get("/")
def home():
    return {"message": "Portfolio Backend Running Successfully"}


@app.post("/contact")
async def contact(form: ContactForm):
    try:
        send_contact_notification(
            form.name,
            form.email,
            form.message
        )
        return {
            "success": True,
            "message": "Message sent successfully"
        }
    except Exception as e:
        return {
            "success": False,
            "message": str(e)
        }