from flask import Flask, render_template

app = Flask(__name__)

# Define quiz data
quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["New York", "London", "Paris", "Dublin"],
        "answer": "Paris",
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["Vincent Van Gogh", "Pablo Picasso", "Leonardo Da Vinci", "Claude Monet"],
        "answer": "Leonardo Da Vinci",
    },
    # Add more quiz questions here
]

@app.route('/')
def quiz():
    return render_template('index.html', quiz_data=quiz_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
