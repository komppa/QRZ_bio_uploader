import requests
from headers import get_bio_update_headers as get_headers


def update(callsign, token, raw_html):
    
    data = {
        's': '',
        'op': 'biosave',
        'qrzbio': '{}'.format(raw_html)
    }

    response = requests.post(
        'https://www.qrz.com/edit/{}'.format(callsign),
        headers=get_headers(callsign, token),
        data=data
    )

    # TODO pretty wibbly wobbly, implement better one
    if response.status_code == 200:
        return True
    
    return False
