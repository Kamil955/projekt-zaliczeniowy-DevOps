from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Example data
data = [
    {"id": 1, "name": "Kamil", "age": 22},
    {"id": 2, "name": "Kacper", "age": 24},
    {"id": 3, "name": "Andrzej", "age": 35},
]

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Form data
        name = request.form['name']
        age = request.form['age']

        # Validation
        if not name or not age.isdigit() or int(age) <= 0:
            error_message = "Please provide a valid name and age (positive number)."
            return render_template('index.html', data=data, error_message=error_message)

        # Add new item
        new_item = {"id": len(data) + 1, "name": name, "age": int(age)}
        data.append(new_item)

        return redirect(url_for('home'))  # Redirect to home after adding data

    return render_template('index.html', data=data)

# Delete data
@app.route('/delete/<int:item_id>', methods=['POST'])
def delete(item_id):
    global data
    data = [item for item in data if item['id'] != item_id]
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
