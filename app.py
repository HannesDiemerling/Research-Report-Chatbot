from flask import Flask, render_template, request
from chatbot import MPIBChatbot

# Website dummy for prototype

app = Flask(__name__)
chatbot = MPIBChatbot()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        user_input = request.form['user_input']
        response = chatbot.generate_response(user_input)
        return render_template('index.html', user_input=user_input, response=response)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)