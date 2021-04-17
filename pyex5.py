import re

roster = {}

input_file = open('roster.txt','r')

for student in input_file.readlines():
    #[last, first, email] = student.split(', ')
    matches = re.search('(.+) *, *(.+) *, *(s[0-9]{7})',student)
    last = matches.group(1)
    first = matches.group(2)
    id = matches.group(3)

    #[id,domain] = email.split('@')


    roster[id] = last + ", " + first


for id in roster.keys():
    print (id + ", " + roster[id])