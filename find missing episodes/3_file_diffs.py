f = open('analysis.txt', 'w')

file1 = open('eplist.txt', 'r')
file2 = open('eps.txt', 'r')

f1_lst = file1.readlines()
f2_lst = file2.readlines()

f1_lwr = [line.lower().capitalize() for line in f1_lst]
f2_lwr = [line.lower().capitalize() for line in f2_lst]

diff = list(set(f1_lwr)^set(f2_lwr))
diff_sorted = sorted(diff)

f.write('Missing Titles:\n\n')

for line in diff_sorted:
    f.write(line)

f.close();
