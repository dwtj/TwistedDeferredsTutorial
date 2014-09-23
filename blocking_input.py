#!/usr/bin/env python

from __future__ import print_function
from twisted.internet import reactor, defer
from twisted.web import client

urls = [ 'http://www.google.com'
       , 'http://www.twitter.com'
       , 'http://www.facebook.com'
       , 'http://www.apple.com'
       , 'http://www.oracle.com'
       , 'a_bad_url' ]

pages = {}

def request_page(url):
    
    # Create three closures and make them callbacks/errbacks for handling
    # the `getPage` request.

    def save_result(result):
        pages[url] = result
        return result
        
    def report_success(result):
        print('Successfully downloaded `{}`.'.format(url))
        return result

    def report_failure(failure):
        print('Failed to download `{}`.'.format(url))
        return None

    d = client.getPage(url)
    d.addCallbacks(report_success, report_failure)
    d.addCallback(save_result)

for url in urls:
    request_page(url)

reactor.run()
