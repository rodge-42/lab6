from flask import Flask, request, make_response 
from functools import wraps
app = Flask(__name__)
@app.route('/')
def index():
    if request.authorization and request.authorization.username =='username' and request.authorization.password =='password':
        return'<h1>You are logged in</h1>'

    return make_response('Could not verify!', 401)

if __name__ =='__main__':
    app.run(host='0.0.0.0', port = 5000)
