#takes two CLAs: a URL and a filename that the URL will be stored under
#and then saves the file to my personal sourdough-momma s3 bucket.
#could modify program to accept a third CLA containing the name of the bucket

import sys
import urllib.request
import shutil
import boto3

def store_url(URL, filename):
    ''' This function downloads the provided URL (string)
        and saves it under a provided file name (string)'''

    with urllib.request.urlopen(URL) as response:
        with open(filename, 'wb') as outfile:
            shutil.copyfileobj(response, outfile)
    print('All done! :)')
        
#storing passed arguments, along with some light error handling

def CLA_url_file():
    '''This function handles commandline arguments passed to
        the program. Expects a URL first, then a filename to
        save it in (both as strings). Then calls the
        store_url function to save the file'''
    
    if len(sys.argv) != 3:
        print('This program accepts two arguments, a URL followed by the name of a destination file')
        sys.exit(1)

    #parsing the passed arguments
    args = sys.argv[1:]
    URL = args[0]
    filename = args[1]

    #finally run the function that stores the URL
    store_url(URL, filename)

def save_to_s3():
    '''This function will save a file in the current local
       directory to AWS' s3 service'''

    filename = sys.argv[2]
    key = 'uploads'+filename
    
    client = boto3.client('s3')
    client.upload_file(filename, 'sourdough-momma', key)

def main():
    CLA_url_file()
    save_to_s3()
    print('This worked.')

if __name__ == "__main__":
    main()



