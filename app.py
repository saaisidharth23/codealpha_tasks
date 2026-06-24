from flask import Flask, request
from chatbot import chatbot_response

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    answer = ""
    if request.method == "POST":
        question = request.form["question"]
        answer = chatbot_response(question)

    return f'''
    <html>
    <body>
    <h1>FAQ Chatbot</h1>
    <form method="post">
    <input name="question" placeholder="Ask a question">
    <button type="submit">Send</button>
    </form>
    <h3>{answer}</h3>
    </body>
    </html>
    '''

app.run(debug=True)
