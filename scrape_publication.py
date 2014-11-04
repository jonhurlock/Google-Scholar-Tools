from bs4 import BeautifulSoup # used for parsing and doing some funky HTML stuff
import urllib # used for grabbing data from URLs
import unicodedata # for converting unicode to ascii

# The following page scrapes important data from a google publication page.
# To run => python scrape_publication.py
# Output =>
# URL: http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C
# Title: Searching Twitter: Separating the Tweet from the Chaff.
# Authors:  ['Jonathan Hurlock', 'Max L Wilson']
# Desription: Abstract Within the millions of digital communications posted in online social networks, thereis undoubtedly some valuable and useful information. Although a large portion of socialmedia content is considered to be babble, research shows that people share useful links,provide recommendations to friends, answer questions, and solve problems. In this paper,we report on a qualitative investigation into the different factors that make tweets 'useful'and'not useful'for a set of common search tasks. The investigation found 16 features that help...

# go get a URL
url_to_scrape = "http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C"
f = urllib.urlopen(url_to_scrape)
html_doc = f.read()

# convert output to something beautiful soup can use
soup = BeautifulSoup(html_doc)

# some setup stuff
count = 0
title = -1
authors = -1
pub_date = -1
conference = -1
pages = -1
description = -1
abstract = -1
divs = soup.find_all('div')
title_text = ""
authors_array = []
author_text = ""
description_text = ""

# traverse the DOM tree by divs
for div in divs:
    #print str(count)+":"+str(div)
    if str(div).startswith('<div id="gsc_title">'):
        title_text = div.get_text(strip=True)
    if str(div).startswith('<div class="gsc_field">Author'):
        authors = count+1
    if count == authors:
        author_text = (div.get_text(strip=True)).split(',')
    if str(div).startswith('<div class="gs_scl"><div class="gsc_field">Description</div>'):
        description = count
        description_text = (div.get_text(strip=True))[11:]
    count+=1

# convert unicode data to ascii
for author in author_text:
    author = (unicodedata.normalize('NFKD', author).encode('ascii','ignore')).strip()
    authors_array.append(author.strip())
description_text = (unicodedata.normalize('NFKD', description_text).encode('ascii','ignore')).strip()
title_text = (unicodedata.normalize('NFKD', title_text).encode('ascii','ignore')).strip()

# the output
print "URL: "+url_to_scrape
print "Title: "+title_text
print "Authors: ",authors_array
print "Desription: "+description_text
