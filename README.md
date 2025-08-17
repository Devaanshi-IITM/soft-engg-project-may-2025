# Saathi: Digital Companion App for Senior Citizens

Saathi is an innovative app designed to provide senior citizens with a comprehensive digital solution to address their unique challenges. It focuses on improving health, social connection, daily tasks, safety and overall well-being by integrating empathetic design, usability, accessibility, and simplicity.

## 📝 Problem Statement

The main challenge we sought to solve was to create a digital solution that caters to the needs of senior citizens by:

- Helping with **health management**
- Enhancing **social connections**
- Assisting with **daily tasks** and reminders
- Ensuring **general well-being**

By directly interacting with our primary users, collecting feedback, and carefully studying their pain points, we have developed an app that emphasizes **usability** and **accessibility**, while ensuring simplicity in design.

## Tech Stack

Here are the key libraries and frameworks used in the project:

### Frontend
- **Vue.js** ![Vue.js](https://img.shields.io/badge/Vue.js-4FC08D?style=flat-square&logo=vue.js&logoColor=white)

### Backend  
- **Flask** ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)  

- **SQLite** ![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)  

### GenAI Integration
- **Langchain** ![Langchain](https://img.shields.io/badge/Langchain-FF9900?style=flat-square&logo=python&logoColor=white)  

- **Groq** ![Groq](https://img.shields.io/badge/Groq-0078D4?style=flat-square&logo=microsoft&logoColor=white)
 
- **Whisper** ![Whisper](https://img.shields.io/badge/Whisper-4F8C99?style=flat-square&logo=python&logoColor=white)

## Prerequisites

To run the app locally, the following libs should've been installed:

- **Python 3.10** or higher
- **Pip**


## 📥 Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/Devaanshi-IITM/soft-engg-project-may-2025-se-May-19.git
cd Team_19_SE_Code_May_2025
```
### 2. Create Virtual environment, install dependencies
-  (Ubuntu/MacOS)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
- Windows
```bash
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Running the app locally
-  (Ubuntu/MacOS)
```bash
python3 app.py
```
- Windows
```bash
python app.py
```
Should be available at `http://127.0.0.1:5000/#/`

## Agent Flow (GenAI)
[![](https://mermaid.ink/img/pako:eNqdkUFvgjAYhv8K-bxsCZJSi0iXLFHwsPtOE0OYfAhZoaSUTEf47yuo225L7Knv8_V5e_h6OMgMgcNRpU1hvUZxbZmzftglSatTpZNk_2jN58_WpheiGp4u841B1kutsc4SLZMWdaKwKusM1fQ47LWU4vY6nFg0do6CafytccxkuzN4f2XbC4tMvIBWnwVaaysvheAzXCLJV3arlfxAPguYH2TuNc4_y0wXnDanv-bmbjO824yu5oG-05z8b44u2GYJZQZcqw5tqFBV6RihH6cx6AIrjIGba4Z52gkdQ1wPRmvS-k3K6mYq2R0L4HkqWpO6Jks1RmVqNlz9UIXjrkLZ1Ro4ZWQqAd7DCbgbrJwFCzzfXzFGXMKYDWfgnucw6hPPd4kfEI-wwYav6VvXIUGw9KnneQFdsCUdvgEy9bdS?type=png)](https://mermaid.live/edit#pako:eNqdkUFvgjAYhv8K-bxsCZJSi0iXLFHwsPtOE0OYfAhZoaSUTEf47yuo225L7Knv8_V5e_h6OMgMgcNRpU1hvUZxbZmzftglSatTpZNk_2jN58_WpheiGp4u841B1kutsc4SLZMWdaKwKusM1fQ47LWU4vY6nFg0do6CafytccxkuzN4f2XbC4tMvIBWnwVaaysvheAzXCLJV3arlfxAPguYH2TuNc4_y0wXnDanv-bmbjO824yu5oG-05z8b44u2GYJZQZcqw5tqFBV6RihH6cx6AIrjIGba4Z52gkdQ1wPRmvS-k3K6mYq2R0L4HkqWpO6Jks1RmVqNlz9UIXjrkLZ1Ro4ZWQqAd7DCbgbrJwFCzzfXzFGXMKYDWfgnucw6hPPd4kfEI-wwYav6VvXIUGw9KnneQFdsCUdvgEy9bdS)

## Presentation

The link to the video can be found at [https://drive.google.com/drive/folders/1QqF2J_u4fjzQyoSwwB7--gevfLkIBFi-?usp=sharing](https://drive.google.com/drive/folders/1QqF2J_u4fjzQyoSwwB7--gevfLkIBFi-?usp=sharing)

---

## Directory Structure
```
saathi-digital-companion
├─── app.py
├─── database.db
├─── models.py
├─── README.md
├─── requirement.txt
│
├─── api
│   ├─── admin_api.py
│   ├─── appointment_api.py
│   ├─── audio_api.py
│   ├─── guardian_api.py
│   ├─── message_api.py
│   ├─── reminder_api.py
│   ├─── senior_api.py
│   └─── __init__.py
│
├─── static
│   └─── index.html
│
├─── audio
│
├─── css
│   └─── style.css
│
└─── js
    ├─── app.js
    ├─── router.js
    └─── pages
        ├─── app.js
        ├─── GuardianAuth.js
        ├─── GuardianDashboard.js
        ├─── ManageReminders.js
        ├─── SeniorDashboard.js
        ├─── SeniorLogin.js
        ├─── SeniorProfileView.js
        └─── SeniorRegister.js
```
