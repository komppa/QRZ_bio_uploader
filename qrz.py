import configparser
import login
import bio
import uuid


def main():

    config = configparser.ConfigParser()
    config.read('config.ini')

    callsign = config['LOGIN']['callsign']
    password = config['LOGIN']['password']

    if len(password) == 0:
        exit("You have not set up your callsign and password in config.ini!")
    
    qrz_session_id = login.get_login_token()
    login.validate_callsign(qrz_session_id, callsign)
    login.login_handshake(qrz_session_id, callsign, password)
    token = login.get_token(callsign, password)

    if not token:
        exit("Could not perform login! Wrong callsign or password?")

    bio.update(callsign, token, '<p>Hi!</p>')


if __name__ == "__main__":
    main()