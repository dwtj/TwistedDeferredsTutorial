#!/usr/bin/env python
from __future__ import print_function

''' This sample code shows how one can use Deferreds to build up work to be
done on a resource which has not yet been fully initialized. '''

from twisted.internet import defer, reactor

class Database():
    ''' TODO '''

    def __init__(self):
        self.db = None
        self.db_deferred = None
        self._updateDB()
        

    def _updateDB(self):
        self.db_deferred = defer.Deferred()
        reactor.callLater(3, self._fire)
        def saveDB(result):
            self.db = result
            print('Done updating.')
            self.db_deferred = None
            return result
        self.db_deferred.addCallback(saveDB)
        print('end of `_updateDB()`')



    def _fire(self):
        self.db_deferred.callback('db_result')



    def getDB(self):
        d = defer.Deferred()
        if self.db is not None:
            d.callback(self.db)
        else:
            def giveUserCodeDB(result):
                d.callback(result)
                return result
            self.db_deferred.addCallback(giveUserCodeDB)
        return d


db = Database()
def printDB(result):
    print(result)
    return result
db.getDB().addCallback(printDB)
print('Starting reactor.')
reactor.run()


# Expected behavior:
#   end of `_updateDB()`
#   Starting Reactor
#   Done updating
#   db_result
