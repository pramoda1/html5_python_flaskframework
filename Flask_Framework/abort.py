from flask import Flask, render_template, request, make_response,abort,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("login.html")

@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        if request.form['un'] == 'admin':
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))
    
@app.route('/success')
def success():
    return 'logged sucessfully'

if __name__ == '__main__':
    app.run(debug=True)