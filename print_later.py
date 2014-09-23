#!/usr/bin/env python

from __future__ import print_function
from twisted.internet import reactor, task

def print_later(mesg):
    ''' Prints the given `mesg` after 1 second has passed. '''
    task.deferLater(reactor, 1, print, mesg)

print_later("The future is now!")
reactor.run()
