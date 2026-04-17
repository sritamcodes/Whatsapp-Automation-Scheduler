# 📲 WhatsApp Automation with Python (Twilio)

Automate sending WhatsApp messages using Python with scheduling support via the Twilio API.

---

## 🚀 Features

* ⏰ Schedule messages for a specific date & time
* ⚡ Send messages instantly
* 🌍 Supports international numbers
* 🔐 Secure configuration using environment variables

---

## 🛠️ Tech Stack

* Python
* Twilio API
* datetime, time

---

## 📦 Installation

```bash
git clone https://github.com/your-username/whatsapp-automation-python.git
cd whatsapp-automation-python
```

```bash
python -m venv .venv
.venv\Scripts\activate
```

```bash
pip install twilio python-dotenv
```

---

## 🔐 Environment Setup

Create a `.env` file:

```env
TWILIO_ACCOUNT_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token
```

Add `.env` to `.gitignore`.

---

## 📲 Twilio WhatsApp Setup

1. Go to **Twilio Console**
2. Navigate to **Messaging → Try it out → Send a WhatsApp message**
3. Join the sandbox by sending the given code (e.g. `join xxxx`) from your WhatsApp
4. Copy your:

   * Account SID
   * Auth Token
5. Use Twilio sandbox number:

   ```text
   whatsapp:+14155238886
   ```

> ⚠️ The recipient must also join the sandbox to receive messages.

---

## ▶️ Usage

Run the script:

```bash
python main.py
```

Provide:

* Recipient number (`+countrycode...`)
* Message
* Scheduled date & time (`YYYY-MM-DD HH:MM`)

---

## ⚠️ Notes

* Time must be in the future
* Ensure stable internet connection
* Sandbox must be active for both sender and receiver

---

## 🧠 What This Project Demonstrates

* API integration (Twilio)
* Time-based scheduling logic
* Automation workflow design
* Secure handling of credentials

---

## 📌 Future Improvements

* GUI interface
* Bulk messaging support
* Logging system

---
> Simple automation projects like this demonstrate practical engineering skills and real-world API usage.

---
