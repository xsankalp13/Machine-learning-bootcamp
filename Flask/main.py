from flask import Flask, render_template, request
import json

app = Flask(__name__)






@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET','POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        return json.dumps({'name':name, 'age':age})
    return render_template('form.html')

#Variable Rules
@app.route('/sucess/<int:score>')
def sucess(score):
    res = ""
    if score >= 50:
        res = "Pass"
    else:
        res = "Fail"

    return render_template('sucess.html', result=res)





if __name__ == '__main__':
    app.run(debug=True)