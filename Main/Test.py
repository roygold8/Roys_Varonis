import pyminizip

from Drive import *
from Utils import *
from Drive_Activity import *
from People import *
CREDS = 'royvaronis@gmail.com'
pas = 'RoyVaronis5'


def main():
    #Create zip
    pyminizip.compress(INPUT_FILE_FOR_ZIP, None, OUTPUT_PATH_FOR_ZIP,
                       ZIP_PASSWORD, 5)
    #upload zip to drive
    drive_service = get_drive_service()
    #dowload zip from drive
    download_file_from_drive(drive_service, upload_file_to_drive(drive_service, 'output.zip', OUTPUT_PATH_FOR_ZIP))
    #unzip and get hash
    pyminizip.uncompress(NEW_ZIP, ZIP_PASSWORD, UNZIPED_FILE, 0)
    get_file_of_hash_from_file(r"D:\Documents\Share\python\Veronis\extracted\Secret.txt",
                               r"D:\Documents\Share\python\Veronis\extracted\Hash.txt")
    #upload zip to drive
    upload_file_to_drive(drive_service, 'Hash.txt', r"D:\Documents\Share\python\Veronis\extracted\Hash.txt")
    #get drive activities
    print(get_activities(get_drive_activity_service()))
    #undone - get user's emails
    print(get_people_email(get_people_service()))


if __name__ == '__main__':
    main()
