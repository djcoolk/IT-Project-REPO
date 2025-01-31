🧘 Wellness Whisperer – AI-Powered Mental Health Support
📌 Overview
Wellness Whisperer is a Django-based mental health application that integrates AI-powered guidance, therapist booking, and real-time video consultations. It provides users with personalized mental health support by leveraging Ollama 3.2 for AI-driven advice and the Agora SDK for secure video calls.

✨ Features
🤖 AI-Powered Mental Health Advice (Ollama 3.2 Integration)
📅 Book Appointments with Therapists (Online & In-Person)
🎥 Real-Time Video Consultations (Agora SDK)
🔒 Secure & Private User Interactions
📊 User Progress Tracking & Recommendations
🛠️ Technologies Used
Python (Django) – Backend Framework
JavaScript (React) – Frontend Interface
Ollama 3.2 – AI-Powered Advice System
Agora SDK – Video Call Functionality
PostgreSQL – Database for Storing User & Therapist Data
Docker – For Containerized Deployment
📦 Installation
Prerequisites
Ensure you have the following installed:

Python 3.8+
Node.js & npm (for frontend)
PostgreSQL (or SQLite for local testing)
Docker (optional for containerized setup)
Steps
Clone the Repository
sh
Copy
Edit
git clone https://github.com/ItsMakha/wellness-whisperer.git
cd wellness-whisperer
Create a Virtual Environment & Install Dependencies
sh
Copy
Edit
python -m venv env  
source env/bin/activate  # (For macOS/Linux)
env\Scripts\activate     # (For Windows)
pip install -r requirements.txt  
Set Up Database
sh
Copy
Edit
python manage.py makemigrations  
python manage.py migrate  
Run the Server
sh
Copy
Edit
python manage.py runserver  
Frontend Setup
sh
Copy
Edit
cd frontend  
npm install  
npm start  
Access the App
Open http://127.0.0.1:8000 in your browser.
🚀 How It Works
Users sign up and log in securely.
The AI chatbot provides mental health guidance.
Users can book appointments with therapists.
Secure video consultations happen via Agora SDK.
The system logs progress and suggests improvements.
📸 Example Screenshots
🖼️ (Add images of your app's UI here)

🔧 Future Enhancements
💡 Mobile App version (React Native)
📊 Sentiment Analysis for improved AI suggestions
🌍 Multi-Language Support
🔔 Automated Reminders & Notifications
🤝 Contribution
Fork the repo, create a feature branch, and submit a pull request!
Report bugs via GitHub Issues.
