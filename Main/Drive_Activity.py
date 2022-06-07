import os
import pickle

import pandas as pd
import json
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

from Globals import *


def get_drive_activity_service():
    """
    create drive_activity api service
    :return: service
    """
    creds = None
    if os.path.exists('activity_token.pickle'):
        with open('activity_token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GOOGLE_AUTH_SECRET, ACTIVITY_SCOPE)
            creds = flow.run_local_server(port=52977)

        with open('activity_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('driveactivity', 'v2', credentials=creds)
    return service


def get_people_id(row):
    return row[0]['user']['knownUser']['personName']


def get_type(row):
    return row.keys()


def get_activities(drive_activity_service):
    """
    :param drive_activity_service:
    :return: df of activities
    """
    results = drive_activity_service.activity().query(body={
        'pageSize': 100
    }).execute()
    activities = results.get('activities', [])
    with open('temp.json', 'w') as file:
        json.dump(activities, file)
    df = pd.read_json('temp.json')
    df['people_id'] = df['actors'].apply(get_people_id)
    df['type'] = df['primaryActionDetail'].apply(get_type)
    return df[['timestamp', 'people_id', 'type', 'actions']]
