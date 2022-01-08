import dropbox 
from dropbox.files import WriteMode
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token
    def upload_file(self, file_from, file_to): 
        dbx = dropbox.Dropbox(self.access_token) 
        for root, dirs, files in os.walk(file_from): 
            for filename in files: 
                # construct the full local path 
                local_path = os.path.join(root, filename) 
                # construct the full Dropbox path  
                relative_path = os.path.relpath(local_path, file_from) 
                dropbox_path = os.path.join(file_to, relative_path) 
                # upload the file 
                with open(local_path, 'rb') as f: 
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))
def main():
    access_token = 'WmazxqMSbbgAAAAAAAAAAQf0rdr1hBOv6MUvN2s9LstzxEB3wV7vLV_MdoQPtDh3'
    transferData = TransferData(access_token)
    file_from = input("Enter the folder to be transferred--")
    file_to = input("Enter the full path to upload in DropBox--")
    transferData.upload_file(file_from, file_to) 
    print("folder has been moved.")
main()
