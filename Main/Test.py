import pyminizip

from Drive import *
from Utils import *

CREDS = 'royvaronis@gmail.com'
pas = 'RoyVaronis5'


def main():
    pyminizip.compress(INPUT_FILE_FOR_ZIP, None, OUTPUT_PATH_FOR_ZIP,
                       ZIP_PASSWORD, 5)
    drive_service = get_drive_service()
    download_file_from_drive(drive_service, upload_file_to_drive(drive_service, 'output.zip', OUTPUT_PATH_FOR_ZIP))
    pyminizip.uncompress(NEW_ZIP, ZIP_PASSWORD, UNZIPED_FILE, 0)
    get_file_of_hash_from_file(r"D:\Documents\Share\python\Veronis\extracted\Secret.txt",
                               r"D:\Documents\Share\python\Veronis\extracted\Hash.txt")
    upload_file_to_drive(drive_service, 'Hash.txt', r"D:\Documents\Share\python\Veronis\extracted\Hash.txt")


if __name__ == '__main__':
    main()
