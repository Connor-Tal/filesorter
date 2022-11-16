fileName = 'test.txt'
linecout = 0
with open(fileName, "r", encoding='utf-8') as f:
    lines = f.readlines()
    line1 = lines[linecout]
    line2 = lines[linecout+1]
    print(line1,line2)
    #compare the two lines first letter and see which one came first in alphabetical order
    if line1[0] == line2[0]:
        print("The two lines are the same")
    elif line1[0] > line2[0]:
        print("line1 came first")
    elif line1[0] < line2[0]:
        print("line2 came first")

        