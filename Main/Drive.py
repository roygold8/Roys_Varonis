import io
import os
import pickle

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload, MediaIoBaseDownload

from Globals import *


def get_drive_service():
    """
    get drive api service
    :return:
    """
    creds = None
    if os.path.exists('drive_token.pickle'):
        with open('drive_token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                GOOGLE_AUTH_SECRET, DRIVE_SCOPE)
            creds = flow.run_local_server(port=52977)

        # Save the credentials for the next run
        with open('drive_token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)
    return service


def upload_file_to_drive(drive_service, file_name, file_path):
    '''
    :param drive_service: service
    :param file_name: str, file name for drive
    :param file_path: path to upload
    :return:
    '''
    file_metadata = {'name': file_name}
    media = MediaFileUpload(file_path)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: {}'.format(file.get('id')))
    return file.get('id')


def download_file_from_drive(drive_service, file_id):
    '''
    :param drive_service: service
    :param file_id: google id of file to dowload
    :return:
    '''
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))
    f = open(NEW_ZIP, 'wb')
    f.write(fh.getvalue())
