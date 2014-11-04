# Google Scholar Tools
Included in this repository are tools to help process data from Google Scholar. The tools are written in Python, and utilise the [Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/) to handle most of the HTML parsing. You will need to install this if you have not already got it installed.

## Scrape a Scholar's Publications (scrape_author.py)
This script scrapes a given author's publication page, then returns a link to each publication on their initial page.

### To scrape an individual's publications page
To scrape an author's page, you enter the following in the command line:
<pre>$ python scrape_author.py "some scholar url"</pre>
You must replace the some scholar url, with the a google scholar link for an individual. However, it is *important* that you **leave the quotations marks**.
#### An Example Author Scrape
Input:
<pre>$ python scrape_author.py "http://scholar.google.co.uk/citations?user=pu0mIWgAAAAJ&hl=en"</pre>
Output:
<pre>Publications for Jonathan Hurlock:

Searching Twitter: Separating the Tweet from the Chaff. ==> http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&oe=ASCII&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u5HHmVD_uO8C

Keyword clouds: having very little effect on sensemaking in web search engines ==> http://scholar.google.co.uk/citations?view_op=view_citation&hl=en&oe=ASCII&user=pu0mIWgAAAAJ&citation_for_view=pu0mIWgAAAAJ:u-x6o8ySG0sC</pre>

## Scrape an Individual Publication Page (scrape_publication.py)
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
