import configparser
import login
import bio
import sys
import argparse


def main():

    # 1) config.ini
    # config = configparser.ConfigParser()
    # config.read('config.ini')

    # callsign = config['LOGIN']['callsign']
    # password = config['LOGIN']['password']

    # 2) environment variables
    # callsign = os.environ['CALLSIGN']
    # password = os.environ['PASSWORD']

    # 3) Arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('callsign')
    parser.add_argument('password')
    parser.add_argument('html')
    args = parser.parse_args()

    callsign = args.callsign
    password = args.password
    html = args.html


    if len(callsign) == 0 or len(password) == 0:
        # exit("You have not set up your callsign and password in config.ini!")
        exit("Cannot find callsign and/or password from your environment variables!")
    
    qrz_session_id = login.get_login_token()
    login.validate_callsign(qrz_session_id, callsign)
    login.login_handshake(qrz_session_id, callsign, password)
    token = login.get_token(callsign, password)

    if not token:
        exit("Could not perform login! Wrong callsign or password?")

    bio.update(callsign, token, html)


if __name__ == "__main__":
    main()