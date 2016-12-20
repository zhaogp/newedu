import hashlib

__author__ = 'zhaoguoping'
from flask import Flask, request, make_response

app = Flask(__name__)
app.debug = True

@app.route('/', methods=['GET', 'POST'])
def wechat_auth():
    if request.method == 'GET':
        token = 'gpsae'
        print token
        query = request.args
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [token, timestamp, nonce]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s).hexdigest() == signature:
            return make_response(echostr)
        else:
            return make_response('auth error ...')
    return make_response(None)

