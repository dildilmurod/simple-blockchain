from flask import Flask
from flask import render_template, redirect, url_for
from flask import request

# from .block import write_block
import block
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
        if request.method == 'POST':
            student = request.form['student']
            s_id = request.form['s_id']
            passport = request.form['passport']
            phone = request.form['phone']
            block.write_block(name=student, p_id=s_id, passport=passport, phone=phone)
            return redirect(url_for('index'))
        else:
            return render_template('index.html')

@app.route('/checking', methods=['GET'])
def check():
    results = block.check_integrity()
    return render_template('index.html', res=results)

if __name__ == '__main__':
    app.run(debug=True)
