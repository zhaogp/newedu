import hashlib
from xml.etree import ElementTree as et
import time

__author__ = 'zhaoguoping'
from flask import Flask, request, make_response

app = Flask(__name__)
app.debug = True

@app.route('/auth', methods=['GET', 'POST'])
def wechat_auth():
    token = 'gpsae'
    print 'token: %s' % token
    query = request.args
    print 'query: %' % query
    signature = query.get('signature', '')
    print 'signature: %s' % signature 
    timestamp = query.get('timestamp', '')
    nonce = query.get('nonce', '')
    echostr = query.get('echostr', '')
    s = [token, timestamp, nonce]
    s.sort()
    s = ''.join(s)
    if hashlib.sha1(s).hexdigest() == signature:
        response = make_response(echostr)
        response.content_type = 'application/text'
        return response
    else:
        response = make_response('auth error ...')
        return response

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        response = make_response('Hello gp.')
        response.content_type = 'application/text'
        return response

    xml_recv = et.fromstring(request.data)
    to_user_name = xml_recv.find('ToUserName').text
    from_user_name = xml_recv.find('FromUserName').text

    latitude_obj = xml_recv.find('Latitude')
    longitude_obj = xml_recv.find('Longitude')

    if latitude_obj:
        latitude = latitude_obj.text
        longitude = longitude_obj.text
        content = xml_recv.find('Content').text + latitude + longitude
    else:
        content = xml_recv.find('Content').text

    reply = '<xml>' \
            '<ToUserName><![CDATA[%s]]></ToUserName>' \
            '<FromUserName><![CDATA[%s]]></FromUserName>' \
            '<CreateTime>%s</CreateTime>' \
            '<MsgType><![CDATA[text]]></MsgType>' \
            '<Content><![CDATA[%s]]></Content>' \
            '<FuncFlag>0</FuncFlag>' \
            '</xml>'

    response = make_response(reply % (from_user_name, to_user_name, str(int(time.time())), content))
    response.content_type = 'application/xml'
    return response


if __name__ == '__main__':
	app.run('0.0.0.0', 5010, debug=True)

