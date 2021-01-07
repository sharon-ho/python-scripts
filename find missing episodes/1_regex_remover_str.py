import re

f = open('eplist.txt', 'w')
neplist = open('neplist.txt', 'r', encoding='utf-8')

titles_only = []

titles = neplist.readlines()

for line in titles:
    title_str = str(line)
    title_no_num = re.sub('[0-9]*\. ', '', title_str)
    titles_only.append(title_no_num)
    
for title in titles_only:
    f.write(title)

f.write('\n')
f.close()
