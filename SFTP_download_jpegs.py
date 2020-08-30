#this program downloads .jpgs from an sftp server. if the file is already in the local directory,
#the file will be downloaded only if the server contains a more up-to-date version.
#if the file is not in the local directory, it will be downloaded

import paramiko
import os

HOST = "demo.wftpserver.com"
PORT = 2222
USER = "demo"
PASSWORD = "demo"

def dirContents_and_ModDate():
    '''make a dictionary containing {file in cwd:last mod time}
    for local directory; will be used later to search whether
    the remote SFTP files are already present locally'''
    
    fileNameDate = {}
    
    for item in os.listdir():
        fileNameDate[item] = os.path.getmtime(item)
    return fileNameDate

def SFTP_get_jpegs(fileNameDate):
    '''This function will download all the .jpeg files from
    a download directory from the remote SFTP server. If the
    same file is present locally, the file will only be
    downloaded if the remote file is more recently modified
    than the local one. Argument is a dictionary of the
    local directory {'file name': mtime} '''

    #initiate SFTP connection
    transport = paramiko.Transport((HOST, PORT))
    transport.connect(username=USER, password=PASSWORD)
    client = paramiko.sftp_client.SFTPClient.from_transport(transport)

    # navigate to the download directory
    client.chdir('/download')

    #storing paths for the remote and local directories for use below
    dirname = client.getcwd()
    localdirname = os.getcwd()

    #iterate through each file on the remote server
    for file in client.listdir():
        if ".jpg" in file:                #identify .jpg files
            if file in fileNameDate:      #reference file name against local directory
                print(file, "is present in local directory")
                #only download if the server file is more recent than the local file
                if client.stat(f"{dirname}/{file}").st_mtime > fileNameDate[file]:
                    print('downloading most up-to-date version of', file, 'from server...')
                    client.get(f"{dirname}/{file}", f"{localdirname}/{file}")
                else:
                    print('Most up-to-date', file, 'already in current working directory.')
            #download file if not present locally already
            else:
                print('Downloading', file, "...")
                client.get(f"{dirname}/{file}", f"{localdirname}/{file}")

    client.close()

def main():
    SFTP_get_jpegs(dirContents_and_ModDate())

if __name__ == '__main__':
    main()
  


