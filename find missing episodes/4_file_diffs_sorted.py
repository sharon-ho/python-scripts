f = open('analysis_manual_sorted.txt', 'w')

file1 = open('analysis_manual.txt', 'r')

f1_lst = file1.readlines()

f1_sorted = sorted(f1_lst)

for line in f1_sorted:
    f.write(line)

f.close();
