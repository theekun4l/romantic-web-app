from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__,static_folder='static')
app.secret_key = "secret123"

@app.route('/', methods=['GET', 'POST'])
def first_page():

    if request.method == 'GET':
        session['count'] = 0   # 🔥 reset on new visit

    if 'count' not in session:
        session['count'] = 0

    if request.method == 'POST':
        choice = request.form.get('choice')

        if choice == 'no':
            session['count'] += 1
        else:
            session['count'] = 0
            return redirect(url_for('yes_page'))

    number_of_count = session['count']

    yes_size = 14 + number_of_count * 4
    no_size = max(10, 14 - number_of_count * 2)

    return render_template(
        "first.html",
        number=number_of_count,
        yes_size=yes_size,
        no_size=no_size
    )

@app.route('/yes')
def yes_page():
    return render_template('yes.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=int(os.environ.get("PORT",5000)))