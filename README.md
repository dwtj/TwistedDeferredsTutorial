Twisted Tutorial
================

This tutorial introduces the [Twisted](https://twistedmatrix.com) networking library for Python. We focus on explaining two concepts which any programmer should understand before trying to make or modify any Twisted application: *asynchronous programming* and *Deferreds*.

If you are already familiar with asynchronous programming (a.k.a. event-driven programming, event-loop programming, reactive programming, the reactor pattern) feel free to jump ahead to [the Twisted-specific stuff](#deferreds).




Other Great Twisted References
------------------------------

The [official Twisted documentation](https://twistedmatrix.com/documents/current/core/index.html) can help you get started understanding how Twisted works, but I've found it to be more useful as an API reference. The resources which I've found that best explain how Twisted is meant to be used are:

- [Krondo Twisted Introduction](http://krondo.com/?page_id=1327)
- [Architecture of Open Source Applications - Twisted](http://www.aosabook.org/en/twisted.html)





The Asynchronous Programming Paradigm
-------------------------------------

### What It Isn't ###

My first mistake when coming to Twisted was not understanding the distinction between multi-threaded programming and asynchronous programming. 

In **multi-threaded programming** the programmer gets work done by managing multiple threads of execution running within a single process. Each of these threads is given some time to run according to the whims of the thread scheduler. (Depending on the programming environment, this scheduler may be in userspace or in the kernel.)

When programming within the multi-threaded paradigm, the programmer must always imagine the possiblity that program execution could jump from one place in one thread to (almost) any other place in any other thread. This can make the programmer's job rather difficult, because it requires that he or she needs to often worry about locking data or carefully synchronizing state between threads.




### What It Is ###

**Asynchronous programming** is quite different. In this paradigm, the programmer must set up a number of event handlers to be executed in response to appropriate triggering events. Ideally, an event handler is a relatively short-running reaction to some occasionally-occurring event (e.g. a system timer, a network message's arrival, and user input). Events happen every once in a while, or they may not happen at all.

There is (generally) just one thread of execution which is handling all of these events. Each event is handled in turn, one-by-one. The whole process looks like this:

(1) The event-loop (fairly) chooses a single event, call it `ev`, to be handled. This `ev` is chosen from the set of recently fired events, each of which is waiting to be handled.

(2) The event-loop calls the event handler for `ev` (possibly with some just-arrived data). This handler is run to completion.

(3) Upon completion, execution returns to the event loop, and the whole process is repeated.

The key is that in the asynchronous paradigm, the programmer never needs to worry about a scheduler non-deterministically jumping between threads of execution: only one thread is needed to manage a very wide variety of events.

So, one can think of the asynchronous programmer's job in the following way: he or she must give commands which set up the system to react to events shortly after they occur.




### What's in a name? ###

The Twisted literature seems to usually use the term "asynchronous programming", but I personally, I find the terms **event-driven programming** and **event-loop programming** to be much more descriptive terms for this programming paradigm.




### What's it Good For? ###

Asynchronous programming is a very appealing alternative to multi-threaded programming when trying to solving certain kinds of problems, in particular, when making [I/O-bound systems](http://en.wikipedia.org/wiki/I/O_bound). It is used very often in both GUI programming and networking programming.






Deferreds
---------

Deferreds are used by a Twisted application to set up work that needs to be done using input that might not be available yet.




### How To Use Deferreds: Set Up the Work To Be Done ###
