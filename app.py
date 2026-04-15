from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
number_of_count = 0

@app.route('/', methods=['GET', 'POST'])
def first_page():
    global number_of_count
    yes_size = 14 + number_of_count * 4
    no_size = max(10, 14 - number_of_count * 2)

    if request.method == 'POST':
        choice = request.form.get('choice')

        if choice == 'no':
            number_of_count += 1
            yes_size = 14 + number_of_count * 4
            no_size = max(10, 14 - number_of_count * 2)
            return render_template("first.html", number=number_of_count, yes_size=yes_size, no_size=no_size)
        else:
            return redirect(url_for('yes_page'))

    return render_template("first.html", number=number_of_count, yes_size=yes_size, no_size=no_size)

@app.route('/yes')
def yes_page():
    return render_template('yes.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))