alexa_stackoverflow_remote_jobs_rank
====================================

Quick and dirty Alexa ranker of StackOverflow remote job listings. I wanted a fast way to scan for new jobs and see how they compared to other jobs. I grabbed the first page of http://careers.stackoverflow.com/jobs/remote and cross referenced those with their alexa.com rankings. Typically, popular sites have a US and Global rank. I search for those payloads. If a site has low traffic can get weird results which I just ignore. This is a quick and dirty script I wrote and wanted to share with a friend.

Installation
============

On Ubuntu, ```apt-get install python-bs4``` for the bs4 dependency. You can also use easy_install to install it. The Beautiful Soup installation docs are here: http://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup
