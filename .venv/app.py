from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from openai import OpenAI

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management
client = OpenAI(api_key="")# Add your secret Api key from OpenAi between ""
app.static_folder = 'static'
# Define the name for the chatbot
chatbot_name = "Emotional Chatbot"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.form['user_input']

    # Only respond if user_input is not empty
    if user_input.strip():
        # Adjusting the prompt for emotional support
        prompt = f"User: {user_input}\n{chatbot_name}:"

        try:
            # Generating a more empathetic response
            response = client.completions.create(
                model="gpt-3.5-turbo-instruct",
                prompt=prompt,
                temperature=1,  # You can tweak the temperature for desired randomness
                max_tokens=256
            )

            bot_response = response.choices[0].text.strip()

            # Replace the phrase with the desired message
            bot_response = bot_response.replace("I am trained by OpenAI", "I am created using API keys for a personal project")
        except Exception as e:
            # Handle exceptions gracefully
            bot_response = "Oops! Something went wrong. Please try again later."
    else:
        # If user_input is empty, return an empty response
        bot_response = ""

    return jsonify({'bot_response': bot_response})

# Logout route
@app.route('/logout')
def logout():
    # Clear the user's session upon logout
    session.pop('username', None)
    # Redirect to the home page or any other desired page
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, port=2000)
