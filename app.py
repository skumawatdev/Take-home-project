from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Define your quiz questions and answers here
questions = [
    {"question": "What is the capital of France?", "options": ["London", "Berlin", "Paris"], "correct_option": 2},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter"], "correct_option": 1},
    # Add more questions here
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        selected_option = int(request.form.get(f'q{i}'))
        if selected_option == question['correct_option']:
            score += 1
    return render_template('result.html', score=score)

if __name__ == '__main__':
    app.run(debug=True)
