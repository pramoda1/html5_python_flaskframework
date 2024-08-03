from flask import Flask, render_template, request, make_response,abort,redirect,url_for,flash

app = Flask(__name__)
app.secret_key = 'ranodam string '

@app.route('/')
def index1():
    return render_template("index1.html")

@app.route('/login1',methods = ['POST','GET'])
def login1():
    error=None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'invalid username or password please tri again'
           
        else:
            flash('your logged sucesssfully')
            flash('log out before login again')
            return redirect(url_for('index1'))
    return render_template('log_in.html',error=error)


if __name__ == '__main__':
    app.run(debug=True)