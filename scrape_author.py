import sys # used for taking input from the command line
from bs4 import BeautifulSoup # used for parsing and doing some funky HTML stuff
import urllib # used for grabbing data from URLs
import unicodedata # for converting unicode to ascii

"""
The following page scrapes important data from a google scholar's page.
You must provide an URL for an individual scholar, enclosed in quotations marks

To run
--------
python scrape_author.py "some url"
python scrape_author.py help

Output
--------
Publications for Jonathan Hurlock:

Searching Twitter: Separating the Tweet from the Chaff. ==> http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&oe=ASCII&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C

Keyword clouds: having very little effect on sensemaking in web search engines ==> http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&oe=ASCII&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u-x6o8ySG0sC

"""

if len(sys.argv) != 2:
    print "Error: You have not given the script an URL"
    print "Try again, and try running something such as:"
    print "$ python scrape_author.py \"http://scholar.google.co.uk/citations?user=pu0mIWgAAAAJ&hl=en\""
    exit()
else:
    url_to_scrape = sys.argv[1]
    if sys.argv[1].strip() == "help":
        print "You must run the following command"
        print "$ python scrape_author.py \"someurl\""
        print "someurl - has to be surrounded by quotation marks"
        print "it must also be a page which is for a specific author."
        print "contact @jonhurlock on twitter for more information."
        exit()

# go get content from an URL
#url_to_scrape = "http://scholar.google.co.uk/citations?user=pu0mIWgAAAAJ&hl=en"
f = urllib.urlopen(url_to_scrape)
html_doc = f.read()

# convert output to something beautiful soup can use
soup = BeautifulSoup(html_doc)

# Get the Authors Name
author_name = ""
divs = soup.find_all('div') # says get all the divs
for div in divs:
    if div.has_attr('id'):
        if div['id']=='gsc_prf_in':
            author_name = div.get_text(strip=True)
            if type(author_name)==unicode:
                author_name = (unicodedata.normalize('NFKD', author_name).encode('ascii','ignore')).strip()

# Get the Publications and Links to
publications = []
# some setup stuff
tables = soup.find_all('table') # says get all the divs
publication_table = None
# traverse the DOM tree by divs
for table in tables:
    if table.has_attr('id'):
        if table['id']=='gsc_a_t':
            publication_table = table.find_all('td')
            for data in publication_table:
                if u'gsc_a_t' in data['class']:
                    # papers title
                    paper_title = data.a.get_text(strip=True)
                    if type(paper_title)==unicode:
                        paper_title = (unicodedata.normalize('NFKD', paper_title).encode('ascii','ignore')).strip()
                    # link to the paper
                    paper_link = data.a['href']
                    if type(paper_link)==unicode:
                        paper_link = (unicodedata.normalize('NFKD', paper_link).encode('ascii','ignore')).strip()
                    paper_link = 'http://scholar.google.co.uk'+paper_link

                    publications.append([paper_title,paper_link])

# Printing out the Info:
print 'Publications for '+author_name+':'
for publication in publications:
    print "\n"+publication[0]+" ==> "+publication[1]
