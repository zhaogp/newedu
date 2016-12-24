import hashlib
import xml.etree.ElementTree as ET
import time

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
        print query
        signature = query.get('signature', '')
        timestamp = query.get('timestamp', '')
        nonce = query.get('nonce', '')
        echostr = query.get('echostr', '')
        s = [token, timestamp, nonce]
        s.sort()
        s = ''.join(s)
        if hashlib.sha1(s).hexdigest() == signature:
            one_response = make_response(echostr)
        else:
            one_response = make_response('auth error ...')
    one_response.content_type = 'application/text'

    xml_recv = ET.fromstring(request.data)
    to_user_name = xml_recv.find('ToUserName').text
    from_user_name = xml_recv.find('FromUserName').test
    content = xml_recv.find('Content').text
    reply = '<xml>' \
            '<ToUserName><![CDATA[%s]]></ToUserName>' \
            '<FromUserName><![CDATA[%s]]></FromUserName>' \
            '<CreateTime>%s</CreateTime>' \
            '<MsgType><![CDATA[text]]></MsgType>' \
            '<Content><![CDATA[%s]]></Content>' \
            '<FuncFlag>0</FuncFlag>' \
            '</xml>'
    response = make_response(reply % (to_user_name, from_user_name, str(int(time.time())), content))
    response.content_type = 'application/xml'
    return response

