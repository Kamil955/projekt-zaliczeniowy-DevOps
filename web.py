from flask import Flask, render_template

app = Flask(__name__)

# Example data
data = [
    {"id": 1, "name": "Kamil", "age": 22},
    {"id": 2, "name": "Kacper", "age": 24},
    {"id": 3, "name": "Andrzej", "age": 35},
]

# Home page
@app.route('/')
def home():
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
