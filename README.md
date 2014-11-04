# Google Scholar Tools
Included in this repository are tools to help process data from Google Scholar. The tools are written in Python.

## Scrape Publication
This script scrapes a given publication page. It will also try and retreive the MIME type of any linked documents.
### To scrape a publication's page
To scrape a publication page, you enter the following in the command line:
<pre>$ python scrape_publication.py "some publication url"</pre>
You must replace the some publication url, with the publicaiton's google scholar link. However, it is *important* that you **leave the quotations marks**.
#### An Example Publication Scrape
Input:
<pre>$ python scrape_publication.py "http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C"</pre>
Output:
<pre>URL Scraped: http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C

Title: Searching Twitter: Separating the Tweet from the Chaff.

Paper URL: http://www.aaai.org/ocs/index.php/ICWSM/ICWSM11/paper/download/2819/3284
Paper File Type: application/pdf

Authors:  ['Jonathan Hurlock', 'Max L Wilson']

Desription: Abstract Within the millions of digital communications posted in online social networks, thereis undoubtedly some valuable and useful information. Although a large portion of socialmedia content is considered to be babble, research shows that people share useful links,provide recommendations to friends, answer questions, and solve problems. In this paper,we report on a qualitative investigation into the different factors that make tweets 'useful'and'not useful'for a set of common search tasks. The investigation found 16 features that help...</pre>
