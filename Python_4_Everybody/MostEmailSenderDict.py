#Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.


file = raw_input('Enter file name: ')
if len(file) < 1 : file = 'mbox-short.txt'

try :
    fhand = open(file)
except :
    print 'Cannot open file:' , file , '.' , '...please try, again.'
    exit()

email_adrs = dict()

for line in fhand :
    if not line.startswith('From ') : continue
    words = line.split()
    email_adrs[words[1]] = email_adrs.get(words[1], 0) + 1

bigcount = None
bigword = None
for word,count in email_adrs.items() :
    if bigcount == None or bigcount < count	:
        bigword = word
        bigcount = count

print bigword, bigcount