# sentence_randomizer
Randomize the orders of english text sentences.

# Purpose

As a writer some common editing advice is read what you wrote sentence by sentence from the bottom up.
The principle is to force your brain to actually read since the flow of what you wrote is disturbed.
I've been using a quick and dirty script to go one step further, to parse an English text file into 
sentences and randomize them.

I mentioned this on Reddit and there seemed to be some interest, so I thought about how to package it up.

I don't know yet.  But a first step is to at least get it onto a public repo.  

The roadmap, if I choose to follow it looks something like this:

* Packaging:  Figure out a way that writers can install and run the script on Windows and Mac.
** Right now this looks like pyInstaller, but that's preliminary.
* GUI: Turn it into something real, rather than just printing the sentences and being done. 
** Terminal
** Qt5
* Edit
** Once there is a UI it would be nice to just be able to edit the sentences as they come up.
* Export
** Once we can edit senteces we need to be able to recreate the original text file with the edits.
* Import
** Read .rtf, .doc, .docx, etc.
* Export Formats
** Be able to recreate anything with can read. 

Once we get to having a UI, it'll probably be useful to other writers, but of course the more features the better.
