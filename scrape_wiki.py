from urllib import parse
from urllib import request
from urllib.robotparser import RobotFileParser

from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Main_Page'
URL_base = 'https://www.wikipedia.org'
destfile = 'wiki_links.txt'

def scrape_urls(URL, destfile):
    ''' This function will scrape all of the URLs
        from a given site and store them in a file.
        This function accepts two arguments, the
        target URL and a file name of your choosing
        to store the links in, both as strings.'''

    links = []

    #open the robots.txt file, which contains scraping permissions
    robotparser = RobotFileParser()
    robotparser.set_url(parse.urljoin(URL_base, 'robots.txt'))
    robotparser.read()
    
    #determine whether you're allowed to scraoe
    if robotparser.can_fetch(useragent='Python-urllib/3.6', url=URL):
        #open the page as a file object and save its contents
        with request.urlopen(URL) as response:
            content = response.read()

        #make a beautifulSoup object from the content, to be read as HTML
        soup = BeautifulSoup(content, 'html.parser')
        
        #'a' is a link in HTML
        for a in soup.find_all('a'):
            #below is necessary to make sure your link has
            #a web address associated with it
            if a.has_attr('href'):
                links.append(a['href'])

        #only proceed if the "links" list was populated in previous step
        if links:
            #save all of the link URLS in an external file
            with open(destfile, 'w') as outfile:
                for link in links:
                    #newline character makes the links separate!
                    outfile.write(link+'\n')

def main(URL, filename):
    scrape_urls(URL, filename)

if __name__ == '__main__':
    main(URL, destfile)

