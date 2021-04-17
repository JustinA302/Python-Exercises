# Python-Exercises
Python exercises I worked on


Exercise 1 - blocks
Create, save and run pyex1.py:

x = 1                       # block 0
if x == 1:                  # header line:
    y = 2                   # block 1
    if y == 2:              # header line:
        print('in block2')  # block 2
    print('in block1')      # block 1
print('in block0')          # block 0
Try changing the indentation.
Try adding blank lines.
Run with 'python3 pyex1.py'.


Exercise 2 - standard input/output
Create, save and run pyex2.py:

import sys
for line in sys.stdin:
    sys.stdout.write( line )
Create a separate input file and redirect its contents to pyex2.py as we did with Perl programs that required standard input.
How does a plain print statement work compared to sys.stdout.write?
See if strings of standard input are “chomped” by Python by default. Try the string len() and rstrip() methods.


Exercise 3 - Count word lengths using a dictionary
Write pyex3.py to find the number of occurrences of each word length in english.sorted.python. That is, find and print the number of words in english.sorted.python that are one character long, two characters long, three characters long and so on. Use a Python dictionary.

You must download and use the english.sorted.python input file which is UTF-8 encoded.


Exercise 4 - roster to dictionary
Reproduce Perl exercise 4 in Python. Save it as pyex4.py.


Exercise 5 - regular expression search and replace
In pyex5.py, write and save a Python program that reads an old webadvisor roster file and writes information to a file called roster2.txt in the following format:

     last name, first name & middle initial, student id    
     
     
Exercise 6 - html parsing with packages
In pyex6.py, parse the article titles and URLs from the HTML source of http://www.monmouth.edu/news/archives. Store the titles and URLs in 2 lists. Use a dictionary newsfeed to store the title:URL key:value pairs. Print the title:URL pairs. Use the requests package to retrieve the HTML.
