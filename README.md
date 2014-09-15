Twisted Deferreds Tutorial
==========================

This tutorial introduces the [Twisted](https://twistedmatrix.com) networking library for Python. We focus on explaining two concepts which any programmer should understand before trying to make or understand any Twisted application: *asynchronous programming* and *Deferreds*.

If you are already familiar with asynchronous programming (a.k.a. event-driven programming, event-loop programming, reactive programming, the reactor pattern) feel free to jump ahead to [the Twisted-specific stuff](#Deferreds).




Other Great Twisted References
------------------------------

The [official Twisted documentation](https://twistedmatrix.com/documents/current/core/index.html) can help you get started understanding how Twisted work, but the resources which I've found which best explain how Twisted works are:

- [Krondo Twisted Introduction](http://krondo.com/?page_id=1327)
- [Architecture of Open Source Applications - Twisted](http://www.aosabook.org/en/twisted.html)





The Asynchronous Programming Paradigm
-------------------------------------

### What It Isn't ###

My first mistake when coming to Twisted was not understanding the distinction between multi-threaded programming and asynchronous programming. 

In **multi-threaded programming** the programmer gets work done by managing multiple threads of execution running within a single process. Each of these threads is given some time to run according to the whims of the thread scheduler. (Depending on the programming environment, this scheduler may be in userspace or in the kernel.)

When programming within the multi-threaded paradigm, the programmer must always imagine the possiblity that program execution could jump from one place in one thread to (almost) any other place in any other thread. It turns out that this can be very hard.




### What It Is ###

In **asynchronous programming**, the programmer must set up a number of event handlers to be executed in response to appropriate triggering events. Ideally, an event handler is a relatively short-running reaction to some occasionally-occurring event (e.g. a system timer, network message arrival, and user input). Events happen every once in a while, or they may not happen at all.

This does not generally require any use of threads, rather, an event-loop (or reactor) runs these event handlers


relatively small computational tasks called event handlers, where each is to be executed if and when the appropriate triggering event occurs.


Personally, I find both **event-driven programming** and **event-loop programming** to be much more descriptive terms for this programming paradigm, but the Twisted literature seems to usually use the term "asynchronous programming" instead.

The key is that asynchronous programming does not have a scheduler which non-deterministically switches between different threads of execution. The programmer does not generally need to worry about thread synchronization, because asynchronous programs (usually) only need one thread.

That thread's behavior is organized around a simple principle. A piece of computation can get done once the necessary pre-conditions occur: data has arrived and/or enough time has passed.




### This Idea Isn't New ###

`select`


### What is it Good For? ###

Asynchronous programming is very useful for when you are making I/O-bound systems.

It is often used for GUI programming and networking programming.

Imagine a GUI just siting there waiting for user input or some other input.







Deferreds
---------

Deferreds are used by a Twisted application to set up work that needs to be done using input that might not be available yet.




### How To Use Deferreds: Set Up the Work To Be Done ###
