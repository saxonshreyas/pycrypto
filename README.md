# pycrypto

This is a personal project of mine to create a crypto content aggregator in Python. We will try and create a website that is able to regularly ingest latest crypto news articles into the website. Biggest inspirations of this website are other (non-crypto) content aggregators such as Alltop, The WebList, and more. 

This can start as a base project of just crypto news but we can look at other expansions, e.g. machine learning models to rate the trustworthiness of news articles, or displaying latest crypto prices up on the website too. Let's start small and see where we can go. 

Any thoughts I have about user requirements and stuff will also be attached to this github repo. Watch this space. 

## Dev Setup

### Creating a Virtual Environment
 - Create a virtual environment called `.pycrypto` using the following command: `python3 -m venv .pycrypto`. 
 - Activate this virtual environment on Mac through the command `source .pycrypto/bin/activate`.
 - Upgrade `pip` to latest version using command `python -m pip install --upgrade pip`
 - Install the following packages: Django (`Django`), feedparser (`feedparser`), django=apscheduler (`django-apscheduler`). 

#### Superuser details (for debugging) 
 - Username: shreyassaxena
 - Password: Cirrus Password
 - Email Address: Gmail Account 

#### Product Requirements 

As a user I would like to: 
1. Know the title of the article 
2. Know the provider of the article 
3. Know when the article was published 
4. Have a way to access the full version of the article 
5. Have tags on the article to summarize basic contents 
6. Have different ways of viewing articles (by provider or by content, etc.)

As a developer I would like to: 
1. Have unique identifier for each article 

