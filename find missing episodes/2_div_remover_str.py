import re

f = open('eps.txt', 'w')
epdivs = open('epsdivs.txt', 'r', encoding='utf-8')

titles = epdivs.readlines()

for line in titles:
    title_str = str(line)
    title_alt = re.findall('alt=\"(.*?)\"', title_str)
    
for title in title_alt:
    f.write(title+"\n")

f.close()
