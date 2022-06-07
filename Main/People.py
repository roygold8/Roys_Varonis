import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from Globals import *


def get_people_service():
    creds = None
    if os.path.exists('people_token.pickle'):
        with open('people_token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GOOGLE_AUTH_SECRET, PEOPLE_SCOPE)
            creds = flow.run_local_server(port=52977)

        with open('people_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('people', 'v1', credentials=creds)
    return service


def get_people_email(people_service):
    profile = people_service.people().get(resourceName = 'people/107473382952311791052', personFields='names,emailAddresses').execute()
    return profile
