from flask import Flask, render_template, request, make_response

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template("setcookie.html")

@app.route('/setcookie', methods=['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form.get("nm")
        print(f'Received user: {user}')  # Debug print
        resp = make_response(render_template("readcookie.html"))
        resp.set_cookie("userID", user)
        print(f'Setting cookie: userID={user}')  # Debug print
        return resp
    return render_template("setcookie.html")

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    print(f'Retrieved cookie: userID={name}')  # Debug print
    if not name:
        name = 'Guest'  # Default to 'Guest' if no cookie is found
    return '<h1>Welcome ' + name + '</h1>'

if __name__ == '__main__':
    app.run(debug=True)
