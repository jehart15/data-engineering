#download all the .jpg images from a particular FTP server 

from ftplib import FTP

with FTP(host="demo.wftpserver.com", user="demo", passwd="demo") as client:
    #navigate to the correct directory
    client.cwd("download")

    #client.nlist generates a list of the names of the directory contents
    for file in client.nlst():
        #narrow down the list to the target file type
        if '.jpg' in file:
            #generate a string that works with retrbinary, which requires
            #RETR at the beginning of the file name to work
            name = "RETR " + file
            #added this so you can see it working
            print(name)
            #download the file, remember to use binary mode.
            with open(file, 'wb') as f:
                client.retrbinary(name, f.write)

    
