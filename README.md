# crawler
Simple Website crawler to generate sitemaps

## Requirements
- python 2.7+
- virtualenv
- pip

## How to use it

Clone this repository:

`git clone https://github.com/menecio/crawler.git`

Move to the repository directory:

`cd crawler`

Create a new virtualenv: 

`virtualenv venv`

Activate your new virtualenv: 

`source venv/bin/activate`

Install python dependencies:

`pip install -r requirements.txt`

Run the crawler:

`scrapy crawl sitemaps -a url=http://www.example.com`

After everything is done, you will find the sitemap.xml file in your directory. That's it!
