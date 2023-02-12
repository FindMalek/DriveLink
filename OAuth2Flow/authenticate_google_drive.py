from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']


def authenticateGoogleDrive():
    creds = None
    user_data_folder = os.path.join(os.path.expanduser("~"), "userData")
    credentials_file = os.path.join(user_data_folder, "credentials.json")
    token_file = os.path.join(user_data_folder, "token.json")

    if os.path.exists(token_file):
        creds = Credentials.from_authorized_user_file(token_file, SCOPES)
        
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            logger.debug(f'Credentials refreshed')
            
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credentials_file, SCOPES)
            creds = flow.run_local_server(port=0)
            logger.debug(f'Credentials obtained')
            
        with open(token_file, 'w') as token:
            token.write(creds.to_json())
            logger.debug(f'Credentials saved')
            
    else:
        logger.debug(f'Credentials already exist')