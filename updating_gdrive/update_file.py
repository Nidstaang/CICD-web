from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
gauth = GoogleAuth()
gauth.LocalWebserverAuth()


def auth_pydrive():

    ### This checks/refreshes/creates credential file

    gauth = GoogleAuth()
   
    gauth.LoadCredentialsFile("client_secrets.json")
    if gauth.credentials is None:
        
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        
        gauth.Refresh()
    else:
        
        gauth.Authorize()
    
    gauth.SaveCredentialsFile("client_secrets.json")

    drive = GoogleDrive(gauth)
    return drive


def update_file_content(drive, file_id):
 
    ### this updates the content file
     
    old_file = drive.CreateFile(
        {'id': f"{file_id}", 'mimeType': '*insertlacosaesa'})  ###FILE ID
    old_file.SetContentFile('/path/to/*insertfilepathwhenifindit*')
    old_file.Upload()
    old_file_id = old_file['id']
    return old_file_id