#!/usr/bin/python

import urllib2
import bs4
import sys


def main():
    page = urllib2.urlopen('http://careers.stackoverflow.com/jobs/remote').read()
    soup = bs4.BeautifulSoup(page)
    for a in soup.findAll('a'):
        try:
            url_string = a['href']
            if url_string.startswith('/jobs/'):
                if url_string[6:7].isdigit():
                    print url_string
                    company = get_company_name('http://careers.stackoverflow.com'+ url_string)
                    print company
                    clean_company = company.replace('http://','')
                    clean_company = clean_company.replace('https://','')
                    clean_company = clean_company.replace('www.','')
                    print clean_company
                    print_rank(clean_company)
        except:
            pass
    print_rank('safaribooksonline.com')

def get_company_name(posting_url):
    page = urllib2.urlopen(posting_url).read()
    soup = bs4.BeautifulSoup(page)
    for a in soup.findAll('a'):
        try:
            if a['class'][0] == 'employer':
                return a['href']
        except:
            pass

    return 'no_url'


def print_rank(company_name):
    url = 'http://www.alexa.com/siteinfo/' + company_name
    page = urllib2.urlopen(url).read()
    soup = bs4.BeautifulSoup(page)
    rank = []
    for s in soup.findAll('strong'):
        try:
            if s['class'][0] == 'metrics-data' and s['class'][1] == 'align-vmiddle':
                rank.append(s.string)
        except:
            pass

    print company_name + " First: " + rank[0] + " Second: " + rank[1]


if __name__ == '__main__':
    sys.exit(main())

