def store_url(URL, filename):
    ''' This function downloads the provided URL (string)
        and saves it under a provided file name (string)'''
    import urllib.request
    import shutil

    with urllib.request.urlopen(URL) as response:
        with open(filename, 'wb') as outfile:
            shutil.copyfileobj(response, outfile)
        
