#takes three CLAs: a URL, a file name that the URL will be stored under,
#and a bucket destination in s3.
#The url is stored under the file name in the s3 bucket

import boto3
import os
import shutil
import sys
import urllib.request

from datetime import datetime
from tempfile import TemporaryDirectory

def store_url_s3(URL, filename, bucket):
    ''' This function downloads the provided URL (string)
        and saves it under a provided file name (string),
        in a given s3 bucket (string) with the time and
        date appended'''
    
    #allows us to circumvent local storage of the file    
    with TemporaryDirectory() as temp_dir:
        #below originates in download_save_URL.py
        with urllib.request.urlopen(URL) as response:
            temp_path = os.path.join(temp_dir, filename)
            with open(temp_path, 'wb') as outfile:
                shutil.copyfileobj(response, outfile)

        #appending the current date and time to the file
        now = str(datetime.now())
        key = f'uploads/{now[:10]}-{now[11:16]}-{filename}'

        #save to s3
        client = boto3.client('s3')
        client.upload_file(temp_path, bucket, key)        
        
def getCLA_url_file_bucket_pass():
    '''This function handles commandline arguments passed to
        the program. Expects a URL first, then a filename to
        save it in, then the name of a destination bucket.
        Then calls the store_url_s3 function to save the file'''

    #enforcing that the passed arguments are correct(ish)
    if len(sys.argv) != 4:
        print('''This program accepts three arguments: a URL,
            the name of the destination file, and an s3
            bucket name''')
        sys.exit(1)

    #parsing the passed arguments
    args = sys.argv[1:]
    URL = args[0]
    filename = args[1]
    bucket = args[2]

    #finally run the function that stores the URL
    store_url_s3(URL, filename, bucket)

def main():
    getCLA_url_file_bucket_pass()
    print('This worked!')

if __name__ == "__main__":
    main()



