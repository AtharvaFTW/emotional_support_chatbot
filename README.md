# **EMOTIONAL SUPPORT CHATBOT**
The Emotional Support Chatbot is a web-based application designed to provide empathetic responses, guidance, and valuable resources to individuals experiencing emotional distress. Leveraging advanced Natural Language Processing (NLP) techniques and the powerful OpenAI API, this chatbot simulates human-like conversations and offers emotional support to users in need.

# Features
Empathetic Conversations
Using the OpenAI API, the chatbot generates responses that aim to be both understanding and supportive, helping users feel heard and validated during their moments of need.

**User Authentication:**
The system includes a secure login and registration process to ensure user privacy and data security. Passwords are hashed using werkzeug.security to protect user information.

**Personalized Support:**
The chatbot can provide customized responses based on user inputs and preferences, enhancing the personalization of the support offered.

**User-Friendly Interface:**
Designed with a clean and intuitive user interface, the chatbot is easy to navigate, ensuring an engaging user experience. The interface is developed using HTML, CSS, and JavaScript.

**Mental Health Resources:**
The chatbot offers access to valuable mental health resources and coping strategies, providing users with practical tools to manage their emotional well-being.

**Multilingual Support:**
While currently in development, the chatbot aims to support multiple languages, making it accessible to a broader audience.

# Technologies Used
**Frontend:** HTML, CSS, JavaScript

**Backend:** Flask (Python)

**Database:** SQLite

**API:** OpenAI API for NLP

**Security:** Password hashing with werkzeug.security

# How to use?

**1.Installation**

Clone or download the repository to your local machine:
 ```bash
 git clone https://github.com/AtharvaFTW/emotional_support_chatbot.git
```


**2.Setup**

Navigate to the project directory:
```bash
cd emotional_support_chatbot
```

Create a virtual environment (optional but recommended):
```bash
python -m venv venv
```

Activate the virtual environment:

On Windows:
```bash
venv\Scripts\activate
```

On macOS and Linux:
```bash
source venv/bin/activate
```


**3.Install Dependancies**

Install required Python packages:
```bash
pip install -r requirements.txt
```


**4.Obtaining your Api key**

Follow these steps to obtain your API key from OpenAI:

Sign Up for an Account: Go to the OpenAI website and sign up for an account.

Select an API Plan: Choose the appropriate API plan based on your usage requirements.

Generate Your API Key: After signing up and selecting a plan, navigate to your account settings or dashboard to generate your API key.

Copy Your API Key: Once your API key is generated, copy it to your clipboard.

Use Your API Key: You can now use your API key for this chatbot. Apply your key in app.py file.


**5.Usage**

Run the application:
```bash
python app.py
```
Access the application through your web browser at http://localhost:5000.


**6.Functionality**

The Emotional Support Chatbot provides empathetic responses and guidance to individuals in emotional distress.

Enter your messages in the chat interface, and the chatbot will respond accordingly.


**7.Customization**

Customize the chatbot's behavior or responses by modifying the source code.


**8.Screenshots**

Home:
![Homepage](screenshots/Homepage.png)

Register:
![Alt text](screenshots/Register.png)

Login:
![Alt text](screenshots/Loginpage.png)

UI:
![Alt text](screenshots/UI.png)

Multi Language Support:
![Alt text](screenshots/UI_eng.png)
![Alt text](screenshots/UI_Hindi.png)
![Alt text](screenshots/UI_Japanese.png)

Feedback:
![Alt text](screenshots/Feedbackpage.png)

**9.Credits**

This project was developed by AtharvaFTW. Special thanks to OpenAi for api.








