#use command line arguments to save a given URL as a file with a given name.

import sys
import urllib.request
import shutil

def store_url(URL, filename):
    ''' This function downloads the provided URL (string)
        and saves it under a provided file name (string)'''

    with urllib.request.urlopen(URL) as response:
        with open(filename, 'wb') as outfile:
            shutil.copyfileobj(response, outfile)
    print('All done! :)')
        
#storing passed arguments,  along with some light error handling
try:
    args = sys.argv[1:]
except IndexError:
    print('This program accepts two arguments, a URL followed by the name of a destination file')
if len(args) != 2:
    print('This program accepts two arguments, a URL followed by the name of a destination file')

#parsing the passed arguments
URL = args[0]
filename = args[1]

#finally run the function that stores the URL
store_url(URL, filename)



