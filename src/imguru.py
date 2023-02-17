# ---------------------------------------------------------------------------- #
# --- Imports ---------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


import os
from time import time
from dotenv import load_dotenv


# ---------------------------------------------------------------------------- #
# --- Imguru Uploader -------------------------------------------------------- #
# ---------------------------------------------------------------------------- #

load_dotenv()

class Imguru():


    # ------------------------------------------------------------------------ #
    # --- Imguru Configuration ----------------------------------------------- #
    # ------------------------------------------------------------------------ #

    base_url = 'https://api.imgur.com'
    CLIENT_ID = os.getenv('CLIENT_ID')
    username = ''
    account_id = ''
    access_token = ''
    expires_in = 0
    expires_at: 0
    token_type = ''
    refresh_token = ''


    def get_auth_url(self) -> str:
        auth_url = f'{self.base_url}/oauth2/authorize'
        auth_url += f'?client_id={self.CLIENT_ID}'
        auth_url += '&response_type=token&state=LOGIN'
        return auth_url


    def parse_authorization(self, url: str) -> None:
        auth_details = url.split("#")[1]
        auth_details = auth_details.split("&")
        details = {}
        for auth in auth_details:
            key, value = auth.split("=")
            details[key] = value
        

        self.access_token = details['access_token']
        self.refresh_token = details['refresh_token']
        self.username = details['account_username']
        self.account_id = details['account_id']
        self.expires_in = details['expires_in']
        self.expires_at = float(details['expires_in']) + (time() * 1000)
        self.token_type = details['token_type']


    def current_user(self) -> dict:
        return {
            'username': self.username,
            'account_id': self.account_id,
            'access_token': self.access_token,
            'expires_in': self.expires_in,
            'expires_at': self.expires_at,
            'token_type': self.token_type,
            'refresh_token': self.refresh_token
        }


# ---------------------------------------------------------------------------- #
# --- Main ------------------------------------------------------------------- #
# ---------------------------------------------------------------------------- #


def main():
    pass

if __name__ == '__main__':
    main()
