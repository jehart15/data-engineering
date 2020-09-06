#This program downloads the diabetes dataset available at the hardcoded URL
#below, and manipulates it so that the 'class' column reads 0 or 1 instead of
#'Negative' or 'Positive', respectively. The original file is copied for
#manipulation, and then transformed. Once the transformation is performed,
#the copied file is deleted; the original file is kept.

import csv
import os
import shutil
import sys
import urllib.request

from datetime import datetime

URL = 'https://archive.ics.uci.edu/ml/machine-learning-databases/00529/diabetes_data_upload.csv'

#formatting a timestamped file name for the file to be downloaded
file_base = 'diabetes_data'
file_type = '.csv'
now = str(datetime.now())
status = 'original'

filename = f'{status}-{now[:10]}-{now[11:16]}-{file_base}{file_type}'

#download the CSV file from the URL, and save it as the original file
def store_url(URL, filename):
    ''' This function downloads the provided URL (string)
        and saves it under a provided file name (string)'''

    with urllib.request.urlopen(URL) as response:
        with open(filename, 'wb') as outfile:
            shutil.copyfileobj(response, outfile)
    print('\nURL copied to local dir under', filename, '\n')

def copy_file(filename):
    '''In the name of data engineering principles, this
       function copies an original piece of data and copies
       it for transformation, changing the filename to show
       it is a copy. Argument = file name as a string, assumes
       the first 8 characters are the word "original". Returns
       the name of the copied file.'''

    #format a name for the copied file
    if 'original' in filename:
        new_name = 'copy'+filename[8:]

    #copying the file here
    with open(filename, 'rb') as original:
        with open(new_name, 'wb') as copy:
            shutil.copyfileobj(original, copy)
            print('copy of original created successfully! \n')

    #passes the name of the file so that it can be
    #transformed by the next function
    return new_name

def transform_csv_column(new_name):
    '''This function transforms the "class" column of the
       diabetes CSV from "positive/negative" to "1/0"
       respectively. Argument is the name of the file to
       be manipulated, which is preferably NOT the original
       data. Creates a new file to store the altered data
       and deletes the unmanipulated file.'''
    
    #storing the csv data as a list of OrderedDicts
    data_store = []
    
    with open(new_name) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data_store.append(row)

    #here we alter the 'class column' by indexing
    #the OrderedDicts within the list and changing
    #the value associated with the 'class' key
    for row in data_store:
        if row['class'] == 'Positive':
            row['class'] = 1
        elif row['class'] == 'Negative':
            row['class'] = 0
        #stop the program if the data is not as expected
        else:
            print('Unexpected value in column "class" \n')
            sys.exit(1)

    #the dict keys are the header for the CSV file
    #to be written. Arbitrarily uses the 1st dict.
    keys = data_store[0].keys()

    #formatting the new filename, with updated time
    status = 'transformed'
    now = str(datetime.now())
    tr_file = f'{status}-{now[:10]}-{now[11:16]}-{file_base}{file_type}'

    #write the data_store list to a new file with above name
    with open(tr_file, 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writeheader()
        for row in data_store:
            writer.writerow(row)
        print('transformed file has been written as', tr_file, '\n')

    #cleaning up: removes the copy we manipulated,
    #leaving us with the original and transformed files
    os.remove(new_name)
                    
def main():
    store_url(URL, filename)
    transform_csv_column(copy_file(filename))

if __name__ == '__main__':
    main()

    
    
