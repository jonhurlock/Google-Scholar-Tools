from bs4 import BeautifulSoup # used for parsing and doing some funky HTML stuff
import urllib # used for grabbing data from URLs
import unicodedata # for converting unicode to ascii
import sys # for taking
"""
The following page scrapes important data from a google publication page.
You must provide an URL for an individual publication, enclosed in quotations marks

To run
--------
python scrape_publication.py "some url"
python scrape_publication.py help

Output
--------
URL Scraped: http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C

Title: Searching Twitter: Separating the Tweet from the Chaff.

Paper URL: http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/download/2819/3284
Paper File Type: application/pdf

Authors:  ['Jonathan Hurlock', 'Max L Wilson']

Desription: Abstract Within the millions of digital communications posted in online social networks, thereis undoubtedly some valuable and useful information. Although a large portion of socialmedia content is considered to be babble, research shows that people share useful links,provide recommendations to friends, answer questions, and solve problems. In this paper,we report on a qualitative investigation into the different factors that make tweets 'useful'and'not useful'for a set of common search tasks. The investigation found 16 features that help...

"""
if len(sys.argv) != 2:
    print "Error: You have not given the script an URL"
    print "Try again, and try running something such as:"
    print "$ python scrape_publication.py \"http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C\""
    exit()
else:
    url_to_scrape = sys.argv[1]
    if sys.argv[1].strip() == "help":
        print "You must run the following command"
        print "$ python scrape_publication.py \"someurl\""
        print "someurl - has to be surrounded by quotation marks"
        print "it must also be a page which is for a specific publication."
        print "contact @jonhurlock on twitter for more information."
        exit()

# go get content from an URL
#url_to_scrape = "http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C"
f = urllib.urlopen(url_to_scrape)
html_doc = f.read()

# convert output to something beautiful soup can use
soup = BeautifulSoup(html_doc)

# some setup stuff
count = 0 # for counting line numbers
divs = soup.find_all('div') # says get all the divs
# line numbers
title = -1
authors = -1
description = -1
## outputs
title_text = ""
paper_url = ""
paper_url_type = ""
author_text = "" # this is a temporary thing
authors_array = [] # this is what you want to ouput at the end
description_text = ""

# traverse the DOM tree by divs
for div in divs:
    #print str(count)+":"+str(div)
    # get the papers title
    if str(div).startswith('<div id="gsc_title">'):
        title_text = div.get_text(strip=True)
        if div.a.has_attr('href'):
            paper_url = div.a['href']
            # figures out what type of filetype this is
            # this slows down the script as it goes and gets the file.
            res = urllib.urlopen(paper_url)
            http_message = res.info()
            paper_url_type = http_message.type # 'text/plain'
            #paper_url_type = http_message.maintype # 'text'
    # get the authors of the paper
    # should really be parsing the DOM but this is quick and dirty
    if str(div).startswith('<div class="gsc_field">Author'):
        authors = count+1
    if count == authors:
        author_text = (div.get_text(strip=True)).split(',')
    # get he description of the paper
    if str(div).startswith('<div class="gs_scl"><div class="gsc_field">Description</div>'):
        description = count
        description_text = (div.get_text(strip=True))[11:]
    count+=1

# convert unicode data to ascii
## convert all author names and add them to the authors_array
for author in author_text:
    if type(author)==unicode:
        author = (unicodedata.normalize('NFKD', author).encode('ascii','ignore')).strip()
    authors_array.append(author.strip())
# convert the description text
if type(description_text)==unicode:
    description_text = (unicodedata.normalize('NFKD', description_text).encode('ascii','ignore')).strip()
# convert the title text
if type(title_text)==unicode:
    title_text = (unicodedata.normalize('NFKD', title_text).encode('ascii','ignore')).strip()
# convert the paper URL
if type(paper_url)==unicode:
    paper_url = (unicodedata.normalize('NFKD', paper_url).encode('ascii','ignore')).strip()

if len(title_text)!=0:
    # the output
    print "URL Scraped: "+url_to_scrape+"\n"
    print "Title: "+title_text+"\n"
    # If we found an URL for the paper
    if len(paper_url)>0:
        print "Paper URL: "+paper_url
        print "Paper File Type: "+paper_url_type+"\n"
    print "Authors: ",authors_array,"\n"
    print "Desription: "+description_text
else: # No data was gathered for some reason.
    print "Error: We encountered an error getting the document, please check the URL"
