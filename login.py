import requests
import json
from headers import get_prelogin_headers as get_headers


def validate_callsign(session_id, callsign):

    data = {
        'loginTicket': '{}'.format(session_id),
        'username': '{}'.format(callsign),
        'step': '1'
    }

    response = requests.post(
        'https://www.qrz.com/login-handshake',
        headers=get_headers(callsign),
        data=data
    )

    data = json.loads(response.text)

    if data['error'] == True:
        # User does not exist on QRZ
        return {
            'valid': True,
            'callsign': data['trustInfoUsername'],
            'fullname': data['fullname']
        }
    
    # No errors, so user exists.
    return {
        'valid': False,
        'callsign': '',
        'fullname': ''
    }


def login_handshake(session_id, callsign, password):

    data = {
        'loginTicket': '{}'.format(session_id),
        'username': '{}'.format(callsign),
        'password': '{}'.format(password),  
        'step': '2'
    }

    response = requests.post(
        'https://www.qrz.com/login-handshake',
        headers=get_headers(callsign),
        data=data
    )

    data = json.loads(response.text)

    # TODO return statuscode


def get_token(callsign, password):

    data = {
        'login_ref': 'https://www.qrz.com',
        'username': '{}'.format(callsign),
        'password': '{}'.format(password),  
        '2fcode': '',   # TODO think 2FA
        'target': '/',
        'flush': '1'
    }

    response = requests.post(
        'https://www.qrz.com/login',
        headers=get_headers(callsign),
        data=data
    )

    return response.cookies.get('xf_session')


def get_login_token():

    keyword = "loginTicket"

    response = requests.get(
        'https://www.qrz.com/login'
    )

    r = response.text

    pos = r.find(keyword)

    # 32 is the length of the uuidv4-like without the "-" characters
    token_p = response.text[pos:pos + 100]
    
    # token_p = 
    # ['loginTicket', ': ', '12345678912345678912345678912345', ',\n                ',...
    
    token = token_p.split("'")[2]

    return token
