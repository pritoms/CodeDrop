import dropbox
import os

class Transfer:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as file:
            dbx.files_upload(file.read(), file_to)

def drop(file_source, file_name):

    access_token = "eQidlVzHaN0AAAAAAAAH4kZdimk5SlKgbZhoZ5f44a28iUULkJZu-U9DyxZCxV4X"
    transfer = Transfer(access_token)

    file_from = os.path.basename(file_source)
    file_to = '/%s.py' %file_name

    transfer.upload_file(file_from, file_to)
    print("\nCode Uploaded!")

if __name__ == "__main__":
    drop()