from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/index", methods=['POST'])
def index_post():
    email = request.form.get('username')
    senha = request.form.get('senha')

    return redirect(url_for('bem_vindo'))


@app.route('/bem_vindo', methods=['GET', 'POST'])
def bem_vindo():
    return render_template('bem_vindo.html')


if __name__ == '__main__':
    app.run(debug=True)
