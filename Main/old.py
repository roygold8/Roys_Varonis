import datetime
import os.path
import pickle
from datetime import datetime, timedelta

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = r"D:\Documents\Share\python\client_secret_555324867241-3cr53s6duepmtjho1inm59isvutl1dql.apps" \
                   r".googleusercontent.com.json"


def get_calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=52977)

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)
    return service


def create_calndar_event_now(title: str = 'Alert', description: str = '', timezone: str = 'Asia/Jerusalem'):
    service = get_calendar_service()

    now = datetime.now() + timedelta(minutes=1)
    start = now.isoformat()
    end = (now + timedelta(hours=1)).isoformat()
    service.events().insert(calendarId='primary',
                            body={"summary": title, "start": {"dateTime": start, "timeZone": timezone},
                                  "end": {"dateTime": end, "timeZone": timezone}}).execute()



